import hashlib
import json
import logging

from . import ScenarioManager
from qadventure.domain import GameScenario, GameScene


_logger = logging.getLogger(__name__)


class JSONScenarioManager(ScenarioManager):
    """
    Scenario manager for JSON format.
    """

    def load(self, file_path: str) -> dict:
        """
        Load the game scenario from JSON file.

        Params:
            file_path: File to load the game scenario from

        Returns:
            Dictionary containing the result of the method.
            Example:
            {
                "game_scenario": GameScenario(),  # GameScenario object loaded from file
                "scenario_hash": "hash"  # Hash of the scenario
            }
        """
        _logger.info("Loading scenario from {}".format(file_path))

        output = {"game_scenario": None, "scenario_hash": ""}

        scenario_dict = {}

        with open(file_path) as f:
            scenario_dict = json.load(f)

        output["scenario_hash"] = hashlib.md5(str(scenario_dict).encode()).hexdigest()

        if scenario_dict["image"]:
            with open(scenario_dict["image"], "rb") as f:
                scenario_dict["image"] = f.read()

        for scene in scenario_dict["scene_dict"].values():
            if scene["image"]:
                with open(scene["image"], "rb") as f:
                    scene["image"] = f.read()

        output["game_scenario"] = GameScenario.from_dict(scenario_dict)

        return output
