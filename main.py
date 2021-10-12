import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, QMainWindow, QMenuBar, \
    QSpinBox, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

profileNames = []
profiles = []
highScores = []
playedGames = []
wins = []
themes = []
pictures = []
coins = []
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
            createFile.write("slovakia\n-\n-\n-\n-\n-")
            createFile.close()

        save = open("savegame.ktg", "r")

        while True:
            tmp = save.readline().rstrip('\n')
            if tmp == "":
                break
            elif tmp == "slovakia" or tmp == "united-kingdom" or tmp == "france" or tmp == "germany" or tmp == "russia":
                lang = tmp
            elif "-" in tmp:
                profileNames.append("-")
                profiles.append("~")
                highScores.append(0)
                playedGames.append(0)
                wins.append(0)
                themes.append("~")
                pictures.append("~")
                coins.append(100)
            else:
                temp = tmp.split("+")
                profileNames.append(temp[0])
                profiles.append(temp[1])
                highScores.append(temp[2])
                playedGames.append(temp[3])
                wins.append(temp[4])
                themes.append(temp[5])
                pictures.append(temp[6])
                coins.append(temp[7])
        save.close()

        mainWindow = QMainWindow()
        mainWindow.setStyleSheet("border-image: url(./images/background.jpg); background-attachment: fixed")

        screen = QDesktopWidget().screenGeometry()

        mainWindow.resize(screen.width(), screen.height())
        mainWindow.setWindowTitle('Kotahi')
        mainWindow.setWindowIcon(QIcon('./images/icon.png'))
        mainWindow.showFullScreen()
#################self.menu()
        self.game()
        sys.exit(app.exec_())

    def game(self):
        global mainWindow
        global background
        global screen
        global profile
        global inputLine
        global profileNames
        global languageButton
        global lang

        background = QWidget(mainWindow)
        background.setFixedSize(screen.width(), screen.height())
        background.setStyleSheet(".QWidget{border-image: url(./images/gameBackground.jpg)}")

        game_layout = QGridLayout(background)

        game_layout.setRowStretch(0, 47)
        game_layout.setRowStretch(1, 189)
        game_layout.setRowStretch(2, 18)
        game_layout.setRowStretch(3, 31)
        game_layout.setRowStretch(4, 78)
        game_layout.setRowStretch(5, 330)
        game_layout.setRowStretch(6, 92)
        game_layout.setRowStretch(7, 224)
        game_layout.setRowStretch(8, 69)

        background.setLayout(game_layout)

