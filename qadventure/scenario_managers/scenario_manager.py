class ScenarioManager:
    """
    Abstract class for scenario managers used by qadventure to manage scenario files.
    This class must be inherited by every scenario manager.
    """

    def load(self, file_path: str) -> dict:
        """
        Load method that should be implemented by every child class.
        It should load the `GameScenario` from file.

        Params:
            file_path: File to load the scenario from

        Returns:
            Dictionary containing the result of the method.
            Example:
            {
                "game_scenario": GameScenario(),  # GameScenario object loaded from file
                "scenario_hash": "hash"  # Hash of the scenario file
            }
        """
        raise NotImplementedError
