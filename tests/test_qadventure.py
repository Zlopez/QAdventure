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
