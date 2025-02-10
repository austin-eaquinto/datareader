import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QSpinBox,
                             QLineEdit, QPushButton, QScrollArea, QDialog, QDialogButtonBox, QComboBox, QMessageBox,
                             QLabel, QGridLayout, QHBoxLayout, QCheckBox, QTabWidget, QTextEdit, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import pyqtSignal, Qt, QThread
# from persist_vector import *

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
# import pandas as pd
from pathlib import Path

class PlotWidget(QWidget):
    def __init__(self, plot_type, headers):
        super().__init__()
        self.figure, self.axes = plt.subplots()
        self.canvas = FigureCanvas(self.figure) # allows for plot graphs in PyQt
        self.plot_type = plot_type # bar, scatter, line?
        self.headers = headers # column headers
        self.data = None  # Will hold pandas DataFrame
        self.init_ui()

    def init_ui(self):
        """Common UI elements for all plot types"""
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.btn = QPushButton(f"Create {self.plot_type}")
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)
        self.btn.clicked.connect(self.show_config_dialog) # pop up plot window on click

    def load_data(self, data_path):
        """Load data from csv file using a given file path"""
        self.data = pd.read_csv(data_path)

    def create_plot_dialog(self):
        """Child classes return instance of plot configuration window"""
        raise NotImplementedError

    def show_config_dialog(self):
        """Show configuration dialog and handle plot creation"""
        dialog = self.create_plot_dialog()
        if dialog.exec_() == QDialog.Accepted:
            # get_parameters returns column headers to create plot visual
            self.generate_plot(dialog.get_parameters())

    def generate_plot(self, params):
        """Child classes fill out plot with column headers
           as dataframe values"""
        raise NotImplementedError

# ----------------------------
# Derived Bar Plot Widget
# ----------------------------
class BarPlotWidget(PlotWidget):
    def __init__(self, headers):
        super().__init__("Bar Plot", headers)
        self.setMinimumSize(1200, 400) # minimum size the window can be, even user adjusted


    def create_plot_dialog(self):
        return BarConfigDialog(self.headers)

    def generate_plot(self, params):
        self.figure.clear()
        plot = self.figure.add_subplot(111)

        print("x", params["x_axis"])  # check for correct x-axis
        print("y", params["y_axis"])  # check for correct y-axis

        # options to filter by column header and/or keyword
        filter_by = params.get("filter_by", None)
        keyword = params.get("keyword", None)

        if filter_by and keyword:
            self.data = self.data[self.data[params["filter_by"]].str.contains(params["keyword"], case=False, na=False)]

        if not filter_by and keyword:
            self.data = self.data[self.data[params["x_axis"]].str.contains(keyword, case=False, na=False)]

        # sort by y-axis values 
        self.data = self.data.sort_values(by=params["y_axis"], ascending=False)

        # limit the number of items to display
        top_n = params.get("top_n", 10)
        self.data = self.data.head(top_n)

        # store dataframe subsets or won't work
        x_values = self.data[params["x_axis"]]
        y_values = self.data[params["y_axis"]]

        plot.bar(x_values.head(5), y_values, color="darkblue")

        plot.set_xlabel(params["x_label"], fontsize=12)
        plot.set_ylabel(params["y_label"], fontsize=12)
        plot.set_title(params["title"], fontsize=14, pad=20)
        plot.tick_params(axis='x', rotation=45, labelsize=10)
        plot.tick_params(axis='y', labelsize=10)

        self.figure.tight_layout()
        self.canvas.draw()

# ----------------------------
# Derived Scatter Plot Widget
# ----------------------------
class ScatterPlotWidget(PlotWidget):
    def __init__(self, headers):
        super().__init__("Scatter Plot", headers)

    def create_plot_dialog(self):
        return ScatterConfigDialog(self.headers)

    def generate_plot(self, params):
        plt.figure(figsize=(10, 6))
        self.data.plot.scatter(x=params['x_axis'], y=params['y_axis'], title=params['title'])
        plt.xlabel(params['x_label'])
        plt.ylabel(params['y_label'])
        plt.show()

# ----------------------------
# Derived Line Plot Component
# ----------------------------
class LinePlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn_load = QPushButton("Create Line Plot")
        

