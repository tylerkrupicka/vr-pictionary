
from threading import Thread

class InputMonitorClass(Thread):
   def __init__(self):
      super().__init__()


   def run(self):
      while True:
         command = input()