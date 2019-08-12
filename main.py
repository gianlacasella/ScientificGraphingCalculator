#                  Modules 
from tkinter import Tk, Spinbox, PhotoImage, Entry, Frame, LEFT, RIGHT, BOTTOM, BOTH, TOP, Label, StringVar, font, Button, Text, DISABLED, NORMAL, INSERT, END, Scrollbar, Y
import scipy.misc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

#               Main  Window

# Creating the  main window, and setting props
mainWindow = Tk()
mainWindow.title("Scientific Calculator v1.0")
mainWindow.resizable(False, False)
img = PhotoImage(file = "calc.png")
mainWindow.call('wm', 'iconphoto', mainWindow._w, img)


#               Global variables

# Fonts
mainWindowFont = font.Font(family = "Verdana", size = 10)
secondaryWindowFont = font.Font(family = "Verdana", size = 10)
buttonsFont = font.Font(family = "Verdana", size = 10, weight = "bold")
amplifiedButtonsFont = font.Font(family = "Verdana", size = 12, weight = "bold")
historyTextFont = font.Font(family = "Verdana", size = 14, weight = "bold")
plotButtonFont = font.Font(family= "Verdana", size = 16, weight = "bold")


# Booleans, StringVar and lists
operationFilling = False
parenthesisOpen = False
actualHistoryOperation = StringVar()
operationMade = False
a_list = ['red', 'blue', 'green', 'black', 'grey', 'yellow']
colorSelected = StringVar()
xminsize = StringVar()
yminsize = StringVar()
xmaxsize = StringVar()
ymaxsize = StringVar()
function = StringVar()
DEGButtonText = StringVar()
ASINButtonText = StringVar()
ACOSButtonText = StringVar()
ATANButtonText = StringVar()
SINButtonText = StringVar()
COSButtonText = StringVar()
TANButtonText = StringVar()
firstScreenText = StringVar()
secondScreenText = StringVar()


#                     Frames 

# Calculator Frame
calculatorFrame = Frame(mainWindow)
calculatorFrame.pack_propagate(0)
calculatorFrame.config(width = "500", height = "700", bg = "grey")
calculatorFrame.pack(fill="y", expand="True", side = LEFT)

# History Frame
historyFrame = Frame(mainWindow)
historyFrame.pack_propagate(0)
historyFrame.config(width = "300", height = "500", bg = "black", borderwidth = "3")
historyFrame.pack(fill="y", expand="True", side = LEFT)

# Plotting Frame
plottingFrame = Frame(mainWindow)
plottingFrame.pack_propagate(0)
plottingFrame.config(width = "700", height = "700", bg = "#20221f")
plottingFrame.pack(fill="y", expand="True", side = LEFT)

# Function to plot Frame
functions2Plot = Frame(plottingFrame)
functions2Plot.pack_propagate(0)
functions2Plot.config(width = "700", height = "163", bg = "#20221f")
functions2Plot.pack(fill="x", expand="True", side = TOP)

# FirstRow on functions2Plot
firstRowFunctions2Plot = Frame(functions2Plot)
firstRowFunctions2Plot.pack_propagate(0)
firstRowFunctions2Plot.config(width = "670", height = "40", bg = "#20221f")
firstRowFunctions2Plot.pack(expand="True", side = TOP)

# SecondRow on functions2Plot
secondRowFunctions2Plot = Frame(functions2Plot)
secondRowFunctions2Plot.pack_propagate(0)
secondRowFunctions2Plot.config(width = "670", height = "40", bg = "#20221f")
secondRowFunctions2Plot.pack(expand="True")

# ThirdRow on functions2Plot
thirdRowFunctions2Plot = Frame(functions2Plot)
thirdRowFunctions2Plot.pack_propagate(0)
thirdRowFunctions2Plot.config(width = "120", height = "80", bg = "#20221f")
thirdRowFunctions2Plot.pack(expand="True", side = BOTTOM)

