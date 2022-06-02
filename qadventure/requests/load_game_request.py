import os

from . import Request


class LoadGameRequest(Request):
    """
    This class represents request, which will be sent to load game use case.

    Attributes:
        file_path (`str`): Path to file to load game from
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialize new object.

        Params:
            file_path (`str`): Path to file to load game from
        """
        super(LoadGameRequest, self).__init__()
        if not os.path.exists(file_path):
            self.add_error(
                "file_path",
                "File '{}' doesn't exist!".format(file_path),
            )
            return

        self.file_path = file_path
