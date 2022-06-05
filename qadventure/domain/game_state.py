from __future__ import annotations
from typing import Dict


class GameState:
    """
    This class represent game state.

    Attributes:
        current_scene (str): Id of the current scene in game
        variables (dict): Dictionary containing all the variables of the game. Default: {}
    """

    def __init__(
        self,
        current_scene: str,
        variables: Dict[str, bool] = {},
    ) -> None:
        """
        Initialize new GameState object.

        Params:
            current_scene (str): Id of the current scene in game
            variables (dict): Dictionary containing all the variables of the game. Default: {}
        """
        self.current_scene = current_scene
        self.variables = variables

    @classmethod
    def from_dict(cls, adict: dict) -> GameState:
        """
        Creates object from dictionary.

        Params:
            adict: A dictionary representing the object.

        Returns:
            Object of this class.
        """
        return cls(
            current_scene=adict["current_scene"],
            variables=adict["variables"],
        )

    def to_dict(self) -> dict:
        """
        Dumps object to dictionary.

        Returns:
           Dictionary representing this object.
        """
        return {
            "current_scene": self.current_scene,
            "variables": self.variables,
        }

    def __eq__(self, other: object) -> bool:
        """
        Compare equal method for object.

        Params:
            other: object to compare with

        Return:
            Compare result.
        """
        if not isinstance(other, GameState):
            raise NotImplementedError

        return self.to_dict() == other.to_dict()
