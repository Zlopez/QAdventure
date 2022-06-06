import logging

from qadventure.game_managers import GameManager
from qadventure.requests import ChangeSceneRequest
from qadventure.responses import Response, ResponseFailure, ResponseSuccess


logger = logging.getLogger(__name__)


class ChangeSceneUseCase:
    """
    This class represents use case for changing scene in the game using
    game manager.

    Attributes:
        game_manager(GameManager): Game manager to use.
    """

    def __init__(self, game_manager: GameManager):
        """
        Class constructor.
        """
        self.game_manager = game_manager

    def change_scene(self, request: ChangeSceneRequest) -> Response:
        """
        Call the change_scene method on the game manager.
        This method will handle any error that happens when changing scene
        in game.

        Params:
            request: Request to handle.

        Return:
            Response object containing the result of this use case.
        """
        if not request:
            return ResponseFailure.invalid_request_error(request)
        try:
            result = self.game_manager.change_scene(
                request.game_scenario, request.scene_option, request.game_state
            )
            return ResponseSuccess(result)
        except Exception as exc:
            logger.exception("Change scene use case failure", exc_info=True)
            return ResponseFailure.game_manager_error(exc)
