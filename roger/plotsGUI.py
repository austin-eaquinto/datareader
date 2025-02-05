# importing various libraries
import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QPushButton, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

FILENAME = "../data/movies_cleaned.csv"
  
class MainWindow(QDialog):
      
    # constructor
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
  
        self.setGeometry(200,200, 1600, 800)
        # a figure instance to plot on
        self.figure = plt.figure()
  
        # this is the Canvas Widget that 
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
  
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
  
        # Just some button connected to 'plot' method
        self.button = QPushButton('Plot')
          
        # adding action to the button
        self.button.clicked.connect(self.plot)
  
        # creating a Vertical Box layout
        layout = QVBoxLayout()
          
        # adding tool bar to the layout
        layout.addWidget(self.toolbar)
          
        # adding canvas to the layout
        layout.addWidget(self.canvas)
          
        # adding push button to the layout
        layout.addWidget(self.button)
          
        # setting layout to the main window
        self.setLayout(layout)
  
    # action called by the push button
    def plot(self):
          
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        genres = "Fantasy Action Adventure"
        filename_df = pd.read_csv(FILENAME)

        action_movies = filename_df[filename_df["genres"].str.contains(genres, case=False, na=False)]
        top_5_action = action_movies.sort_values("popularity", ascending=False).head(5)

        ax.bar(top_5_action["original_title"], top_5_action["popularity"], color="darkred")
        ax.set_xlabel("Movie Titles", fontsize=12)
        ax.set_ylabel("Popularity Score", fontsize=12)
        ax.set_title("Top 5 Most Popular Action Movies", fontsize=14, pad=20)
        ax.tick_params(axis='x', rotation=45, labelsize=10)
        ax.tick_params(axis='y', labelsize=10)
        self.figure.tight_layout()
  
        # refresh canvas
        self.canvas.draw()


# driver code
if __name__ == '__main__':
      
    # creating apyqt5 application
    app = QApplication(sys.argv)
  
    # creating a window object
    main_window = MainWindow()
      
    # showing the window
    main_window.show()
  
    # loop
    sys.exit(app.exec_())



"""
    IGNORE THESE FILES BELOW

"""
# class PlotWindow(FigureCanvas):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super().__init__(fig)

# # main window
# # which inherits QMainWindow
# class MainWindow(QMainWindow):
      
#     # constructor
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
  
#         self.setGeometry(200,200, 1600, 800)
#         self.button = QPushButton("Graphs", self)
#         self.label = QLabel("Menu Options", self)
#         self.initUI()
        
#     def initUI(self):
#         self.button = QPushButton("Show plot", self)
#         self.button.setGeometry(50, 50, 100,50)
#         self.button.setStyleSheet("font-size: 20px;")
#         self.button.clicked.connect(self.on_plot_click)

#         self.label.setGeometry(0,0, 1600, 80)
#         self.label.setStyleSheet("font-size: 30px")

#     def on_plot_click(self):
#         print("plot clicked on")


  
#     # action called by the push button
#     def plot(self):
          
#         self.figure.clear()
#         ax = self.figure.add_subplot(111)
#         genres = "Fantasy Action Adventure"
#         filename_df = pd.read_csv(FILENAME)

#         action_movies = filename_df[filename_df["genres"].str.contains(genres, case=False, na=False)]
#         top_5_action = action_movies.sort_values("popularity", ascending=False).head(5)

#         ax.bar(top_5_action["original_title"], top_5_action["popularity"], color="darkred")
#         ax.set_xlabel("Movie Titles", fontsize=12)
#         ax.set_ylabel("Popularity Score", fontsize=12)
#         ax.set_title("Top 5 Most Popular Action Movies", fontsize=14, pad=20)
#         ax.tick_params(axis='x', rotation=45, labelsize=10)
#         ax.tick_params(axis='y', labelsize=10)
#         self.figure.tight_layout()
  
#         # refresh canvas
#         self.canvas.draw()