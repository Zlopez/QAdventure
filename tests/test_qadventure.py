from qadventure.qadventure import MainWindow


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
        assert window.load_game_action.text() == "&Load game"
        assert window.load_game_action.statusTip() == "Load saved game"
        assert window.save_game_action.text() == "&Save game"
        assert window.save_game_action.statusTip() == "Save current progress in game"
        assert window.restart_game_action.text() == "&Restart game"
        assert window.restart_game_action.statusTip() == "Restart current scenario"
        assert window.game_menu.title() == "&Game"
        assert window.load_scenario_action in window.game_menu.actions()
        assert window.load_game_action in window.game_menu.actions()
        assert window.save_game_action in window.game_menu.actions()
        assert window.restart_game_action in window.game_menu.actions()
