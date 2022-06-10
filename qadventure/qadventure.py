import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    """
    Class representing the main window of application.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        super().__init__()

        self.setWindowTitle("QAdventure")


# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)  # pragma: no cover

    window = MainWindow()  # pragma: no cover
    window.show()  # pragma: no cover

    sys.exit(app.exec_())  # pragma: no cover
