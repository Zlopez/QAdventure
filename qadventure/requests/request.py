from typing import List


class Request:
    """
    Parent class for requests. Defines error management methods for requests.
    Every request class inherits this class and adds error during validation of
    attributes. Attributes are validated during initialization phase.

    Attributes:
        errors (list): List of errors, every entry is dict containing parameter
                       and error related to this parameter.
    """

    def __init__(self) -> None:
        """
        Class contructor.
        """
        self.errors: List[dict] = []

    def add_error(self, parameter: str, error: str) -> None:
        """
        Adds error to `self.errors`.

        Params:
            parameter: Parameter for which the error is added.
            error: Error encountered during validation of parameter.
        """
        self.errors.append({"parameter": parameter, "error": error})

    def __bool__(self) -> bool:
        """
        Validates the request and returns appropriate response.

        Returns:
            True if `self.errors` is empty, False otherwise.
        """
        return self.errors == []
