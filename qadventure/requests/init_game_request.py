from typing import Optional

from . import Request
from qadventure.domain import GameScenario, GameState


class InitGameRequest(Request):
    """
    This class represents request, which will be sent to init game use case.

    Attributes:
        game_scenario (`GameScenario`): Game scenario to initialize game for
        game_state (`GameState`): Game state to use for game initialization.
            If not provided, new one will be created from start of the game.
    """

    def __init__(
        self, game_scenario: GameScenario, game_state: Optional[GameState] = None
    ) -> None:
        """
        Initialize new object.

        Params:
            game_scenario (`GameScenario`): Game scenario to initialize game for
            game_state (`GameState`): Game state to use for game initialization.
                If not provided, new one will be created from start of the game.
                Default: None.
        """
        super(InitGameRequest, self).__init__()
        self.game_scenario = game_scenario
        self.game_state = game_state
