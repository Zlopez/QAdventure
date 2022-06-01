import pytest
from unittest import mock

from qadventure.save_managers import SaveManager


class TestSaveManagerSave:
    """
    Test class for `qadventure.save_managers.SaveManager.save` method.
    """

    def test_save(self):
        """
        Assert that method in abstract class raise NotImplementedError.
        """
        game_state = mock.Mock()
        scenario_hash = "hash"
        file_path = "save.sav"
        save_manager = SaveManager()

        with pytest.raises(NotImplementedError):
            save_manager.save(
                game_state=game_state,
                file_path=file_path,
                scenario_hash=scenario_hash,
            )


class TestSaveManagerLoad:
    """
    Test class for `qadventure.save_managers.SaveManager.load` method.
    """

    def test_load(self):
        """
        Assert that method in abstract class raise NotImplementedError.
        """
        file_path = "save.sav"
        save_manager = SaveManager()

        with pytest.raises(NotImplementedError):
            save_manager.load(
                file_path=file_path,
            )
