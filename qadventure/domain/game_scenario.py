from __future__ import annotations
from typing import Dict, Optional

from .game_scene import GameScene


class GameScenario:
    """
    This class represent whole game scenario.

    Attributes:
        name (str): Name of the scenario
        description (str): Description of the scenario
        image (str): Image in binary string that will be associated to scenario
        start_scene (str): Id of the scene that will be loaded on the start of the scenario
        scene_dict (dict): This dictionary contains all `GameScene` available for the scenario.
            Needs to contain at least the `start_scene`.
    """

    def __init__(
        self,
        name: str,
        description: Optional[str],
        image: Optional[str],
        start_scene: str,
        scene_dict: Dict[str, GameScene],
    ) -> None:
        """
        Initialize new GameScenario object.

        Params:
            name (str): Name of the scenario
            description (str): Description of the scenario
            image (str): Image in binary string that will be associated to scenario
            start_scene (str): Id of the scene that will be loaded on the start of the scenario
            scene_dict (dict): This dictionary contains all `GameScene` available for the scenario.
                Needs to contain at least the `start_scene`.
        """
        self.name = name
        self.description = description
        self.image = image
        self.start_scene = start_scene
        self.scene_dict = scene_dict

    @classmethod
    def from_dict(cls, adict: dict) -> GameScenario:
        """
        Creates object from dictionary.

        Params:
            adict: A dictionary representing the object.

        Returns:
            Object of this class.
        """
        return cls(
            name=adict["name"],
            description=adict["description"],
            image=adict["image"],
            start_scene=adict["start_scene"],
            scene_dict={
                key: GameScene.from_dict(value)
                for key, value in adict["scene_dict"].items()
            },
        )

    def to_dict(self) -> dict:
        """
        Dumps object to dictionary.

        Returns:
           Dictionary representing this object.
        """
        return {
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "start_scene": self.start_scene,
            "scene_dict": {
                key: value.to_dict() for key, value in self.scene_dict.items()
            },
        }

    def __eq__(self, other: object) -> bool:
        """
        Compare equal method for object.

        Params:
            other: object to compare with

        Return:
            Compare result.
        """
        if not isinstance(other, GameScenario):
            raise NotImplementedError

        return self.to_dict() == other.to_dict()
