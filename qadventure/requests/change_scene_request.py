from . import Request
from qadventure.domain import GameScenario, GameState, SceneOption


class ChangeSceneRequest(Request):
    """
    This class represents request, which will be sent to change scene use case.

    Attributes:
        game_scenario (`GameScenario`): Game scenario to take the scene from
        game_state (`GameState`): Game state to update
        scene_option (`SceneOption`): Scene option picked by player
    """

    def __init__(
        self,
        game_scenario: GameScenario,
        game_state: GameState,
        scene_option: SceneOption,
    ) -> None:
        """
        Initialize new object.

        Params:
            game_scenario (`GameScenario`): Game scenario to take the scene from
            game_state (`GameState`): Game state to update
            scene_option (`SceneOption`): Scene option picked by player
        """
        super(ChangeSceneRequest, self).__init__()
        self.game_scenario = game_scenario
        self.game_state = game_state
        self.scene_option = scene_option