## TOP PART
        topPart = QWidget(background)
        topPart.setStyleSheet(".QWidget {border-image: none}")
        game_layout.addWidget(topPart, 1, 0)
        topLayout = QGridLayout(topPart)
        topLayout.setContentsMargins(0, 0, 0, 0)

        topLayout.setColumnStretch(0, 62)
        topLayout.setColumnStretch(1, 119)
        topLayout.setColumnStretch(2, 487)
        topLayout.setColumnStretch(3, 115)
        topLayout.setColumnStretch(4, 24)
        topLayout.setColumnStretch(5, 330)
        topLayout.setColumnStretch(6, 24)
        topLayout.setColumnStretch(7, 138)
        topLayout.setColumnStretch(8, 439)
        topLayout.setColumnStretch(9, 119)
        topLayout.setColumnStretch(10, 62)

        time = QLabel(topPart)
        time.setText("Time")
        time.setAlignment(Qt.AlignTop)
        time.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
        topLayout.addWidget(time, 0, 1)

    ##BOT 1 NAME
        bot1 = QWidget(topPart)
        bot1.setStyleSheet(".QWidget {border-image: none}")
        topLayout.addWidget(bot1, 0, 3)
        bot1NameLayout = QGridLayout(bot1)
        bot1NameLayout.setContentsMargins(0, 10, 0, 0)

        bot1Image = QWidget(topPart)
        bot1Image.setStyleSheet("border-image: url(./images/profile.jpg)")
        bot1Image.setFixedSize(115, 115)
        bot1NameLayout.addWidget(bot1Image, 1, 0)

        bot1Name = QLabel(topPart)
        bot1Name.setText("Name")
        bot1Name.setAlignment(Qt.AlignCenter)
        bot1Name.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
        bot1NameLayout.addWidget(bot1Name, 2, 0)
    ##

    ##BOT 1 CARDS
        bot1Cards = QWidget(topPart)
        bot1Cards.setStyleSheet(".QWidget {border-image: none}")
        topLayout.addWidget(bot1Cards, 0, 5)
        bot1Layout = QGridLayout(bot1Cards)
        bot1Layout.setContentsMargins(0, 0, 0, 0)

        bot1Layout.setRowStretch(0, 130)

        bot1Card1 = QWidget(topPart)
        bot1Card1.setStyleSheet("border-image: url(./images/cardBackV.png)")
        bot1Layout.addWidget(bot1Card1, 0, 0)
        bot1Card2 = QWidget(topPart)
        bot1Card2.setStyleSheet("border-image: url(./images/cardBackV.png)")
        bot1Layout.addWidget(bot1Card2, 0, 1)
        bot1Card3 = QWidget(topPart)
        bot1Card3.setStyleSheet("border-image: url(./images/cardBackV.png)")
        bot1Layout.addWidget(bot1Card3, 0, 2)
        bot1Card4 = QWidget(topPart)
        bot1Card4.setStyleSheet("border-image: url(./images/cardBackV.png)")
        bot1Layout.addWidget(bot1Card4, 0, 3)
        bot1Card5 = QWidget(topPart)
        bot1Card5.setStyleSheet("border-image: url(./images/cardBackV.png)")
        bot1Layout.addWidget(bot1Card5, 0, 4)
    ##

        bot1More = QLabel(topPart)
        bot1More.setText("+X")
        bot1More.setAlignment(Qt.AlignCenter)
        bot1More.setStyleSheet(".QLabel {color: black; font: bold 32px} QWidget {border-image: none}")
        topLayout.addWidget(bot1More, 0, 7)

        buttonFont = QFont("Arial", 12)
        buttonFont.setItalic(True)

        menuButton = QPushButton(topPart)
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
        menuButton.setStyleSheet("border-image: none;" "border: 1px dashed black;" "border-radius: 15%;" "background-color: qlineargradient( x1:1 y1:1, x2:0 y2:0, stop:0 white, stop:1 gray);")
        menuButton.setFont(buttonFont)
        menuButton.setCursor(Qt.PointingHandCursor)
        topLayout.addWidget(menuButton, 0, 9, alignment=Qt.AlignTop)
        menuButton.clicked.connect(self.menu)

## MIDDLE TOP PART
        middleTopPart = QWidget(background)
        middleTopPart.setStyleSheet(".QWidget {border-image: none}")
        game_layout.addWidget(middleTopPart, 3, 0)
        middleTopLayout = QGridLayout(middleTopPart)

        middleTopLayout.setColumnStretch(0, 193)
        middleTopLayout.setColumnStretch(1, 138)
        middleTopLayout.setColumnStretch(2, 1259)
        middleTopLayout.setColumnStretch(3, 138)
        middleTopLayout.setColumnStretch(4, 193)

        bot2More = QLabel(topPart)
        bot2More.setText("+X")
        bot2More.setAlignment(Qt.AlignCenter)
        bot2More.setStyleSheet(".QLabel {color: black; font: bold 32px} QWidget {border-image: none}")
        middleTopLayout.addWidget(bot2More, 0, 1)

        bot3More = QLabel(topPart)
        bot3More.setText("+X")
        bot3More.setAlignment(Qt.AlignCenter)
        bot3More.setStyleSheet(".QLabel {color: black; font: bold 32px} QWidget {border-image: none}")
        middleTopLayout.addWidget(bot3More, 0, 3)
##

