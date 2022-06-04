import traceback

from qadventure.responses import ResponseFailure
from qadventure.requests import Request


class TestResponseFailureInit:
    """
    Test class for `qadventure.responses.ResponseFailure.__init__` method.
    """

    def test_init(self):
        """
        Assert that object is initialized correctly.
        """
        # Test
        response = ResponseFailure(
            type=ResponseFailure.GAME_MANAGER_ERROR, message="This is heresy!"
        )

        # Asserts
        assert response.type == ResponseFailure.GAME_MANAGER_ERROR
        assert response.value == {
            "type": ResponseFailure.GAME_MANAGER_ERROR,
            "message": "This is heresy!",
        }
        assert response.traceback == []


class TestResponseFailureBool:
    """
    Test class for `qadventure.responses.ResponseFailure.__bool__` method.
    """

    def test_bool(self):
        """
        Assert that ResponseFailure always returns False.
        """
        # Test
        response = ResponseFailure(
            type=ResponseFailure.GAME_MANAGER_ERROR,
            message=Exception("This is heresy!"),
        )

        # Asserts
        assert bool(response) is False


class TestResponseFailureGameManagerError:
    """
    Test class for `qadventure.responses.ResponseFailure.game_manager_error` method.
    """

    def test_game_manager_error(self):
        """
        Assert that game manager error response is created correctly.
        """
        # Preparation
        exception = Exception("This is game manager heresy!")

        # Test
        response = ResponseFailure.game_manager_error(message=exception)

        # Asserts
        assert response.type == ResponseFailure.GAME_MANAGER_ERROR
        assert response.value == {
            "type": ResponseFailure.GAME_MANAGER_ERROR,
            "message": "Exception: This is game manager heresy!",
        }
        assert response.traceback == traceback.format_tb(exception.__traceback__)


class TestResponseFailureSaveManagerError:
    """
    Test class for `qadventure.responses.ResponseFailure.save_manager_error` method.
    """

    def test_save_manager_error(self):
        """
        Assert that save manager error response is created correctly.
        """
        # Preparation
        exception = Exception("This is save manager heresy!")

        # Test
        response = ResponseFailure.save_manager_error(message=exception)

        # Asserts
        assert response.type == ResponseFailure.SAVE_MANAGER_ERROR
        assert response.value == {
            "type": ResponseFailure.SAVE_MANAGER_ERROR,
            "message": "Exception: This is save manager heresy!",
        }
        assert response.traceback == traceback.format_tb(exception.__traceback__)


class TestResponseFailureScenarioManagerError:
    """
    Test class for `qadventure.responses.ResponseFailure.scenario_manager_error` method.
    """

    def test_scenario_manager_error(self):
        """
        Assert that scenario manager error response is created correctly.
        """
        # Preparation
        exception = Exception("This is scenario manager heresy!")

        # Test
        response = ResponseFailure.scenario_manager_error(message=exception)

        # Asserts
        assert response.type == ResponseFailure.SCENARIO_MANAGER_ERROR
        assert response.value == {
            "type": ResponseFailure.SCENARIO_MANAGER_ERROR,
            "message": "Exception: This is scenario manager heresy!",
        }
        assert response.traceback == traceback.format_tb(exception.__traceback__)


class TestResponseFailureInvalidRequestError:
    """
    Test class for `qadventure.responses.ResponseFailure.invalid_request_error` method.
    """

    def test_invalid_request_error(self):
        """
        Assert that invalid_request error response is created correctly.
        """
        request = Request()
        request.add_error("param", "You shall not pass!")
        response = ResponseFailure.invalid_request_error(request=request)

        assert response.type == ResponseFailure.INVALID_REQUEST_ERROR
        assert response.value == {
            "type": ResponseFailure.INVALID_REQUEST_ERROR,
            "message": "[{'parameter': 'param', 'error': 'You shall not pass!'}]",
        }
