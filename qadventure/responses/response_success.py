from typing import Any, Optional

from qadventure.responses import Response


class ResponseSuccess(Response):
    """
    Class that represents successful response returned from use case.
    It has type SUCCESS and bool method returns true.

    Attributes:
        value: Value returned from the use case.
    """

    SUCCESS = "Success"

    def __init__(self, value: Optional[Any]) -> None:
        """
        Class constructor.
        """
        self.type = self.SUCCESS
        self.result = value

    def __bool__(self) -> bool:
        """
        Boolean representation of response.
        """
        return True

    @property
    def value(self) -> Any:
        """
        Returns the value represented by this response.

        Returns:
            Any value obtained from the use case.
        """
        return self.result