# Screens Frame
screensFrame = Frame(calculatorFrame)
screensFrame.pack_propagate(0)
screensFrame.config(width = "500", height = "150", bg = "#20221f")
screensFrame.grid(row = 1, column = 1)
screensFrame.pack(fill="both", expand = "True")

# Buttons Frame
buttonsFrame = Frame(calculatorFrame)
buttonsFrame.pack_propagate(0)
buttonsFrame.config(width = "500", height = "550", bg = "#20221f")
buttonsFrame.grid(row = 2, column = 1)
buttonsFrame.pack(fill="both", expand = "True")

# First row of buttons Frame
firstRowButtons = Frame(buttonsFrame)
firstRowButtons.pack_propagate(0)
firstRowButtons.config(width = "500", height = "200", bg = "grey")
firstRowButtons.grid(row = 0,  column = 0, columnspan = 9)
firstRowButtons.pack(fill = "x",expand = "True")


# Second row of buttons Frame
secondRowButtons = Frame(buttonsFrame)
secondRowButtons.pack_propagate(0)
secondRowButtons.config(width = "500", height = "200", bg = "grey")
secondRowButtons.grid(row = 1,  column = 0, columnspan = 9)
secondRowButtons.pack(fill = "x",expand = "True")

# Third row of buttons Frame
thirdRowButtons = Frame(buttonsFrame)
thirdRowButtons.pack_propagate(0)
thirdRowButtons.config(width = "500", height = "200", bg = "grey")
thirdRowButtons.grid(row = 2,  column = 0, columnspan = 9)
thirdRowButtons.pack(fill = "x",expand = "True")

# Fourth row of buttons Frame
fourthRowButtons = Frame(buttonsFrame)
fourthRowButtons.pack_propagate(0)
fourthRowButtons.config(width = "500", height = "200", bg = "grey")
fourthRowButtons.grid(row = 3,  column = 0, columnspan = 9)
fourthRowButtons.pack(fill = "x",expand = "True")

# Fifth row of buttons Frame
fifthRowButtons = Frame(buttonsFrame)
fifthRowButtons.pack_propagate(0)
fifthRowButtons.config(width = "500", height = "200", bg = "grey")
fifthRowButtons.grid(row = 4,  column = 0, columnspan = 9)
fifthRowButtons.pack(fill = "x",expand = "True")

# Sixth row of buttons Frame
sixthRowButtons = Frame(buttonsFrame)
sixthRowButtons.pack_propagate(0)
sixthRowButtons.config(width = "500", height = "200", bg = "grey")
sixthRowButtons.grid(row = 5,  column = 0, columnspan = 9)
sixthRowButtons.pack(fill = "x",expand = "True")


#                   Text and scrollbar

history = Text(historyFrame, width = "300" , height = "100", fg = "white", bg = "black", font = historyTextFont)
history.config(state = DISABLED)
history.grid(row = 1, column = 0)
textScrollbar = Scrollbar(historyFrame)
textScrollbar.config(background = "#20221f", activebackground = "#20221f", activerelief = "sunken")
textScrollbar.pack(side=RIGHT, fill=Y)
history.config(yscrollcommand=textScrollbar.set)
textScrollbar.config(command=history.yview)
history.pack()

#                   Plotting an empty graph with matplotlib, into the tkinter window

firstPlot = False
myFigure = Figure(figsize=(5,5), dpi = 100)
a = myFigure.add_subplot(111)
a.plot([],[])
canvas = FigureCanvasTkAgg(myFigure, plottingFrame)
canvas.draw()
canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
toolbar = NavigationToolbar2Tk(canvas, plottingFrame)
canvas._tkcanvas.pack(side = TOP, fill = BOTH, expand = True)


#                    Screens
# We use 2 screens, firstScreen and secondScreen, both  as labels


firstScreen = Label(screensFrame, textvariable = firstScreenText, font = mainWindowFont, anchor = "e")
firstScreen.grid(row = 1, column = 0, padx = 0, pady = 2)
firstScreen.config(background = "black", fg = "white", justify = "right",height = "5", width = "62")

