from unittest import mock

from qadventure.use_cases import LoadGameUseCase
from qadventure import responses


class TestLoadGameUseCaseInit:
    """
    Test class for `qadventure.use_cases.LoadGameUseCase.__init__` method
    """

    def test_init(self):
        """
        Assert that the object is correctly created.
        """
        manager = mock.Mock()

        use_case = LoadGameUseCase(save_manager=manager)

        assert use_case.save_manager == manager


class TestLoadGameUseCaseLoad:
    """
    Test class for `qadventure.use_cases.LoadGameUseCase.load` method
    """

    def test_load(self):
        """
        Assert that the load is called correctly and successful response
        is returned when no error is encountered.
        """
        manager = mock.Mock()
        result_dict = {"game_state": mock.Mock(), "scenario_hash": "hash"}
        manager.load.return_value = result_dict

        request = mock.MagicMock()
        request.file_path = "some/path"
        request.__bool__.return_value = True

        use_case = LoadGameUseCase(save_manager=manager)

        result = use_case.load(request)

        manager.load.assert_called_with(request.file_path)
        assert type(result) is responses.ResponseSuccess
        assert bool(result) is True
        assert result.value == result_dict

    def test_load_invalid_request(self):
        """
        Assert that the load fails when request validation fails.
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

        use_case = LoadGameUseCase(save_manager=manager)

        result = use_case.load(request)

        assert type(result) is responses.ResponseFailure
        assert bool(result) is False
        assert result.value == {
            "type": responses.ResponseFailure.INVALID_REQUEST_ERROR,
            "message": str(errors),
        }

    def test_load_failure(self):
        """
        Assert that the load is called correctly and failure response
        is returned when manager raises exception.
        """
        manager = mock.Mock()
        manager.load.side_effect = Exception("This is heresy!")

        request = mock.MagicMock()
        request.file_path = "some/path"
        request.__bool__.return_value = True

        use_case = LoadGameUseCase(save_manager=manager)

        result = use_case.load(request)

        manager.load.assert_called_with(request.file_path)
        assert type(result) is responses.ResponseFailure
        assert bool(result) is False
        assert result.value == {
            "type": responses.ResponseFailure.SAVE_MANAGER_ERROR,
            "message": "Exception: This is heresy!",
        }
