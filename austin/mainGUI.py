import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QGroupBox, QStatusBar, QSizePolicy, QCheckBox, QScrollArea
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

# Note that this GUI uses QVBoxLayout rules for displaying all added widgets (buttons, text boxes, etc.)

# creates the main window
class MainWindow(QMainWindow):
    def __init__(self): # names the window as 'self'
        super().__init__()
        self.setWindowTitle("File Reader") # title of window
        self.setGeometry(200, 200, 600, 400) # size of window

        self.setMinimumSize(600, 400) # minimum size the window can be, even user adjusted
        
        centralWidget = QWidget(self) # QWidget = base class for UI objects. 'self' makes centralWidget a child of main window (or self)
        self.setCentralWidget(centralWidget) # sets centralWidget as the central widget of the main window (QMainWindow)
        # QMainWindow has a specific layout. Using setCentralWidget makes centralWidget the main content area
        # --Any other widgets and layouts added to the main window need to be added to centralWidget--

        vLayout = QVBoxLayout() # initialized the vertical layout into a variable
        centralWidget.setLayout(vLayout) # sets layout for centralWidget, .setLayout uses vLayout to vertically arrange child widgets in vertical a column
        # any widgets added to vLayout will be vertically arranged within centralWidget

        # Grouping widgets. Sections off the text boxes into their own area
        groupBox = QGroupBox("Search Parameters") # establishes the search paramaters text box
        groupBoxLayout = QVBoxLayout() # initializes the vertical layout again into a variable
        # QVBoxLayout arranges its child widgets in a vertical column, one below the other
        # Search textbox
        parametersLabel = QLabel("Look for: ", self) # Creates label "Look for: ". self says this is a child of MainWindow
        parameters = QLineEdit(self) # Creates the user input box
        parameters.setPlaceholderText("Enter search parameter") # Puts placeholder text into the input box
        parameters.setToolTip("Type the column name you want to search for") # Creates tool tip text for this input box when mouse hovers over it
        groupBoxLayout.addWidget(parametersLabel) # Adds parametersLabel to the layout to its vertical rules
        groupBoxLayout.addWidget(parameters) # Adds the input box to the layout
        # File textbox --Follow same rules for lines 32-37
        pickFileLabel = QLabel("From file: ", self)
        pickFile = QLineEdit(self)
        pickFile.setPlaceholderText("Enter file name")
        pickFile.setToolTip("Type the file name from which to search")
        groupBoxLayout.addWidget(pickFileLabel)
        groupBoxLayout.addWidget(pickFile)
        
        # sets the layout for the 'search parameters' section
        groupBox.setLayout(groupBoxLayout) # Applies QVBoxLayout rules to line 28, which applies to lines 32-37
        vLayout.addWidget(groupBox) # Adds groupbox to vLayout, which makes the widgets be displayed
        
        # Adding spacing and margins by pixels
        vLayout.setSpacing(10) # Space between widgets
        vLayout.setContentsMargins(20, 20, 20, 20) # top, left, right, bottom margin spacing from window edge
        

        # --For the lower section of MainWindow--
        # Labels the lower section of the initial window display
        self.label = QLabel("What are you looking for?", self) # Header for the lower section. Again, 'self' makes it a child element of MainWindow
        vLayout.addWidget(self.label) # Adds the label to the window display
        
        # display categories button
        self.displayButton = QPushButton("Display Categories", self) # Creates the categories button. Child element of MainWindow
        self.displayButton.setIcon(QIcon('path/to/icon.png'))  # replace path. sets an image to the button
        vLayout.addWidget(self.displayButton) # Adds button to the display
        
        # new search button
        newButton = QPushButton("New Search", self) # Creates button
        vLayout.addWidget(newButton) # Adds button to the display
        
        # search button
        searchButton = QPushButton("Search", self)
        vLayout.addWidget(searchButton)
        
        # Resizable layout
        centralWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # Sets size 'policies' for vertical and horizontal dimensions of centralWidget
        # QSizePolicy means that the centralWidget can grow and shrink, and take up as much space in MainWindow (parent layout)
        
        # Status bar
        statusBar = QStatusBar() # Displays status information
        self.setStatusBar(statusBar) # Has MainWindow use the statusBar
        
        #--Lines 85-100 are only visible in the GUI after the Display Categories button is clicked
        # Category list (only appears after Display Categories button is clicked)
        self.categoryWidget = QWidget() # Creates container widget for checkbox section
        self.categoryLayout = QVBoxLayout(self.categoryWidget) # Applies layout rules to categoryWidget
        self.categoryWidget.setVisible(False) # This is what hides the section until the button is clicked
        vLayout.addWidget(self.categoryWidget) # Adds categoryWidget to the layout for a nice display
        
        # Placeholder categories for actual categories in data set
        categories = ["Category 1", "Category 2", "Category 3", "Category 4"]
        for category in categories:
            checkbox = QCheckBox(category)
            self.categoryLayout.addWidget(checkbox)
        
        # create graph button
        # --Same rules as lines 63-73--
        self.createGraphButton = QPushButton("Create Graph", self)
        self.createGraphButton.setVisible(False) # Hides the Create Graph button until the Display Categories button is clicked
        vLayout.addWidget(self.createGraphButton)
        
        # Connects button clicking to specific funtions
        self.displayButton.clicked.connect(self.toggle_categories) # When clicked, handles display of categories
        newButton.clicked.connect(lambda: self.label.setText("Okie Dokie")) # Displays text message when clicked
        searchButton.clicked.connect(lambda: self.label.setText("Searching...")) # Displays text when clicked
        
        self.show() # Displays MainWindow for appearance and use
    
    def toggle_categories(self): # Toggles the visibility of the categories section
        if self.categoryWidget.isVisible():
            self.categoryWidget.setVisible(False)
            self.createGraphButton.setVisible(False)
        else:
            self.categoryWidget.setVisible(True)
            self.createGraphButton.setVisible(True)
        self.adjustSize() # adjusts the size of the widget to properly display all of its contents

def create_app():
    app = QApplication(sys.argv) # Manages app resources
    window = MainWindow() # Sets up instance of MainWindow. Initializes all widgets and layouts defined in the class
    app.setStyleSheet("QPushButton { font-size: 14px; padding: 10px; } QLabel { font-size: 16px; }") # Sets stylesheet for app. Applies styles to QLabel and QPushButton
    sys.exit(app.exec_()) # Loop for app use. Processes user input, updates to the window, etc.

if __name__ == "__main__":
    create_app()