secondScreen = Label(screensFrame, textvariable = secondScreenText, font = secondaryWindowFont, anchor = "e")
secondScreen.grid(row = 0, column = 0, padx = 0, pady = 2)
secondScreen.config(background = "#20221f", fg = "white", justify = "right",height = "5", width = "62")

# First execution settings
firstScreenText.set("0")
secondScreenText.set("0")
DEGButtonText.set("DEG")
ASINButtonText.set("asin()")
ACOSButtonText.set("acos()")
ATANButtonText.set("atan()")
SINButtonText.set("sin()")
COSButtonText.set("cos()")
TANButtonText.set("tan()")


#                          Usefull functions

def firstScreenTextSet(num):
    # We need global variables
    global operationFilling
    global parenthesisOpen
    global operationMade
    # Analizing if thera are parenthesis
    if num == "(":
        parenthesisOpen = True
    elif  num == ")":
        parenthesisOpen = False
    if operationMade == True:
        firstScreenText.set("")
        operationMade = False
    # We get  whats on the second screen
    textSecondScreen = secondScreenText.get()
    if textSecondScreen[-1] == True and operationFilling == True:
        firstScreenText.set("")
        operationFilling = True
    if(firstScreenText.get() == "0" and num == 0):
        return
    elif(firstScreenText.get() == "0" and num != 0):
        firstScreenText.set("")
        firstScreenText.set(firstScreenText.get() + str(num))
        operationFilling= False
    else:
        firstScreenText.set(firstScreenText.get() + str(num))
        operationFilling = False
    return


# Function to use on C button
def C():
    firstScreenText.set("0")
    secondScreenText.set("0")
    return



def Delete():
    actualNumber = firstScreenText.get()
    actualNumber = actualNumber[:-1]
    firstScreenText.set(actualNumber)
    return



# Function to use when the user clicks on a operation sign
def clickOnOperation(operation):
    global parenthesisOpen
    if operation == "exp(":
        firstScreenText.set("")
    elif operation == "factorial(":
        firstScreenText.set("")
    textFirstScreen = firstScreenText.get()
    if textFirstScreen == "nan":
        textFirstScreen = ""
    textFirstScreen += operation
    firstScreenText.set(textFirstScreen)
    if parenthesisOpen == True:
        return
    firstScreenText.set("")
    textSecondScreen = secondScreenText.get()
    if textSecondScreen == "0":
        secondScreenText.set("")
    textSecondScreen = secondScreenText.get()
    textSecondScreen += textFirstScreen
    secondScreenText.set(textSecondScreen)
    return



# Button to change the DEG button text to RAD
def changeDEGtext():
    if DEGButtonText.get() == "DEG":
        DEGButtonText.set("RAD")
    else:
        DEGButtonText.set("DEG")
    return



# Function to change the trigonometric functions button text 
def changeTrigonometricFunctionsText():
    if ASINButtonText.get() == "asin()":
        ASINButtonText.set("asinh()")
        ACOSButtonText.set("acosh()")
        ATANButtonText.set("atanh()")
        SINButtonText.set("sinh()")
        COSButtonText.set("cosh()")
        TANButtonText.set("tanh()")
    else:
        ASINButtonText.set("asin()")
        ACOSButtonText.set("acos()")
        ATANButtonText.set("atan()")
        SINButtonText.set("sin()")
        COSButtonText.set("cos()")
        TANButtonText.set("tan()")
    return



# Function to use on the CE button
def CE():
    firstScreenText.set("0")
    return




def calculate():
    global operationMade
    global actualHistoryOperation
    if secondScreenText.get() == "0":
        secondScreenText.set("")



    # We get the complete operation
    completeText = secondScreenText.get() + firstScreenText.get()
    completeTextWithDot = completeText.replace(",", ".")
    secondScreenText.set(completeText)
    solution = eval(completeTextWithDot)
    solutionTextWithoutDot = str(solution).replace(".", ",")
    firstScreenText.set(solutionTextWithoutDot)
    secondScreenText.set("0")
    operationMade = True
    actualHistoryOperation.set(completeText+" = "+solutionTextWithoutDot + "\n\n")
    addHistory()
    return



