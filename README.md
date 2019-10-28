# SnakeGame *Note this file is subject to change

SnakeGame is a compilation of code that deals with game logic and rendering

## Libraries

The list of libraries used are in the ext folder in the Requirements.txt file.
To install the libraries using pycharm open the Requirements.txt file and click
on the prompt that will automatically download the files.

## Settings

All the required settings are in the ext folder, in the settings.jar file. To
use these settings click on the file tab, then click import settings and select
the settings.jar from the directory.

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

        from folder.file_name import class_name

Look at SnakeGame class for an example

Items such as snake body or food should be subclasses of the item class. Write
the class files for such objects in the items folder. Make sure to define the
render function so the code knows how to draw it (or leave a reminder to
implement it and I will add it later)

If you wish to render your object go into the render handler's update method
and add your object to the chain of if else statements in the form

        elif current == num:  # num is the number that represents your item
            item = your_item((row * 100, col * 100), (width, height))
            temp_col.append(item)

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