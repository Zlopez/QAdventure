import logging

from qadventure.save_managers import SaveManager
from qadventure.requests import LoadGameRequest
from qadventure.responses import Response, ResponseFailure, ResponseSuccess


logger = logging.getLogger(__name__)


class LoadGameUseCase:
    """
    This class represents use case for loading game using save manager.

    Attributes:
        save_manager(SaveManager): Save manager to use.
    """

    def __init__(self, save_manager: SaveManager):
        """
        Class constructor.
        """
        self.save_manager = save_manager

    def load(self, request: LoadGameRequest) -> Response:
        """
        Call the load method on the save manager.
        This method will handle any error that happens when saving game.

        Params:
            request: Request to handle.

        Return:
            Response object containing the result of this use case.
        """
        if not request:
            return ResponseFailure.invalid_request_error(request)
        try:
            result = self.save_manager.load(request.file_path)
            return ResponseSuccess(result)
        except Exception as exc:
            logger.exception("Load game use case failure", exc_info=True)
            return ResponseFailure.save_manager_error(exc)
