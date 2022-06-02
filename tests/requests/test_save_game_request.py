import os
from unittest import mock

from qadventure.requests import SaveGameRequest


class TestSaveGameRequestInit:
    """
    Test class for `qadventure.requests.SaveGameRequest.__init__` method.
    """

    def test_init(self, tmpdir):
        """
        Assert that request object is correctly initialized.
        """
        # Preparation
        game_state = mock.Mock()
        file_path = os.path.join(tmpdir, "save.json")
        scenario_hash = "hash"

        # Test
        request = SaveGameRequest(
            game_state=game_state, file_path=file_path, scenario_hash=scenario_hash
        )

        # Asserts
        assert bool(request) is True
        assert request.errors == []
        assert request.game_state == game_state
        assert request.file_path == file_path
        assert request.scenario_hash == scenario_hash

    def test_init_not_existing_path(self):
        """
        Assert that request object is not validated if the directory
        doesn't exist.
        """
        # Preparation
        game_state = mock.Mock()
        file_path = "dummy/save.json"
        scenario_hash = "hash"
        error = "Directory 'dummy' doesn't exist!"

        # Test
        request = SaveGameRequest(
            game_state=game_state, file_path=file_path, scenario_hash=scenario_hash
        )

        # Asserts
        assert bool(request) is False
        assert request.errors == [{"parameter": "file_path", "error": error}]
