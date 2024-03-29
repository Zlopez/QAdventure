import hashlib
import json
import logging
import os
from typing import Dict, Optional, Union

from . import ScenarioManager
from qadventure.domain import GameScenario


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

        output: Dict[str, Union[Optional[GameScenario], str]] = {
            "game_scenario": None,
            "scenario_hash": "",
        }

        scenario_dict = {}

        scenario_folder = os.path.dirname(file_path)

        with open(file_path) as f:
            scenario_dict = json.load(f)

        output["scenario_hash"] = hashlib.sha256(
            str(scenario_dict).encode()
        ).hexdigest()

        if scenario_dict["image"]:
            image_path = os.path.join(scenario_folder, scenario_dict["image"])
            with open(image_path, "rb") as f:
                scenario_dict["image"] = f.read()

        for scene in scenario_dict["scene_dict"].values():
            if scene["image"]:
                image_path = os.path.join(scenario_folder, scene["image"])
                with open(image_path, "rb") as f:
                    scene["image"] = f.read()

        output["game_scenario"] = GameScenario.from_dict(scenario_dict)

        return output
