from __future__ import annotations
from typing import Optional


class SceneOption:
    """
    This class represent one option on the `qadventure.domain.GameScene`.

    Attributes:
        order (int): Position of the option on the scene
        text (str): Text of the option
        show_if (str): Show the option only if this variable is set
        hide_if (str): Hide the option if this variable is set
        target_scene (str): Identifier of the `qadventure.domain.GameScene` which will
            be loaded when this option is chosen by player
    """

    def __init__(
        self,
        order: int,
        text: str,
        show_if: Optional[str],
        hide_if: Optional[str],
        target_scene: str,
    ) -> None:
        """
        Initialize new SceneOption object.

        Params:
            order (int): Position of the option on the scene
            text (str): Text of the option
            show_if (str): Show the option only if this variable is set
            hide_if (str): Hide the option if this variable is set
            target_scene (str): Identifier of the `qadventure.domain.GameScene` which will
                be loaded when this option is chosen by player
        """
        self.order = order
        self.text = text
        self.show_if = show_if
        self.hide_if = hide_if
        self.target_scene = target_scene

    @classmethod
    def from_dict(cls, adict: dict) -> SceneOption:
        """
        Creates object from dictionary.

        Params:
            adict: A dictionary representing the object.

        Returns:
            Object of this class.
        """
        return cls(**adict)

    def to_dict(self) -> dict:
        """
        Dumps object to dictionary.

        Returns:
           Dictionary representing this object.
        """
        return {
            "order": self.order,
            "text": self.text,
            "show_if": self.show_if,
            "hide_if": self.hide_if,
            "target_scene": self.target_scene,
        }

    def __eq__(self, other: object) -> bool:
        """
        Compare equal method for object.

        Params:
            other: object to compare with

        Return:
            Compare result.
        """
        if not isinstance(other, SceneOption):
            raise NotImplementedError

        return self.to_dict() == other.to_dict()

    def __lt__(self, other: object) -> bool:
        """
        Compare lesser than method for object.

        Params:
            other: object to compare with

        Return:
            Compare result.
        """
        if not isinstance(other, SceneOption):
            raise NotImplementedError

        return self.order < other.order
