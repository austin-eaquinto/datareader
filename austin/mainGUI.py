import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox, QStatusBar, QSizePolicy
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Reader")
        self.setGeometry(200, 200, 600, 400)
        
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        
        vLayout = QVBoxLayout()
        centralWidget.setLayout(vLayout)
        
        # Grouping widgets
        groupBox = QGroupBox("Search Parameters")
        groupBoxLayout = QVBoxLayout()
        
        # Search textbox
        parametersLabel = QLabel("Look for: ", self)
        parameters = QLineEdit(self)
        parameters.setPlaceholderText("Enter search parameter")
        parameters.setToolTip("Type the column name you want to search for")
        groupBoxLayout.addWidget(parametersLabel)
        groupBoxLayout.addWidget(parameters)
        
        # File textbox
        pickFileLabel = QLabel("From file: ", self)
        pickFile = QLineEdit(self)
        pickFile.setPlaceholderText("Enter file name")
        pickFile.setToolTip("Type the file name from which to search")
        groupBoxLayout.addWidget(pickFileLabel)
        groupBoxLayout.addWidget(pickFile)
        
        groupBox.setLayout(groupBoxLayout)
        vLayout.addWidget(groupBox)
        
        # Adding spacing and margins
        vLayout.setSpacing(10)
        vLayout.setContentsMargins(20, 20, 20, 20)
        
        # Widgets
        label = QLabel("What are you looking for?", self)
        vLayout.addWidget(label)
        
        displayButton = QPushButton("Display Categories", self)
        displayButton.setIcon(QIcon('path/to/icon.png'))  # Add appropriate path
        vLayout.addWidget(displayButton)
        
        newButton = QPushButton("New Search", self)
        vLayout.addWidget(newButton)
        
        searchButton = QPushButton("Search", self)
        vLayout.addWidget(searchButton)
        
        # Resizable layout
        centralWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Status bar
        statusBar = QStatusBar()
        self.setStatusBar(statusBar)
        
        # Event handling
        displayButton.clicked.connect(lambda: label.setText("Categories: "))
        newButton.clicked.connect(lambda: label.setText("Okie Dokie"))
        searchButton.clicked.connect(lambda: label.setText("Searching..."))
        
        self.show()

def create_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet("QPushButton { font-size: 14px; padding: 10px; } QLabel { font-size: 16px; }")
    sys.exit(app.exec_())

if __name__ == "__main__":
    create_app()
