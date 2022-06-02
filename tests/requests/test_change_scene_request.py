from unittest import mock

from qadventure.requests import ChangeSceneRequest


class TestChangeSceneRequestInit:
    """
    Test class for `qadventure.requests.ChangeSceneRequest.__init__` method.
    """

    def test_init(self):
        """
        Assert that request object is correctly initialized.
        """
        # Preparation
        game_scenario = mock.Mock()
        game_state = mock.Mock()
        scene_option = mock.Mock()

        # Test
        request = ChangeSceneRequest(
            game_scenario=game_scenario,
            game_state=game_state,
            scene_option=scene_option,
        )

        # Asserts
        assert bool(request) is True
        assert request.errors == []
        assert request.game_scenario == game_scenario
        assert request.game_state == game_state
        assert request.scene_option == scene_option
