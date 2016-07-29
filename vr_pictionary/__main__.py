import sys

def start():
   print("\nPick a category.");
   for id in categories:
      print("%d) %s" % (id, categories[id]));
   
   try:
      category = int(input(""));
      category = categories[category]
   except (ValueError, KeyError):
      print("Not a valid category");
      sys.exit();

   print("\nChoose a difficulty.");
   print("1) Easy");
   print("2) Medium");
   print("3) Hard");

   try:
      difficulty = int(input(""));
      if difficulty not in range(0,5):
         raise ValueError;
   except ValueError:
      print("Not a valid difficulty");
      sys.exit();

   try:
      engine = Engine(category, difficulty);

      # Implement try/except to print score
      engine.letsPlay();
   except NotImplementedError as e:
      raise e;

def main():
   print("Welcome to Pictionary");

   while True:
      try:
         start();
      except (EOFError, KeyboardInterrupt):
         if input("\nPlay again? (y/n) ").lower() != "y":
            break;

if __name__ == '__main__':

   import os
   path = os.path.dirname(sys.modules[__name__].__file__);
   path = os.path.join(path, '..');
   if (path not in sys.path):
      sys.path.insert(0, path);

   from vr_pictionary import Engine, categories

   try:
      main();
   except (EOFError, KeyboardInterrupt):
      pass

   print("\nAll done!\n")
   sys.exit();
