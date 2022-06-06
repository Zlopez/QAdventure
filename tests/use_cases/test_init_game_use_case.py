from unittest import mock

from qadventure.use_cases import InitGameUseCase
from qadventure import responses


class TestInitGameUseCaseInit:
    """
    Test class for `qadventure.use_cases.InitGameUseCase.__init__` method
    """

    def test_init(self):
        """
        Assert that the object is correctly created.
        """
        manager = mock.Mock()

        use_case = InitGameUseCase(game_manager=manager)

        assert use_case.game_manager == manager


class TestInitGameUseCaseInitGame:
    """
    Test class for `qadventure.use_cases.InitGameUseCase.init_game` method
    """

    def test_init_game(self):
        """
        Assert that the init_game is called correctly and successful response
        is returned when no error is encountered.
        """
        manager = mock.Mock()
        result_dict = {"game_state": mock.Mock(), "game_scene": mock.Mock()}
        manager.init_game.return_value = result_dict

        request = mock.MagicMock()
        request.game_scenario = mock.Mock()
        request.game_state = None
        request.__bool__.return_value = True

        use_case = InitGameUseCase(game_manager=manager)

        result = use_case.init_game(request)

        manager.init_game.assert_called_with(request.game_scenario, request.game_state)
        assert type(result) is responses.ResponseSuccess
        assert bool(result) is True
        assert result.value == result_dict

    def test_init_game_invalid_request(self):
        """
        Assert that the game initialization fails when request validation fails.
        """
        errors = [
            {
                "parameter": "param",
                "error": "This is not the parameter you are looking for.",
            }
        ]
        manager = mock.Mock()

        request = mock.MagicMock()
        request.__bool__.return_value = False
        request.errors = errors

        use_case = InitGameUseCase(game_manager=manager)

        result = use_case.init_game(request)

        assert type(result) is responses.ResponseFailure
        assert bool(result) is False
        assert result.value == {
            "type": responses.ResponseFailure.INVALID_REQUEST_ERROR,
            "message": str(errors),
        }

    def test_init_game_failure(self):
        """
        Assert that the game initialization is called correctly and failure response
        is returned when manager raises exception.
        """
        manager = mock.Mock()
        manager.init_game.side_effect = Exception("This is heresy!")

        request = mock.MagicMock()
        request.game_scenario = mock.Mock()
        request.game_state = None
        request.__bool__.return_value = True

        use_case = InitGameUseCase(game_manager=manager)

        result = use_case.init_game(request)

        manager.init_game.assert_called_with(request.game_scenario, request.game_state)
        assert type(result) is responses.ResponseFailure
        assert bool(result) is False
        assert result.value == {
            "type": responses.ResponseFailure.GAME_MANAGER_ERROR,
            "message": "Exception: This is heresy!",
        }
