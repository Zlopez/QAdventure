from unittest.mock import Mock, patch
from os import path

from qadventure.main import MainWindow


class TestMainWindowInit:
    """
    Test class for `qadventure.qadventure.MainWindow.__init__` method.
    """

    def test_init(self, qtbot):
        """
        Assert that window is created correctly.
        """
        # Preparation
        window = MainWindow()
        window.show()

        # Test
        qtbot.addWidget(window)

        # Asserts
        assert window.isVisible()
        assert window.windowTitle() == "QAdventure"
        assert window.load_scenario_action.text() == "&Open scenario"
        assert window.load_scenario_action.statusTip() == "Load scenario JSON file"
        assert window.load_scenario_action.isEnabled()
        assert window.load_game_action.text() == "&Load game"
        assert window.load_game_action.statusTip() == "Load saved game"
        assert not window.load_game_action.isEnabled()
        assert window.save_game_action.text() == "&Save game"
        assert window.save_game_action.statusTip() == "Save current progress in game"
        assert not window.save_game_action.isEnabled()
        assert window.restart_game_action.text() == "&Restart game"
        assert window.restart_game_action.statusTip() == "Restart current scenario"
        assert not window.restart_game_action.isEnabled()
        assert window.game_menu.title() == "&Game"
        assert window.load_scenario_action in window.game_menu.actions()
        assert window.load_game_action in window.game_menu.actions()
        assert window.save_game_action in window.game_menu.actions()
        assert window.restart_game_action in window.game_menu.actions()
        assert window.geometry().width() == 800
        assert window.geometry().height() == 600


class TestMainWindowOpenScenario:
    """
    Test class for `qadventure.qadventure.MainWindow.open_scenario` method.
    """

    @patch("qadventure.main.QFileDialog")
    def test_open_scenario(self, mock_file_dialog, qtbot):
        """
        Assert that file is loaded correctly.
        """
        # Preparation
        window = MainWindow()

        tutorial_scenario_path = path.abspath(
            "scenarios/QAdventure tutorial/qadventure_tutorial.json"
        )

        mock_file_dialog_instance = Mock()
        mock_file_dialog_instance.selectedFiles.return_value = [tutorial_scenario_path]

        mock_file_dialog.return_value = mock_file_dialog_instance

        # Test
        window.open_scenario()

        # Asserts
        assert window.game_scenario.name == "QAdventure tutorial"
        assert window.game_state.current_scene == "start_scene"
