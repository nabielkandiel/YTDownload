from PySide6 import QtWidgets, QtCore, QtGui
from yt_interface import YTinterface
import requests

class Form(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.__yt = None
        # Creating Widgets
        self.__buildLinkInput()
        self.__buildSubmitButton()
        self.__buildClearButton()
        self.__buildDownloadSelector()
        self.__buildDownloadButton()
        self.__buildVideoTitle()
        self.__thumbLabel = QtWidgets.QLabel()
        
        self.__designLayout()
        


    def __designLayout(self) -> None:
        # Creating Layout
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.__subButton)
        hlayout.addWidget(self.__clearButton)
        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(self.__downloadSelector)
        hlayout2.addWidget(self.__downloadButton)
        self.__layout = QtWidgets.QVBoxLayout()
        self.__layout.addWidget(self.__linkEdit)
        self.__layout.addLayout(hlayout)
        self.__layout.addWidget(self.__titleLable)
        self.__layout.addWidget(self.__thumbLabel)
        self.__layout.addLayout(hlayout2)
        self.__layout.setAlignment(QtCore.Qt.AlignCenter)

        # Set dialog layout
        self.setLayout(self.__layout)


    def __buildVideoTitle(self) -> None:
        self.__titleLable = QtWidgets.QLabel("No Video Selected")
        self.__titleLable.setFont(QtGui.QFont('Arial',weight=QtGui.QFont.Bold, pointSize=18))
        self.__titleLable.setAlignment(QtCore.Qt.AlignCenter)



    def __buildDownloadButton(self) -> None:
        self.__downloadButton = QtWidgets.QPushButton("Download")
        self.__downloadButton.setFixedWidth(100)
        self.__downloadButton.clicked.connect(self.downloadBtnPress)

    def __buildDownloadSelector(self) -> None:
        self.__downloadSelector = QtWidgets.QComboBox()


    def __buildLinkInput(self) -> None:
        self.__linkEdit = QtWidgets.QLineEdit("Enter Youtube Link Here")


    def __buildSubmitButton(self) -> None:
        self.__subButton = QtWidgets.QPushButton("Get Video")
        self.__subButton.setFixedWidth(100)
        self.__subButton.clicked.connect(self.linkSubmit)
    

    def __buildClearButton(self) -> None:
        self.__clearButton = QtWidgets.QPushButton("Clear")
        self.__clearButton.setFixedWidth(100)
        self.__clearButton.clicked.connect(self.clearText)


    def __updateVideoTitle(self) -> None:
        self.__titleLable.setText(self.__yt.getTitle())


    @QtCore.Slot()
    def clearText(self) -> None:
        self.__linkEdit.clear()


    @QtCore.Slot()
    def downloadBtnPress(self) -> None:
        if self.__yt != None:
            self.__yt.download(self.__downloadSelector.currentText())

    
    @QtCore.Slot()
    def linkSubmit(self) -> None:
        self.__yt = YTinterface()
        if not self.__yt.submitLink(self.__linkEdit.text()):
            return
        self.__updateVideoTitle()
        self.__yt.getStreams()
        req = requests.get(self.__yt.getThumbURL())
        image = QtGui.QImage()
        image.loadFromData(req.content)
        pxmap = QtGui.QPixmap(image)
        self.__thumbLabel.setPixmap(pxmap)
        self.__thumbLabel.show()
        streams = self.__yt.getStreams()
        for stream in streams:
            self.__downloadSelector.addItem(stream)