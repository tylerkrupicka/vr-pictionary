# vr-pictionary
Quick script for playing vr pictionary with movies, etc

#### Dependencies

* PySide

Installation:

`pip install PySide --only-binary :all:`

If you experience the following error (Unix systems):

```
>>> import PySide.QtGui
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: dlopen(/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/PySide/QtGui.so, 2): Library not loaded: libpyside.cpython-34m.1.2.dylib
  Referenced from: /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/PySide/QtGui.so
  Reason: image not found
```

Then just export the following environment variable in your bash_profile or bashrc:

```
DYLD_LIBRARY_PATH=/your/path/to/pyside/libraries
export DYLD_LIBRARY_PATH
```

Then to run, just enter the following command:

`python vr_pictionary`

#### Add Categories

1. Create a directory within vr_pictionary
1. Copy the __init__.py file from vr_pictionary/movies to the new directory
1. Change the `NAME` variable at the top of the new __init__.py file to the desired category name
 * Note: Category names _MUST_ be unique. If the category already exists, see [below](#add-decks) on adding new decks to an existing category
1. Viola, you have created a category. See [below](#add-decks) for instructions on how to add decks to your category

#### Add Decks

2. Within the category directory, create a new file with the extension .py (e.g. vr_pictionary/movies/newDeck.py)
2. Create a `NAME` variable at the top with the name of the deck. (e.g. `NAME = "Medium"`)
 * Note: Deck names _MUST_ be unique.
2. Create a `CARDS` variable that contains a list of strings representing the card
