from unittest import mock

from qadventure.requests import InitGameRequest


class TestInitGameRequestInit:
    """
    Test class for `qadventure.requests.InitGameRequest.__init__` method.
    """

    def test_init(self):
        """
        Assert that request object is correctly initialized.
        """
        # Preparation
        game_scenario = mock.Mock()
        game_state = mock.Mock()

        # Test
        request = InitGameRequest(game_scenario=game_scenario, game_state=game_state)

        # Asserts
        assert bool(request) is True
        assert request.errors == []
        assert request.game_scenario == game_scenario
        assert request.game_state == game_state

    def test_init_no_game_state(self):
        """
        Assert that request object is correctly initialized
        even if the game state isn't provided.
        """
        # Preparation
        game_scenario = mock.Mock()

        # Test
        request = InitGameRequest(
            game_scenario=game_scenario,
        )

        # Asserts
        assert bool(request) is True
        assert request.errors == []
        assert request.game_scenario == game_scenario
        assert request.game_state is None
