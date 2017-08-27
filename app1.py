
# coding: utf-8

# In[1]:

from PyQt4 import QtCore, QtGui
import os
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName(_fromUtf8("Window"))
        Window.resize(400, 163)
    
        # The (Save_AS) Button.. !!
        self.button_place = QtGui.QPushButton(Window)
        self.button_place.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.button_place.setObjectName(_fromUtf8("button_place"))
        self.button_place.clicked.connect(self.Save_As)
        self.button_place.setStyleSheet(_fromUtf8("QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"font-size: 12px;\n"
"border-radius: 10px\n"
"\n"
"}"))
        
        # The (New Folder) Button ..!!!
        self.button = QtGui.QPushButton(Window)
        self.button.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.button.setObjectName(_fromUtf8("button"))
        self.button.clicked.connect(self.make_file)
        self.button.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"color:#fff;\n"
"background-color:#357ebd;\n"
"font-size: 12px;\n"
"border-radius: 10px\n"
"}"))
        
        # The Clear button For Clearing the Line
        self.Clear_button = QtGui.QPushButton(Window)
        self.Clear_button.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.Clear_button.setObjectName(_fromUtf8("Clear_button"))
        self.Clear_button.setStyleSheet(_fromUtf8("QPushButton{\n"
"color:rgb(0, 66, 0);\n"
"background-color:rgb(158, 255, 181);\n"
"font-size: 12px;\n"
"border-radius: 10px\n"
"\n"
"}"))
        
        # The (Linde Edit) for the (Save_As ).!!!!
        self.lineEdit_plase = QtGui.QLineEdit(Window)
        self.lineEdit_plase.setGeometry(QtCore.QRect(100, 130, 271, 20))
        self.lineEdit_plase.setObjectName(_fromUtf8("lineEdit_plase"))
        self.lineEdit_plase.returnPressed.connect(self.Save_As)
        
        # The (Line Edit) for the (Foldar name) .,.!!!!
        self.Folder_Line = QtGui.QLineEdit(Window)
        self.Folder_Line.setGeometry(QtCore.QRect(100, 30, 91, 20))
        self.Folder_Line.setObjectName(_fromUtf8("Folder_Line"))
        self.Folder_Line.returnPressed.connect(self.make_file)
        
        # The Line_Edit that shows the Direction of the the New File >><<><!!!!
        self.line_dir = QtGui.QLineEdit(Window)
        self.line_dir.setGeometry(QtCore.QRect(100, 70, 241, 20))
        self.line_dir.setObjectName(_fromUtf8("line_dir"))
        
        # The Singal and slots Staff ...!!
        self.retranslateUi(Window)
        QtCore.QObject.connect(self.lineEdit_plase, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.button_place.click)
        QtCore.QObject.connect(self.Folder_Line, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.button.click)
        QtCore.QObject.connect(self.Clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Folder_Line.clear)
        QtCore.QMetaObject.connectSlotsByName(Window)
    
    def retranslateUi(self, Window):
        Window.setWindowTitle(_translate("Window", "Archives Helper", None))
        self.button.setText(_translate("Window", "New Folder", None))
        self.button_place.setText(_translate("Window", "Save As", None))
        self.Clear_button.setText(_translate("Window", "Clear", None))

    @QtCore.pyqtSlot()
    def Save_As(self):
        Save = self.lineEdit_plase.text()
        print Save
        Str_Save = str(Save)
        print Str_Save
        os.chdir(Str_Save)   
    
    @QtCore.pyqtSlot()
    def make_file(self):
        CodeNumber = self.Folder_Line.text()
        os.mkdir(CodeNumber)
        ID = os.getcwd()
        label = ID +'\\' +CodeNumber
        self.line_dir.setText(_translate("Window", label, None))
        
    def save_file(self):
        
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        
    
    
    
    
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('Menuicon.png'))
    Window = QtGui.QWidget()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())



# In[ ]:



