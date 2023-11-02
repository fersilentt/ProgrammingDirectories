
# Import Module 
import sys 
from PyQt5.QtWidgets import *
  
  
class ListBox(QWidget): 
  
    def __init__(self): 
        super().__init__() 
  
        self.initUI() 
  
    def initUI(self): 
        # Vertical box layout 
        vbox = QVBoxLayout(self) 
  
        # Horizontal box layout 
        hbox = QHBoxLayout() 
  
        # Create QlistWidget Object 
        self.listWidget = QListWidget(self) 
  
        # Add Items to QlistWidget 
        self.listWidget.addItems( 
            ['python', 'c++', 'java', 'pyqt5', 'javascript', 'geeksforgeeks']) 
  
        # Add Push Button 
        clear_btn = QPushButton('Clear', self) 
        clear_btn.clicked.connect(self.clearListWidget) 
  
        vbox.addWidget(self.listWidget) 
        hbox.addWidget(clear_btn) 
        vbox.addLayout(hbox) 
  
        self.setLayout(vbox) 
  
        # Set geometry 
        self.setGeometry(300, 300, 350, 250) 
  
        # Set window title 
        self.setWindowTitle('QListWidget') 
  
        # Display QlistWidget 
        self.show() 
  
    def clearListWidget(self): 
        self.listWidget.clear() 
  
  
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
  
    # Call ListBox Class 
    ex = ListBox() 
  
    # Close the window 
    sys.exit(app.exec_()) 
