from qadventure.domain import SceneOption

import pytest


class TestSceneOptionInit:
    """
    Test class for `qadventure.domain.SceneOption.__init__` method.
    """

    def test_init(self):
        """
        Assert that object is correctly created.
        """
        # Preparation
        order = 1
        text = "Text of the option"
        show_if = "variable"
        hide_if = "variable"
        target_scene = "scene_id"

        # Test
        option = SceneOption(
            order=order,
            text=text,
            show_if=show_if,
            hide_if=hide_if,
            target_scene=target_scene,
        )

        # Asserts
        assert option.order == order
        assert option.text == text
        assert option.show_if == show_if
        assert option.hide_if == hide_if
        assert option.target_scene == target_scene


class TestSceneOptionFromDict:
    """
    Test class for `qadventure.domain.SceneOption.from_dict` method.
    """

    def test_from_dict(self):
        """
        Assert that object is correctly created from dictionary.
        """
        # Preparation
        order = 1
        text = "Text of the option"
        show_if = "variable"
        hide_if = "variable"
        target_scene = "scene_id"

        # Test
        option = SceneOption.from_dict(
            {
                "order": order,
                "text": text,
                "show_if": show_if,
                "hide_if": hide_if,
                "target_scene": target_scene,
            }
        )

        # Asserts
        assert option.order == order
        assert option.text == text
        assert option.show_if == show_if
        assert option.hide_if == hide_if
        assert option.target_scene == target_scene


class TestSceneOptionToDict:
    """
    Test class for `qadventure.domain.SceneOption.to_dict` method.
    """

    def test_to_dict(self):
        """
        Assert that object is correctly dumped to dictionary.
        """
        # Preparation
        order = 1
        text = "Text of the option"
        show_if = "variable"
        hide_if = "variable"
        target_scene = "scene_id"

        # Test
        option = SceneOption(
            order=order,
            text=text,
            show_if=show_if,
            hide_if=hide_if,
            target_scene=target_scene,
        )

        # Asserts
        exp_dict = {
            "order": order,
            "text": text,
            "show_if": show_if,
            "hide_if": hide_if,
            "target_scene": target_scene,
        }

        assert exp_dict == option.to_dict()


class TestSceneOptionEq:
    """
    Test class for `qadventure.domain.SceneOption.__eq__` method.
    """

    @pytest.mark.parametrize(
        "option1,option2,expected",
        [
            (
                SceneOption(
                    order=1,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="scene_id",
                ),
                SceneOption(
                    order=1,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="scene_id",
                ),
                True,
            ),
            (
                SceneOption(
                    order=1,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="scene_id",
                ),
                SceneOption(
                    order=2,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="scene_id",
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
        order = 1
        text = "Text of the option"
        show_if = "variable"
        hide_if = "variable"
        target_scene = "scene_id"

        # Test
        option = SceneOption(
            order=order,
            text=text,
            show_if=show_if,
            hide_if=hide_if,
            target_scene=target_scene,
        )

        # Asserts
        with pytest.raises(NotImplementedError):
            option == "string"


class TestSceneOptionLt:
    """
    Test class for `qadventure.domain.SceneOption.__lt__` method.
    """

    @pytest.mark.parametrize(
        "option1,option2,expected",
        [
            (
                SceneOption(
                    order=2,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="scene_id",
                ),
                SceneOption(
                    order=1,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="scene_id",
                ),
                False,
            ),
            (
                SceneOption(
                    order=1,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="scene_id",
                ),
                SceneOption(
                    order=2,
                    text="",
                    show_if=None,
                    hide_if=None,
                    target_scene="scene_id",
                ),
                True,
            ),
        ],
    )
    def test_lt(self, option1, option2, expected):
        """
        Assert that lesser than operation is working correctly.
        """
        # Asserts
        result = option1 < option2
        assert result == expected

    def test_lt_exception(self):
        """
        Assert that exception is thrown when object class is not correct.
        """
        # Preparation
        order = 1
        text = "Text of the option"
        show_if = "variable"
        hide_if = "variable"
        target_scene = "scene_id"

        # Test
        option = SceneOption(
            order=order,
            text=text,
            show_if=show_if,
            hide_if=hide_if,
            target_scene=target_scene,
        )

        # Asserts
        with pytest.raises(NotImplementedError):
            option < "string"
