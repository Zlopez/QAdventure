from qadventure.domain import GameScene


class TestGameSceneInit:
    """
    Test class for `qadventure.domain.GameScene.__init__` method.
    """

    def test_init(self):
        """
        Assert that object is correctly created.
        """
        # Preparation
        scene_id = "id"
        text = "Text on the scene"
        image = b"image"
        set_variable = ""
        options = []

        # Test
        game_scene = GameScene(
            id=scene_id,
            text=text,
            image=image,
            set_variable=set_variable,
            options=options,
        )

        # Asserts
        assert game_scene.id == scene_id
        assert game_scene.text == text
        assert game_scene.image == image
        assert game_scene.set_variable == set_variable
        assert game_scene.options == options