# ----------------------------
# Derived Histogram Plot Component
# ----------------------------  
class HistogramPlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn_load = QPushButton("Create Histogram Plot")

# ----------------------------
# Configuration Dialogs
# ----------------------------
class BaseConfigDialog(QDialog):
    def __init__(self, headers):
        super().__init__()
        self.headers = headers
        self.init_ui()
        self.resize(500, 250)

    def init_ui(self):
        self.layout = QFormLayout()
        
        # Common elements
        self.title_input = QLineEdit("My Plot")
        self.layout.addRow("Title:", self.title_input)
        
        # Will be extended by child classes
        self.setLayout(self.layout)
        
    def get_parameters(self):
        """To be implemented by child classes"""
        raise NotImplementedError

# ----------------------------
# Derived Bar Plot Configuration Dialog Box
# ----------------------------
class BarConfigDialog(BaseConfigDialog):
    def __init__(self, headers):
        super().__init__(headers)
        
        # Bar plot select-from inputs
        self.x_axis = QComboBox()
        self.x_axis.addItems(self.headers)
        self.y_axis = QComboBox()
        self.y_axis.addItems(self.headers)
        self.filter_by = QComboBox()
        self.filter_by.addItems(self.headers)
        
        # input layout
        self.layout.addRow("X Axis (base column):", self.x_axis)
        self.layout.addRow("Y Axis (Sort-by column):", self.y_axis)
        self.layout.addRow("Filter by Column:", self.filter_by)
        
        # keyword filter inputs
        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("Enter keyword to filter (optional)")
        self.layout.addRow("Filter by Keyword:", self.filter_input)

        # Number of top results
        self.top_n_input = QSpinBox()
        self.top_n_input.setMinimum(1) 
        self.top_n_input.setMaximum(100)
        self.top_n_input.setValue(10)
        self.layout.addRow("Number of results (Top N):", self.top_n_input)

        # Ok and Cancel buttons
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addRow(self.buttons)

    def get_parameters(self):
        return {
            "x_axis": self.x_axis.currentText(),
            "y_axis": self.y_axis.currentText(),
            "filter_by": self.filter_by.currentText(),
            "title": self.title_input.text(),
            "x_label": self.x_axis.currentText(),
            "y_label": self.y_axis.currentText(),
            "keyword": self.filter_input.text().strip(), 
            "top_n": self.top_n_input.value() 
        }
 
class ScatterConfigDialog(BaseConfigDialog):
    def __init__(self, headers):
        super().__init__(headers)

# ----------------------------
# Load File Component
# ----------------------------
class FileInput(QWidget):
    filenameSubmitted = pyqtSignal(str)  # Custom signal
    
    def __init__(self):
        super().__init__()
        self.file_input = QLineEdit()
        self.initUI()
        
    def initUI(self):
        layout = QGridLayout()
        
        # load CSV button based on path
        self.btn_load = QPushButton("Load CSV")
        
        # Connect button click to signal emission
        self.btn_load.clicked.connect(lambda: self.filenameSubmitted.emit(self.file_input.text()))
        
        # Add to layout
        layout.addWidget(QLabel("CSV File Path:"), 0, 0)
        layout.addWidget(self.file_input, 0, 1)
        layout.addWidget(self.btn_load, 0, 2)
        
        self.setLayout(layout)
        self.setFixedSize(600, 80)

    def get_file_path(self):
        return self.file_input.text()

# ----------------------------
# Left-side CSV Header Column Component
# ----------------------------
class ColumnHeader(QWidget):
    def __init__(self):
        super().__init__()
        self.checkboxes = []  # Track all checkboxes
        self.initUI()
        
    def initUI(self):
        self.scroll = QScrollArea() # scroll bar
        self.scroll.setWidgetResizable(True)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.scroll) 

        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.scroll.setWidget(self.container)

    def clear_checkboxes(self):
        """clear previous content on each start up """
        
        while self.container_layout.count():
            child = self.container_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.checkboxes.clear()

    def load_csv(self, filename):
        """Load csv file and reads only the first row for
           column header values. Adds a checkbox to each
           header and adds to a checkbox list"""
        
        self.clear_checkboxes()

        try:
            with open("../data/movies_cleaned_v2." + filename, 'r') as file:
                reader = csv.reader(file)
                headers = next(reader) # first line only
                
                # creates checkboxes for each column header
                for header in headers:
                    cb = QCheckBox(header)
                    cb.setStyleSheet("font-size: 14px; margin: 5px;")
                    self.container_layout.addWidget(cb)
                    self.checkboxes.append(cb)
                
                # Add spacer to push checkboxes to top
                self.container_layout.addStretch()

        except Exception as e:
            print(f"Error loading CSV: {e}")
    
    def get_selected_headers(self):
        """Returns list of selected header texts"""
        return [cb.text() for cb in self.checkboxes if cb.isChecked()]

