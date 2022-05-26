from qadventure.domain import SceneOption


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
