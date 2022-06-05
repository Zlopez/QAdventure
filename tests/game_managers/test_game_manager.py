import pytest
from unittest import mock

from qadventure.game_managers import GameManager


class TestGameManagerInitGame:
    """
    Test class for `qadventure.game_managers.GameManager.init_game` method.
    """

    def test_init_game(self):
        """
        Assert that method in abstract class raise NotImplementedError.
        """
        game_state = mock.Mock()
        game_scenario = mock.Mock()
        game_manager = GameManager()

        with pytest.raises(NotImplementedError):
            game_manager.init_game(game_scenario=game_scenario, game_state=game_state)


class TestGameManagerChangeScene:
    """
    Test class for `qadventure.game_managers.GameManager.change_scene` method.
    """

    def test_change_scene(self):
        """
        Assert that method in abstract class raise NotImplementedError.
        """
        game_scenario = mock.Mock()
        scene_option = mock.Mock()
        game_state = mock.Mock()
        game_manager = GameManager()

        with pytest.raises(NotImplementedError):
            game_manager.change_scene(
                game_scenario=game_scenario,
                scene_option=scene_option,
                game_state=game_state,
            )
