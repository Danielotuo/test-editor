from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QUrl 
import sys
 
class TextEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        uic.loadUi('text.ui', self)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionExit.triggered.connect(self.fileExit)

    def fileExit(self):
        QtWidgets.QApplication.quit()

    def fileSave(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

            data = self.textEdit.toPlainText()
            print(data)

            fobj = open(fileName,"w+")
            fobj.write(data)
            fobj.close()

    def fileOpen(self):
        print('open')

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

            fobj = open(fileName,"r")            
            data = fobj.read()
            fobj.close()
            self.textEdit.setText(data)

app = QtWidgets.QApplication([])
win = TextEditor()
win.show()
sys.exit(app.exec())
