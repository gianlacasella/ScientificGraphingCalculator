from tkinter import Frame, LEFT, TOP, BOTTOM


def CalculatorFrame(mainWindow):
    calculatorFrame = Frame(mainWindow)
    calculatorFrame.pack_propagate(0)
    calculatorFrame.config(width = "500", height = "700", bg = "grey")
    calculatorFrame.pack(fill="y", expand="True", side = LEFT)
    return calculatorFrame
    
def HistoryFrame(mainWindow):
    historyFrame = Frame(mainWindow)
    historyFrame.pack_propagate(0)
    historyFrame.config(width = "300", height = "500", bg = "black", borderwidth = "3")
    historyFrame.pack(fill="y", expand="True", side = LEFT)
    return historyFrame
    
def PlottingFrame(mainWindow):
    plottingFrame = Frame(mainWindow)
    plottingFrame.pack_propagate(0)
    plottingFrame.config(width = "700", height = "700", bg = "#20221f")
    plottingFrame.pack(fill="y", expand="True", side = LEFT)
    return plottingFrame
    
def Functions2PlotFrame(plottingFrame):
    functions2Plot = Frame(plottingFrame)
    functions2Plot.pack_propagate(0)
    functions2Plot.config(width = "700", height = "163", bg = "#20221f")
    functions2Plot.pack(fill="x", expand="True", side = TOP)
    return functions2Plot
    
def FirstRowFunctions2PlotFrame(functions2Plot):
    firstRowFunctions2Plot = Frame(functions2Plot)
    firstRowFunctions2Plot.pack_propagate(0)
    firstRowFunctions2Plot.config(width = "670", height = "40", bg = "#20221f")
    firstRowFunctions2Plot.pack(expand="True", side = TOP)
    return firstRowFunctions2Plot
    
    
def SecondRowFunctions2PlotFrame(functions2Plot):
    secondRowFunctions2Plot = Frame(functions2Plot)
    secondRowFunctions2Plot.pack_propagate(0)
    secondRowFunctions2Plot.config(width = "670", height = "40", bg = "#20221f")
    secondRowFunctions2Plot.pack(expand="True")
    return secondRowFunctions2Plot
    
    
def ThirdRowFunctions2PlotFrame(functions2Plot):
    thirdRowFunctions2Plot = Frame(functions2Plot)
    thirdRowFunctions2Plot.pack_propagate(0)
    thirdRowFunctions2Plot.config(width = "120", height = "80", bg = "#20221f")
    thirdRowFunctions2Plot.pack(expand="True", side = BOTTOM)
    return thirdRowFunctions2Plot
    
    
def ScreensFrame(calculatorFrame):
    screensFrame = Frame(calculatorFrame)
    screensFrame.pack_propagate(0)
    screensFrame.config(width = "500", height = "150", bg = "#20221f")
    screensFrame.grid(row = 1, column = 1)
    screensFrame.pack(fill="both", expand = "True")
    return screensFrame
    
def ButtonsFrame(calculatorFrame):
    buttonsFrame = Frame(calculatorFrame)
    buttonsFrame.pack_propagate(0)
    buttonsFrame.config(width = "500", height = "550", bg = "#20221f")
    buttonsFrame.grid(row = 2, column = 1)
    buttonsFrame.pack(fill="both", expand = "True")
    return buttonsFrame
    
    
def FirstRowButtonsFrame(buttonsFrame):
    firstRowButtons = Frame(buttonsFrame)
    firstRowButtons.pack_propagate(0)
    firstRowButtons.config(width = "500", height = "200", bg = "grey")
    firstRowButtons.grid(row = 0,  column = 0, columnspan = 9)
    firstRowButtons.pack(fill = "x",expand = "True")
    return firstRowButtons
    
    
def SecondRowButtonsFrame(buttonsFrame):
    secondRowButtons = Frame(buttonsFrame)
    secondRowButtons.pack_propagate(0)
    secondRowButtons.config(width = "500", height = "200", bg = "grey")
    secondRowButtons.grid(row = 1,  column = 0, columnspan = 9)
    secondRowButtons.pack(fill = "x",expand = "True")
    return secondRowButtons
    
    
def ThirdRowButtonsFrame(buttonsFrame):
    thirdRowButtons = Frame(buttonsFrame)
    thirdRowButtons.pack_propagate(0)
    thirdRowButtons.config(width = "500", height = "200", bg = "grey")
    thirdRowButtons.grid(row = 2,  column = 0, columnspan = 9)
    thirdRowButtons.pack(fill = "x",expand = "True")
    return thirdRowButtons
    
    
def FourthRowButtonsFrame(buttonsFrame):
    fourthRowButtons = Frame(buttonsFrame)
    fourthRowButtons.pack_propagate(0)
    fourthRowButtons.config(width = "500", height = "200", bg = "grey")
    fourthRowButtons.grid(row = 3,  column = 0, columnspan = 9)
    fourthRowButtons.pack(fill = "x",expand = "True")
    return fourthRowButtons
    
    
def FifthRowButtonsFrame(buttonsFrame):
    fifthRowButtons = Frame(buttonsFrame)
    fifthRowButtons.pack_propagate(0)
    fifthRowButtons.config(width = "500", height = "200", bg = "grey")
    fifthRowButtons.grid(row = 4,  column = 0, columnspan = 9)
    fifthRowButtons.pack(fill = "x",expand = "True")
    return fifthRowButtons
    
    
def SixthRowButtonsFrame(buttonsFrame):
    sixthRowButtons = Frame(buttonsFrame)
    sixthRowButtons.pack_propagate(0)
    sixthRowButtons.config(width = "500", height = "200", bg = "grey")
    sixthRowButtons.grid(row = 5,  column = 0, columnspan = 9)
    sixthRowButtons.pack(fill = "x",expand = "True")
    return sixthRowButtons
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    