from __future__ import annotations
from typing import List, Optional

from .scene_option import SceneOption


class GameScene:
    """
    This class represent one scene in the game.

    Attributes:
        scene_id (str): Identifier of the scene
        text (str): Text that will be shown on the scene
        image (str): Image in binary string that will be shown on the scene
        set_variable (str): When this scene is loaded in the game this variable
            will be set in the `qadventure.domain.GameState`
        options (list): This List contains all `SceneOptions` available for the scene.
            Could be empty for game over scene.
    """

    def __init__(
        self,
        id: str,
        text: str,
        image: Optional[str],
        set_variable: Optional[str],
        options: List[SceneOption],
    ) -> None:
        """
        Initialize new GameScene object.

        Params:
            scene_id (str): Identifier of the scene
            text (str): Text that will be shown on the scene
            image (str): Image in binary string that will be shown on the scene
            set_variable (str): When this scene is loaded in the game this variable
                will be set in the `qadventure.domain.GameState`
            options (list): This List contains all `SceneOptions` available for the scene.
                Could be empty for game over scene.
        """
        self.id = id
        self.text = text
        self.image = image
        self.set_variable = set_variable
        self.options = options

    @classmethod
    def from_dict(cls, adict: dict) -> GameScene:
        """
        Creates object from dictionary.

        Params:
            adict: A dictionary representing the object.

        Returns:
            Object of this class.
        """
        return cls(
            id=adict["id"],
            text=adict["text"],
            image=adict["image"],
            set_variable=adict["set_variable"],
            options=[SceneOption.from_dict(option) for option in adict["options"]],
        )

    def to_dict(self) -> dict:
        """
        Dumps object to dictionary.

        Returns:
           Dictionary representing this object.
        """
        return {
            "id": self.id,
            "text": self.text,
            "image": self.image,
            "set_variable": self.set_variable,
            "options": [option.to_dict() for option in self.options],
        }

    def __eq__(self, other: object) -> bool:
        """
        Compare equal method for object.

        Params:
            other: object to compare with

        Return:
            Compare result.
        """
        if not isinstance(other, GameScene):
            raise NotImplementedError

        return self.to_dict() == other.to_dict()
