# Usefull modules and tools 
from tkinter import BOTTOM, BOTH, TOP, Label, DISABLED, NORMAL, INSERT, END, messagebox
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
import buttonsCreator
import windowCreator
from numpy import *
import math


class App:
    def __init__(self):
        windowCreator.CreateWindow(self)
        self.FirstExecutionSettings()
        self.SetScreens()
        buttonsCreator.CreateButtons(self)
        self.mainWindow.mainloop()
        
    def FirstExecutionSettings(self):
        self.firstScreenText.set("0")
        self.secondScreenText.set("0")
        self.DEGButtonText.set("DEG")
        self.ASINButtonText.set("asin()")
        self.ACOSButtonText.set("acos()")
        self.ATANButtonText.set("atan()")
        self.SINButtonText.set("sin()")
        self.COSButtonText.set("cos()")
        self.TANButtonText.set("tan()")
        
    def SetScreens(self):
        # First screen
        self.firstScreen = Label(self.screensFrame, textvariable = self.firstScreenText, font = self.mainWindowFont, anchor = "e")
        self.firstScreen.grid(row = 1, column = 0, padx = 0, pady = 2)
        self.firstScreen.config(background = "black", fg = "white", justify = "right",height = "5", width = "62")

        # Second screen
        self.secondScreen = Label(self.screensFrame, textvariable = self.secondScreenText, font = self.secondaryWindowFont, anchor = "e")
        self.secondScreen.grid(row = 0, column = 0, padx = 0, pady = 2)
        self.secondScreen.config(background = "#20221f", fg = "white", justify = "right",height = "5", width = "62")
        
    # Function to add elements to the firstScreenText
    def firstScreenTextSet(self, num):
        # We need global variables
        global operationFilling
        global parenthesisOpen
        global operationMade
        # Analizing if thera are parenthesis
        if num == "(":
            self.parenthesisOpen = True
        elif  num == ")":
            self.parenthesisOpen = False
        if operationMade == True:
            self.firstScreenText.set("")
            self.operationMade = False
        # We get  whats on the second screen
        self.textSecondScreen = self.secondScreenText.get()
        if self.textSecondScreen[-1] == True and self.operationFilling == True:
            self.firstScreenText.set("")
            self.operationFilling = True
        if(self.firstScreenText.get() == "0" and num == 0):
            return
        elif(self.firstScreenText.get() == "0" and num != 0):
            self.firstScreenText.set("")
            self.firstScreenText.set(self.firstScreenText.get() + str(num))
            self.operationFilling= False
        else:
            self.firstScreenText.set(self.firstScreenText.get() + str(num))
            self.operationFilling = False
        return
        
    
    # Function to use on C button
    def C(self):
        self.firstScreenText.set("0")
        self.secondScreenText.set("0")
        return
        
    # Function to use de Delete button
    def Delete(self):
        actualNumber = self.firstScreenText.get()
        actualNumber = actualNumber[:-1]
        self.firstScreenText.set(actualNumber)
        return
        
        
    def clickOnOperation(self, operation):
        if operation == "exp(":
            self.firstScreenText.set("")
        elif operation == "factorial(":
            self.firstScreenText.set("")
        textFirstScreen = self.firstScreenText.get()
        if textFirstScreen == "nan":
            textFirstScreen = ""
        textFirstScreen += operation
        self.firstScreenText.set(textFirstScreen)
        if self.parenthesisOpen == True:
            return
        self.firstScreenText.set("")
        textSecondScreen = self.secondScreenText.get()
        if textSecondScreen == "0":
            self.secondScreenText.set("")
        textSecondScreen = self.secondScreenText.get()
        textSecondScreen += textFirstScreen
        self.secondScreenText.set(textSecondScreen)
        return
        
    # Function to change the DEG button text to RAD (user clicks on DEG button)
    def changeDEGtext(self):
        if self.DEGButtonText.get() == "DEG":
            self.DEGButtonText.set("RAD")
        else:
            self.DEGButtonText.set("DEG")
        return
        
        
    # Function to change the trigonometric functions buttons text (user clicks on RAD button) 
    def changeTrigonometricFunctionsText(self):
        if self.ASINButtonText.get() == "asin()":
            self.ASINButtonText.set("asinh()")
            self.ACOSButtonText.set("acosh()")
            self.ATANButtonText.set("atanh()")
            self.SINButtonText.set("sinh()")
            self.COSButtonText.set("cosh()")
            self.TANButtonText.set("tanh()")
        else:
            self.ASINButtonText.set("asin()")
            self.ACOSButtonText.set("acos()")
            self.ATANButtonText.set("atan()")
            self.SINButtonText.set("sin()")
            self.COSButtonText.set("cos()")
            self.TANButtonText.set("tan()")
        return
        
    # Function to make CE (the users clicks on CE button)
    def CE(self):
        self.firstScreenText.set("0")
        return
    
    # Function to use to calculate the result of the operations and add them to the history
    def calculate(self):
        global operationMade
        global actualHistoryOperation
        if self.secondScreenText.get() == "0":
            self.secondScreenText.set("")
        # We get the complete operation
        completeText = self.secondScreenText.get() + self.firstScreenText.get()
        completeTextWithDot = completeText.replace(",", ".")
        self.secondScreenText.set(completeText)
        solution = eval(completeTextWithDot)
        solutionTextWithoutDot = str(solution).replace(".", ",")
        self.firstScreenText.set(solutionTextWithoutDot)
        self.secondScreenText.set("0")
        self.operationMade = True
        self.actualHistoryOperation.set(completeText+" = "+solutionTextWithoutDot + "\n\n")
        self.addHistory()
        return
        
    # Function to add an operation to the history
    def addHistory(self):
        global actualHistoryOperation
        self.history.config(state = NORMAL)
        self.history.insert(INSERT, "\n\n" + self.actualHistoryOperation.get())
        self.history.config(state = DISABLED)
        return
        
    # Function to use when the user clicks on CLEAR HISTORY button
    def clearHistory(self):
        global actualHistoryOperation
        self.actualHistoryOperation.set("")
        self.history.config(state = NORMAL)
        self.history.delete(1.0, END)
        self.history.config(state = DISABLED)
        return
        
    # Function to use when the user wants to calculate trigonometric functions
    def calculateTrigonometric(self, function):
        if self.secondScreenText.get() == "0":
            self.secondScreenText.set("")
        # We get the complete operation value for the trigonometric function
        completeText = self.secondScreenText.get() + self.firstScreenText.get()
        completeTextWithDot = completeText.replace(",", ".")
        self.secondScreenText.set(completeText)
        # We get the  actual value  to  evaluate  in the trigonometric function
        value = eval(completeTextWithDot)
        # We need to  know  if the   value   is  in rads or degrees
        typevalue = self.DEGButtonText.get()
        # Now we call solveTrigonometric
        if typevalue == "RAD":
            fulloperation = function + "(" + str(value) + ")"
        else:
            fulloperation = function + "(deg2rad(" + str(value) + "))" 
        solution = eval(fulloperation)
        solutionTextWithoutDot = str(solution).replace(".", ",")
        self.firstScreenText.set(solutionTextWithoutDot)
        self.secondScreenText.set("0")
        self.operationMade = True
        self.actualHistoryOperation.set(function + "(" + str(value) + ")" + " = "+ solutionTextWithoutDot + "\n\n")
        self.addHistory()
        return
        
        
    # Function to use when the user clicks on sin() button
    def _sin(self):
        if self.SINButtonText.get() == "sin()":
            self.calculateTrigonometric("sin")
        else:
            self.calculateTrigonometric("sinh")
        return

    # Function to use when the user clicks on cos() button
    def _cos(self):
        if self.COSButtonText.get() == "cos()":
            self.calculateTrigonometric("cos")
        else:
            self.calculateTrigonometric("cosh")
        return

    # Function to use when the user clicks on tan() button
    def _tan(self):
        if self.TANButtonText.get() == "tan()":
            self.calculateTrigonometric("tan")
        else:
            self.calculateTrigonometric("tanh")
        return

    # Function to use when the user clicks on asin() button
    def asin(self):
        if self.ASINButtonText.get() == "asin()":
            self.calculateTrigonometric("arcsin")
        else:
            self.calculateTrigonometric("arcsinh")
        return

    # Function to use when the user clicks on acos() button
    def acos(self):
        if self.ACOSButtonText.get() == "acos()":
            self.calculateTrigonometric("arccos")
        else:
            self.calculateTrigonometric("arccosh")
        return

    # Function to use when the user clicks on atan() button
    def atan(self):
        if self.ATANButtonText.get() == "atan()":
            self.calculateTrigonometric("arctan")
        else:
            self.calculateTrigonometric("arctanh")
        return

        
    # Function to use when the user wants to calculate a logarithm or an exponential 
    def calculateLogarithmExponential(self, function):
        global operationMade
        global actualHistoryOperation
        if self.secondScreenText.get() == "0":
            self.secondScreenText.set("")
        # We get the complete operation value for the logarithm function
        completeText = self.secondScreenText.get() + self.firstScreenText.get()
        completeTextWithDot = completeText.replace(",", ".")
        self.secondScreenText.set(completeText)
        # We get the  actual value  to  evaluate  in the trigonometric function
        value = eval(completeTextWithDot)
        fulloperation = function + "(" + str(value) + ")"
        solution = eval(fulloperation)
        solutionTextWithoutDot = str(solution).replace(".", ",")
        self.firstScreenText.set(solutionTextWithoutDot)
        self.secondScreenText.set("0")
        self.operationMade = True
        self.actualHistoryOperation.set(function + "(" + str(value) + ")" + " = "+ solutionTextWithoutDot + "\n\n")
        self.addHistory()
        return
        
    # Function to use when the user clicks on PI button
    def insertPI(self):
        self.firstScreenText.set("3,141592")
        return
        
    # Function to use when the user clicks on DMS button
    def usingDMS(self):
        firstScreen = self.firstScreenText.get()
        secondScreen = self.secondScreenText.get()
        if secondScreen != "0":
            new = secondScreen + firstScreen
        else:
            new = firstScreen
        self.secondScreenText.set(new)
        self.firstScreenText.set(0)
        value = float(eval(str(self.secondScreenText.get()).replace(",", ".")))
        mnt,sec = divmod(value*3600,60)
        deg,mnt = divmod(mnt,60)
        result = (deg, mnt, sec)
        self.actualHistoryOperation.set("dms(" + str(value) + ") = " + str(result))
        self.addHistory()
        return
        
    # Function to use when the user clicks on DEG button
    def usingDEG(self):
        firstScreen = self.firstScreenText.get()
        secondScreen = self.secondScreenText.get()
        if secondScreen != "0":
            new = secondScreen + firstScreen
        else:
            new = firstScreen
        self.secondScreenText.set(new)
        self.firstScreenText.set(0)
        value = float(eval(str(self.secondScreenText.get()).replace(",", ".")))
        result = ((value *  180) / 3.1412)
        self.actualHistoryOperation.set("deg(" + str(value) + ") = " + str(result))
        self.addHistory()
        return
        
    # Function to use when the user clicks on Factorial button
    def usingFactorial(self):
        firstScreen = self.firstScreenText.get()
        secondScreen = self.secondScreenText.get()
        if secondScreen != "0":
            new = secondScreen + firstScreen
        else:
            new = firstScreen
        self.secondScreenText.set(new)
        self.firstScreenText.set(0)
        value = float(eval(str(self.secondScreenText.get()).replace(",", ".")))
        result = math.factorial(value)
        self.actualHistoryOperation.set("fact(" + str(value) + ") = " + str(result))
        self.addHistory()
        return
        
    # Function to use when the user clicks on 1/x button
    def using1X(self):
        firstScreen = self.firstScreenText.get()
        self.firstScreenText.set(firstScreen + "1/")
        return
        
    # Function to use when the user clicks on +- button
    def usingPlusMinus(self):
        firstScreen = self.firstScreenText.get()
        if firstScreen[0] == "-":
            self.firstScreenText.set(firstScreen[1:])
        else:
            self.firstScreenText.set("-" + firstScreen)
        return
        
    # Function to use when the user clicks on PLOT button
    def plotFunction(self):
        chosenColor = self.colorSelected.get()
        chosenFunction = self.function.get()
        try:
            x = array(arange(int(self.xminsize.get()), int(self.xmaxsize.get())+1, 0.1))
            y = eval(chosenFunction)
        except:
            messagebox.showerror('Warning', 'There was a problem with the plotting\nPlease check the limits and the function')
        self.a.clear()
        self.a.set_xlim([int(self.xminsize.get()), int(self.xmaxsize.get())])
        self.a.set_ylim([int(self.yminsize.get()), int(self.ymaxsize.get())])
        self.a.plot(x,y, color = chosenColor)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.plottingFrame)
        self.canvas._tkcanvas.pack(side = TOP, fill = BOTH, expand = True)
        return

if __name__ == '__main__':
    myApp = App()