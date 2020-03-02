from tkinter import Tk, RIGHT, BOTTOM, BOTH, TOP, StringVar, font, Text, DISABLED, Scrollbar, Y
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import frameCreator

def CreateWindow(window):
        #Main window and setting props
        window.mainWindow = Tk()
        window.mainWindow.title("Scientific Plotting Calculator v1.0")
        window.mainWindow.resizable(False, False)
        
        # Fonts
        window.mainWindowFont = font.Font(family = "Verdana", size = 10)
        window.secondaryWindowFont = font.Font(family = "Verdana", size = 10)
        window.buttonsFont = font.Font(family = "Verdana", size = 10, weight = "bold")
        window.amplifiedButtonsFont = font.Font(family = "Verdana", size = 12, weight = "bold")
        window.historyTextFont = font.Font(family = "Verdana", size = 14, weight = "bold")
        window.plotButtonFont = font.Font(family= "Verdana", size = 16, weight = "bold")
        
        # Booleans, StringVar and lists
        window.operationFilling = False
        window.parenthesisOpen = False
        window.actualHistoryOperation = StringVar()
        window.operationMade = False
        window.a_list = ['red', 'blue', 'green', 'black', 'grey', 'yellow', 'cyan', 'magenta']
        window.colorSelected = StringVar()
        window.xminsize = StringVar()
        window.yminsize = StringVar()
        window.xmaxsize = StringVar()
        window.ymaxsize = StringVar()
        window.function = StringVar()
        window.DEGButtonText = StringVar()
        window.ASINButtonText = StringVar()
        window.ACOSButtonText = StringVar()
        window.ATANButtonText = StringVar()
        window.SINButtonText = StringVar()
        window.COSButtonText = StringVar()
        window.TANButtonText = StringVar()
        window.firstScreenText = StringVar()
        window.secondScreenText = StringVar()
        
        # Frames
        window.calculatorFrame = frameCreator.CalculatorFrame(window.mainWindow)
        window.historyFrame = frameCreator.HistoryFrame(window.mainWindow)
        window.plottingFrame = frameCreator.PlottingFrame(window.mainWindow)
        window.functions2Plot = frameCreator.Functions2PlotFrame(window.plottingFrame)
        window.firstRowFunctions2Plot = frameCreator.FirstRowFunctions2PlotFrame(window.functions2Plot)
        window.secondRowFunctions2Plot = frameCreator.SecondRowFunctions2PlotFrame(window.functions2Plot)
        window.thirdRowFunctions2Plot = frameCreator.ThirdRowFunctions2PlotFrame(window.functions2Plot)
        window.screensFrame = frameCreator.ScreensFrame(window.calculatorFrame)
        window.buttonsFrame = frameCreator.ButtonsFrame(window.calculatorFrame)
        window.firstRowButtons = frameCreator.FirstRowButtonsFrame(window.buttonsFrame)
        window.secondRowButtons = frameCreator.SecondRowButtonsFrame(window.buttonsFrame)
        window.thirdRowButtons = frameCreator.ThirdRowButtonsFrame(window.buttonsFrame)
        window.fourthRowButtons = frameCreator.FourthRowButtonsFrame(window.buttonsFrame)
        window.fifthRowButtons = frameCreator.FifthRowButtonsFrame(window.buttonsFrame)
        window.sixthRowButtons = frameCreator.SixthRowButtonsFrame(window.buttonsFrame)
        
        #Text and scrollbar

        window.history = Text(window.historyFrame, width = "300" , height = "100", fg = "white", bg = "black", font = window.historyTextFont)
        window.history.config(state = DISABLED)
        window.history.grid(row = 1, column = 0)
        window.textScrollbar = Scrollbar(window.historyFrame)
        window.textScrollbar.config(background = "#20221f", activebackground = "#20221f", activerelief = "sunken")
        window.textScrollbar.pack(side=RIGHT, fill=Y)
        window.history.config(yscrollcommand=window.textScrollbar.set)
        window.textScrollbar.config(command=window.history.yview)
        window.history.pack()
        
        # Plotting an empty graph with matplotlib, into the tkinter window
        window.firstPlot = False
        window.myFigure = Figure(figsize=(5,5), dpi = 100)
        window.a = window.myFigure.add_subplot(111)
        window.a.plot([],[])
        window.canvas = FigureCanvasTkAgg(window.myFigure, window.plottingFrame)
        window.canvas.draw()
        window.canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
        window.toolbar = NavigationToolbar2TkAgg(window.canvas, window.plottingFrame)
        window.canvas._tkcanvas.pack(side = TOP, fill = BOTH, expand = True)