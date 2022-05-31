from qadventure.responses import ResponseSuccess


class TestResponseSuccessInit:
    """
    Test class for `qadventure.responses.ResponseSuccess.__init__` method.
    """

    def test_init(self):
        """
        Assert that object is created correctly.
        """
        response = ResponseSuccess(value="something")

        assert response.value == "something"
        assert response.type == ResponseSuccess.SUCCESS


class TestResponseSuccessBool:
    """
    Test class for `qadventure.responses.ResponseSuccess.__bool__` method.
    """

    def test_bool(self):
        """
        Assert that response success is True.
        """
        response = ResponseSuccess(value=None)

        assert bool(response) is True


class TestResponseSuccessValue:
    """
    Test class for `qadventure.responses.ResponseSuccess.value` property.
    """

    def test_value(self):
        """
        Assert that response success returns value.
        """
        value = "value"

        response = ResponseSuccess(value=value)

        assert response.value == value
