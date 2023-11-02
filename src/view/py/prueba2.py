from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.listView = QtWidgets.QListView(
            editTriggers=QtWidgets.QAbstractItemView.NoEditTriggers,
            selectionMode=QtWidgets.QAbstractItemView.SingleSelection,
            selectionBehavior=QtWidgets.QAbstractItemView.SelectRows,
        )
        self.entry = QtGui.QStandardItemModel()
        self.listView.setModel(self.entry)

        for letter in list("abcdefghijklmnopqrstuvwxyz"):
            it = QtGui.QStandardItem(letter)
            self.entry.appendRow(it)

        ix = self.entry.index(0, 0)
        sm = self.listView.selectionModel()
        sm.select(ix, QtCore.QItemSelectionModel.Select)

        self.setCentralWidget(self.listView)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())