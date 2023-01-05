import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStyleFactory, QListWidget, QHBoxLayout, QLineEdit, QTabWidget
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

       # Create the QWebEngineView
        self.view = QWebEngineView(self)
        self.view.setUrl(QUrl("http://www.google.com"))


        # Create the "back", "forward", and "refresh" buttons
        self.back_button = QPushButton("<", self)
        self.back_button.clicked.connect(self.go_back)
        self.forward_button = QPushButton(">", self)
        self.forward_button.clicked.connect(self.go_forward)
        self.refresh_button = QPushButton("", self)
        self.refresh_button.clicked.connect(self.refresh)

        # Set the icon for the refresh button
        self.refresh_button.setIcon(QIcon("refresh.png"))


        # Create the URL bar
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.load_url)

        # Add the buttons and URL bar to a horizontal layout
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.back_button)
        hlayout.addWidget(self.forward_button)
        hlayout.addWidget(self.refresh_button)
        hlayout.addWidget(self.url_bar)

        # Add the QWebEngineView and the horizontal layout to a vertical layout
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.view)
        vlayout.addLayout(hlayout)

        # Add the vertical layout to the central widget
        central_widget = QWidget(self)
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)

        # Set the window title
        self.setWindowTitle("Jolof Browser")

     # Add the vertical layout to the central widget
        central_widget = QWidget(self)
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)


    def go_back(self):
        self.view.back()

    def go_forward(self):
        self.view.forward()
    
    def refresh(self):
        self.view.reload()

    def load_url(self):
        url = self.url_bar.text()
        self.view.setUrl(QUrl(url))


# Create the QApplication
app = QApplication(sys.argv)

# Set the GUI style to the Opera style
app.setStyle(QStyleFactory.create("Opera"))

# Set the window icon
icon = QIcon("gameinjolof_icone.jpg")
app.setWindowIcon(icon)


# Create the main window
window = MainWindow()
window.show()

# Run the main event loop
app.exec_()
