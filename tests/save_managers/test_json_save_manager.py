import json
import os

from qadventure.domain import GameState
from qadventure.save_managers import JSONSaveManager


class TestJSONSaveManagerSave:
    """
    Test class for `qadventure.save_managers.JSONSaveManager.save` method.
    """

    def setup(self):
        """
        Initialize object to test.
        """
        self.save_manager = JSONSaveManager()

    def test_save(self, tmpdir):
        """
        Assert that save file is created successfully when no issue
        is encountered.
        """
        # Preparation
        file_path = os.path.join(tmpdir, "save.json")
        game_state = GameState(
            current_scene="scene_id",
            variables={
                "variable": True,
            },
        )
        scenario_hash = "Hash"

        # Test
        output = self.save_manager.save(
            game_state=game_state, file_path=file_path, scenario_hash=scenario_hash
        )

        # Asserts
        expected_json = json.dumps(
            {"game_state": game_state.to_dict(), "scenario_hash": scenario_hash}
        )

        with open(file_path) as f:
            assert f.read() == expected_json

        assert output is True


class TestJSONSaveManagerLoad:
    """
    Test class for `qadventure.save_managers.JSONSaveManager.load` method.
    """

    def setup(self):
        """
        Initialize object to test.
        """
        self.save_manager = JSONSaveManager()

    def test_load(self, tmpdir):
        """
        Assert that save file is loaded successfully when no issue
        is encountered.
        """
        # Preparation
        file_path = os.path.join(tmpdir, "save.json")
        game_state = GameState(
            current_scene="scene_id",
            variables={
                "variable": True,
            },
        )
        scenario_hash = "Hash"

        with open(file_path, "w") as f:
            json.dump(
                {"game_state": game_state.to_dict(), "scenario_hash": scenario_hash}, f
            )

        # Test
        output = self.save_manager.load(
            file_path=file_path,
        )

        # Asserts
        assert output["game_state"].to_dict() == game_state.to_dict()
        assert output["scenario_hash"] == scenario_hash
