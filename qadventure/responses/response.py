from typing import Any


class Response:
    """
    Abstract class for response object. Defines shared methods
    for both Success and Failure response.
    """

    def __bool__(self) -> bool:
        """
        This method is used for checking if the response is failure or success.
        Needs to be implemented by every child class.

        Returns:
           True if success, False if failure.
        """
        raise NotImplementedError

    @property
    def value(self) -> Any:
        """
        This property should contain the value of the response, either error or data.
        Needs to be implemented by every child.

        Returns:
            Any value that represents the response from use case.
        """
        raise NotImplementedError
