from __future__ import annotations
import traceback
from typing import Any, List

from qadventure.responses import Response


class ResponseFailure(Response):
    """
    Class that represents failure response returned from use case.
    It is send when some exception happen during the use case.
    Defines constants for error types.

    Attributes:
        type: Type of the failure.
        message: Error message.
        traceback: Exception traceback as string.
    """

    GAME_MANAGER_ERROR = "GameManagerError"
    SAVE_MANAGER_ERROR = "SaveManagerError"
    SCENARIO_MANAGER_ERROR = "ScenarioManagerError"

    def __init__(self, type: str, message: Any) -> None:
        """
        Class constructor.
        """
        self.type = type
        self.message = self._format_message(message)
        self.traceback = self._get_stack_trace(message)

    def _get_stack_trace(self, message: Any) -> List[str]:
        """
        Retrieves the stack trace information from Exception,
        otherwise just returns empty list.

        Params:
            message: Input to retrieve stack trace from

        Returns:
            Stack trace if message is Exception, otherwise empty string
        """
        stack_trace = []

        if isinstance(message, Exception):
            stack_trace = traceback.format_tb(message.__traceback__)

        return stack_trace

    def _format_message(self, message: Any) -> Any:
        """
        Formats the input message if the message inherits from Exception,
        otherwise just return it back.

        Params:
            message: Input message to format

        Returns:
            String if exception, otherwise return the same object we received.
        """
        if isinstance(message, Exception):
            return "{}: {}".format(message.__class__.__name__, "{}".format(message))

        return message

    @property
    def value(self):
        """
        Returns the dict representation of the failure response.
        """
        return {
            "type": self.type,
            "message": self.message,
        }

    def __bool__(self) -> bool:
        """
        Boolean representation of response.
        """
        return False

    @classmethod
    def game_manager_error(cls, message: Any) -> ResponseFailure:
        """
        Creates response for game manager failure.

        Params:
            message: Message to add to this error

        Returns:
            ResponseFailure object
        """
        response = ResponseFailure(
            type=ResponseFailure.GAME_MANAGER_ERROR, message=message
        )

        return response

    @classmethod
    def save_manager_error(cls, message: Any) -> ResponseFailure:
        """
        Creates response for save manager failure.

        Params:
            message: Message to add to this error

        Returns:
            ResponseFailure object
        """
        response = ResponseFailure(
            type=ResponseFailure.SAVE_MANAGER_ERROR, message=message
        )

        return response

    @classmethod
    def scenario_manager_error(cls, message: Any) -> ResponseFailure:
        """
        Creates response for scenario manager failure.

        Params:
            message: Message to add to this error

        Returns:
            ResponseFailure object
        """
        response = ResponseFailure(
            type=ResponseFailure.SCENARIO_MANAGER_ERROR, message=message
        )

        return response
