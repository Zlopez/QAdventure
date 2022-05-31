from qadventure.domain import GameState


class TestGameStateInit:
    """
    Test class for `qadventure.domain.GameState.__init__` method.
    """

    def test_init(self):
        """
        Assert that object is correctly created.
        """
        # Preparation
        current_scene = "scene_id"
        variables = {}

        # Test
        game_state = GameState(current_scene=current_scene, variables=variables)

        # Asserts
        assert game_state.current_scene == current_scene
        assert game_state.variables == variables


class TestGameStateFromDict:
    """
    Test class for `qadventure.domain.GameState.from_dict` method.
    """

    def test_from_dict(self):
        """
        Assert that object is correctly created from dictionary.
        """
        # Preparation
        current_scene = "scene_id"
        variables = {"variable": True}

        # Test
        game_state = GameState.from_dict(
            {
                "current_scene": current_scene,
                "variables": variables,
            }
        )

        # Asserts
        assert game_state.current_scene == current_scene
        assert game_state.variables == variables


class TestGameStateToDict:
    """
    Test class for `qadventure.domain.GameState.to_dict` method.
    """

    def test_to_dict(self):
        """
        Assert that object is correctly dumped to dictionary.
        """
        # Preparation
        current_scene = "scene_id"
        variables = {"variable": True}

        # Test
        game_state = GameState(current_scene=current_scene, variables=variables)

        # Asserts
        exp_dict = {
            "current_scene": current_scene,
            "variables": variables,
        }

        assert exp_dict == game_state.to_dict()