# ------------------------
# SearchThread class meant to resolve issue of program crashing during API call
# ----------------------------
class SearchThread(QThread):
    finished = pyqtSignal(list)
    error = pyqtSignal(str)

    def __init__(self, query):
        super().__init__()
        self.query = query

    def retrieve_semantic_recommendations(query: str, k: int = 5) -> pd.DataFrame:
        """Checks directory for Chroma database. Searches vector database based on
        user query. Returns initial database records most related to records in 
        the vector database."""

        load_dotenv()
        movies = pd.read_csv("../data/movies_cleaned_v2.csv")

        # Initialize or load the Chroma database
        persist_dir = "./chroma_db"
        if Path(persist_dir).exists():
            db_movies = Chroma(
                persist_directory=persist_dir,
                embedding_function=OpenAIEmbeddings()
            )
        else:
            # creation of vector database if chroma_db doesn't exist in current directory
            raw_documents = TextLoader("tagged_overview.txt", encoding="utf-8").load()
            text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator="\n")  # Fixed chunk_size
            documents = text_splitter.split_documents(raw_documents)
            db_movies = Chroma.from_documents(
                documents,
                embedding=OpenAIEmbeddings(),
                persist_directory=persist_dir
            )
            db_movies.persist()
            
        recs = db_movies.similarity_search(query, k)
        movies_list = []

        for i in range(0, len(recs)):
            movies_list += [int(recs[i].page_content.strip('"').split()[0])]
        
        return movies[movies["id"].isin(movies_list)].head(k)

    def run(self):
        try:
            results = self.retrieve_semantic_recommendations(self.query)
            print(results) # log to see if dataframe returns successfully
            self.finished.emit(results)
        except Exception as e:
            self.error.emit(str(e))

