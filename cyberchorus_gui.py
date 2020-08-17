from PyQt5 import (QtWidgets, QtCore, QtGui)
from PyQt5.QtWidgets import qApp
import cyberchorus
import sys


WINDOW_X_DIM = 500
WINDOW_Y_DIM = 100

aboutText = ['About', 'Developed by Benjamin Swanson and Noah Brown. Thanks for using our software! <license info here>']
helpText = ['Help', '<help text here>']

# Displays text in a new window.
class TextViewWindow(QtWidgets.QMainWindow):
	def __init__(self, text, parent=None):
		super().__init__(parent)

		self.text = text

		self.textLabel = QtWidgets.QLabel(text)
		self.textLabel.setWordWrap(True)
		self.scrollArea = QtWidgets.QScrollArea()

		self.scrollArea.setWidget(self.textLabel)
		self.setCentralWidget(self.scrollArea)

		self.text = QtWidgets.QLabel(text)
		self.text.setMinimumSize(800, 800)
		self.text.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
								QtWidgets.QSizePolicy.Expanding)

		# Layout
		self.layout = QtWidgets.QGridLayout()
		self.layout.addWidget(self.textLabel, 0, 0)
		self.layout.addWidget(self.text, 1, 0)
		self.layout.setContentsMargins(15, 15, 15, 15)
		self.layout.setSpacing(5)

		self.setLayout(self.layout)

		self.setMinimumSize(self.sizeHint())

# The main user window. Wraps WindowContents.
class MainWindow(QtWidgets.QMainWindow):

	def __init__(self, windowName='Window', parent=None):

		super().__init__(parent)

		# Window config
		self.setWindowTitle(windowName)
		self.setGeometry(100, 100, WINDOW_X_DIM, WINDOW_Y_DIM)

		# centralize main widget contents
		self.form_widget = WindowContent()
		self.setCentralWidget(self.form_widget)

		# create menu bar
		bar = self.menuBar()
		barHelp = bar.addMenu('Help')
		barAbout = bar.addMenu('About')

		# Implement bar actions
		actionHelp = QtWidgets.QAction('Show Usage', self)
		actionAbout = QtWidgets.QAction('About CyberChorus', self)

		actionHelp.triggered.connect(lambda: self.DisplayText(helpText))
		actionAbout.triggered.connect(lambda: self.DisplayText(aboutText))

		# Add actions to tabs
		barHelp.addAction(actionHelp)
		barAbout.addAction(actionAbout)

	def DisplayText(self, text):
		QtWidgets.QMessageBox.about(self, text[0], text[1])


# The contents of the MainWindow.
class WindowContent(QtWidgets.QWidget):

	def __init__(self, parent=None):
		super().__init__(parent)

		# Button inits
		self.buttonGetConfig = QtWidgets.QPushButton('Get Gonfiguration')
		self.buttonRecord = QtWidgets.QPushButton('Record')
		self.buttonUpload = QtWidgets.QPushButton('Upload Recording')
		self.buttonQuit = QtWidgets.QPushButton('Quit')

		# Set button callbacks
		self.buttonGetConfig.clicked.connect(lambda: cyberchorus.GetConfig())
		self.buttonRecord.clicked.connect(lambda: cyberchorus.RecordSinger())
		self.buttonUpload.clicked.connect(lambda: cyberchorus.UploadRecording())
		self.buttonQuit.clicked.connect(lambda: self.Quit())

		# Label inits
		self.labelEmpty = QtWidgets.QLabel('')

		# Build layout
		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(self.buttonGetConfig)
		v_box.addWidget(self.buttonRecord)
		v_box.addWidget(self.labelEmpty)
		v_box.addWidget(self.buttonUpload)
		self.setLayout(v_box)

	def Quit(self):
		qApp.quit()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('note_icon.png'))
	mainWindow = MainWindow(windowName='CyberChorus')
	mainWindow.show()
	sys.exit(app.exec_())
