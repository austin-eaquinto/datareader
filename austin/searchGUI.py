import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

# in the import line above, the two box layouts are for Vertical and Horizontal parameters
# Now, you can import trypandas
# Add jeremy directory to sys.path so we can import trypandas.py
# sys.path.append(os.path.abspath('../jeremy'))  # Adjust path if necessary

# import trypandas
# result = trypandas.write_csv()

# Add the directory containing trypandas.py to the system path
# trypandas_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'jeremy'))
# print(f"Adding to sys.path: {trypandas_path}")  # Debug print
# sys.path.append(trypandas_path)

# try:
#     from trypandas import write_csv  # Import the write_csv function from trypandas.py
#     print("Imported write_csv successfully")
# except ImportError as e:
#     print(f"Error importing write_csv: {e}")

def create_app():
    app = QApplication(sys.argv) # starts and manages main event loop
                                # used to respond to user input like clicks and keys
                                # initializes app and sets up environment for it to run
                                # manages app-wide resources like config settings
                                # handles app state like startup and shutdown process
    window = QWidget()
    window.setWindowTitle("File Reader")
    window.setGeometry(200, 200, 600, 400)

# window = QWidget() # creates a window or a widget that can contain other widgets
# window.setWindowTitle("My First PyQt GUI") # name of the window

    vLayout = QVBoxLayout()
    # hLayout = QHBoxLayout()

    label = QLabel("What are you looking for?", window) 
# label.move(50, 100) # size of the GUI window
    vLayout.addWidget(label)

    displayButton = QPushButton("Display Categories", window)
    vLayout.addWidget(displayButton)
# firstButton.move(50, 100) # sets the position of the button within the parent widget(the window)
                     # move() places the button according to the top left corner relative to the parent
                     # the parameters of move() determine where the corner is placed

    newButton = QPushButton("New Search", window)
    vLayout.addWidget(newButton)

    searchButton = QPushButton("Search", window)
    vLayout.addWidget(searchButton)

    graphButton = QPushButton("Graph Results", window)
    vLayout.addWidget(graphButton)

# the search textbox
    hLayoutParameters = QHBoxLayout()
    parametersLabel = QLabel("Look for: ", window)
    parameters = QLineEdit(window)
    # vLayout.addWidget(parameters)
    hLayoutParameters.addWidget(parametersLabel)
    hLayoutParameters.addWidget(parameters)
    vLayout.addLayout(hLayoutParameters)

# the file textbox
    hLayoutFile = QHBoxLayout()
    pickFileLabel = QLabel("From file: ", window)
    pickFile = QLineEdit(window)
    # vLayout.addWidget(pickFile)
    hLayoutFile.addWidget(pickFileLabel)
    hLayoutFile.addWidget(pickFile)
    vLayout.addLayout(hLayoutFile)

    def on_display_click():
        label.setText("Categories: ")

    def on_search_click():
        label.setText("Searching...")
        column = parameters.text()
        # write_csv(column)
    
    def on_newsearch_click():
        label.setText("Okie Dokie")
    
    def on_graph_click():
        label.setText("Graphing...")

# when the button is clicked, it runs the related function
    displayButton.clicked.connect(on_display_click)
    searchButton.clicked.connect(on_search_click)
    newButton.clicked.connect(on_newsearch_click)
    graphButton.clicked.connect(on_graph_click)
    
# window spacing settings
    vLayout.setSpacing(10)
    vLayout.setContentsMargins(20, 20, 20, 20)
    
# these have temporary text in the text boxes and hover text boxes for user guidance
    parameters.setPlaceholderText("Enter search parameter")
    parameters.setToolTip("Type the column name you want to search for")
    pickFile.setPlaceholderText("Enter file name")
    pickFile.setToolTip("Type the file name from which to search")

# supposed to adapt the layout to whatever size the window is
    # window.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

# adds a status bar to provide feedback to the user
    statusBar = QStatusBar(window)
    window.setStatusBar(statusBar)

    window.setLayout(vLayout)
    window.show() # makes the window appear

    sys.exit(app.exec_()) # sys.exit() terminates python interpreter
                        # app.exec_() starts the main loop of the app. handles physical user input
                        # exec_() keeps app running until user closes it. keeps GUI responsive and reacts to user interactions

if __name__ == "__main__":
    create_app()