from unittest import mock

from qadventure.use_cases import ChangeSceneUseCase
from qadventure import responses


class TestChangeSceneUseCaseInit:
    """
    Test class for `qadventure.use_cases.ChangeSceneUseCase.__init__` method
    """

    def test_init(self):
        """
        Assert that the object is correctly created.
        """
        manager = mock.Mock()

        use_case = ChangeSceneUseCase(game_manager=manager)

        assert use_case.game_manager == manager


class TestChangeSceneUseCaseChangeScene:
    """
    Test class for `qadventure.use_cases.ChangeSceneUseCase.change_scene` method
    """

    def test_change_scene(self):
        """
        Assert that the changing scene is called correctly and successful response
        is returned when no error is encountered.
        """
        manager = mock.Mock()
        result_dict = {"game_state": mock.Mock(), "game_scene": mock.Mock()}
        manager.change_scene.return_value = result_dict

        request = mock.MagicMock()
        request.game_scenario = mock.Mock()
        request.game_state = mock.Mock()
        request.scene_option = mock.Mock()
        request.__bool__.return_value = True

        use_case = ChangeSceneUseCase(game_manager=manager)

        result = use_case.change_scene(request)

        manager.change_scene.assert_called_with(
            request.game_scenario, request.scene_option, request.game_state
        )
        assert type(result) is responses.ResponseSuccess
        assert bool(result) is True
        assert result.value == result_dict

    def test_change_scene_invalid_request(self):
        """
        Assert that the scene change fails when request validation fails.
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

        use_case = ChangeSceneUseCase(game_manager=manager)

        result = use_case.change_scene(request)

        assert type(result) is responses.ResponseFailure
        assert bool(result) is False
        assert result.value == {
            "type": responses.ResponseFailure.INVALID_REQUEST_ERROR,
            "message": str(errors),
        }

    def test_change_scene_failure(self):
        """
        Assert that the change scene is called correctly and failure response
        is returned when manager raises exception.
        """
        manager = mock.Mock()
        manager.change_scene.side_effect = Exception("This is heresy!")

        request = mock.MagicMock()
        request.game_scenario = mock.Mock()
        request.game_state = mock.Mock()
        request.scene_option = mock.Mock()
        request.__bool__.return_value = True

        use_case = ChangeSceneUseCase(game_manager=manager)

        result = use_case.change_scene(request)

        manager.change_scene.assert_called_with(
            request.game_scenario, request.scene_option, request.game_state
        )
        assert type(result) is responses.ResponseFailure
        assert bool(result) is False
        assert result.value == {
            "type": responses.ResponseFailure.GAME_MANAGER_ERROR,
            "message": "Exception: This is heresy!",
        }
