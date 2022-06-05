from typing import Optional

from qadventure.domain import GameState, GameScenario, SceneOption


class GameManager:
    """
    Abstract class for game managers used by qadventure to manage game flow.
    This class must be inherited by every game manager.
    """

    def init_game(
        self, game_scenario: GameScenario, game_state: Optional[GameState] = None
    ) -> dict:
        """
        Game initialization method that should be implemented by every child class.
        It prepares the scene based on the game scenario and game state. Game state
        is optional, if not provided it should mean that the game starts from beginning.

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
        raise NotImplementedError

    def change_scene(
        self,
        game_scenario: GameScenario,
        scene_option: SceneOption,
        game_state: GameState,
    ) -> dict:
        """
        Change scene method that should be implemented by every child class.
        Based on the provided SceneOption it should provide new GameState
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
        raise NotImplementedError
