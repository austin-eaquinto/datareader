import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

def create_app():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Centered Label PyQt5 GUI")
    window.setGeometry(100, 100, 300, 200)

    # Create layouts
    main_layout = QVBoxLayout()
    h_layout = QHBoxLayout()

    label = QLabel("Hello, PyQt", window)
    h_layout.addStretch(1)  # Add stretch to push the label to the center
    h_layout.addWidget(label)  # Add the label to the horizontal layout
    h_layout.addStretch(1)

    button1 = QPushButton("Button 1", window)
    main_layout.addWidget(button1)  # Add the horizontal layout to the main vertical layout
    # main_layout.addWidget(button1)

    def on_button1_click():
        label.setText("Button 1 Clicked!")

    button1.clicked.connect(on_button1_click)

    window.setLayout(main_layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    create_app()