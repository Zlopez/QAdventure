import json
import logging

from . import SaveManager
from qadventure.domain import GameState


_logger = logging.getLogger(__name__)


class JSONSaveManager(SaveManager):
    """
    Save manager saving the game in JSON format.
    """

    def save(self, game_state: GameState, file_path: str, scenario_hash: str) -> bool:
        """
        Save the game state to JSON file and add the scenario hash.

        Params:
            game_state: State of the current game
            file_path: File to save the game to
            scenario_hash: Hash of the currently loaded scenario.
                This could be used to verify that the game scenario didn't
                changed till the save was created.

        Returns:
            True if game was saved successfully, False otherwise.
        """
        _logger.info("Saving game to {}".format(file_path))

        json_dict = {"game_state": game_state.to_dict(), "scenario_hash": scenario_hash}

        with open(file_path, "w") as f:
            json.dump(json_dict, f)

        return True

    def load(self, file_path: str) -> dict:
        """
        Load the game state from JSON file.

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
        _logger.info("Loading game from {}".format(file_path))

        save_game_dict = {}

        with open(file_path) as f:
            save_game_dict = json.load(f)

        save_game_dict["game_state"] = GameState.from_dict(save_game_dict["game_state"])

        return save_game_dict
