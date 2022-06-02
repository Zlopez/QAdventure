from qadventure.requests import Request


class TestRequestInit:
    """
    Test class for `qadventure.requests.Request.__init__` method.
    """

    def test_init(self):
        """
        Assert that request object is correctly initialized.
        """
        request = Request()

        assert request.errors == []


class TestRequestAddError:
    """
    Test class for `qadventure.requests.Request.add_error` method.
    """

    def test_add_error(self):
        """
        Assert that error is added correctly.
        """
        parameter = "param"
        error = "You shall not pass!"
        request = Request()

        request.add_error(parameter, error)

        exp = [{"parameter": parameter, "error": error}]

        assert request.errors == exp


class TestRequestBool:
    """
    Test class for `qadventure.requests.Request.__bool__` method.
    """

    def test_bool_true(self):
        """
        Assert that valid request returns true.
        """
        request = Request()

        assert bool(request) is True

    def test_bool_false(self):
        """
        Assert that invalid request returns false.
        """
        parameter = "param"
        error = "You shall not pass!"
        request = Request()

        request.add_error(parameter, error)

        assert bool(request) is False
