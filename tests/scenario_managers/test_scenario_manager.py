import pytest

from qadventure.scenario_managers import ScenarioManager


class TestScenarioManagerLoad:
    """
    Test class for `qadventure.scenario_managers.ScenarioManager.load` method.
    """

    def test_load(self):
        """
        Assert that method in abstract class raise NotImplementedError.
        """
        file_path = "scenario.json"
        scenario_manager = ScenarioManager()

        with pytest.raises(NotImplementedError):
            scenario_manager.load(
                file_path=file_path,
            )
