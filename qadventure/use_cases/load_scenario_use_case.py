import logging

from qadventure.scenario_managers import ScenarioManager
from qadventure.requests import LoadScenarioRequest
from qadventure.responses import Response, ResponseFailure, ResponseSuccess


logger = logging.getLogger(__name__)


class LoadScenarioUseCase:
    """
    This class represents use case for loading scenario using scenario manager.

    Attributes:
        scenario_manager(ScenarioManager): Scenario manager to use.
    """

    def __init__(self, scenario_manager: ScenarioManager):
        """
        Class constructor.
        """
        self.scenario_manager = scenario_manager

    def load(self, request: LoadScenarioRequest) -> Response:
        """
        Call the load method on the scenario manager.
        This method will handle any error that happens when loading scenario.

        Params:
            request: Request to handle.

        Return:
            Response object containing the result of this use case.
        """
        if not request:
            return ResponseFailure.invalid_request_error(request)
        try:
            result = self.scenario_manager.load(request.file_path)
            return ResponseSuccess(result)
        except Exception as exc:
            logger.exception("Load scenario use case failure", exc_info=True)
            return ResponseFailure.scenario_manager_error(exc)
