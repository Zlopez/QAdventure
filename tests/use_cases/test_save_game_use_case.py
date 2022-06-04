from unittest import mock

from qadventure.use_cases import SaveGameUseCase
from qadventure import responses


class TestSaveGameUseCaseInit:
    """
    Test class for `qadventure.use_cases.SaveGameUseCase.__init__` method
    """

    def test_init(self):
        """
        Assert that the object is correctly created.
        """
        manager = mock.Mock()

        use_case = SaveGameUseCase(save_manager=manager)

        assert use_case.save_manager == manager


class TestSaveGameUseCaseSave:
    """
    Test class for `qadventure.use_cases.SaveGameUseCase.save` method
    """

    def test_save(self):
        """
        Assert that the save is called correctly and successful response
        is returned when no error is encountered.
        """
        manager = mock.Mock()
        manager.save.return_value = True

        request = mock.MagicMock()
        request.game_state = mock.Mock()
        request.file_path = "some/path"
        request.scenario_hash = "scenario_hash"
        request.__bool__.return_value = True

        use_case = SaveGameUseCase(save_manager=manager)

        result = use_case.save(request)

        manager.save.assert_called_with(
            request.game_state, request.file_path, request.scenario_hash
        )
        assert type(result) is responses.ResponseSuccess
        assert bool(result) is True
        assert result.value is True

    def test_save_invalid_request(self):
        """
        Assert that the save fails when request validation fails.
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

        use_case = SaveGameUseCase(save_manager=manager)

        result = use_case.save(request)

        assert type(result) is responses.ResponseFailure
        assert bool(result) is False
        assert result.value == {
            "type": responses.ResponseFailure.INVALID_REQUEST_ERROR,
            "message": str(errors),
        }

    def test_save_failure(self):
        """
        Assert that the save is called correctly and failure response
        is returned when manager raises exception.
        """
        manager = mock.Mock()
        manager.save.side_effect = Exception("This is heresy!")

        request = mock.MagicMock()
        request.game_state = mock.Mock()
        request.file_path = "some/path"
        request.scenario_hash = "scenario_hash"
        request.__bool__.return_value = True

        use_case = SaveGameUseCase(save_manager=manager)

        result = use_case.save(request)

        manager.save.assert_called_with(
            request.game_state, request.file_path, request.scenario_hash
        )
        assert type(result) is responses.ResponseFailure
        assert bool(result) is False
        assert result.value == {
            "type": responses.ResponseFailure.SAVE_MANAGER_ERROR,
            "message": "Exception: This is heresy!",
        }
