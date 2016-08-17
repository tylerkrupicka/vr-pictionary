from .defines import *
from random import shuffle
from time import sleep
from threading import Thread
from getpass import getpass

#######################
#  Utility Functions  #
#######################

def unix_clear_prompt(prompt=''):
   stream.write('\r')
   stream.write(' ' * len(prompt))
   stream.write('\r')

def unix_input_no_echo(prompt='', end='\n', clear=False):
   import contextlib

   passwd = None
   with contextlib.ExitStack() as stack:
      try:
         # Always try reading and writing directly on the tty first.
         fd = os.open('/dev/tty', os.O_RDWR|os.O_NOCTTY)
         tty = io.FileIO(fd, 'w+')
         stack.enter_context(tty)
         input = io.TextIOWrapper(tty)
         stack.enter_context(input)
         if not stream:
            stream = input

      except OSError as e:
         # If that fails, see if stdin can be controlled.
         stack.close()
         try:
            fd = sys.stdin.fileno()
         except (AttributeError, ValueError):
            fd = None
            import time
            time.sleep(3)
            unix_clear_prompt(prompt)

         input = sys.stdin
         if not stream:
            stream = sys.stderr

      if fd is not None:
         try:
            old = termios.tcgetattr(fd)     # a copy to save
            new = old[:]
            new[3] &= ~termios.ECHO  # 3 == 'lflags'
            tcsetattr_flags = termios.TCSAFLUSH
            if hasattr(termios, 'TCSASOFT'):
               tcsetattr_flags |= termios.TCSASOFT
            try:
               termios.tcsetattr(fd, tcsetattr_flags, new)
               passwd = _raw_input(prompt, stream, input=input)
            finally:
               termios.tcsetattr(fd, tcsetattr_flags, old)
               stream.flush()  # issue7208
         except termios.error:
            if passwd is not None:
               # _raw_input succeeded.  The final tcsetattr failed.  Reraise
               # instead of leaving the terminal in an unknown state.
               raise
            # We can't control the tty or stdin.  Give up and use normal IO.
            # input() raises an appropriate warning.
            if stream is not input:
               # clean up unused file objects before blocking
               stack.close()

            import time
            time.sleep(3)
            unix_clear_prompt(prompt)
            return

      if clear:
         unix_clear_prompt(prompt)

      stream.write(end)
      return passwd

def _raw_input(prompt="", stream=None, input=None):
   # This doesn't save the string in the GNU readline history.
   if not stream:
      stream = sys.stderr
   if not input:
      input = sys.stdin
   prompt = str(prompt)
   if prompt:
      try:
         stream.write(prompt)
      except UnicodeEncodeError:
         # Use replace error handler to get as much as possible printed.
         prompt = prompt.encode(stream.encoding, 'replace')
         prompt = prompt.decode(stream.encoding)
         stream.write(prompt)
      stream.flush()
   # NOTE: The Python C API calls flockfile() (and unlock) during readline.
   line = input.readline()
   if not line:
      raise EOFError
   if line[-1] == '\n':
      line = line[:-1]
   return line

def win_clear_prompt(prompt=''):
   msvcrt.putwch('\r')
   for c in prompt:
      msvcrt.putwch(' ')
   msvcrt.putwch('\r')

def win_input_no_echo(prompt='', end='\n', clear=False):
   for c in prompt:
      msvcrt.putwch(c)
   pw = ""
   while 1:
      c = msvcrt.getwch()
      if c == '\r' or c == '\n':
         break
      if c == '\003':
         raise KeyboardInterrupt
      if c == '\b':
         pw = pw[:-1]
      else:
         pw = pw + c

   if clear:
      win_clear_prompt(prompt)

   for c in end:
      msvcrt.putwch(c)
   return pw

# Find the right input function
try:
    import termios
    termios.tcgetattr, termios.tcsetattr
except (ImportError, AttributeError):
   try:
      import msvcrt
   except ImportError:
      # TODO: Set flag here
      input_no_echo = input
   else:
      input_no_echo = win_input_no_echo
else:
   input_no_echo = unix_input_no_echo


#######################

