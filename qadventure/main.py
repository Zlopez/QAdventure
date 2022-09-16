import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QAction

from qadventure.domain import GameScenario, GameScene, GameState
from qadventure.game_managers import BasicGameManager
from qadventure.requests import InitGameRequest, LoadScenarioRequest
from qadventure.scenario_managers import JSONScenarioManager
from qadventure.use_cases import InitGameUseCase, LoadScenarioUseCase


class MainWindow(QMainWindow):
    """
    Class representing the main window of application.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super().__init__()

        # Initialize empty engine variables
        self.game_state: GameState = GameState("")
        self.scenario_hash: str = ""
        self.current_game_scene: GameScene = GameScene("", "", "", "", [])
        self.game_scenario: GameScenario = GameScenario(
            "", "", "", "", {"": self.current_game_scene}
        )

        self.scenario_manager = JSONScenarioManager()
        self.game_manager = BasicGameManager()

        self.initUI()

    def initUI(self):
        """
        Initialize the UI of the application.
        """
        self.setWindowTitle("QAdventure")

        # Register dialog windows
        # This is good for unit testing
        self.load_file_dialog = QFileDialog()

        self.load_scenario_action = QAction("&Open scenario", self)
        self.load_scenario_action.setStatusTip("Load scenario JSON file")
        self.load_scenario_action.triggered.connect(self.open_scenario)

        self.load_game_action = QAction("&Load game", self)
        self.load_game_action.setStatusTip("Load saved game")
        self.load_game_action.setDisabled(True)

        self.save_game_action = QAction("&Save game", self)
        self.save_game_action.setStatusTip("Save current progress in game")
        self.save_game_action.setDisabled(True)

        self.restart_game_action = QAction("&Restart game", self)
        self.restart_game_action.setStatusTip("Restart current scenario")
        self.restart_game_action.setDisabled(True)

        self.menubar = self.menuBar()
        self.game_menu = self.menubar.addMenu("&Game")
        self.game_menu.addAction(self.load_scenario_action)
        self.game_menu.addSeparator()
        self.game_menu.addAction(self.load_game_action)
        self.game_menu.addAction(self.save_game_action)
        self.game_menu.addSeparator()
        self.game_menu.addAction(self.restart_game_action)

        self.setGeometry(0, 0, 800, 600)

        self.statusBar()

    def open_scenario(self) -> None:
        """
        Open scenario method for the Qt window.
        """
        self.load_file_dialog = QFileDialog(self, "Open Scenario")
        self.load_file_dialog.setMimeTypeFilters(["application/json"])

        if self.load_file_dialog.exec_():
            file_list = self.load_file_dialog.selectedFiles()

            # We only expect one file to be selected
            if file_list[0]:
                # Load scenario
                load_scenario_request = LoadScenarioRequest(file_list[0])
                load_scenario_use_case = LoadScenarioUseCase(self.scenario_manager)

                response = load_scenario_use_case.load(load_scenario_request)

                if response:
                    self.game_scenario = response.value["game_scenario"]
                    self.scenario_hash = response.value["scenario_hash"]

                # Initialize Game State
                init_game_request = InitGameRequest(self.game_scenario)
                init_game_use_case = InitGameUseCase(self.game_manager)

                response = init_game_use_case.init_game(init_game_request)

                if response:
                    self.game_state = response.value["game_state"]
                    self.current_game_scene = response.value["game_scene"]


# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)  # pragma: no cover

    window = MainWindow()  # pragma: no cover
    window.show()  # pragma: no cover

    sys.exit(app.exec_())  # pragma: no cover
