from unittest import mock

from qadventure.domain import GameState, GameScene, SceneOption
from qadventure.game_managers import BasicGameManager


class TestBasicGameManagerInitGame:
    """
    Test class for `qadventure.game_managers.BasicGameManager.init_game` method.
    """

    def test_init_game(self):
        """
        Assert that game is correctly initialized.
        """
        # Preparation
        game_state = GameState(current_scene="some_scene", variables={})
        game_scene = mock.Mock()
        game_scene.set_variable = "variable"
        game_scene.options = []
        game_scenario = mock.Mock()
        game_scenario.scene_dict = {"some_scene": game_scene}
        game_manager = BasicGameManager()

        # Test
        result = game_manager.init_game(
            game_scenario=game_scenario, game_state=game_state
        )

        # Asserts
        game_state.variables["variable"] = True

        assert result == {"game_state": game_state, "game_scene": game_scene}

    def test_init_game_no_game_state(self):
        """
        Assert that game is correctly initialized when game state is not provided.
        """
        # Preparation
        game_state = GameState(current_scene="some_scene", variables={"variable": True})

        hide_scene_option = SceneOption(
            order=1,
            text="text",
            show_if=None,
            hide_if="variable",
            target_scene="start_scene",
        )
        show_scene_option = SceneOption(
            order=1,
            text="text",
            show_if="variable",
            hide_if=None,
            target_scene="start_scene",
        )
        game_scene = GameScene(
            id="some_scene",
            text="text",
            image=b"image",
            set_variable="variable",
            options=[hide_scene_option, show_scene_option],
        )
        game_scenario = mock.Mock()
        game_scenario.start_scene = "some_scene"
        game_scenario.scene_dict = {"some_scene": game_scene}
        game_manager = BasicGameManager()

        # Test
        result = game_manager.init_game(game_scenario=game_scenario)

        # Asserts
        exp_game_scene = GameScene(
            id="some_scene",
            text="text",
            image=b"image",
            set_variable="variable",
            options=[show_scene_option],
        )

        assert result == {"game_state": game_state, "game_scene": exp_game_scene}


class TestBasicGameManagerChangeScene:
    """
    Test class for `qadventure.game_managers.BasicGameManager.change_scene` method.
    """

    def test_change_scene_no_variable(self):
        """
        Assert that change is correctly changed.
        """
        # Preparation
        game_state = GameState(current_scene="start_scene", variables={})
        game_scene = GameScene(
            id="some_scene", text="text", image=b"image", set_variable=None, options=[]
        )
        game_scenario = mock.Mock()
        game_scenario.scene_dict = {"some_scene": game_scene}
        scene_option = mock.Mock()
        scene_option.target_scene = "some_scene"

        game_manager = BasicGameManager()

        # Test
        result = game_manager.change_scene(
            game_scenario=game_scenario,
            scene_option=scene_option,
            game_state=game_state,
        )

        # Assert
        exp_game_state = GameState(current_scene="some_scene", variables={})

        assert result == {"game_state": exp_game_state, "game_scene": game_scene}

    def test_change_scene_variable(self):
        """
        Assert that scene is correctly changed and the options are hidden or shown
        based on the variable.
        """
        # Preparation
        game_state = GameState(current_scene="start_scene", variables={})
        hide_scene_option = SceneOption(
            order=1,
            text="text",
            show_if=None,
            hide_if="variable",
            target_scene="start_scene",
        )
        show_scene_option = SceneOption(
            order=1,
            text="text",
            show_if="variable",
            hide_if=None,
            target_scene="start_scene",
        )
        game_scene = GameScene(
            id="some_scene",
            text="text",
            image=b"image",
            set_variable="variable",
            options=[hide_scene_option, show_scene_option],
        )
        game_scenario = mock.Mock()
        game_scenario.scene_dict = {"some_scene": game_scene}
        scene_option = mock.Mock()
        scene_option.target_scene = "some_scene"

        game_manager = BasicGameManager()

        # Test
        result = game_manager.change_scene(
            game_scenario=game_scenario,
            scene_option=scene_option,
            game_state=game_state,
        )

        # Assert
        exp_game_state = GameState(
            current_scene="some_scene", variables={"variable": True}
        )
        exp_game_scene = GameScene(
            id="some_scene",
            text="text",
            image=b"image",
            set_variable="variable",
            options=[show_scene_option],
        )

        assert result == {"game_state": exp_game_state, "game_scene": exp_game_scene}
