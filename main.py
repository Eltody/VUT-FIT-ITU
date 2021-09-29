import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QMainWindow, QMenuBar, \
    QSpinBox, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

def quit():
    exit()

def main():
    app = QApplication(sys.argv)
    windows = QWidget()

    screen = QDesktopWidget().screenGeometry()

    windows.resize(screen.width(), screen.height())
    windows.setWindowTitle('Kotahi')
    windows.setWindowIcon(QIcon('icon.png'))

    menu_layout = QGridLayout(windows)
    menu_layout.setContentsMargins(screen.width() % 3, screen.height() % 10, screen.width() % 3, screen.height() % 10)
#BACKGROUND
    windows.setStyleSheet("border-image: url(background.jpg); background-attachment: fixed")

    windows.showFullScreen()

    title = QPushButton(windows)
    title.setText("Kotahi")
#    title.setFixedSize(screen.width() // 5, screen.height() // 10)
    menu_layout.addWidget(title, 0, 2)

    profile1 = QPushButton(windows)
    profile1.setText("Create new profile")
    profile1.setStyleSheet('QPushButton {border-color: #A3C1DA; color: red;}')
#    profile1.clicked.connect()
    menu_layout.addWidget(profile1, 1, 2)

    profile2 = QPushButton(windows)
    profile2.setText("Create new profile")
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile2, 2, 2)

    profile3 = QPushButton(windows)
    profile3.setText("Create new profile")
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile3, 3, 2)

    profile4 = QPushButton(windows)
    profile4.setText("Create new profile")
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile4, 4, 2)

    profile5 = QPushButton(windows)
    profile5.setText("Create new profile")
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile5, 5, 2)

    quitButton = QPushButton(windows)
    quitButton.setText("Quit game")
    quitButton.clicked.connect(quit)
    #    quitButton.setFixedSize(screen.width() // 5, screen.height() // 10)
    menu_layout.addWidget(quitButton, 6, 2)

    shop = QPushButton(windows)
    shop.setText("Quit game")
    shop.clicked.connect(quit)
    #    quitButton.setFixedSize(screen.width() // 5, screen.height() // 10)
    menu_layout.addWidget(shop, 10, 0)

    languageButton = QPushButton(windows)
    languageButton.setText("Quit game")
    languageButton.clicked.connect(quit)
    #    quitButton.setFixedSize(screen.width() // 5, screen.height() // 10)
    menu_layout.addWidget(languageButton, 10, 4)

    sys.exit(app.exec_())

main()
