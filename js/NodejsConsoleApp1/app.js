'use strict';

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const fs = require('fs');
var id = 0;
var shapeMem = [];

var instructions = `
    Welcome to the program. Please read the instructions below.\n\n

    Enter one of the following commands in the following formats:\n\n

    circle <center x> <center y> <radius>\n
    square <corner x> <corner y> <length of sides>\n
    rectangle <corner x> <corner y> <side length 1> <side length 2>\n
    triangle <vertice 1 x> <vertice 1 y> <vertice 2 x> <vertice 2 y> <vertice 3 x> <vertice 3 y>\n
    donut <center x> <center y> <radius 1> <radius 2>\n\n

    All shape words are literal inputs and inputs in brackets afterward are numeric (e.g. 4.5, 7, etc.)\n\n`;

console.log(instructions);
    
shapePrompt();

function shapePrompt() {
    readline.question('Enter Command:', val => {
        var result = val.split(' '),
            shape = result[0],
            var1 = parseFloat(result[1]),
            var2 = parseFloat(result[2]),
            var3 = parseFloat(result[3]),
            var4 = parseFloat(result[4]),
            var5 = parseFloat(result[5]),
            var6 = parseFloat(result[6]);

        if (shape == 'circle' || shape == 'square' || shape == 'rectangle' || shape == 'triangle' || shape == 'donut' || shape == 'file' || shape == 'help' || shape == 'exit' || shape == 'pair') {
            switch (shape) {
                case 'circle':
                    if (var1 && var2 && var3) {
                        circle(shape, var1, var2, var3);
                    } else {
                        console.log('error: please use the following format for circles: circle <center x> <center y> <radius>')
                    }
                    break;
                case 'square':
                    if (var1 && var2 && var3) {
                        square(shape, var1, var2, var3);
                    } else {
                        console.log('error: please use the following format for squares: square <corner x> <corner y> <length of sides>')
                    }
                    break;
                case 'rectangle':
                    if (var1 && var2 && var3 && var4) {
                        rectangle(shape, var1, var2, var3, var4);
                    } else {
                        console.log('error: please use the following format for rectangles: rectangle <corner x> <corner y> <side length 1> <side length 2>')
                    }
                    break;
                case 'triangle':
                    if (var1 && var2 && var3 && var4 && var5 && var6) {
                        triangle(shape, var1, var2, var3, var4, var5, var6);
                    } else {
                        console.log('error: please use the following format for triangles: triangle <vertice 1 x> <vertice 1 y> <vertice 2 x> <vertice 2 y> <vertice 3 x> <vertice 3 y>')
                    }
                    break;
                case 'donut':
                    if (var1 && var2 && var3 && var4) {
                        donut(shape, var1, var2, var3, var4);
                    } else {                 
                        console.log('error: please use the following format for donuts: donut <center x> <center y> <radius 1> <radius 2>')
                    }
                    break;
                case 'file':
                    fileRead(result[1]);
                    break;
                case 'pair':
                    pairRead(result[1], result[2]);
                case 'help':
                    console.log(instructions);
                    break;
                case 'exit':
                    console.log('goodbye!');
                    process.exit();
            }
        } else {
            console.log("please check for misspelled input and try again");
        }

        shapePrompt();
    });
};

function circle (shape, var1, var2, var3) {
    id = id + 1;
    console.log('shape ' + id + ': ' + shape + ' with center at (' + var1 + ', ' + var2 + ') and radius of ' + var3);
    shapeMem.push({
        'shape': shape,
        'id': id,
        'x': var1,
        'y': var2,
        'radius': var3
    });
} 

function square (shape, var1, var2, var3) {
    id = id + 1;
    console.log('shape ' + id + ': ' + shape + ' with corner at (' + var1 + ', ' + var2 + ') and side length of ' + var3);
    shapeMem.push({
        'shape': shape,
        'id': id,
        'x': var1,
        'y': var2,
        'sideLength': var3
    });
} 

function rectangle (shape, var1, var2, var3, var4) {
    id = id + 1;
    console.log('shape ' + id + ': ' + shape + ' with corner at (' + var1 + ', ' + var2 + '), side length 1 of ' + var3 + ', and side length 2 of ' + var4);
    shapeMem.push({
        'shape': shape,
        'id': id,
        'x': var1,
        'y': var2,
        'sideLength1': var3,
        'sideLength2': var4
    });
}

function triangle (shape, var1, var2, var3, var4, var5, var6) {
    id = id + 1;
    console.log('shape ' + id + ': ' + shape + ' with vertice 1 at (' + var1 + ', ' + var2 + '), vertice 2 at (' + var3 + ', ' + var4 + '), and vertice 3 at (' + var5 + ', ' + var6 + ')');
    shapeMem.push({
        'shape': shape,
        'id': id,
        'x1': var1,
        'y1': var2,
        'x2': var3,
        'y2': var4,
        'x3': var5,
        'y3': var6
    });
}

function donut (shape, var1, var2, var3, var4) {
    id = id + 1;
    console.log('shape ' + id + ': ' + shape + ' with center at (' + var1 + ', ' + var2 + '), radius 1 of ' + var3 + ', and radius 2 of ' + var4);
    shapeMem.push({
        'shape': shape,
        'id': id,
        'x': var1,
        'y': var2,
        'radius1': var3,
        'radius2': var4
    });
}

