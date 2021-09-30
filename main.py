import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QMainWindow, QMenuBar, \
    QSpinBox, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

global background
global mainWindow
global languageButton
global lang
global name
name = ""
lang = "slovakia"

def selectName(self):
    name = self.inputLine.text()
    print("Changed: " + name)

def new():
    global mainWindow
    global name
    global lang

    newWindow = QWidget()

    screen = QDesktopWidget().screenGeometry()

    newLayout = QGridLayout(newWindow)
    newLayout.setColumnStretch(0, screen.width() // 3)
    newLayout.setColumnStretch(2, screen.width() // 15)
    newLayout.setColumnStretch(4, screen.width() // 3)

    newLayout.setRowStretch(0, screen.height() // 3)
    newLayout.setRowStretch(2, screen.height() // 15)
    newLayout.setRowStretch(4, screen.height() // 3)

    newWindow.setLayout(newLayout)

    title = QLabel(background)
    if lang == "slovakia":
        title.setText("Zadajte meno:")
    elif lang == "united-kingdom":
        title.setText("Select a name:")
    elif lang == "france":
        title.setText("Sélectionnez un nom :")
    elif lang == "germany":
        title.setText("Wählen sie einen namen:")
    else:
        title.setText("Выберите имя:")
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
    title.setFixedSize(screen.width() // 5, screen.height() // 7)
    newLayout.addWidget(title, 1, 2)

    inputLine = QLineEdit(background)
    inputLine.setStyleSheet("border-image: none")
    inputLine.setFont(QFont("Arial", 20))
    inputLine.setMaxLength(20)
    inputLine.setAlignment(Qt.AlignCenter)
    newLayout.addWidget(inputLine, 2, 2)

    backButton = QPushButton(newWindow)
    if lang == "slovakia":
        backButton.setText("Späť")
    elif lang == "united-kingdom":
        backButton.setText("Back")
    elif lang == "france":
        backButton.setText("Arrière")
    elif lang == "germany":
        backButton.setText("Zurück")
    else:
        backButton.setText("Назад")
    backButton.setStyleSheet("border-image: none")
    backButton.setFixedSize(screen.width() // 7, screen.height() // 7)
    backButton.clicked.connect(selectName)
    newLayout.addWidget(backButton, 3, 2, alignment=Qt.AlignCenter)

    mainWindow.setCentralWidget(newWindow)
    mainWindow.update()

def help():
    global mainWindow
    global quitWindow
    global lang

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
    if lang == "slovakia":
        title.setText("Nápoveda po slovensky")
    elif lang == "united-kingdom":
        title.setText("Nápoveda po anglicky")
    elif lang == "france":
        title.setText("Nápoveda po francúzsky")
    elif lang == "germany":
        title.setText("Nápoveda po nemecky")
    else:
        title.setText("Nápoveda po rusky")
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
    title.setFixedSize(screen.width() // 5, screen.height() // 7)
    quitLayout.addWidget(title, 1, 2, )

    backButton = QPushButton(quitWindow)
    if lang == "slovakia":
        backButton.setText("Späť")
    elif lang == "united-kingdom":
        backButton.setText("Back")
    elif lang == "france":
        backButton.setText("Arrière")
    elif lang == "germany":
        backButton.setText("Zurück")
    else:
        backButton.setText("Назад")
    backButton.setStyleSheet("border-image: none")
    backButton.setFixedSize(screen.width() // 7, screen.height() // 7)
    backButton.clicked.connect(menu)
    quitLayout.addWidget(backButton, 3, 2, alignment=Qt.AlignCenter)

    mainWindow.setCentralWidget(quitWindow)
    mainWindow.update()

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
    else:
        lang = "slovakia"

    languageButton.setStyleSheet("border-image: url(./images/%s.png)" % lang)
    menu()

def quitConfirm():
    global mainWindow
    global quitWindow
    global lang
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
    if lang == "slovakia":
        title.setText("Ste si istý?")
    elif lang == "united-kingdom":
        title.setText("Are you sure?")
    elif lang == "france":
        title.setText("Es-tu sûr?")
    elif lang == "germany":
        title.setText("Bist du sicher?")
    else:
        title.setText("Вы уверены?")
    title.setAlignment(Qt.AlignCenter)
    title.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
    title.setFixedSize(screen.width() // 5, screen.height() // 7)
    quitLayout.addWidget(title, 1, 2)

    confirmButton = QPushButton(quitWindow)
    if lang == "slovakia":
        confirmButton.setText("Áno")
    elif lang == "united-kingdom":
        confirmButton.setText("Yes")
    elif lang == "france":
        confirmButton.setText("Oui")
    elif lang == "germany":
        confirmButton.setText("Ja")
    else:
        confirmButton.setText("да")
    confirmButton.setStyleSheet("border-image: none")
    confirmButton.setFixedSize(screen.width() // 7, screen.height() // 7)
    confirmButton.clicked.connect(confirm)
    quitLayout.addWidget(confirmButton, 3, 1)

    declineButton = QPushButton(quitWindow)
    if lang == "slovakia":
        declineButton.setText("Nie")
    elif lang == "united-kingdom":
        declineButton.setText("No")
    elif lang == "france":
        declineButton.setText("Non")
    elif lang == "germany":
        declineButton.setText("Nein")
    else:
        declineButton.setText("Нет")
    declineButton.setStyleSheet("border-image: none")
    declineButton.setFixedSize(screen.width() // 7, screen.height() // 7)
    declineButton.clicked.connect(menu)
    quitLayout.addWidget(declineButton, 3, 3)

    mainWindow.setCentralWidget(quitWindow)
    mainWindow.update()

def confirm():
    sys.exit(1)

def menu():
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
    else:
        profile1.setText("Создать новый профиль")
    profile1.setStyleSheet("border-image: none")
    profile1.setCursor(Qt.PointingHandCursor)
    profile1.setFixedSize(screen.width() // 3, screen.height() // 13)
    profile1.clicked.connect(new)
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
    else:
        profile2.setText("Создать новый профиль")
    profile2.setStyleSheet("border-image: none")
    profile2.setCursor(Qt.PointingHandCursor)
    profile2.setFixedSize(screen.width() // 3, screen.height() // 13)
    profile2.clicked.connect(new)
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
    else:
        profile3.setText("Создать новый профиль")
    profile3.setStyleSheet("border-image: none")
    profile3.setCursor(Qt.PointingHandCursor)
    profile3.setFixedSize(screen.width() // 3, screen.height() // 13)
    profile3.clicked.connect(new)
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
    else:
        profile4.setText("Создать новый профиль")
    profile4.setStyleSheet("border-image: none")
    profile4.setCursor(Qt.PointingHandCursor)
    profile4.setFixedSize(screen.width() // 3, screen.height() // 13)
    profile4.clicked.connect(new)
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
    else:
        profile5.setText("Создать новый профиль")
    profile5.setStyleSheet("border-image: none")
    profile5.setCursor(Qt.PointingHandCursor)
    profile5.setFixedSize(screen.width() // 3, screen.height() // 13)
    profile5.clicked.connect(new)
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
    else:
        quitButton.setText("Выйти из игры")
    quitButton.setStyleSheet("border-image: none")
    quitButton.setCursor(Qt.PointingHandCursor)
    quitButton.setFixedSize(screen.width() // 7, screen.height() // 13)
    menu_layout.addWidget(quitButton, 13, 3, alignment=Qt.AlignCenter)
    quitButton.clicked.connect(quitConfirm)

    helpButton = QPushButton(mainWindow)
    if lang == "slovakia":
        helpButton.setText("Nápoveda")
    elif lang == "united-kingdom":
        helpButton.setText("Help")
    elif lang == "france":
        helpButton.setText("Aider")
    elif lang == "germany":
        helpButton.setText("Hilfe")
    else:
        helpButton.setText("Помощь")
    helpButton.setStyleSheet("border-image: none")
    helpButton.setCursor(Qt.PointingHandCursor)
    helpButton.setFixedSize(screen.width() // 7, screen.height() // 13)
    menu_layout.addWidget(helpButton, 13, 1)
    helpButton.clicked.connect(help)

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

    menu()
    sys.exit(app.exec_())

main()