def addHistory():
    global actualHistoryOperation
    history.config(state = NORMAL)
    history.insert(INSERT, "\n\n" + actualHistoryOperation.get())
    history.config(state = DISABLED)
    return



def clearHistory():
    global actualHistoryOperation
    actualHistoryOperation.set("")
    history.config(state = NORMAL)
    history.delete(1.0, END)
    history.config(state = DISABLED)
    return



def calculateTrigonometric(function):
    global operationMade
    global actualHistoryOperation
    if secondScreenText.get() == "0":
        secondScreenText.set("")
    # We get the complete operation value for the trigonometric function
    completeText = secondScreenText.get() + firstScreenText.get()
    completeTextWithDot = completeText.replace(",", ".")
    secondScreenText.set(completeText)
    # We get the  actual value  to  evaluate  in the trigonometric function
    value = eval(completeTextWithDot)
    # We need to  know  if the   value   is  in rads or degrees
    typevalue = DEGButtonText.get()
    # Now we call solveTrigonometric
    if typevalue == "RAD":
        fulloperation = function + "(" + str(value) + ")"
    else:
        fulloperation = function + "(deg2rad(" + str(value) + "))" 
    solution = eval(fulloperation)
    solutionTextWithoutDot = str(solution).replace(".", ",")
    firstScreenText.set(solutionTextWithoutDot)
    secondScreenText.set("0")
    operationMade = True
    actualHistoryOperation.set(function + "(" + str(value) + ")" + " = "+ solutionTextWithoutDot + "\n\n")
    addHistory()
    return



def _sin():
    if SINButtonText.get() == "sin()":
        calculateTrigonometric("sin")
        return
    else:
        calculateTrigonometric("sinh")
        return



def _cos():
    if COSButtonText.get() == "cos()":
        calculateTrigonometric("cos")
        return
    else:
        calculateTrigonometric("cosh")
        return



def _tan():
    if TANButtonText.get() == "tan()":
        calculateTrigonometric("tan")
        return
    else:
        calculateTrigonometric("tanh")
        return



def asin():
    if ASINButtonText.get() == "asin()":
        calculateTrigonometric("arcsin")
        return
    else:
        calculateTrigonometric("arcsinh")
        return



def acos():
    if ACOSButtonText.get() == "acos()":
        calculateTrigonometric("arccos")
        return
    else:
        calculateTrigonometric("arccosh")
        return



def atan():
    if ATANButtonText.get() == "atan()":
        calculateTrigonometric("arctan")
        return
    else:
        calculateTrigonometric("arctanh")
        return



def calculateLogarithmExponential(function):
    global operationMade
    global actualHistoryOperation
    if secondScreenText.get() == "0":
        secondScreenText.set("")
    # We get the complete operation value for the logarithm function
    completeText = secondScreenText.get() + firstScreenText.get()
    completeTextWithDot = completeText.replace(",", ".")
    secondScreenText.set(completeText)
    # We get the  actual value  to  evaluate  in the trigonometric function
    value = eval(completeTextWithDot)
    fulloperation = function + "(" + str(value) + ")"
    solution = eval(fulloperation)
    solutionTextWithoutDot = str(solution).replace(".", ",")
    firstScreenText.set(solutionTextWithoutDot)
    secondScreenText.set("0")
    operationMade = True
    actualHistoryOperation.set(function + "(" + str(value) + ")" + " = "+ solutionTextWithoutDot + "\n\n")
    addHistory()
    return



def insertPI():
    firstScreenText.set("3,141592")
    return