# ----------------------------
# Main Window
# ----------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_data_path = None  # initialize as None
        self.plot_widgets=[] # list of visual plots
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("DataReader")
        self.setGeometry(200, 100, 1600, 900)
        
        # Create main tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create and add tabs
        self.create_main_tab()
        self.create_secondary_tab()

    def create_main_tab(self):
        """Main tab window for data analytic and plotting purposes.
           Contains necessary UI components for CSV loading, column
           header selection, and plot graph creation."""
        
        main_tab = QWidget()
        layout = QVBoxLayout()
        # Create components
        # central_widget = QWidget()
        # central_widget.setStyleSheet("border: 2px solid red;")
        # self.main_layout = QVBoxLayout(central_widget)
        
        # instantiate top file path search field
        self.file_input = FileInput()
        layout.addWidget(self.file_input)

        self.body_layout = QHBoxLayout()
        layout.addLayout(self.body_layout)
        
        # instantiate left-side column headers
        self.column_header = ColumnHeader()
        self.column_header.setFixedWidth(250)
        
        # Set up layout
        self.body_layout.addWidget(self.column_header, stretch=0)
        self.body_layout.addStretch(1) 

        # connect signals for the Load CSV button
        self.file_input.filenameSubmitted.connect(self.handle_file_submission)
        
        # self.setCentralWidget(central_widget)

        # Add plot buttons to right panel
        self.right_panel = QWidget()
        # self.right_panel.setStyleSheet("border: 2px solid black;")
        # self.right_panel.setFixedSize(200,50)

        self.right_layout = QVBoxLayout()
        self.right_layout
        self.plot_button_layout = QHBoxLayout()
        
        # Create plot type buttons
        self.btn_bar = QPushButton("Add Bar Plot")
        self.btn_scatter = QPushButton("Add Scatter Plot")
        
        # Connect buttons to handlers
        self.btn_bar.clicked.connect(lambda: self.add_plot(BarPlotWidget))
        self.btn_scatter.clicked.connect(lambda: self.add_plot(ScatterPlotWidget))
        
        self.plot_button_layout.addWidget(self.btn_bar)
        self.plot_button_layout.addWidget(self.btn_scatter)
        self.right_layout.addLayout(self.plot_button_layout)
        self.right_panel.setLayout(self.right_layout)
        
        # Add to main layout
        layout.addWidget(self.right_panel)

        main_tab.setLayout(layout)

        # Add tab to main interface
        self.tabs.addTab(main_tab, "Main Analytics")


    def create_secondary_tab(self):
        """Second tab for AI recommendations"""

        secondary_tab = QWidget()
        layout = QVBoxLayout(secondary_tab)
        
        # search field component
        search_widget = QWidget()
        search_layout = QHBoxLayout(search_widget)
        self.user_query = QLineEdit()
        self.user_query.setPlaceholderText("What are you looking for?")
        self.btn_search = QPushButton("Search")
        
        search_layout.addWidget(self.user_query)
        search_layout.addWidget(self.btn_search)
        
        # recommender results component
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        
        # Add to main layout
        layout.addWidget(search_widget)
        layout.addWidget(self.results_display)
        
        # on search button click, call helper function
        self.btn_search.clicked.connect(self.handle_ai_search)
        
        self.tabs.addTab(secondary_tab, "AI Recommender")
        return secondary_tab

    # In handle_ai_search:
    def handle_ai_search(self):
        """Helper method using QThread class to combat application
        crashing as API call takes time to load and return results."""

        query = self.user_query.text()
        if not query: return
        
        self.thread = SearchThread(query)
        self.thread.finished.connect(self.display_results)
        self.thread.error.connect(lambda err: QMessageBox.critical(self, "Error", err))
        self.thread.start()
        self.btn_search.setEnabled(False)
        self.thread.finished.connect(lambda: self.btn_search.setEnabled(True))
        
    def display_results(self, dataframe):
        """Display AI recommended dataframe into a PyQt Table Widget. Show 4 columns and
        n amount of rows based on dataframe length."""

        # Clear existing content
        self.results_table = QTableWidget()
        self.results_table.setRowCount(len(dataframe))
        
        # Configure table
        self.results_table.setColumnCount(len(dataframe.columns))
        self.results_table.setHorizontalHeaderLabels(["Title", "Year", "Rating", "Genres"])
        # self.results_table.setHorizontalHeaderLabels(dataframe.columns)
        
        # Populate rows
        for row, result in enumerate(dataframe):
            self.results_table.insertRow(row)
            self.results_table.setItem(row, 0, QTableWidgetItem(result['original_title']))
            self.results_table.setItem(row, 1, QTableWidgetItem(str(result['release_date'])))
            self.results_table.setItem(row, 2, QTableWidgetItem(f"{result['vote_average']:.2f}"))
            self.results_table.setItem(row, 3, QTableWidgetItem(result['genres']))
    
        # Resize columns
        self.results_table.resizeColumnsToContents()

        self.results_table.show()

    def handle_file_submission(self, file_path):
        """Slot for when filename is submitted"""

        self.current_data_path = "../data/movies_cleaned_v2." + file_path
        print("Loaded file path:", self.current_data_path)
        
        # load CSV to display headers on left side of screen
        self.column_header.load_csv(file_path)

    def add_plot(self, plot_class:PlotWidget): 
        """Create a new plot widget of specified type"""
        selected_headers = self.column_header.get_selected_headers()
        # have to selected at least two column headers
        if len(selected_headers) < 2:
            QMessageBox.warning(self, "Selection Error", "Select at least 2 headers!")
            return
            
        plot_widget = plot_class(selected_headers)
        plot_widget.load_data(self.current_data_path) # store data path from input component for plots
        self.plot_widgets.append(plot_widget)
        self.body_layout.addWidget(plot_widget)

# ----------------------------
# Application Entry Point
# ----------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())