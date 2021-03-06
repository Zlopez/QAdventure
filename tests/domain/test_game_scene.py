import pytest

from qadventure.domain import GameScene, SceneOption


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


class TestGameSceneFromDict:
    """
    Test class for `qadventure.domain.GameScene.from_dict` method.
    """

    def test_from_dict(self):
        """
        Assert that object is correctly created from dictionary.
        """
        # Preparation
        scene_id = "id"
        text = "Text on the scene"
        image = b"image"
        set_variable = ""
        options = [
            SceneOption(
                order=1,
                text="Text",
                show_if=None,
                hide_if=None,
                target_scene="scene_id",
            ),
            SceneOption(
                order=2,
                text="Text",
                show_if=None,
                hide_if=None,
                target_scene="scene_id",
            ),
        ]

        # Test
        game_scene = GameScene.from_dict(
            {
                "id": scene_id,
                "text": text,
                "image": image,
                "set_variable": set_variable,
                "options": [option.to_dict() for option in options],
            }
        )

        # Asserts
        assert game_scene.id == scene_id
        assert game_scene.text == text
        assert game_scene.image == image
        assert game_scene.set_variable == set_variable
        for option in game_scene.options:
            assert option.to_dict() in [option.to_dict() for option in options]


class TestGameSceneToDict:
    """
    Test class for `qadventure.domain.GameScene.to_dict` method.
    """

    def test_to_dict(self):
        """
        Assert that object is correctly dumped to dictionary.
        """
        # Preparation
        scene_id = "id"
        text = "Text on the scene"
        image = b"image"
        set_variable = ""
        options = [
            SceneOption(
                order=1,
                text="Text",
                show_if=None,
                hide_if=None,
                target_scene="scene_id",
            ),
            SceneOption(
                order=2,
                text="Text",
                show_if=None,
                hide_if=None,
                target_scene="scene_id",
            ),
        ]

        # Test
        game_scene = GameScene(
            id=scene_id,
            text=text,
            image=image,
            set_variable=set_variable,
            options=options,
        )

        # Asserts
        exp_dict = {
            "id": scene_id,
            "text": text,
            "image": image,
            "set_variable": set_variable,
            "options": [option.to_dict() for option in options],
        }

        assert exp_dict == game_scene.to_dict()


class TestGameSceneEq:
    """
    Test class for `qadventure.domain.GameScene.__eq__` method.
    """

    @pytest.mark.parametrize(
        "option1,option2,expected",
        [
            (
                GameScene(
                    id="start_scene",
                    text="",
                    image=b"image",
                    set_variable=None,
                    options=[],
                ),
                GameScene(
                    id="start_scene",
                    text="",
                    image=b"image",
                    set_variable=None,
                    options=[],
                ),
                True,
            ),
            (
                GameScene(
                    id="start_scene",
                    text="",
                    image=b"image",
                    set_variable=None,
                    options=[],
                ),
                GameScene(
                    id="some_scene",
                    text="",
                    image=b"image",
                    set_variable=None,
                    options=[],
                ),
                False,
            ),
        ],
    )
    def test_eq(self, option1, option2, expected):
        """
        Assert that equal operation is working correctly.
        """
        # Asserts
        result = option1 == option2
        assert result == expected

    def test_eq_exception(self):
        """
        Assert that exception is thrown when object class is not correct.
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
        with pytest.raises(NotImplementedError):
            game_scene == "string"
