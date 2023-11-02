from PyQt5.QtWidgets import QListView, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QModelIndex
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        mainlayout = QVBoxLayout()
        self.setLayout(mainlayout)
    
        self.listView = QListView()
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.setObjectName("listView-1")

        mainlayout.addWidget(self.listView)

        values = ['one','two', 'three']
        for i in values:
            self.model.appendRow(QStandardItem(i))
        
        self.listView.clicked[QModelIndex].connect(self.on_clicked)
    
    def on_clicked(self, index):
        item = self.model.itemFromIndex(index)
        print (item.text())
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())