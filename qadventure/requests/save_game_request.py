import os

from . import Request
from qadventure.domain import GameState


class SaveGameRequest(Request):
    """
    This class represents request, which will be sent to save game use case.

    Attributes:
        game_state (`GameState`): `GameState` object to save
        file_path (`str`): Path to file to save game to
        scenario_hash (`str`): Hash of the scenario file to add to save file
    """

    def __init__(
        self, game_state: GameState, file_path: str, scenario_hash: str
    ) -> None:
        """
        Initialize new object.

        Params:
            game_state (`GameState`): `GameState` object to save
            file_path (`str`): Path to file to save game to
            scenario_hash (`str`): Hash of the scenario file to add to save file
        """
        super(SaveGameRequest, self).__init__()
        if not os.path.exists(os.path.dirname(file_path)):
            self.add_error(
                "file_path",
                "Directory '{}' doesn't exist!".format(os.path.dirname(file_path)),
            )
            return

        self.game_state = game_state
        self.file_path = file_path
        self.scenario_hash = scenario_hash
