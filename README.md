# SnakeGame *Note this file is subject to change

SnakeGame is a compilation of code that deals with game logic and rendering

## Installation

1. Make sure that Python 3 installed. If not, you can download and install it [here](https://www.python.org/downloads/).

2. Install [pygame](https://www.pygame.org) by running the following command:
```
pip install pygame
```

3. [Download project files](https://github.com/olawuyio/snake290/archive/master.zip) or clone repo with the following command:
```
git clone https://github.com/olawuyio/snake290
```

4. From the project root folder, run `src/snake_game.py` with Python
```
python src/snake_game.py
```

## Libraries

The list of libraries used are found in the requirements.txt file on the root directory.
To install the libraries run: `pip install requirements.txt`

## Folder and their content

src: Main class, Handler classes, interface classes and abstract classes
ext: The external libraries and settings
items: item classes
menus: menu classes
misc: miscellaneous classes
build: Computer build files
doc: all documentation

## Usage

When adding classes make sure to put them in the correct folder
If you wish to import a class simply follow the form

```python
from folder.file_name import class_name
```

Look at SnakeGame class for an example

Items such as snake body or food should be subclasses of the item class. Write
the class files for such objects in the items folder. Make sure to define the
render function so the code knows how to draw it (or leave a reminder to
implement it and I will add it later)

If you wish to render your object go into the render handler's update method
and add your object to the chain of if else statements in the form

```python
elif current == num:  # num is the number that represents your item
    item = your_item((row * 100, col * 100), (width, height))
    temp_col.append(item)
```

Note the row and the col are the x y position which will be given
and the *100 places it in the right spot on the map relative to the 2d array.
However, you must define the width and height which should be scaled relative
to the array as well.

To make the item show up you must change the temp map which can be found
inside the SnakeGame class in the run function, such that it includes
your number associated with the object


## Contributing

Please document your code and add to the doc file how your code works, as well
as edit the readme file.
