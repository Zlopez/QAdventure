from typing import Optional

from qadventure.domain import GameState, GameScenario, SceneOption
from . import GameManager


class BasicGameManager(GameManager):
    """
    Basic game manager used by qadventure to manage game flow.
    This class works with domain objects available in qadventure.
    """

    def init_game(
        self, game_scenario: GameScenario, game_state: Optional[GameState] = None
    ) -> dict:
        """
        Game initialization method.
        It prepares the scene based on the game scenario and game state. Game state
        is optional, if not provided the game will be started from beginning.

        Params:
            game_scenario: Game scenario to initialize
            game_state: State of the game to initialize from. Default: None

        Returns:
            Dictionary containing the result of the method.
            Example:
            {
                # GameState object representing the initialized state of game
                "game_state": GameState(),
                # Initialized GameScene
                "game_scene": GameScene()
            }
        """
        result_game_state = None
        result_game_scene = None

        target_scene = game_scenario.start_scene
        if game_state:
            target_scene = game_state.current_scene
            result_game_state = game_state
        else:
            result_game_state = GameState(current_scene=target_scene, variables={})

        result_game_scene = game_scenario.scene_dict[target_scene]

        if result_game_scene.set_variable:
            result_game_state.variables[result_game_scene.set_variable] = True

        if result_game_state.variables:
            for option in game_scenario.scene_dict[target_scene].options:
                if option.hide_if in result_game_state.variables:
                    result_game_scene.options.remove(option)

        return {"game_state": result_game_state, "game_scene": result_game_scene}

    def change_scene(
        self,
        game_scenario: GameScenario,
        scene_option: SceneOption,
        game_state: GameState,
    ) -> dict:
        """
        Change scene method.
        Based on the provided SceneOption it provides new GameState
        and GameScene.

        Params:
            game_scenario: Game scenario to change scene in
            scene_option: Scene option that caused the change of the scene
            game_state: Current state of the game

        Returns:
            Dictionary containing the result of the method.
            Example:
            {
                # GameState object representing the changed state of game
                "game_state": GameState(),
                # New GameScene
                "game_scene": GameScene()
            }
        """
        result_game_state = None
        result_game_scene = None

        target_scene = scene_option.target_scene
        result_game_state = game_state
        result_game_state.current_scene = target_scene

        result_game_scene = game_scenario.scene_dict[target_scene]

        if result_game_scene.set_variable:
            result_game_state.variables[result_game_scene.set_variable] = True

        if result_game_state.variables:
            for option in game_scenario.scene_dict[target_scene].options:
                if option.hide_if in result_game_state.variables:
                    result_game_scene.options.remove(option)

        return {"game_state": result_game_state, "game_scene": result_game_scene}