def usingDMS():
    firstScreen = firstScreenText.get()
    secondScreen = secondScreenText.get()
    if secondScreen != "0":
        new = secondScreen + firstScreen
    else:
        new = firstScreen
    secondScreenText.set(new)
    firstScreenText.set(0)
    value = float(eval(str(secondScreenText.get()).replace(",", ".")))
    mnt,sec = divmod(value*3600,60)
    deg,mnt = divmod(mnt,60)
    result = (deg, mnt, sec)
    actualHistoryOperation.set("dms(" + str(value) + ") = " + str(result))
    addHistory()
    return
    


def usingDEG():
    firstScreen = firstScreenText.get()
    secondScreen = secondScreenText.get()
    if secondScreen != "0":
        new = secondScreen + firstScreen
    else:
        new = firstScreen
    secondScreenText.set(new)
    firstScreenText.set(0)
    value = float(eval(str(secondScreenText.get()).replace(",", ".")))
    result = ((value *  180) / 3.1412)
    actualHistoryOperation.set("deg(" + str(value) + ") = " + str(result))
    addHistory()
    return



def usingFactorial():
    firstScreen = firstScreenText.get()
    secondScreen = secondScreenText.get()
    if secondScreen != "0":
        new = secondScreen + firstScreen
    else:
        new = firstScreen
    secondScreenText.set(new)
    firstScreenText.set(0)
    value = float(eval(str(secondScreenText.get()).replace(",", ".")))
    result = math.factorial(value)
    actualHistoryOperation.set("fact(" + str(value) + ") = " + str(result))
    addHistory()
    return



def using1X():
    firstScreen = firstScreenText.get()
    firstScreenText.set(firstScreen + "1/")
    return



def usingPlusMinus():
    firstScreen = firstScreenText.get()
    if firstScreen[0] == "-":
        firstScreenText.set(firstScreen[1:])
    else:
        firstScreenText.set("-" + firstScreen)
    return



def plotFunction():
    global a
    global canvas
    global toolbar
    global xminsize
    global xmaxsize
    global yminsize
    global ymaxsize
    chosenColor = colorSelected.get()
    chosenFunction = function.get()
    x = array(arange(int(xminsize.get()), int(xmaxsize.get())+1, 0.1))
    y = eval(chosenFunction)
    a.clear()
    a.set_xlim([int(xminsize.get()), int(xmaxsize.get())])
    a.set_ylim([int(yminsize.get()), int(ymaxsize.get())])
    a.plot(x,y, color = chosenColor)
    canvas.draw()
    canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
    toolbar = NavigationToolbar2Tk(canvas, plottingFrame)
    canvas._tkcanvas.pack(side = TOP, fill = BOTH, expand = True)
    return



#                     Buttons 
# Clean history button
buttonClearHistory = Button(historyFrame, font = buttonsFont, text = "Clear History", bg = "#20221f", height = 1, width = 35, fg = "white", command = lambda:clearHistory(),activebackground = "#383737", activeforeground = "white")
buttonClearHistory.grid(row = 0, column = 0, sticky = "EWNS")


# FIRST ROW
firstRowButtons.columnconfigure((0,1,2), weight=1)

buttonDEG = Button(firstRowButtons, font = buttonsFont, textvariable = DEGButtonText, width = 10, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:changeDEGtext())
buttonDEG.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonHYP = Button(firstRowButtons, font = buttonsFont, text = "HYP", width = 10, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:changeTrigonometricFunctionsText())
buttonHYP.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonFE = Button(firstRowButtons, font = buttonsFont, text = "F-E", width = 10, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white")
buttonFE.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")



# SECOND ROW

secondRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)

