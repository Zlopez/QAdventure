from typing import Optional


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
        self, id: str, text: str, image: str, set_variable: str, options: Optional[list]
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
