import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QMainWindow, QMenuBar, \
    QSpinBox, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

global background
global mainWindow
global languageButton
global lang
lang = "slovakia"

def shop():
    sys.exit(0)

def language():
    global lang
    global languageButton

    if lang == "slovakia":
        lang = "united-kingdom"
    elif lang == "united-kingdom":
        lang = "france"
    elif lang == "france":
        lang = "germany"
    elif lang == "germany":
        lang = "russia"
    elif lang == "russia":
        lang = "spain"
    else:
        lang = "slovakia"

    languageButton.setStyleSheet("border-image: url(./images/%s.png)" % lang)
    decline()

def quitConfirm():
    global mainWindow
    global quitWindow
    quitWindow = QWidget()

    screen = QDesktopWidget().screenGeometry()

    quitLayout = QGridLayout(quitWindow)
    quitLayout.setColumnStretch(0, screen.width() // 3)
    quitLayout.setColumnStretch(2, screen.width() // 15)
    quitLayout.setColumnStretch(4, screen.width() // 3)

    quitLayout.setRowStretch(0, screen.height() // 3)
    quitLayout.setRowStretch(2, screen.height() // 15)
    quitLayout.setRowStretch(4, screen.height() // 3)

    quitWindow.setLayout(quitLayout)

    title = QLabel(background)
    title.setText("Are you sure?")
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
    title.setFixedSize(screen.width() // 5, screen.height() // 7)
    quitLayout.addWidget(title, 1, 2)

    confirmButton = QPushButton(quitWindow)
    confirmButton.setText("Yes")
    confirmButton.setStyleSheet("border-image: none")
    confirmButton.setFixedSize(screen.width() // 7, screen.height() // 7)
    confirmButton.clicked.connect(confirm)
    quitLayout.addWidget(confirmButton, 3, 1)

    declineButton = QPushButton(quitWindow)
    declineButton.setText("No")
    declineButton.setStyleSheet("border-image: none")
    declineButton.setFixedSize(screen.width() // 7, screen.height() // 7)
    declineButton.clicked.connect(decline)
    quitLayout.addWidget(declineButton, 3, 3)

    mainWindow.setCentralWidget(quitWindow)
    mainWindow.update()
    return

def confirm():
    sys.exit(1)

def decline():
    global mainWindow
    global background
    global languageButton
    global lang

    screen = QDesktopWidget().screenGeometry()
    background = QWidget(mainWindow)
    background.setFixedSize(screen.width(), screen.height())
    background.setStyleSheet(".QWidget{border-image: url(./images/background.jpg)}")

    menu_layout = QGridLayout(background)
    menu_layout.setColumnStretch(0, screen.width() // 21)
    menu_layout.setColumnStretch(2, screen.width() // 7)
    menu_layout.setColumnStretch(4, screen.width() // 7)
    menu_layout.setColumnStretch(5, screen.width() // 7)
    menu_layout.setColumnStretch(6, screen.width() // 21)

    menu_layout.setRowStretch(0, screen.height() // 27)
    menu_layout.setRowStretch(2, screen.height() // 13)
    menu_layout.setRowStretch(4, screen.height() // 27)
    menu_layout.setRowStretch(6, screen.height() // 27)
    menu_layout.setRowStretch(8, screen.height() // 27)
    menu_layout.setRowStretch(10, screen.height() // 27)
    menu_layout.setRowStretch(12, screen.height() // 9)
    menu_layout.setRowStretch(14, screen.height() // 27)

    background.setLayout(menu_layout)

    title = QLabel(background)
    title.setStyleSheet("border-image: url(./images/kotahi.png)")
    title.setFixedSize(screen.width() // 3, screen.height() // 10)
    menu_layout.addWidget(title, 1, 3)

    profile1 = QPushButton(mainWindow)
    if lang == "slovakia":
        profile1.setText("Vytvoriť nový profil")
    elif lang == "united-kingdom":
        profile1.setText("Create new profile")
    elif lang == "france":
        profile1.setText("Créer un nouveau profil")
    elif lang == "germany":
        profile1.setText("Neues profil erstellen")
    elif lang == "russia":
        profile1.setText("Создать новый профиль")
    else:
        profile1.setText("Crear nuevo perfil")
    profile1.setStyleSheet("border-image: none")
    profile1.setCursor(Qt.PointingHandCursor)
    profile1.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile1, 3, 3)

    profile2 = QPushButton(mainWindow)
    if lang == "slovakia":
        profile2.setText("Vytvoriť nový profil")
    elif lang == "united-kingdom":
        profile2.setText("Create new profile")
    elif lang == "france":
        profile2.setText("Créer un nouveau profil")
    elif lang == "germany":
        profile2.setText("Neues profil erstellen")
    elif lang == "russia":
        profile2.setText("Создать новый профиль")
    else:
        profile2.setText("Crear nuevo perfil")
    profile2.setStyleSheet("border-image: none")
    profile2.setCursor(Qt.PointingHandCursor)
    profile2.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile2, 5, 3)

    profile3 = QPushButton(mainWindow)
    if lang == "slovakia":
        profile3.setText("Vytvoriť nový profil")
    elif lang == "united-kingdom":
        profile3.setText("Create new profile")
    elif lang == "france":
        profile3.setText("Créer un nouveau profil")
    elif lang == "germany":
        profile3.setText("Neues profil erstellen")
    elif lang == "russia":
        profile3.setText("Создать новый профиль")
    else:
        profile3.setText("Crear nuevo perfil")
    profile3.setStyleSheet("border-image: none")
    profile3.setCursor(Qt.PointingHandCursor)
    profile3.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile3, 7, 3)

    profile4 = QPushButton(mainWindow)
    if lang == "slovakia":
        profile4.setText("Vytvoriť nový profil")
    elif lang == "united-kingdom":
        profile4.setText("Create new profile")
    elif lang == "france":
        profile4.setText("Créer un nouveau profil")
    elif lang == "germany":
        profile4.setText("Neues profil erstellen")
    elif lang == "russia":
        profile4.setText("Создать новый профиль")
    else:
        profile4.setText("Crear nuevo perfil")
    profile4.setStyleSheet("border-image: none")
    profile4.setCursor(Qt.PointingHandCursor)
    profile4.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile4, 9, 3)

    profile5 = QPushButton(mainWindow)
    if lang == "slovakia":
        profile5.setText("Vytvoriť nový profil")
    elif lang == "united-kingdom":
        profile5.setText("Create new profile")
    elif lang == "france":
        profile5.setText("Créer un nouveau profil")
    elif lang == "germany":
        profile5.setText("Neues profil erstellen")
    elif lang == "russia":
        profile5.setText("Создать новый профиль")
    else:
        profile5.setText("Crear nuevo perfil")
    profile5.setStyleSheet("border-image: none")
    profile5.setCursor(Qt.PointingHandCursor)
    profile5.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile5, 11, 3)

    quitButton = QPushButton(mainWindow)
    if lang == "slovakia":
        quitButton.setText("Ukončiť hru")
    elif lang == "united-kingdom":
        quitButton.setText("Quit game")
    elif lang == "france":
        quitButton.setText("Quitter le jeu")
    elif lang == "germany":
        quitButton.setText("Spiel verlassen")
    elif lang == "russia":
        quitButton.setText("Выйти из игры")
    else:
        quitButton.setText("Salir del juego")
    quitButton.setStyleSheet("border-image: none")
    quitButton.setCursor(Qt.PointingHandCursor)
    quitButton.setFixedSize(screen.width() // 7, screen.height() // 13)
    menu_layout.addWidget(quitButton, 13, 3, alignment=Qt.AlignCenter)
    quitButton.clicked.connect(quitConfirm)

    shopButton = QPushButton(mainWindow)
    if lang == "slovakia":
        shopButton.setText("Obchod")
    elif lang == "united-kingdom":
        shopButton.setText("Shop")
    elif lang == "france":
        shopButton.setText("Boutique")
    elif lang == "germany":
        shopButton.setText("Einkaufen")
    elif lang == "russia":
        shopButton.setText("Магазин")
    else:
        shopButton.setText("Tienda")
    shopButton.setStyleSheet("border-image: none")
    shopButton.setCursor(Qt.PointingHandCursor)
    shopButton.setFixedSize(screen.width() // 7, screen.height() // 13)
    menu_layout.addWidget(shopButton, 13, 1)
    shopButton.clicked.connect(shop)

    languageButton = QPushButton(mainWindow)
    languageButton.setStyleSheet("border-image: url(./images/%s.png)" % lang)
    languageButton.setCursor(Qt.PointingHandCursor)
    languageButton.setFixedSize(screen.height() // 13, screen.height() // 13)
    menu_layout.addWidget(languageButton, 13, 5, alignment=Qt.AlignCenter)
    languageButton.clicked.connect(language)

    mainWindow.setCentralWidget(background)
    mainWindow.update()

def main():
    app = QApplication(sys.argv)
    global background
    global mainWindow
    global languageButton
    global lang
    mainWindow = QMainWindow()
    mainWindow.setStyleSheet("border-image: url(./images/background.jpg); background-attachment: fixed")

    screen = QDesktopWidget().screenGeometry()

    mainWindow.resize(screen.width(), screen.height())
    mainWindow.setWindowTitle('Kotahi')
    mainWindow.setWindowIcon(QIcon('./images/icon.png'))
    mainWindow.showFullScreen()

#BACKGROUND
    background = QWidget(mainWindow)
    background.setFixedSize(screen.width(), screen.height())
    background.setStyleSheet(".QWidget{border-image: url(./images/background.jpg)}")

    menu_layout = QGridLayout(background)
    menu_layout.setColumnStretch(0, screen.width() // 21)
    menu_layout.setColumnStretch(2, screen.width() // 7)
    menu_layout.setColumnStretch(4, screen.width() // 7)
    menu_layout.setColumnStretch(5, screen.width() // 7)
    menu_layout.setColumnStretch(6, screen.width() // 21)

    menu_layout.setRowStretch(0, screen.height() // 27)
    menu_layout.setRowStretch(2, screen.height() // 13)
    menu_layout.setRowStretch(4, screen.height() // 27)
    menu_layout.setRowStretch(6, screen.height() // 27)
    menu_layout.setRowStretch(8, screen.height() // 27)
    menu_layout.setRowStretch(10, screen.height() // 27)
    menu_layout.setRowStretch(12, screen.height() // 9)
    menu_layout.setRowStretch(14, screen.height() // 27)

    background.setLayout(menu_layout)

    title = QLabel(background)
    title.setStyleSheet("border-image: url(./images/kotahi.png)")
    title.setFixedSize(screen.width() // 3, screen.height() // 10)
    menu_layout.addWidget(title, 1, 3)

    profile1 = QPushButton(mainWindow)
    profile1.setText("Vytvoriť nový profil")
    profile1.setStyleSheet("border-image: none")
    profile1.setCursor(Qt.PointingHandCursor)
    profile1.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile1, 3, 3)

    profile2 = QPushButton(mainWindow)
    profile2.setText("Vytvoriť nový profil")
    profile2.setStyleSheet("border-image: none")
    profile2.setCursor(Qt.PointingHandCursor)
    profile2.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile2, 5, 3)

    profile3 = QPushButton(mainWindow)
    profile3.setText("Vytvoriť nový profil")
    profile3.setStyleSheet("border-image: none")
    profile3.setCursor(Qt.PointingHandCursor)
    profile3.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile3, 7, 3)

    profile4 = QPushButton(mainWindow)
    profile4.setText("Vytvoriť nový profil")
    profile4.setStyleSheet("border-image: none")
    profile4.setCursor(Qt.PointingHandCursor)
    profile4.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile4, 9, 3)

    profile5 = QPushButton(mainWindow)
    profile5.setText("Vytvoriť nový profil")
    profile5.setStyleSheet("border-image: none")
    profile5.setCursor(Qt.PointingHandCursor)
    profile5.setFixedSize(screen.width() // 3, screen.height() // 13)
    #    profile1.clicked.connect()
    menu_layout.addWidget(profile5, 11, 3)

    quitButton = QPushButton(mainWindow)
    quitButton.setText("Ukončiť hru")
    quitButton.setStyleSheet("border-image: none")
    quitButton.setCursor(Qt.PointingHandCursor)
    quitButton.setFixedSize(screen.width() // 7, screen.height() // 13)
    menu_layout.addWidget(quitButton, 13, 3, alignment=Qt.AlignCenter)
    quitButton.clicked.connect(quitConfirm)

    shopButton = QPushButton(mainWindow)
    shopButton.setText("Obchod")
    shopButton.setStyleSheet("border-image: none")
    shopButton.setCursor(Qt.PointingHandCursor)
    shopButton.setFixedSize(screen.width() // 7, screen.height() // 13)
    menu_layout.addWidget(shopButton, 13, 1)
    shopButton.clicked.connect(shop)

    languageButton = QPushButton(mainWindow)
    languageButton.setStyleSheet("border-image: url(./images/%s.png)" % lang)
    languageButton.setCursor(Qt.PointingHandCursor)
    languageButton.setFixedSize(screen.height() // 13, screen.height() // 13)
    menu_layout.addWidget(languageButton, 13, 5, alignment=Qt.AlignCenter)
    languageButton.clicked.connect(language)

    mainWindow.setCentralWidget(background)
    mainWindow.update()

    sys.exit(app.exec_())

main()
