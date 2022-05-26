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