## MIDDLE PART
        middlePart = QWidget(background)
        middlePart.setStyleSheet(".QWidget {border-image: none}")
        game_layout.addWidget(middlePart, 5, 0)
        middleLayout = QGridLayout(middlePart)

        ##BOT 2 NAME
        bot2 = QWidget(topPart)
        bot2.setStyleSheet(".QWidget {border-image: none}")
        middleLayout.addWidget(bot2, 0, 0)
        bot2NameLayout = QGridLayout(bot2)
        bot2NameLayout.setContentsMargins(32, 10, 32, 0)

        bot2Image = QWidget(topPart)
        bot2Image.setStyleSheet("border-image: url(./images/profile.jpg)")
        bot2Image.setFixedSize(115, 115)
        bot2NameLayout.addWidget(bot2Image, 1, 0)

        bot2Name = QLabel(topPart)
        bot2Name.setText("Name")
        bot2Name.setAlignment(Qt.AlignCenter)
        bot2Name.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
        bot2NameLayout.addWidget(bot2Name, 2, 0)
        ##

        ##BOT 3 NAME
        bot3 = QWidget(topPart)
        bot3.setStyleSheet(".QWidget {border-image: none}")
        middleLayout.addWidget(bot3, 0, 7)
        bot3NameLayout = QGridLayout(bot3)
        bot3NameLayout.setContentsMargins(32, 10, 32, 0)

        bot3Image = QWidget(topPart)
        bot3Image.setStyleSheet("border-image: url(./images/profile.jpg)")
        bot3Image.setFixedSize(115, 115)
        bot3NameLayout.addWidget(bot3Image, 1, 0)

        bot3Name = QLabel(topPart)
        bot3Name.setText("Name")
        bot3Name.setAlignment(Qt.AlignCenter)
        bot3Name.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
        bot3NameLayout.addWidget(bot3Name, 2, 0)
        ##
##

## BOTTOM PART
        bottomPart = QWidget(background)
        bottomPart.setStyleSheet(".QWidget {border-image: none}")
        game_layout.addWidget(bottomPart, 7, 0)
        bottomLayout = QGridLayout(bottomPart)
        bottomLayout.setContentsMargins(0, 0, 47, 0)
        bottomLayout.setColumnStretch(1, 1402)
        bottomLayout.setColumnStretch(2, 47)

        ##PLAYER NAME
        player = QWidget(topPart)
        player.setStyleSheet(".QWidget {border-image: none}")
        bottomLayout.addWidget(player, 0, 0)
        playerNameLayout = QGridLayout(player)
        playerNameLayout.setContentsMargins(62, 10, 62, 0)

        playerImage = QWidget(topPart)
        playerImage.setStyleSheet("border-image: url(./images/panda.png)")
        playerImage.setFixedSize(133, 133)
        playerNameLayout.addWidget(playerImage, 1, 0)

        playerName = QLabel(topPart)
        playerName.setText("Diduška")
        playerName.setAlignment(Qt.AlignCenter)
        playerName.setStyleSheet(".QLabel {color: white; font: bold 32px} QWidget {border-image: none}")
        playerNameLayout.addWidget(playerName, 2, 0)
        ##

        ##PLAYER CARDS
        playerCards = QWidget(bottomPart)
        playerCards.setStyleSheet(".QWidget {border-image: none}")
        bottomLayout.addWidget(playerCards, 0, 1)
        playerLayout = QGridLayout(playerCards)
        playerLayout.setContentsMargins(0, 0, 0, 0)

        playerCard1 = QPushButton(bottomPart)
        playerCard1.setFixedSize(155, 225)
        playerCard1.setStyleSheet("border-image: url(./images/cardBackV.png)")
        playerCard1.setCursor(Qt.PointingHandCursor)
        playerLayout.addWidget(playerCard1, 0, 0)
        playerCard2 = QPushButton(bottomPart)
        playerCard2.setFixedSize(155, 225)
        playerCard2.setStyleSheet("border-image: url(./images/cardBackV.png)")
        playerCard2.setCursor(Qt.PointingHandCursor)
        playerLayout.addWidget(playerCard2, 0, 1)
        playerCard3 = QPushButton(bottomPart)
        playerCard3.setFixedSize(155, 225)
        playerCard3.setStyleSheet("border-image: url(./images/cardBackV.png)")
        playerCard3.setCursor(Qt.PointingHandCursor)
        playerLayout.addWidget(playerCard3, 0, 2)
        playerCard4 = QPushButton(bottomPart)
        playerCard4.setFixedSize(155, 225)
        playerCard4.setStyleSheet("border-image: url(./images/cardBackV.png)")
        playerCard4.setCursor(Qt.PointingHandCursor)
        playerLayout.addWidget(playerCard4, 0, 3)
        playerCard5 = QPushButton(bottomPart)
        playerCard5.setFixedSize(155, 225)
        playerCard5.setStyleSheet("border-image: url(./images/cardBackV.png)")
        playerCard5.setCursor(Qt.PointingHandCursor)
        playerLayout.addWidget(playerCard5, 0, 4)
        ##

        kotahiFont = QFont("Arial", 24)

        kotahiButton = QPushButton(topPart)
        kotahiButton.setFixedSize(168, 168)
        kotahiButton.setStyleSheet("QWidget {border-image: none;" "border: 5px solid black;" "border-radius: 80%;" "background-color: rgba(255, 0, 0, 65)}")
        kotahiButton.setCursor(Qt.PointingHandCursor)
        bottomLayout.addWidget(kotahiButton, 0, 3, alignment=Qt.AlignCenter)
        kotahiButton.clicked.connect(self.menu)

        kotahiText = QLabel(kotahiButton)
        kotahiText.setText("KOTAHI")
        kotahiText.setAlignment(Qt.AlignCenter)
        kotahiText.setAttribute(Qt.WA_TransparentForMouseEvents)
        kotahiText.setStyleSheet(".QLabel {color: white; font: 32px} QWidget {border-image: none}")
        kotahiText.setFixedSize(168, 168)
        bottomLayout.addWidget(kotahiText, 0, 3, alignment=Qt.AlignCenter)
