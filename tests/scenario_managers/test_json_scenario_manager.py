import hashlib
import json
import os

from qadventure.domain import GameScene, GameScenario, SceneOption
from qadventure.scenario_managers import JSONScenarioManager


class TestJSONSaveManagerLoad:
    """
    Test class for `qadventure.save_managers.JSONSaveManager.load` method.
    """

    def setup(self):
        """
        Initialize object to test.
        """
        self.scenario_manager = JSONScenarioManager()

    def test_load(self, tmpdir):
        """
        Assert that scenario file is loaded successfully when no issue
        is encountered.
        """
        # Preparation
        file_path = os.path.join(tmpdir, "scenario.json")
        scenario_image_path = os.path.join(tmpdir, "scenario_image.jpg")
        scene_image_path = os.path.join(tmpdir, "scene_image.jpg")
        scenario_image = b"scenario_image"
        scene_image = b"scene_image"

        with open(scenario_image_path, "wb") as f:
            f.write(scenario_image)
        with open(scene_image_path, "wb") as f:
            f.write(scene_image)

        game_scene = GameScene(
            id="start_scene",
            text="",
            image=scene_image,
            set_variable=None,
            options=[
                SceneOption(
                    order=1,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="start_scene",
                )
            ],
        )
        game_scenario = GameScenario(
            name="name",
            description="",
            image=scenario_image,
            start_scene="start_scene",
            scene_dict={"start_scene": game_scene},
        )

        # Change the images to path for json dump
        game_scene_dict = game_scene.to_dict()
        game_scene_dict["image"] = scene_image_path

        game_scenario_dict = game_scenario.to_dict()
        game_scenario_dict["image"] = scenario_image_path
        game_scenario_dict["scene_dict"] = {"start_scene": game_scene_dict}

        with open(file_path, "w") as f:
            json.dump(game_scenario_dict, f)

        scenario_hash = hashlib.sha256(str(game_scenario_dict).encode()).hexdigest()

        # Test
        output = self.scenario_manager.load(
            file_path=file_path,
        )

        # Asserts
        assert output["game_scenario"] == game_scenario
        assert output["scenario_hash"] == scenario_hash
