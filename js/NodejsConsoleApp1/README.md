# Nodejs Console App - Shape Exercise
Hello, All

I recently started on a project for a client that never came to fruition, so I decided to post it here. It is a DEFINITE work in progress but I made the majority of this in a few hours.

## Description
This console app is a user input program that returns shape, dimensions, and surface areas back to the user.

The program takes certain shape inputs like "circle", "square", "rectangle", etc. paired with dimensions as the additional arguments and returns the input in a comprehensible format. The shape and information will be added to a shape memory array used for surface area calculation with the ```pair``` command (mentioned below).

## Example
![image](https://user-images.githubusercontent.com/25441533/179361273-d3230667-45e1-42fe-9359-a992a5a05a29.png)


## Syntax
Here is the block of code that instructs the user on syntax and commands.
```javascript
var instructions = `
    Welcome to the program. Please read the instructions below.\n\n

    Enter one of the following commands in the following formats:\n\n

    circle <center x> <center y> <radius>\n
    square <corner x> <corner y> <length of sides>\n
    rectangle <corner x> <corner y> <side length 1> <side length 2>\n
    triangle <vertice 1 x> <vertice 1 y> <vertice 2 x> <vertice 2 y> <vertice 3 x> <vertice 3 y>\n
    donut <center x> <center y> <radius 1> <radius 2>\n\n

    All shape words are literal inputs and inputs in brackets afterward are numeric (e.g. 4.5, 7, etc.)\n\n`;
```

## Reading from file
To read from a file, please use the ```file``` command followed by the relative file path. For example: ```file test.txt```.

# Shape memory and surface area calculations
UNDER CONSTRUCTION - To read back shapes that overlap your input along with the surface area of the shapes, use the ```pair``` command followed by a pair of coordinates. For example, ```pair 4.5 7.5```. The program will ultimately return the total surface area of all shapes that overlap.

## Help and exit
For a repeat of the instructions, simply enter the ```help``` command.

To exit the program, simply enter the ```exit``` command.

## Future implementation
Soon, I hope to implement more complex calculations to the program. I am currently looking to implement libraries that will hopefully help me avoid manual calculations in the code. 

## Credits
Original motivation for this comes from https://github.com/CallMeGary/ShapeExercise, which is originally written in Java Factory Design Method. I am simply taking this project as motivation, as this is not written in Factory Design or in Java. I do not intend to copy the original work, but to implement my own design using the original project's idea. 


