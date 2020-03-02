from tkinter import Button, Label, Entry, Spinbox, LEFT

def CreateButtons(window):
    # Clean history button
    buttonClearHistory = Button(window.historyFrame, font = window.buttonsFont, text = "Clear History", bg = "#20221f", height = 1, width = 35, fg = "white", command = lambda:window.clearHistory(),activebackground = "#383737", activeforeground = "white")
    buttonClearHistory.grid(row = 0, column = 0, sticky = "EWNS")
    
    
    # First row of buttons inside the calculatorFrame
    window.firstRowButtons.columnconfigure((0,1,2), weight=1)
    
    window.buttonDEG = Button(window.firstRowButtons, font = window.buttonsFont, textvariable = window.DEGButtonText, width = 10, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.changeDEGtext())
    window.buttonDEG.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonHYP = Button(window.firstRowButtons, font = window.buttonsFont, text = "HYP", width = 10, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.changeTrigonometricFunctionsText())
    window.buttonHYP.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonFE = Button(window.firstRowButtons, font = window.buttonsFont, text = "F-E", width = 10, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.buttonFE.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    
    
    # Second row of buttons inside the calculatorFrame
    window.secondRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)
    
    window.buttonX2 = Button(window.secondRowButtons, font = window.buttonsFont, text = "X^2", width = 5, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.clickOnOperation("**2"))
    window.buttonX2.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonXY = Button(window.secondRowButtons, font = window.buttonsFont, text = "X^Y", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.clickOnOperation("**"))
    window.buttonXY.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonSin = Button(window.secondRowButtons, font = window.buttonsFont, textvariable = window.SINButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window._sin())
    window.buttonSin.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonCos = Button(window.secondRowButtons, font = window.buttonsFont, textvariable = window.COSButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window._cos())
    window.buttonCos.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonTan = Button(window.secondRowButtons, font = window.buttonsFont, textvariable = window.TANButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window._tan())
    window.buttonTan.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonCE = Button(window.secondRowButtons, font = window.buttonsFont, text = "CE", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.CE())
    window.buttonCE.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonC = Button(window.secondRowButtons, font = window.buttonsFont, text = "C", width = 2, height = 3, bg = "#20221f", fg = "white", command = lambda:window.C(), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.buttonC.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonDEL = Button(window.secondRowButtons, font = window.buttonsFont, text = "DEL", width = 2, height = 3, bg = "#20221f", fg = "white", command = lambda:window.Delete(), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.buttonDEL.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonDiv = Button(window.secondRowButtons, font = window.buttonsFont, text = "/", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.clickOnOperation("/"))
    window.buttonDiv.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    
    
    # Third row of buttons inside the calculatorFrame
    window.thirdRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)  # when window is resized
    
    window.buttonX3 = Button(window.thirdRowButtons, font = window.buttonsFont, text = "X^3", width = 5, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.clickOnOperation("**3"))
    window.buttonX3.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonSQY = Button(window.thirdRowButtons, font = window.buttonsFont, text = "sqy()", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.clickOnOperation("**(1/"))
    window.buttonSQY.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonSin1 = Button(window.thirdRowButtons, font = window.buttonsFont, textvariable = window.ASINButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.asin())
    window.buttonSin1.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonCos1 = Button(window.thirdRowButtons, font = window.buttonsFont, textvariable = window.ACOSButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.acos())
    window.buttonCos1.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonTan1 = Button(window.thirdRowButtons, font = window.buttonsFont, textvariable = window.ATANButtonText, width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.atan())
    window.buttonTan1.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button7 = Button(window.thirdRowButtons, font = window.buttonsFont, text = "7", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(7), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button7.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button8 = Button(window.thirdRowButtons, font = window.buttonsFont, text = "8", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(8), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button8.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button9 = Button(window.thirdRowButtons, font = window.buttonsFont, text = "9", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(9), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button9.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonMult = Button(window.thirdRowButtons, font = window.buttonsFont, text = "*", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.clickOnOperation("*"))
    window.buttonMult.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    
    
    
    # Fourth row of buttons inside the calculatorFrame
    window.fourthRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)  # when window is resized
    
    window.buttonSQRT = Button(window.fourthRowButtons, font = window.buttonsFont, text = "sqrt()", width = 5, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.clickOnOperation("**(1/2)"))
    window.buttonSQRT.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button10X = Button(window.fourthRowButtons, font = window.buttonsFont, text = "10^X", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.clickOnOperation("*10**"))
    window.button10X.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonLog = Button(window.fourthRowButtons, font = window.buttonsFont, text = "log()", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.calculateLogarithmExponential("log10"))
    window.buttonLog.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonExp = Button(window.fourthRowButtons, font = window.buttonsFont, text = "exp()", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.calculateLogarithmExponential("exp"))
    window.buttonExp.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonMod = Button(window.fourthRowButtons, font = window.buttonsFont, text = "Mod", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.clickOnOperation("%"))
    window.buttonMod.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button4 = Button(window.fourthRowButtons, font = window.buttonsFont, text = "4", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(4), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button4.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button5 = Button(window.fourthRowButtons, font = window.buttonsFont, text = "5", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(5), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button5.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button6 = Button(window.fourthRowButtons, font = window.buttonsFont, text = "6", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(6), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button6.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonSubst = Button(window.fourthRowButtons, font = window.buttonsFont, text = "-", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.clickOnOperation("-"))
    window.buttonSubst.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    
    
    # Fifth row of buttons inside the calculatorFrame
    window.fifthRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)  # when window is resized
    
    window.button1X = Button(window.fifthRowButtons, font = window.buttonsFont, text = "1/x", width = 5, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.using1X())
    window.button1X.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonEx = Button(window.fifthRowButtons, font = window.buttonsFont, text = "e^X", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.clickOnOperation("exp("))
    window.buttonEx.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonLn = Button(window.fifthRowButtons, font = window.buttonsFont, text = "ln()", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.calculateLogarithmExponential("log"))
    window.buttonLn.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonDMS = Button(window.fifthRowButtons, font = window.buttonsFont, text = "dms", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.usingDMS())
    window.buttonDMS.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonDEG = Button(window.fifthRowButtons, font = window.buttonsFont, text = "deg", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.usingDEG())
    window.buttonDEG.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button1 = Button(window.fifthRowButtons, font = window.buttonsFont, text = "1", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(1), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button1.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button2 = Button(window.fifthRowButtons, font = window.buttonsFont, text = "2", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(2), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button2.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button3 = Button(window.fifthRowButtons, font = window.buttonsFont, text = "3", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(3), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button3.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonAdd = Button(window.fifthRowButtons, font = window.buttonsFont, text = "+", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.clickOnOperation("+"))
    window.buttonAdd.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    
    # Sixth row of buttons inside the calculatorFrame
    window.sixthRowButtons.columnconfigure((8,1,2,3,4,5,6,7), weight=1)  # when window is resized
    
    window.buttonX = Button(window.sixthRowButtons, font = window.buttonsFont, text = "X", width = 5, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.buttonX.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonPI = Button(window.sixthRowButtons, font = window.buttonsFont, text = "pi", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.insertPI())
    window.buttonPI.grid(row = 0, column = 1, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonFact = Button(window.sixthRowButtons, font = window.buttonsFont, text = "n!", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.usingFactorial())
    window.buttonFact.grid(row = 0, column = 2, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonP1 = Button(window.sixthRowButtons, font = window.buttonsFont, text = "(", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.firstScreenTextSet("("))
    window.buttonP1.grid(row = 0, column = 3, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonP2 = Button(window.sixthRowButtons, font = window.buttonsFont, text = ")", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white",  command = lambda:window.firstScreenTextSet(")"))
    window.buttonP2.grid(row = 0, column = 4, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonPM = Button(window.sixthRowButtons, font = window.buttonsFont, text = "+-", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.usingPlusMinus())
    window.buttonPM.grid(row = 0, column = 5, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.button0 = Button(window.sixthRowButtons, font = window.buttonsFont, text = "0", width = 2, height = 3, bg = "black", fg = "white", command = lambda:window.firstScreenTextSet(0), relief = "raised",  activebackground = "#383737", activeforeground = "white")
    window.button0.grid(row = 0, column = 6, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonComma = Button(window.sixthRowButtons, font = window.buttonsFont, text = ",", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command=lambda:window.firstScreenTextSet(","))
    window.buttonComma.grid(row = 0, column = 7, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    window.buttonEqual = Button(window.sixthRowButtons, font = window.buttonsFont, text = "=", width = 2, height = 3, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.calculate())
    window.buttonEqual.grid(row = 0, column = 8, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    
    
    # PLOTTING STUFF SECTION ============================================================================================================================================================================================================
    
    # PLOT button on the plottingFrame
    window.buttonPLOT = Button(window.thirdRowFunctions2Plot, font = window.plotButtonFont, text = "PLOT", width = 5, height = 2, bg = "#20221f", fg = "white", relief = "raised",  activebackground = "#383737", activeforeground = "white", command = lambda:window.plotFunction())
    window.buttonPLOT.grid(row = 0, column = 0, padx = 0, pady = 0, columnspan = 1, sticky = "EWNS")
    
    # Xmin label and entry on the plottingFrame
    window.Xminlabel = Label(window.firstRowFunctions2Plot, font = window.buttonsFont, text = "X min:", width = 6, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
    window.Xminlabel.pack(side = LEFT, padx = 3)
    
    window.XminEntry = Entry(window.firstRowFunctions2Plot, width = 6, textvariable = window.xminsize)
    window.XminEntry.pack(side = LEFT, padx = 3)
    
    # Ymin label and entry on the plottingFrame
    window.Yminlabel = Label(window.firstRowFunctions2Plot, font = window.buttonsFont, text = "Y min:", width = 6, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
    window.Yminlabel.pack(side = LEFT, padx = 3)
    
    window.YminEntry = Entry(window.firstRowFunctions2Plot, width = 6, textvariable = window.yminsize)
    window.YminEntry.pack(side = LEFT, padx = 3)
    
    # Xmax label and entry on the plottingFrame
    window.Xmaxlabel = Label(window.secondRowFunctions2Plot, font = window.buttonsFont, text = "X max:", width = 6, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
    window.Xmaxlabel.pack(side = LEFT, padx = 3)
    
    window.XmaxEntry = Entry(window.secondRowFunctions2Plot, width = 6, textvariable = window.xmaxsize)
    window.XmaxEntry.pack(side = LEFT, padx = 3)
    
    # Ymax label and entry on the plottingFrame
    window.Ymaxlabel = Label(window.secondRowFunctions2Plot, font = window.buttonsFont, text = "Y max:", width = 6, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
    window.Ymaxlabel.pack(side = LEFT, padx = 3)
    
    window.YmaxEntry = Entry(window.secondRowFunctions2Plot, width = 6, textvariable = window.ymaxsize)
    window.YmaxEntry.pack(side = LEFT, padx = 3)
    
    # Function label and entry on the plottingFrame
    window.Functionlabel = Label(window.firstRowFunctions2Plot, font = window.buttonsFont, text = "Function:", width = 8, height = 2, bg = "#20221f", fg = "white", activeforeground = "white")
    window.Functionlabel.pack(side = LEFT, padx = 3)
    
    window.FunctionEntry = Entry(window.firstRowFunctions2Plot, textvariable = window.function)
    window.FunctionEntry.pack(side = LEFT, padx = 3)
    
    # Spinbox to select graph's color on the plottingFrame
    window.spinbox = Spinbox(window.firstRowFunctions2Plot, values=window.a_list, textvariable=window.colorSelected)
    window.spinbox.config(state = "readonly", background = "#20221f", foreground = "#20221f")
    window.spinbox.pack(side = LEFT, padx = 3)

    return