##

        mainWindow.setCentralWidget(background)
        mainWindow.update()

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

        startGame = QPushButton(mainWindow)
        if lang == "slovakia":
            startGame.setText("Začať hru")
        elif lang == "united-kingdom":
            startGame.setText("Start game")
        elif lang == "france":
            startGame.setText("Démarrer jeu")
        elif lang == "germany":
            startGame.setText("Spiel starten")
        else:
            startGame.setText("Начать игру")
        startGame.setStyleSheet("border-image: none")
        startGame.setCursor(Qt.PointingHandCursor)
        startGame.setFixedSize(screen.width() // 3, screen.height() // 13)
        startGame.clicked.connect(self.game)
        menu_layout.addWidget(startGame, 7, 3)

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
            newLayout.setColumnStretch(0, screen.width() // 7)
            newLayout.setColumnStretch(1, screen.width() // 7)
            newLayout.setColumnStretch(2, screen.width() // 7)
            newLayout.setColumnStretch(3, screen.width() // 5)
            newLayout.setColumnStretch(4, screen.width() // 7)
            newLayout.setColumnStretch(5, screen.width() // 7)
            newLayout.setColumnStretch(6, screen.width() // 7)

            newLayout.setRowStretch(0, screen.height() // 3)
            newLayout.setRowStretch(2, screen.height() // 32)
            newLayout.setRowStretch(3, screen.height() // 8)
            newLayout.setRowStretch(4, screen.height() // 3)
            newLayout.setRowStretch(6, screen.height() // 8)

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
            title.setFixedSize(screen.width() // 5, screen.height() // 8)
            newLayout.addWidget(title, 1, 3)

            inputLine = QLineEdit(background)
            inputLine.setStyleSheet("border-image: none")
            inputLine.setFont(QFont("Arial", 20))
            inputLine.setMaxLength(20)
            inputLine.setAlignment(Qt.AlignCenter)
            newLayout.addWidget(inputLine, 3, 3)

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
            nextButton.setFixedSize(screen.width() // 7, screen.height() // 16)
            nextButton.clicked.connect(self.gameConfig)
            newLayout.addWidget(nextButton, 5, 5, alignment=Qt.AlignCenter)

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
            backButton.setFixedSize(screen.width() // 7, screen.height() // 16)
            backButton.clicked.connect(self.menu)
            newLayout.addWidget(backButton, 5, 1, alignment=Qt.AlignCenter)

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
        global lang
        global profileNames
        global profiles
        global highScores
        global playedGames
        global wins
        global themes
        global pictures
        global coins

        save = open("savegame.ktg", "w+")
        save.write("%s\n" % lang)
        save.write("%s+%s+%d+%d+%d+%s+%s+%d+\n" % (profileNames[0], profiles[0], highScores[0], playedGames[0], wins[0], themes[0], pictures[0], coins[0]))
        save.write("%s+%s+%d+%d+%d+%s+%s+%d+\n" % (profileNames[1], profiles[1], highScores[1], playedGames[1], wins[1], themes[1], pictures[1], coins[1]))
        save.write("%s+%s+%d+%d+%d+%s+%s+%d+\n" % (profileNames[2], profiles[2], highScores[2], playedGames[2], wins[2], themes[2], pictures[2], coins[2]))
        save.write("%s+%s+%d+%d+%d+%s+%s+%d+\n" % (profileNames[3], profiles[3], highScores[3], playedGames[3], wins[3], themes[3], pictures[3], coins[3]))
        save.write("%s+%s+%d+%d+%d+%s+%s+%d+\n" % (profileNames[4], profiles[4], highScores[4], playedGames[4], wins[4], themes[4], pictures[4], coins[4]))
        save.close()

        sys.exit(1)

    def deleteProfile(self):
        global profile1delete
        global profile2delete
        global profile3delete
        global profile4delete
        global profile5delete
        global profileNames
        global profile

        if self.sender().text() == "0" or self.sender().text() == "1" or self.sender().text() == "2" or self.sender().text() == "3" or self.sender().text() == "4":
            profile = self.sender().text()
            if profile == "0":
                profile1delete.setText(".")
                profile1delete.setStyleSheet("border-image: url(./images/deleteConfirm.png)")
                profile1delete.clicked.connect(self.deleteProfile)
            elif profile == "1":
                profile2delete.setText(".")
                profile2delete.setStyleSheet("border-image: url(./images/deleteConfirm.png)")
                profile2delete.clicked.connect(self.deleteProfile)
            elif profile == "2":
                profile3delete.setText(".")
                profile3delete.setStyleSheet("border-image: url(./images/deleteConfirm.png)")
                profile3delete.clicked.connect(self.deleteProfile)
            elif profile == "3":
                profile4delete.setText(".")
                profile4delete.setStyleSheet("border-image: url(./images/deleteConfirm.png)")
                profile4delete.clicked.connect(self.deleteProfile)
            elif profile == "4":
                profile5delete.setText(".")
                profile5delete.setStyleSheet("border-image: url(./images/deleteConfirm.png)")
                profile5delete.clicked.connect(self.deleteProfile)
        else:
            profileNames[int(profile)] = "-"
            self.menu()
        return

    def menu(self):
        global profile1delete
        global profile2delete
        global profile3delete
        global profile4delete
        global profile5delete
        global mainWindow
        global background
        global languageButton
        global profileName
        global screen
        global lang

        invisible = QFont("Arial", 1)
        buttonFont = QFont("Arial", 16)
        buttonFont.setItalic(True)
        background = QWidget(mainWindow)
        background.setFixedSize(screen.width(), screen.height())
        background.setStyleSheet("border-image: url(./images/background.jpg);")

        menu_layout = QGridLayout(background)
        menu_layout.setColumnStretch(0, screen.width() // 21)
        menu_layout.setColumnStretch(2, screen.width() // 7)
        menu_layout.setColumnStretch(4, screen.width() // 7)
        menu_layout.setColumnStretch(5, screen.width() // 7)
        menu_layout.setColumnStretch(6, screen.width() // 21)

        menu_layout.setRowStretch(0, screen.height() // 27)
        menu_layout.setRowStretch(2, screen.height() // 27)
        menu_layout.setRowStretch(4, screen.height() // 27)
        menu_layout.setRowStretch(6, screen.height() // 27)
        menu_layout.setRowStretch(8, screen.height() // 27)
        menu_layout.setRowStretch(10, screen.height() // 27)
        menu_layout.setRowStretch(12, screen.height() // 9)
        menu_layout.setRowStretch(14, screen.height() // 27)

        background.setLayout(menu_layout)

        title = QLabel(background)
        title.setStyleSheet("border-image: url(./images/kotahi.png)")
        title.setFixedSize((screen.height() // 9) * 3, screen.height() // 9)
        menu_layout.addWidget(title, 1, 3, alignment=Qt.AlignCenter)

        profile1 = QPushButton(mainWindow)
        profile1.setStyleSheet("border-image: none;" "border: 2px dashed black;" "border-radius: 15%;" "background-color: qlineargradient( x1:1 y1:1, x2:0 y2:0, stop:0 white, stop:1 gray);")
        profile1.setFont(buttonFont)
        profile1.setCursor(Qt.PointingHandCursor)
        profile1.clicked.connect(self.new)
        menu_layout.addWidget(profile1, 3, 3, alignment=Qt.AlignLeft)
        if profileNames[0] == "-":
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
        else:
            profile1.setText(profileNames[0])
            profile1.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)

            profile1score = QLabel(profile1)
            if lang == "slovakia":
                profile1score.setText("Odohrané: %s / %s\nRekord: %s\nZostatok: %s" % (wins[0], playedGames[0], highScores[0], coins[0]))
            elif lang == "united-kingdom":
                profile1score.setText("Played: %s / %s\nHighscore: %s\nBalance: %s" % (wins[0], playedGames[0], highScores[0], coins[0]))
            elif lang == "france":
                profile1score.setText("Joué: %s / %s\nScore élevé: %s\nÉquilibre: %s" % (wins[0], playedGames[0], highScores[0], coins[0]))
            elif lang == "germany":
                profile1score.setText("Gespielt: %s / %s\nHighscore: %s\nGleichgewicht: %s" % (wins[0], playedGames[0], highScores[0], coins[0]))
            else:
                profile1score.setText("Играл: %s / %s\nРекорд: %s\nОстаток средств: %s" % (wins[0], playedGames[0], highScores[0], coins[0]))
            profile1score.setAlignment(Qt.AlignRight)
            profile1score.setAttribute(Qt.WA_TransparentForMouseEvents)
            profile1score.setContentsMargins(0, 18, 18, 0)
            profile1score.setStyleSheet(".QLabel {color: black; font: thin 24px} QWidget {border-image: none}")
            profile1score.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
            menu_layout.addWidget(profile1score, 3, 3, alignment=Qt.AlignLeft)

            profile1delete = QPushButton(mainWindow)
            profile1delete.setText("0")
            profile1delete.setFont(invisible)
            profile1delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile1delete.setCursor(Qt.PointingHandCursor)
            profile1delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile1delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile1delete, 3, 3, alignment=Qt.AlignRight)

        profile2 = QPushButton(mainWindow)
        profile2.setStyleSheet("border-image: none;" "border: 2px dashed black;" "border-radius: 15%;" "background-color: qlineargradient( x1:1 y1:1, x2:0 y2:0, stop:0 white, stop:1 gray);")
        profile2.setFont(buttonFont)
        profile2.setCursor(Qt.PointingHandCursor)
        profile2.clicked.connect(self.new)
        menu_layout.addWidget(profile2, 5, 3, alignment=Qt.AlignLeft)
        if profileNames[1] == "-":
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
        else:
            profile2.setText(profileNames[1])
            profile2.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)

            profile2score = QLabel(profile2)
            if lang == "slovakia":
                profile2score.setText("Odohrané: %s / %s\nRekord: %s\nZostatok: %s" % (wins[1], playedGames[1], highScores[1], coins[1]))
            elif lang == "united-kingdom":
                profile2score.setText("Played: %s / %s\nHighscore: %s\nBalance: %s" % (wins[1], playedGames[1], highScores[1], coins[1]))
            elif lang == "france":
                profile2score.setText("Joué: %s / %s\nScore élevé: %s\nÉquilibre: %s" % (wins[1], playedGames[1], highScores[1], coins[1]))
            elif lang == "germany":
                profile2score.setText("Gespielt: %s / %s\nHighscore: %s\nGleichgewicht: %s" % (wins[1], playedGames[1], highScores[1], coins[1]))
            else:
                profile2score.setText("Играл: %s / %s\nРекорд: %s\nОстаток средств: %s" % (wins[1], playedGames[1], highScores[1], coins[1]))
            profile2score.setAlignment(Qt.AlignRight)
            profile2score.setAttribute(Qt.WA_TransparentForMouseEvents)
            profile2score.setContentsMargins(0, 18, 18, 0)
            profile2score.setStyleSheet(".QLabel {color: black; font: thin 24px} QWidget {border-image: none}")
            profile2score.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
            menu_layout.addWidget(profile2score, 5, 3, alignment=Qt.AlignLeft)

            profile2delete = QPushButton(mainWindow)
            profile2delete.setText("1")
            profile2delete.setFont(invisible)
            profile2delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile2delete.setCursor(Qt.PointingHandCursor)
            profile2delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile2delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile2delete, 5, 3, alignment=Qt.AlignRight)

        profile3 = QPushButton(mainWindow)
        profile3.setStyleSheet("border-image: none;" "border: 2px dashed black;" "border-radius: 15%;" "background-color: qlineargradient( x1:1 y1:1, x2:0 y2:0, stop:0 white, stop:1 gray);")
        profile3.setFont(buttonFont)
        profile3.setCursor(Qt.PointingHandCursor)
        profile3.clicked.connect(self.new)
        menu_layout.addWidget(profile3, 7, 3, alignment=Qt.AlignLeft)
        if profileNames[2] == "-":
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
        else:
            profile3.setText(profileNames[2])
            profile3.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)

            profile3score = QLabel(profile3)
            if lang == "slovakia":
                profile3score.setText("Odohrané: %s / %s\nRekord: %s\nZostatok: %s" % (wins[2], playedGames[2], highScores[2], coins[2]))
            elif lang == "united-kingdom":
                profile3score.setText("Played: %s / %s\nHighscore: %s\nBalance: %s" % (wins[2], playedGames[2], highScores[2], coins[2]))
            elif lang == "france":
                profile3score.setText("Joué: %s / %s\nScore élevé: %s\nÉquilibre: %s" % (wins[2], playedGames[2], highScores[2], coins[2]))
            elif lang == "germany":
                profile3score.setText("Gespielt: %s / %s\nHighscore: %s\nGleichgewicht: %s" % (wins[2], playedGames[2], highScores[2], coins[2]))
            else:
                profile3score.setText("Играл: %s / %s\nРекорд: %s\nОстаток средств: %s" % (wins[2], playedGames[2], highScores[2], coins[2]))
            profile3score.setAlignment(Qt.AlignRight)
            profile3score.setAttribute(Qt.WA_TransparentForMouseEvents)
            profile3score.setContentsMargins(0, 18, 18, 0)
            profile3score.setStyleSheet(".QLabel {color: black; font: thin 24px} QWidget {border-image: none}")
            profile3score.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
            menu_layout.addWidget(profile3score, 7, 3, alignment=Qt.AlignLeft)

            profile3delete = QPushButton(mainWindow)
            profile3delete.setText("2")
            profile3delete.setFont(invisible)
            profile3delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile3delete.setCursor(Qt.PointingHandCursor)
            profile3delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile3delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile3delete, 7, 3, alignment=Qt.AlignRight)

        profile4 = QPushButton(mainWindow)
        profile4.setStyleSheet("border-image: none;" "border: 2px dashed black;" "border-radius: 15%;" "background-color: qlineargradient( x1:1 y1:1, x2:0 y2:0, stop:0 white, stop:1 gray);")
        profile4.setFont(buttonFont)
        profile4.setCursor(Qt.PointingHandCursor)
        profile4.clicked.connect(self.new)
        menu_layout.addWidget(profile4, 9, 3, alignment=Qt.AlignLeft)
        if profileNames[3] == "-":
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
        else:
            profile4.setText(profileNames[3])
            profile4.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)

            profile4score = QLabel(profile4)
            if lang == "slovakia":
                profile4score.setText("Odohrané: %s / %s\nRekord: %s\nZostatok: %s" % (wins[3], playedGames[3], highScores[3], coins[3]))
            elif lang == "united-kingdom":
                profile4score.setText("Played: %s / %s\nHighscore: %s\nBalance: %s" % (wins[3], playedGames[3], highScores[3], coins[3]))
            elif lang == "france":
                profile4score.setText("Joué: %s / %s\nScore élevé: %s\nÉquilibre: %s" % (wins[3], playedGames[3], highScores[3], coins[3]))
            elif lang == "germany":
                profile4score.setText("Gespielt: %s / %s\nHighscore: %s\nGleichgewicht: %s" % (wins[3], playedGames[3], highScores[3], coins[3]))
            else:
                profile4score.setText("Играл: %s / %s\nРекорд: %s\nОстаток средств: %s" % (wins[3], playedGames[3], highScores[3], coins[3]))
            profile4score.setAlignment(Qt.AlignRight)
            profile4score.setAttribute(Qt.WA_TransparentForMouseEvents)
            profile4score.setContentsMargins(0, 18, 18, 0)
            profile4score.setStyleSheet(".QLabel {color: black; font: thin 24px} QWidget {border-image: none}")
            profile4score.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
            menu_layout.addWidget(profile4score, 9, 3, alignment=Qt.AlignLeft)

            profile4delete = QPushButton(mainWindow)
            profile4delete.setText("3")
            profile4delete.setFont(invisible)
            profile4delete.setStyleSheet("border-image: url(./images/delete.png)")
            profile4delete.setCursor(Qt.PointingHandCursor)
            profile4delete.setFixedSize(screen.height() // 13, screen.height() // 13)
            profile4delete.clicked.connect(self.deleteProfile)
            menu_layout.addWidget(profile4delete, 9, 3, alignment=Qt.AlignRight)

        profile5 = QPushButton(mainWindow)
        profile5.setStyleSheet("border-image: none;" "border: 2px dashed black;" "border-radius: 15%;" "background-color: qlineargradient( x1:1 y1:1, x2:0 y2:0, stop:0 white, stop:1 gray);")
        profile5.setFont(buttonFont)
        profile5.setCursor(Qt.PointingHandCursor)
        profile5.clicked.connect(self.new)
        menu_layout.addWidget(profile5, 11, 3, alignment=Qt.AlignLeft)
        if profileNames[4] == "-":
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
        else:
            profile5.setText(profileNames[4])
            profile5.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)

            profile5score = QLabel(profile1)
            if lang == "slovakia":
                profile5score.setText("Odohrané: %s / %s\nRekord: %s\nZostatok: %s" % (wins[4], playedGames[4], highScores[4], coins[4]))
            elif lang == "united-kingdom":
                profile5score.setText("Played: %s / %s\nHighscore: %s\nBalance: %s" % (wins[4], playedGames[4], highScores[4], coins[4]))
            elif lang == "france":
                profile5score.setText("Joué: %s / %s\nScore élevé: %s\nÉquilibre: %s" % (wins[4], playedGames[4], highScores[4], coins[4]))
            elif lang == "germany":
                profile5score.setText("Gespielt: %s / %s\nHighscore: %s\nGleichgewicht: %s" % (wins[4], playedGames[4], highScores[4], coins[4]))
            else:
                profile5score.setText("Играл: %s / %s\nРекорд: %s\nОстаток средств: %s" % (wins[4], playedGames[4], highScores[4], coins[4]))
            profile5score.setAlignment(Qt.AlignRight)
            profile5score.setAttribute(Qt.WA_TransparentForMouseEvents)
            profile5score.setContentsMargins(0, 18, 18, 0)
            profile5score.setStyleSheet(".QLabel {color: black; font: thin 24px} QWidget {border-image: none}")
            profile5score.setFixedSize(round(screen.width() // 3.6), screen.height() // 13)
            menu_layout.addWidget(profile5score, 11, 3, alignment=Qt.AlignLeft)

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
        quitButton.setStyleSheet("border-image: none;" "border: 2px dashed black;" "border-radius: 15%;" "background-color: qlineargradient( x1:1 y1:1, x2:0 y2:0, stop:0 white, stop:1 gray);")
        quitButton.setFont(buttonFont)
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
        helpButton.setStyleSheet("border-image: none;" "border: 2px dashed black;" "border-radius: 15%;" "background-color: qlineargradient( x1:1 y1:1, x2:0 y2:0, stop:0 white, stop:1 gray);")
        helpButton.setFont(buttonFont)
        helpButton.setCursor(Qt.PointingHandCursor)
        helpButton.setFixedSize(screen.width() // 7, screen.height() // 13)
        menu_layout.addWidget(helpButton, 13, 1)
        helpButton.clicked.connect(self.help)

        languageButton = QPushButton(mainWindow)
        languageButton.setStyleSheet("border-image: url(./images/%s.png)" % lang)
        languageButton.setCursor(Qt.PointingHandCursor)
        languageButton.setFixedSize(screen.height() // 13, screen.height() // 13)
        menu_layout.addWidget(languageButton, 13, 5, alignment=Qt.AlignRight)
        languageButton.clicked.connect(self.language)

        mainWindow.setCentralWidget(background)
        mainWindow.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
