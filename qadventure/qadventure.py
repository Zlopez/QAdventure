import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class MainWindow(QMainWindow):
    """
    Class representing the main window of application.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        Initialize the UI of the application.
        """
        self.setWindowTitle("QAdventure")

        self.load_scenario_action = QAction("&Open scenario", self)
        self.load_scenario_action.setStatusTip("Load scenario JSON file")

        self.load_game_action = QAction("&Load game", self)
        self.load_game_action.setStatusTip("Load saved game")

        self.save_game_action = QAction("&Save game", self)
        self.save_game_action.setStatusTip("Save current progress in game")

        self.restart_game_action = QAction("&Restart game", self)
        self.restart_game_action.setStatusTip("Restart current scenario")

        self.menubar = self.menuBar()
        self.game_menu = self.menubar.addMenu("&Game")
        self.game_menu.addAction(self.load_scenario_action)
        self.game_menu.addSeparator()
        self.game_menu.addAction(self.load_game_action)
        self.game_menu.addAction(self.save_game_action)
        self.game_menu.addSeparator()
        self.game_menu.addAction(self.restart_game_action)

        self.statusBar()


# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)  # pragma: no cover

    window = MainWindow()  # pragma: no cover
    window.show()  # pragma: no cover

    sys.exit(app.exec_())  # pragma: no cover
