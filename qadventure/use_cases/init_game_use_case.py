import logging

from qadventure.game_managers import GameManager
from qadventure.requests import InitGameRequest
from qadventure.responses import Response, ResponseFailure, ResponseSuccess


logger = logging.getLogger(__name__)


class InitGameUseCase:
    """
    This class represents use case for initialization of the game using
    game manager.

    Attributes:
        game_manager(GameManager): Game manager to use.
    """

    def __init__(self, game_manager: GameManager):
        """
        Class constructor.
        """
        self.game_manager = game_manager

    def init_game(self, request: InitGameRequest) -> Response:
        """
        Call the init_game method on the game manager.
        This method will handle any error that happens when initializing game.

        Params:
            request: Request to handle.

        Return:
            Response object containing the result of this use case.
        """
        if not request:
            return ResponseFailure.invalid_request_error(request)
        try:
            result = self.game_manager.init_game(
                request.game_scenario, request.game_state
            )
            return ResponseSuccess(result)
        except Exception as exc:
            logger.exception("Init game use case failure", exc_info=True)
            return ResponseFailure.game_manager_error(exc)