buttonX2 = Button(secondRowButtons, font = buttonsFont, text = "X^2", width = 2, height = 4, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:clickOnOperation("**2"))
buttonX2.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonXY = Button(secondRowButtons, font = buttonsFont, text = "X^Y", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:clickOnOperation("**"))
buttonXY.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonSin = Button(secondRowButtons, font = buttonsFont, textvariable = SINButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:_sin())
buttonSin.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonCos = Button(secondRowButtons, font = buttonsFont, textvariable = COSButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:_cos())
buttonCos.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonTan = Button(secondRowButtons, font = buttonsFont, textvariable = TANButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:_tan())
buttonTan.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonCE = Button(secondRowButtons, font = buttonsFont, text = "CE", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:CE())
buttonCE.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonC = Button(secondRowButtons, font = buttonsFont, text = "C", width = 2, height = 3, bg = "#20221f", fg = "white", command = lambda:C(), relief = "raised",  activebackground = "#383737", activeforeground = "white")
buttonC.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonDEL = Button(secondRowButtons, font = buttonsFont, text = "DEL", width = 2, height = 3, bg = "#20221f", fg = "white", command = lambda:Delete(), relief = "raised",  activebackground = "#383737", activeforeground = "white")
buttonDEL.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonDiv = Button(secondRowButtons, font = buttonsFont, text = "/", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:clickOnOperation("/"))
buttonDiv.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")



# THIRD ROW
thirdRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)  # when window is resized

