# memogame
Text-based memorisation game in Python for digits of irrational constants.

## Playing
Simply run `memogame.py`.

The game will prompt you to choose a constant; these can be chosen by inputting the shown name or the index number before it.

Recall as many digits of the constant as you can verbatim (including the decimal point and before) and press enter when you're done. If you made a mistake, the game will tell you where you went wrong.

For further improvement, the next ten digits of the constant are also printed.

## Constants
Four constants are built in by default; pi (3.14159...), tau (6.28318...), the square root of two (1.41421...), and phi/the golden ratio (1.61903...). These can be found in the `digits` folder.

To add more, open the `paths.txt` file and add a new line containing the name of the constant, followed by a colon, followed by the path to the file. The program will automatically parse `paths.txt` at runtime.
