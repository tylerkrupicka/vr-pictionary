# vr-pictionary
Quick script for playing vr pictionary with movies, etc

To run, just enter the following command:

`python vr_pictionary`

To add categories,

1) Create a directory within vr_pictionary
2) Copy the __init__.py file from vr_pictionary/movies to the new directory
3) Change the `NAME` variable at the top of the new __init__.py file to the desired category name
 --> Note: Category names _MUST_ be unique. If the category already exists, see below on adding new decks to an existing category
4) Viola, you have created a category. See below for instructions on how to add decks to your category

To add decks to an already existing category,

1) Within the category directory, create a new file with the extension .py (e.g. vr_pictionary/movies/newDeck.py)
2) Create a `NAME` variable at the top with the name of the deck. (e.g. `NAME = "Medium"`)
 --> Note: Deck names _MUST_ be unique.
3) Create a `CARDS` variable that contains a list of strings representing the card