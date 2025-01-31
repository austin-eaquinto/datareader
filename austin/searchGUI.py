import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
# in the import line above, the two box layouts are for Vertical and Horizontal parameters

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
    hLayout = QHBoxLayout()

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

# the search textbox
    parametersLabel = QLabel("Look for: ", window)
    parameters = QLineEdit(window)
    # vLayout.addWidget(parameters)
    hLayout.addWidget(parametersLabel)
    hLayout.addWidget(parameters)
    vLayout.addLayout(hLayout)

# the file textbox
    pickFileLabel = QLabel("From file: ", window)
    pickFile = QLineEdit(window)
    # vLayout.addWidget(pickFile)
    hLayout.addWidget(pickFileLabel)
    hLayout.addWidget(pickFile)
    vLayout.addLayout(hLayout)

    def on_display_click():
        label.setText("Categories: ")

    def on_search_click():
        label.setText("Searching...")
    
    def on_newsearch_click():
        label.setText("Okie Dokie")

    displayButton.clicked.connect(on_display_click)
    searchButton.clicked.connect(on_search_click)
    newButton.clicked.connect(on_newsearch_click)

    window.setLayout(vLayout)
    window.show() # makes the window appear

    sys.exit(app.exec_()) # sys.exit() terminates python interpreter
                        # app.exec_() starts the main loop of the app. handles physical user input
                        # exec_() keeps app running until user closes it. keeps GUI responsive and reacts to user interactions

if __name__ == "__main__":
    create_app()