import pytest

from qadventure.responses import Response


class TestResponseBool:
    """
    Test class for `qadventure.responses.Response.__bool__` method.
    """

    def test_bool(self):
        """
        Assert that abstract class returns NotImplementedError.
        """
        response = Response()

        with pytest.raises(NotImplementedError):
            response.__bool__()


class TestResponseValue:
    """
    Test class for `qadventure.responses.Response.value` property.
    """

    def test_value(self):
        """
        Assert that abstract class returns NotImplementedError.
        """
        response = Response()

        with pytest.raises(NotImplementedError):
            response.value
