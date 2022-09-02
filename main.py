from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from pytube import YouTube
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 680, 400)
        self.setFixedSize(self.size())
        self.setWindowTitle("Youtube Video Downloader")
        self.initUI()

    def initUI(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 83, 16))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Video information")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 74, 171, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("audio/mp3")
        self.comboBox.addItem("video/mp4")

        self.input_field_url = QtWidgets.QLineEdit(self.centralwidget)
        self.input_field_url.setGeometry(QtCore.QRect(10, 29, 171, 20))
        self.input_field_url.setObjectName("input_field_url")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 48, 16))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.label.setText("Video URL")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 55, 71, 16))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Choose format")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(200, 30, 471, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.input_field_path = QtWidgets.QLineEdit(self.centralwidget)
        self.input_field_path.setGeometry(QtCore.QRect(10, 119, 141, 20))
        self.input_field_path.setObjectName("input_field_path")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Output path")

        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.button_search.setObjectName("button_search")
        self.button_search.setText("Search")
        self.button_search.clicked.connect(self.search_video)

        self.button_download = QtWidgets.QPushButton(self.centralwidget)
        self.button_download.setGeometry(QtCore.QRect(100, 160, 75, 23))
        self.button_download.setObjectName("button_download")
        self.button_download.setText("Download")
        self.button_download.setEnabled(False)
        self.button_download.clicked.connect(self.download)

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(157, 120, 25, 19))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setText("...")
        self.toolButton.clicked.connect(self.tool_button_clicked)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 310, 91, 16))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Download status")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 330, 191, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def tool_button_clicked(self):
        self.input_field_path.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

    def search_video(self):
        url = self.input_field_url.text()
        if not url or url == "":
            QMessageBox.about(self, "Error", "URL field is empty. Please enter a valid URL.")
        else: 
            self.textBrowser.setText("")
            self.progressBar.setValue(0)
            try:
                video = YouTube(self.input_field_url.text(), on_progress_callback=self.progress_function, on_complete_callback=self.finish_function)
                self.textBrowser.append("<b>Title:</b>")
                self.textBrowser.append(video.title)
                self.textBrowser.append("\n----------------------------------------------------------\n")

                self.textBrowser.append("\n\n<b>Author:</b>\n")
                self.textBrowser.append(video.author)
                self.textBrowser.append("\n----------------------------------------------------------\n")

                self.textBrowser.append("\n\n<b>Length:</b>\n")
                self.textBrowser.append(str(video.length) + " seconds")
                self.textBrowser.append("\n----------------------------------------------------------\n")

                self.textBrowser.append("\n\n<b>Description:</b>\n")
                self.textBrowser.append(video.description)
                self.textBrowser.append("\n----------------------------------------------------------\n")

                self.textBrowser.append("\n\n<b>Publish date:</b>\n")
                self.textBrowser.append(video.publish_date.strftime('%d/%m/%Y'))
                self.textBrowser.append("\n----------------------------------------------------------\n")

                self.textBrowser.append("\n\n<b>Views:</b>\n")
                self.textBrowser.append(str(video.views))
                
                self.selection = self.comboBox.currentText()
                if "mp3" in self.selection:
                    filtered_streams = video.streams.filter(mime_type="audio/mp4")
                    self.target = filtered_streams.get_audio_only()
                else:
                    filtered_streams = video.streams.filter(progressive=True, mime_type="video/mp4")
                    self.target = filtered_streams.get_highest_resolution()
                
            except Exception as e:
                print(e)
                QMessageBox.about(self, "Error", "Cannot find the video for the URL you inserted. Please enter a valid URL.")

            self.button_download.setEnabled(True)

    def download(self):
        output_path = self.input_field_path.text()
        if not output_path or output_path == "":
            QMessageBox.about(self, "Error", "Output path field is empty. Please enter an output path to save downloaded file.")
        else:
            name = None
            if "mp3" in self.selection:
                name = self.target.title + ".mp3"
            self.target.download(output_path, name)

    def progress_function(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        progress = int((float(abs(bytes_remaining-size)/size)) * float(100))
        self.progressBar.setValue(progress)

    def finish_function(self, stream, file_path):
        self.button_download.setEnabled(False)
        QMessageBox.about(self, "Download finished", "Download has finished! File save in '" + file_path + "'")
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()