function fileRead(var1) {
    var filename = var1.toString();
    fs.readFile(filename, 'utf8', function (err, data) {
        
        if (err) {
            console.error(err);
            return;
        }

        var fileVal = data.split(' ');
        switch (fileVal[0]) {
            case 'circle':
                if (fileVal[1] && fileVal[2] && fileVal[3]) {
                    circle(fileVal[0], fileVal[1], fileVal[2], fileVal[3]);
                } else {
                    console.log('error: please use the following format for circles: circle <center x> <center y> <radius>')
                }
                break;
            case 'square':
                if (fileVal[1] && fileVal[2] && fileVal[3]) {
                    square(fileVal[0], fileVal[1], fileVal[2], fileVal[3]);
                } else {
                    console.log('error: please use the following format for squares: square <corner x> <corner y> <length of sides>')
                }
                break;
            case 'rectangle':
                if (fileVal[1] && fileVal[2] && fileVal[3] && fileVal[4]) {
                    rectangle(fileVal[0], fileVal[1], fileVal[2], fileVal[3], fileVal[4]);
                } else {
                    console.log('error: please use the following format for rectangles: rectangle <corner x> <corner y> <side length 1> <side length 2>')
                }
                break;
            case 'triangle':
                if (fileVal[1] && fileVal[2] && fileVal[3] && fileVal[4] && fileVal[5] && fileVal[6]) {
                    triangle(fileVal[0], fileVal[1], fileVal[2], fileVal[3], fileVal[4], fileVal[5], fileVal[6]);
                } else {
                    console.log('error: please use the following format for triangles: triangle <vertice 1 x> <vertice 1 y> <vertice 2 x> <vertice 2 y> <vertice 3 x> <vertice 3 y>')
                }
                break;
            case 'donut':
                if (fileVal[1] && fileVal[2] && fileVal[3] && fileVal[4]) {
                    donut(fileVal[0], fileVal[1], fileVal[2], fileVal[3], fileVal[4]);
                } else {
                    console.log('error: please use the following format for donuts: donut <center x> <center y> <radius 1> <radius 2>')
                }
                break;
        }
    });
}

function pairRead(x, y) {
    var surfaceTotal = 0;
    shapeMem.forEach((element) => {
        console.log(element);
        //switch (element.shape) {
        //    case 'circle':
        //        if (element.x == x && element.y == y) {
        //            console.log(element.shape + ' ' + element.id + ', with surface area of ' + (Math.PI * Math.pow(element.radius, 2)));
        //            surfaceTotal = surfaceTotal + (Math.PI * Math.pow(element.radius, 2));
        //        }
        //    case 'square':
        //        if (element.x == x && element.y == y) {
        //            console.log(element.shape + ' ' + element.id + ', with surface area of ' + Math.pow(element.sideLength, 2));
        //            surfaceTotal = surfaceTotal + Math.pow(element.sideLength, 2);
        //        }
        //    case 'rectangle':
        //        if (element.x == x && element.y == y) {
        //            console.log(element.shape + ' ' + element.id + ', with surface area of ' + (element.sideLength1 * element.sideLength2));
        //            surfaceTotal = surfaceTotal + (element.sideLength1 * element.sideLength2);
        //        }
        //    case 'triangle':
        //        if (element.x1 == x && element.y1 == y) {
        //            console.log(element.shape + ' ' + element.id + ', with surface area of ' + (0.5 * (element.x1 * (element.y2 - element.y3) +
        //                element.x2 * (element.y3 - element.y1) +
        //                element.x3 * (element.y1 - element.y2)
        //            )));
        //            surfaceTotal = surfaceTotal + (0.5 * (element.x1 * (element.y2 - element.y3) +
        //                element.x2 * (element.y3 - element.y1) +
        //                element.x3 * (element.y1 - element.y2)
        //            ));
        //        } else if (element.x2 == x && element.y2 == y) {
        //            console.log(element.shape + ' ' + element.id + ', with surface area of ' + (0.5 * (element.x1 * (element.y2 - element.y3) +
        //                element.x2 * (element.y3 - element.y1) +
        //                element.x3 * (element.y1 - element.y2)
        //            )));
        //            surfaceTotal = surfaceTotal + (0.5 * (element.x1 * (element.y2 - element.y3) +
        //                element.x2 * (element.y3 - element.y1) +
        //                element.x3 * (element.y1 - element.y2)
        //            ));
        //        } else if (element.x3 == x && element.y3 == y) {
        //            console.log(element.shape + ' ' + element.id + ', with surface area of ' + (0.5 * (element.x1 * (element.y2 - element.y3) +
        //                element.x2 * (element.y3 - element.y1) +
        //                element.x3 * (element.y1 - element.y2)
        //            )));
        //            surfaceTotal = surfaceTotal + (0.5 * (element.x1 * (element.y2 - element.y3) +
        //                element.x2 * (element.y3 - element.y1) +
        //                element.x3 * (element.y1 - element.y2)
        //            ));
        //        }
        //    case 'donut':
        //        if (element.x == x && element.y == y) {
        //            console.log(element.shape + ' ' + element.id + ', with surface area of ' + (4 * math.pow(math.PI, 2) * element.radius1 * element.radius2));
        //            surfaceTotal = surfaceTotal + (4 * math.pow(math.PI, 2) * element.radius1 * element.radius2);
        //        }
        //}
    });
    console.log('Total surface area: ' + surfaceTotal.toString());
}



