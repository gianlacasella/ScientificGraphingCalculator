# Scientific Graphing Calculator

A Python program that I wrote to learn (self-taught) to use Tkinter. The program is a scientific/plotting calculator, powered by
Tkinter, matplotlib and numpy.

## Getting started

There are two ways to execute this program:

1. You can clone/download this repository and open a command prompt / bash inside the downloaded folder. Be sure to check the Prerequisites section before you continue.

Then, just type in the cmd:
```
	python main.py
```

2. You can download my last release on this repository, and run scientificCalculator.exe on Windows

![Screenshot](/img/7.JPG)

As you can see in the previous picture, the window has a left frame that works as scientific calculator, a center frame to show
the operations made, and the right frame is a plotter. On this frame, you have to introduce X and Y min and max, which are the plot axis limits. Then, you can choose a function to plot and a color. 

It is necessary to introduce the function in the same way as you would introduce it on the Python interpreter.
Example:

* If you want to plot x squared function, you will have to write it as:
```
	x**2
```

* If you want to plot the absolute value of x cubed, you will have to write it as:
```
	abs(x**3)
```

On the bottom, you have also the matplotlib's Navigation Toolbar, which will allow you to navigate the plotted function (zoom in and out, move the graph and return to original state) and to save the picture on .png format.

![Screenshot](/img/4.JPG)

## Prerequisites

If you want to execute the program in the first way, you will need to have installed before:
* Python 3.6
* Matplotlib
* Numpy
* Tkinter

## What I learned

* Managing windows with Tkinter
* Managing Tkinter tools
* Learned some Python's functions such as exec(), eval() and lambda functions
* Learned to add Matplotlib's Figures, Plots and Toolbars into a Tkinter Frame

## Authors

* **Gianfranco Lacasella** - *Initial work* - [glacasellaUANDES](https://github.com/glacasellaUANDES)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE- see the [LICENSE.md](LICENSE.md) file for details