class Engine(object):
   STARTUP_STATE  = 0
   COMMAND_STATE  = 1
   SHOWCARD_STATE = 2
   TIMING_STATE   = 3
   SCORING_STATE  = 4
   SHUTDOWN_STATE = 5

   STATES = [
      STARTUP_STATE,
      SHOWCARD_STATE,
      COMMAND_STATE,
      TIMING_STATE,
      SCORING_STATE,
      SHUTDOWN_STATE
   ]

   PROMPT = "\nCommand: "

   def __init__(self, cards):
      self._cards = cards
      self._teams = {}
      self._score = {}
      self._state = self.STARTUP_STATE
      self._inputThread = Thread(target=self.inputProcessor)

   def letsPlay(self):
      if self._state == self.STARTUP_STATE:
         # Begin startup
         if input("\nKeep score? (y) ").lower() == 'y':
            try:
               numTeams = int(input("# of teams: "))
               for teamID in range(1, numTeams+1):
                  teamName = input("%d) " % teamID);
                  self._teams[teamID] = teamName
                  self._score[teamName] = 0
               self._scoreKeeping = True
            except ValueError:
               print("Invalid number of teams.\nNot keeping score.")
               self._scoreKeeping = False
         else:
            self._scoreKeeping = False

         self._inputThread.start()
         print("Shuffling cards.")
         shuffle(self._cards)
         if self._scoreKeeping:
            print("Commands: (h, s, n, q)")
         else:
            print("Commands: (h, n, q)")

         self._state = self.COMMAND_STATE

      elif self._state == self.COMMAND_STATE:
         # Process command
         print(self.PROMPT, end="")
         while self._state == self.COMMAND_STATE:
            pass

      elif self._state == self.SHOWCARD_STATE:
         if len(self._cards) != 0:
            time = 10
            card = self._cards.pop()
            self._spaceBuff = len(card)
            print(card, end="\r")

            while self._state == self.SHOWCARD_STATE:
               sleep(.5)
               time = time - .5
               if time == 0:
                  self._state == self.TIMING_STATE

            print(" " * len(card), end="\r")
         else:
            self._state = self.SHUTDOWN_STATE
            print("All out of cards!")
            if self._scoreKeeping:
               print("Final tally....")
               self.printScore()

      elif self._state == self.TIMING_STATE:
         # Process interrupt
         time = 60 * 2
         while time != 0:
            if self._state != self.TIMING_STATE:
               print(" " * 15, end="\r")
               break
            print("Time left: %d" % (time // 2), end="\r")
            sleep(.25)
            time = time - .5
         else:
            print(" " * 15, end="\r")
            print("Time's Up!")
            if self._scoreKeeping:
               self._state = self.SCORING_STATE
            else:
               self._state = self.COMMAND_STATE

      elif self._state == self.SCORING_STATE:
         # Process score
         print("Teams: ")
         self.printTeams()
         print("Award point to team: ", end='')
         while self._state == self.SCORING_STATE:
            pass

      else:
         # Begin shutdown
         self._inputThread.join()
         return

      self.letsPlay()

   def inputProcessor(self):
      while self._state != self.SHUTDOWN_STATE:
         if self._state == self.SHOWCARD_STATE:
            inputStr = input_no_echo()
         else:
            inputStr = input()
         if self._state == self.COMMAND_STATE:
            # Process command
            command = inputStr
            if command == "q":
               self._state = self.SHUTDOWN_STATE
            elif command == "h":
               if self._scoreKeeping:
                  print("Commands: (h, s, n, q)")
               else:
                  print("Commands: (h, n, q)")
               print(self.PROMPT, end="")
            elif command == "s":
               if self._scoreKeeping:
                  self.printScore()
               else:
                  self._state = self.SHOWCARD_STATE
            else:
               self._state = self.SHOWCARD_STATE

         elif self._state == self.SHOWCARD_STATE:
            print(" " * self._spaceBuff, end="\r")
            self._state = self.TIMING_STATE

         elif self._state == self.TIMING_STATE:
            # Process interrupt
            if self._scoreKeeping:
               self._state = self.SCORING_STATE
            else:
               self._state = self.COMMAND_STATE

         elif self._state == self.SCORING_STATE:
            # Process score
            teamID = inputStr
            try:
               if teamID in self._score:
                  self._score[teamID] += 1
               else:
                  self._score[self._teams[int(teamID)]] += 1
            except (KeyError, ValueError):
               print("No point awarded")
            self._state = self.COMMAND_STATE

         else:
            pass

   def printTeams(self):
      for teamID in self._teams:
         print("%d) %s" % (teamID, self._teams[teamID]))

   def printScore(self):
      print("---------------")
      for team in self._score:
         print(team + ": " + str(self._score[team]))