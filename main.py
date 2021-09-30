import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QMainWindow, QMenuBar, \
    QSpinBox, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

profileNames = []
lang = "slovakia"
name = ""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        global background
        global mainWindow
        global languageButton
        global screen
        global lang
        global profileNames

        try:
            open("savegame.ktg", "r")
        except IOError:
            createFile = open("savegame.ktg", "w")
            createFile.write("~\n~\n~\n~\n~")
            createFile.close()

        save = open("savegame.ktg", "r")
        while True:
            tmp = save.readline()
            if tmp == "":
                break
            elif "~" in tmp:
                profileNames.append("~")
            else:
                temp = tmp.split("+")
                profileNames.append(temp[0])
        save.close()

        print(profileNames)

        mainWindow = QMainWindow()
        mainWindow.setStyleSheet("border-image: url(./images/background.jpg); background-attachment: fixed")

        screen = QDesktopWidget().screenGeometry()

        mainWindow.resize(screen.width(), screen.height())
        mainWindow.setWindowTitle('Kotahi')
        mainWindow.setWindowIcon(QIcon('./images/icon.png'))
        mainWindow.showFullScreen()

        self.menu()
        sys.exit(app.exec_())

    def gameConfig(self):
        global mainWindow
        global background
        global screen
        global profile
        global inputLine
        global profileNames
        global languageButton
        global lang

        if profile not in profileNames or "Profil" in profile or "Профиль" in profile:
            if not inputLine.text():
                return

            if profile == "Profil 1":
                profileNames[0] = inputLine.text()
            elif profile == "Profil 2":
                profileNames[1] = inputLine.text()
            elif profile == "Profil 3":
                profileNames[2] = inputLine.text()
            elif profile == "Profil 4":
                profileNames[3] = inputLine.text()
            elif profile == "Profil 5":
                profileNames[4] = inputLine.text()

            profile = inputLine.text()

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

        if lang == "slovakia":
            name = "%s" % (profile)
        elif lang == "united-kingdom":
            name = "%s" % (profile)
        elif lang == "france":
            name = "%s" % (profile)
        elif lang == "germany":
            name = "%s" % (profile)
        else:
            name = "%s" % (profile)
        title = QLabel(background)
        title.setText(name)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
        title.setFixedSize(screen.width() // 3, screen.height() // 10)
        menu_layout.addWidget(title, 1, 3)

        profile1 = QPushButton(mainWindow)
        if lang == "slovakia":
            profile1.setText("Počet hráčov")
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
        profile1.clicked.connect(self.new)
        menu_layout.addWidget(profile1, 3, 3)

        profile2 = QPushButton(mainWindow)
        if lang == "slovakia":
            profile2.setText("Výber témy")
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
        profile2.clicked.connect(self.new)
        menu_layout.addWidget(profile2, 5, 3)

        profile3 = QPushButton(mainWindow)
        if lang == "slovakia":
            profile3.setText("Výber obrázku profilu")
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
        profile3.clicked.connect(self.new)
        menu_layout.addWidget(profile3, 7, 3)

        shopButton = QPushButton(mainWindow)
        if lang == "slovakia":
            shopButton.setText("Obchod")
        elif lang == "united-kingdom":
            shopButton.setText("Create new profile")
        elif lang == "france":
            shopButton.setText("Créer un nouveau profil")
        elif lang == "germany":
            shopButton.setText("Neues profil erstellen")
        else:
            shopButton.setText("Создать новый профиль")
        shopButton.setStyleSheet("border-image: none")
        shopButton.setCursor(Qt.PointingHandCursor)
        shopButton.setFixedSize(screen.width() // 3, screen.height() // 13)
        shopButton.clicked.connect(self.new)
        menu_layout.addWidget(shopButton, 11, 3)

        menuButton = QPushButton(mainWindow)
        if lang == "slovakia":
            menuButton.setText("Hlavné menu")
        elif lang == "united-kingdom":
            menuButton.setText("Main menu")
        elif lang == "france":
            menuButton.setText("Menu principal")
        elif lang == "germany":
            menuButton.setText("Hauptmenü")
        else:
            menuButton.setText("Главное меню")
        menuButton.setStyleSheet("border-image: none")
        menuButton.setCursor(Qt.PointingHandCursor)
        menuButton.setFixedSize(screen.width() // 7, screen.height() // 13)
        menu_layout.addWidget(menuButton, 13, 1)
        menuButton.clicked.connect(self.menu)

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
        menu_layout.addWidget(quitButton, 13, 5)
        quitButton.clicked.connect(self.quitConfirm)

        mainWindow.setCentralWidget(background)
        mainWindow.update()

    def new(self):
        global mainWindow
        global inputLine
        global screen
        global profile
        global lang

        profile = self.sender().text()

        if profile in profileNames and "Profil" not in profile and "Профиль" not in profile:
            self.gameConfig()
        else:
            newWindow = QWidget()

            newLayout = QGridLayout(newWindow)
            newLayout.setColumnStretch(0, screen.width() // 3)
            newLayout.setColumnStretch(2, screen.width() // 15)
            newLayout.setColumnStretch(4, screen.width() // 3)

            newLayout.setRowStretch(0, screen.height() // 3)
            newLayout.setRowStretch(2, screen.height() // 15)
            newLayout.setRowStretch(5, screen.height() // 3)

            newWindow.setLayout(newLayout)

            title = QLabel(background)
            if lang == "slovakia":
                title.setText("Zadajte meno:")
            elif lang == "united-kingdom":
                title.setText("Select a name:")
            elif lang == "france":
                title.setText("Sélectionnez un nom:")
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

            nextButton = QPushButton(newWindow)
            if lang == "slovakia":
                nextButton.setText("Ďalej")
            elif lang == "united-kingdom":
                nextButton.setText("Next")
            elif lang == "france":
                nextButton.setText("Prochain")
            elif lang == "germany":
                nextButton.setText("Nächste")
            else:
                nextButton.setText("Следующий")
            nextButton.setStyleSheet("border-image: none")
            nextButton.setFixedSize(screen.width() // 7, screen.height() // 7)
            nextButton.clicked.connect(self.gameConfig)
            newLayout.addWidget(nextButton, 3, 2, alignment=Qt.AlignCenter)

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
            backButton.clicked.connect(self.menu)
            newLayout.addWidget(backButton, 4, 2, alignment=Qt.AlignCenter)

            mainWindow.setCentralWidget(newWindow)
            mainWindow.update()

    def help(self):
        global mainWindow
        global quitWindow
        global screen
        global lang

        quitWindow = QWidget()

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
        backButton.clicked.connect(self.menu)
        quitLayout.addWidget(backButton, 3, 2, alignment=Qt.AlignCenter)

        mainWindow.setCentralWidget(quitWindow)
        mainWindow.update()

    def language(self):
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

        self.menu()

    def quitConfirm(self):
        global mainWindow
        global quitWindow
        global screen
        global lang
        quitWindow = QWidget()

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
        confirmButton.clicked.connect(self.confirm)
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
        declineButton.clicked.connect(self.menu)
        quitLayout.addWidget(declineButton, 3, 3)

        mainWindow.setCentralWidget(quitWindow)
        mainWindow.update()

    def confirm(self):
        global profileNames

        save = open("savegame.ktg", "w+")
        save.write("%s+\n%s+\n%s+\n%s+\n%s+" % (profileNames[0], profileNames[1], profileNames[2], profileNames[3], profileNames[4]))
        save.close()

        sys.exit(1)

    def deleteProfile(self):
        global profileNames

        profile = self.sender().text()
        profileNames[int(profile)] = "~"

        self.menu()

    def menu(self):
        global mainWindow
        global background
        global languageButton
        global profileName
        global screen
        global lang

        invisible = QFont("Arial", 1)
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
        if profileNames[0] != "~":
            profile1.setText(profileNames[0])
            profile1.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
        else:
            if lang == "slovakia":
                profile1.setText("Profil 1")
            elif lang == "united-kingdom":
                profile1.setText("Profile 1")
            elif lang == "france":
                profile1.setText("Profil 1")
            elif lang == "germany":
                profile1.setText("Profil 1")
            else:
                profile1.setText("Профиль 1")
            profile1.setFixedSize(screen.width() // 3, screen.height() // 13)
        profile1.setStyleSheet("border-image: none")
        profile1.setCursor(Qt.PointingHandCursor)
        profile1.clicked.connect(self.new)
        menu_layout.addWidget(profile1, 3, 3, alignment=Qt.AlignLeft)

        if profileNames[0] != "~":
            profile1delete = QPushButton(mainWindow)
            profile1delete.setText("0")
            profile1delete.setFont(invisible)
            profile1delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile1delete.setCursor(Qt.PointingHandCursor)
            profile1delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile1delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile1delete, 3, 3, alignment=Qt.AlignRight)

        profile2 = QPushButton(mainWindow)
        if profileNames[1] != "~":
            profile2.setText(profileNames[1])
            profile2.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
        else:
            if lang == "slovakia":
                profile2.setText("Profil 2")
            elif lang == "united-kingdom":
                profile2.setText("Profile 2")
            elif lang == "france":
                profile2.setText("Profil 2")
            elif lang == "germany":
                profile2.setText("Profil 2")
            else:
                profile2.setText("Профиль 2")
            profile2.setFixedSize(screen.width() // 3, screen.height() // 13)
        profile2.setStyleSheet("border-image: none")
        profile2.setCursor(Qt.PointingHandCursor)
        profile2.clicked.connect(self.new)
        menu_layout.addWidget(profile2, 5, 3, alignment=Qt.AlignLeft)

        if profileNames[1] != "~":
            profile2delete = QPushButton(mainWindow)
            profile2delete.setText("1")
            profile2delete.setFont(invisible)
            profile2delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile2delete.setCursor(Qt.PointingHandCursor)
            profile2delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile2delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile2delete, 5, 3, alignment=Qt.AlignRight)

        profile3 = QPushButton(mainWindow)
        if profileNames[2] != "~":
            profile3.setText(profileNames[2])
            profile3.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
        else:
            if lang == "slovakia":
                profile3.setText("Profil 3")
            elif lang == "united-kingdom":
                profile3.setText("Profile 3")
            elif lang == "france":
                profile3.setText("Profil 3")
            elif lang == "germany":
                profile3.setText("Profil 3")
            else:
                profile3.setText("Профиль 3")
            profile3.setFixedSize(screen.width() // 3, screen.height() // 13)
        profile3.setStyleSheet("border-image: none")
        profile3.setCursor(Qt.PointingHandCursor)
        profile3.clicked.connect(self.new)
        menu_layout.addWidget(profile3, 7, 3, alignment=Qt.AlignLeft)

        if profileNames[2] != "~":
            profile3delete = QPushButton(mainWindow)
            profile3delete.setText("2")
            profile3delete.setFont(invisible)
            profile3delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile3delete.setCursor(Qt.PointingHandCursor)
            profile3delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile3delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile3delete, 7, 3, alignment=Qt.AlignRight)

        profile4 = QPushButton(mainWindow)
        if profileNames[3] != "~":
            profile4.setText(profileNames[3])
            profile4.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
        else:
            if lang == "slovakia":
                profile4.setText("Profil 4")
            elif lang == "united-kingdom":
                profile4.setText("Profile 4")
            elif lang == "france":
                profile4.setText("Profil 4")
            elif lang == "germany":
                profile4.setText("Profil 4")
            else:
                profile4.setText("Профиль 4")
            profile4.setFixedSize(screen.width() // 3, screen.height() // 13)
        profile4.setStyleSheet("border-image: none")
        profile4.setCursor(Qt.PointingHandCursor)
        profile4.clicked.connect(self.new)
        menu_layout.addWidget(profile4, 9, 3, alignment=Qt.AlignLeft)

        if profileNames[3] != "~":
            profile4delete = QPushButton(mainWindow)
            profile4delete.setText("3")
            profile4delete.setFont(invisible)
            profile4delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile4delete.setCursor(Qt.PointingHandCursor)
            profile4delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile4delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile4delete, 9, 3, alignment=Qt.AlignRight)

        profile5 = QPushButton(mainWindow)
        if profileNames[4] != "~":
            profile5.setText(profileNames[4])
            profile5.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
        else:
            if lang == "slovakia":
                profile5.setText("Profil 5")
            elif lang == "united-kingdom":
                profile5.setText("Profile 5")
            elif lang == "france":
                profile5.setText("Profil 5")
            elif lang == "germany":
                profile5.setText("Profil 5")
            else:
                profile5.setText("Профиль 5")
            profile5.setFixedSize(screen.width() // 3, screen.height() // 13)
        profile5.setStyleSheet("border-image: none")
        profile5.setCursor(Qt.PointingHandCursor)
        profile5.clicked.connect(self.new)
        menu_layout.addWidget(profile5, 11, 3, alignment=Qt.AlignLeft)

        if profileNames[4] != "~":
            profile5delete = QPushButton(mainWindow)
            profile5delete.setText("4")
            profile5delete.setFont(invisible)
            profile5delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile5delete.setCursor(Qt.PointingHandCursor)
            profile5delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile5delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile5delete, 11, 3, alignment=Qt.AlignRight)

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
        quitButton.clicked.connect(self.quitConfirm)

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
        helpButton.clicked.connect(self.help)

        languageButton = QPushButton(mainWindow)
        languageButton.setStyleSheet("border-image: url(./images/%s.png)" % lang)
        languageButton.setCursor(Qt.PointingHandCursor)
        languageButton.setFixedSize(screen.height() // 13, screen.height() // 13)
        menu_layout.addWidget(languageButton, 13, 5, alignment=Qt.AlignCenter)
        languageButton.clicked.connect(self.language)

        mainWindow.setCentralWidget(background)
        mainWindow.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
