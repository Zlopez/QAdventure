import os

from qadventure.requests import LoadScenarioRequest


class TestLoadScenarioRequestInit:
    """
    Test class for `qadventure.requests.LoadScenarioRequest.__init__` method.
    """

    def test_init(self, tmpdir):
        """
        Assert that request object is correctly initialized.
        """
        # Preparation
        file_path = os.path.join(tmpdir, "scenario.json")
        open(file_path, "x")

        # Test
        request = LoadScenarioRequest(file_path=file_path)

        # Asserts
        assert bool(request) is True
        assert request.errors == []
        assert request.file_path == file_path

    def test_init_not_existing_path(self, tmpdir):
        """
        Assert that request object is not validated if the file
        doesn't exist.
        """
        # Preparation
        file_path = os.path.join(tmpdir, "save.json")
        error = "File '{}' doesn't exist!".format(file_path)

        # Test
        request = LoadScenarioRequest(file_path=file_path)

        # Asserts
        assert bool(request) is False
        assert request.errors == [{"parameter": "file_path", "error": error}]
