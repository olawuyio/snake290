# SnakeGame *Note this file is subject to change

SnakeGame is a compilation of code that deals with game logic and rendering

![Snake Game](/images/snake_game.png?raw=true)

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
## How To Play
1. Using "W", "A", "S", "D" to move the direction the snake is moving to. "W" to move up, 
"A" to move to the left, "S" to move down, and "D" to move to the right.
2. Control the snake to avoid touching the wall or the snake's body with it's head.
3. Control the snake to consume the food to gain score.

## Folders and their content

src: Main class, Handler classes, interface classes and abstract classes
ext: The external libraries and settings
items: item classes
menus: menu classes
misc: miscellaneous classes
build: Computer build files
doc: all documentation

## Advanced code overview

The code is structured into three parts: the game, arena, and items.
The game holds the snake_game, state, and render_handler classes,
the arena holds the board class, and the items holds the player,
food, and wall classes.

The Board class contains a 2d array, where each integer represents an element 
on the board, which will be modified in player and food class whenever 
the snake moves and a new food appears. While the index representing the walls 
shall remain unchanged.

The game is structured into a front-end and a back-end. The front end contains the
item and render_handler classes, while the back end contains the arena, player, food,
and snake_game classes. The main jobs for the front-end are to display the game and
keep the game running at 50 fps. For the back-end, the main purposes consists of
running the game, tracking objects, and moving the player.

Structuring the code this way will make it easier to find and solve issues, easier to
make changes and additions, and possible to add to the game without knowledge of PyGame.

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

Please document your code and add how your code works to the doc file, as well
as edit the readme file.

## Extending the code
Although there are multiple features the user can add to the game, a few that we 
would like to mention are below.  

1. Changing background colour
    * Change the ```background_color``` attribute in the ```__init__```
     method inside the snake_game class.
    * For instance changing ```self.background_color = 0, 0, 0``` to 
    ```self.background_color = 255, 255, 255``` turns the background white.

2. Changing player and item colour
    * To change the item and player colour, go into the ```render_handler``` 
    class and update the ```food_color```, ```player_color```, and 
    ```wall_color``` attributes in the ```update``` 
    method to your desired colours.
    * An example of this is updating ```self.player_color = 0, 255, 0``` to 
    ```self.player_color = 255, 0, 255 ``` will make the snake purple. 

3. Adding obstacles to the map
    * In the ```__init__``` method inside the board class, change the default 
    initializer to a preset array, adding a three where a wall should be.
    Note the board should be a 48 by 64 grid. 
    * A smaller 10 by 5 example would look like
      ```
      Self.board = [[3,3,3,3,3,3,3,3,3,3]] 
                   [[3,3,0,0,0,0,3,0,0,3]]
                   [[3,0,3,3,1,0,0,0,0,3]]
                   [[3,0,0,0,0,0,0,0,0,3]]
                   [[3,3,3,3,3,3,3,3,3,3]]
       ```
      where the 3's on the board represent a wall.
      
## License

SnakeGame is released under the [MIT License](https://github.com/olawuyio/snake290/blob/master/LICENSE).

## Our contributions

##### Syed Jaffay 

My main contribution to the game was the rendering components. I was in charge 
of designing how the game would look and rendering it. This largely involved 
the classes, Render Handler, and Snake game. Notably, the Render Handler was 
designed to read a 2D array of numbers and display that as objects onto Pygame. 
While the Snake game class was in charge of updating a 2D array and contained 
the loop which ran the game. I also created the states class and items class 
which aided in managing the looping. Furthermore, my contribution to the readme 
file was how to add new features. Mainly, I talked about how the reader could 
make changes. My last contribution was checking over my team's code and making 
sure it followed the proper guidelines. 

##### Daren Liang

In regards to the code, I've contributed to the logic components. I worked on implementing the board and food classes, as well as, handling move events for the player class which interacts with the board and food classes. I have also contributed to the main game class and have implemented methods for modifying the state of the game (ex. quitting the game). For the README, I've contributed to the installation steps section, adding screenshots and committing the license file.
