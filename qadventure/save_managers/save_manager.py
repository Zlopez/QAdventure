from qadventure.domain import GameState


class SaveManager:
    """
    Abstract class for save managers used by qadventure to manage saved games.
    This class must be inherited by every save manager.
    """

    def save(self, game_state: GameState, file_path: str, scenario_hash: str) -> bool:
        """
        Save method that should be implemented by every child class.
        It should save the current `GameState` to file adding the
        scenario hash.

        Params:
            game_state: State of the current game
            file_path: File to save the game to
            scenario_hash: Hash of the currently loaded scenario.
                This could be used to verify that the game scenario didn't
                changed till the save was created.

        Returns:
            True if game was saved successfully, False otherwise.
        """
        raise NotImplementedError

    def load(self, file_path: str) -> dict:
        """
        Load method that should be implemented by every child class.
        It should load the current `GameState` from save file.

        Params:
            file_path: File to load the game state from

        Returns:
            Dictionary containing the result of the method.
            Example:
            {
                "game_state": GameState(),  # GameState object loaded from file
                "scenario_hash": "hash"  # Hash recovered from save file
            }
        """
        raise NotImplementedError