buttonX3 = Button(thirdRowButtons, font = buttonsFont, text = "X^3", width = 2, height = 4, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:clickOnOperation("**3"))
buttonX3.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonSQY = Button(thirdRowButtons, font = buttonsFont, text = "sqy()", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:clickOnOperation("**(1/"))
buttonSQY.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonSin1 = Button(thirdRowButtons, font = buttonsFont, textvariable = ASINButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:asin())
buttonSin1.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonCos1 = Button(thirdRowButtons, font = buttonsFont, textvariable = ACOSButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:acos())
buttonCos1.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonTan1 = Button(thirdRowButtons, font = buttonsFont, textvariable = ATANButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:atan())
buttonTan1.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button7 = Button(thirdRowButtons, font = buttonsFont, text = "7", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(7), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button7.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button8 = Button(thirdRowButtons, font = buttonsFont, text = "8", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(8), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button8.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button9 = Button(thirdRowButtons, font = buttonsFont, text = "9", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(9), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button9.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonMult = Button(thirdRowButtons, font = buttonsFont, text = "*", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:clickOnOperation("*"))
buttonMult.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")




# FOURTH ROW
fourthRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)  # when window is resized

buttonSQRT = Button(fourthRowButtons, font = buttonsFont, text = "sqrt()", width = 2, height = 4, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:clickOnOperation("**(1/2)"))
buttonSQRT.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button10X = Button(fourthRowButtons, font = buttonsFont, text = "10^X", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:clickOnOperation("*10**"))
button10X.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonLog = Button(fourthRowButtons, font = buttonsFont, text = "log()", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:calculateLogarithmExponential("log10"))
buttonLog.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonExp = Button(fourthRowButtons, font = buttonsFont, text = "exp()", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:calculateLogarithmExponential("exp"))
buttonExp.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonMod = Button(fourthRowButtons, font = buttonsFont, text = "Mod", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:clickOnOperation("%"))
buttonMod.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button4 = Button(fourthRowButtons, font = buttonsFont, text = "4", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(4), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button4.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button5 = Button(fourthRowButtons, font = buttonsFont, text = "5", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(5), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button5.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button6 = Button(fourthRowButtons, font = buttonsFont, text = "6", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(6), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button6.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonSubst = Button(fourthRowButtons, font = buttonsFont, text = "-", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:clickOnOperation("-"))
buttonSubst.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")



# FIFTH ROW
fifthRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)  # when window is resized

button1X = Button(fifthRowButtons, font = buttonsFont, text = "1/x", width = 2, height = 4, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:using1X())
button1X.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonEx = Button(fifthRowButtons, font = buttonsFont, text = "e^X", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:clickOnOperation("exp("))
buttonEx.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonLn = Button(fifthRowButtons, font = buttonsFont, text = "ln()", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:calculateLogarithmExponential("log"))
buttonLn.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonDMS = Button(fifthRowButtons, font = buttonsFont, text = "dms", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:usingDMS())
buttonDMS.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonDEG = Button(fifthRowButtons, font = buttonsFont, text = "deg", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:usingDEG())
buttonDEG.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button1 = Button(fifthRowButtons, font = buttonsFont, text = "1", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(1), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button1.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button2 = Button(fifthRowButtons, font = buttonsFont, text = "2", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(2), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button2.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button3 = Button(fifthRowButtons, font = buttonsFont, text = "3", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(3), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button3.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonAdd = Button(fifthRowButtons, font = buttonsFont, text = "+", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:clickOnOperation("+"))
buttonAdd.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")


# SIXTH ROW
sixthRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)  # when window is resized

buttonX = Button(sixthRowButtons, font = buttonsFont, text = "X", width = 2, height = 4, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white")
buttonX.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonPI = Button(sixthRowButtons, font = buttonsFont, text = "pi", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:insertPI())
buttonPI.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonFact = Button(sixthRowButtons, font = buttonsFont, text = "n!", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:usingFactorial())
buttonFact.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonP1 = Button(sixthRowButtons, font = buttonsFont, text = "(", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:firstScreenTextSet("("))
buttonP1.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonP2 = Button(sixthRowButtons, font = buttonsFont, text = ")", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:firstScreenTextSet(")"))
buttonP2.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonPM = Button(sixthRowButtons, font = buttonsFont, text = "+-", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:usingPlusMinus())
buttonPM.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

button0 = Button(sixthRowButtons, font = buttonsFont, text = "0", width = 2, height = 3, bg = "black", fg = "white", command = lambda:firstScreenTextSet(0), relief = "raised",  activebackground = "#383737", activeforeground = "white")
button0.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonComma = Button(sixthRowButtons, font = buttonsFont, text = ",", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command=lambda:firstScreenTextSet(","))
buttonComma.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

buttonEqual = Button(sixthRowButtons, font = buttonsFont, text = "=", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:calculate())
buttonEqual.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")


# PLOTTING FRAME LABELS, ENTRIES, AND BUTTONS

buttonPLOT = Button(thirdRowFunctions2Plot, font = plotButtonFont, text = "PLOT", width = 5, height = 2, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:plotFunction())
buttonPLOT.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")

Xminlabel = Label(firstRowFunctions2Plot, font = buttonsFont, text = "X min:", width = 6, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
Xminlabel.pack(side = LEFT, padx = 3)

XminEntry = Entry(firstRowFunctions2Plot, width = 6, textvariable = xminsize)
XminEntry.pack(side = LEFT, padx = 3)

Yminlabel = Label(firstRowFunctions2Plot, font = buttonsFont, text = "Y min:", width = 6, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
Yminlabel.pack(side = LEFT, padx = 3)

YminEntry = Entry(firstRowFunctions2Plot, width = 6, textvariable = yminsize)
YminEntry.pack(side = LEFT, padx = 3)

Xmaxlabel = Label(secondRowFunctions2Plot, font = buttonsFont, text = "X max:", width = 6, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
Xmaxlabel.pack(side = LEFT, padx = 3)

XmaxEntry = Entry(secondRowFunctions2Plot, width = 6, textvariable = xmaxsize)
XmaxEntry.pack(side = LEFT, padx = 3)

Ymaxlabel = Label(secondRowFunctions2Plot, font = buttonsFont, text = "Y max:", width = 6, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
Ymaxlabel.pack(side = LEFT, padx = 3)

YmaxEntry = Entry(secondRowFunctions2Plot, width = 6, textvariable = ymaxsize)
YmaxEntry.pack(side = LEFT, padx = 3)

Functionlabel = Label(firstRowFunctions2Plot, font = buttonsFont, text = "Function:", width = 8, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
Functionlabel.pack(side = LEFT, padx = 3)

FunctionEntry = Entry(firstRowFunctions2Plot, textvariable = function)
FunctionEntry.pack(side = LEFT, padx = 3)

spinbox = Spinbox(firstRowFunctions2Plot, values=a_list, textvariable=colorSelected)
spinbox.config(state = "readonly", background = "#20221f", foreground = "#20221f")
spinbox.pack(side = LEFT, padx = 3)

#                     Main Loop 
mainWindow.mainloop()
