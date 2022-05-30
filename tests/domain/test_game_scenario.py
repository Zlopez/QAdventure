from qadventure.domain import GameScenario, GameScene


class TestGameScenarioInit:
    """
    Test class for `qadventure.domain.GameScenario.__init__` method.
    """

    def test_init(self):
        """
        Assert that object is correctly created.
        """
        # Preparation
        name = "name"
        description = "description"
        image = b"image"
        start_scene = "scene_id"
        game_scene = GameScene(
            id=start_scene,
            text="text",
            image=None,
            set_variable=None,
            options=[]
        )
        scene_dict = {
            start_scene: game_scene
        }

        # Test
        game_scenario = GameScenario(
            name=name,
            description=description,
            image=image,
            start_scene=start_scene,
            scene_dict=scene_dict,
        )

        # Asserts
        assert game_scenario.name == name
        assert game_scenario.description == description
        assert game_scenario.image == image
        assert game_scenario.start_scene == start_scene
        assert game_scenario.scene_dict == scene_dict


class TestGameScenarioFromDict:
    """
    Test class for `qadventure.domain.GameScenario.from_dict` method.
    """

    def test_from_dict(self):
        """
        Assert that object is correctly created from dictionary.
        """
        # Preparation
        name = "name"
        description = "description"
        image = b"image"
        start_scene = "scene_id"
        game_scene = GameScene(
            id=start_scene,
            text="text",
            image=None,
            set_variable=None,
            options=[]
        )
        scene_dict = {
            start_scene: game_scene
        }

        # Test
        game_scenario = GameScenario.from_dict(
            {
                "name": name,
                "description": description,
                "image": image,
                "start_scene": start_scene,
                "scene_dict": {start_scene: game_scene.to_dict()},
            }
        )

        # Asserts
        assert game_scenario.name == name
        assert game_scenario.description == description
        assert game_scenario.image == image
        assert game_scenario.start_scene == start_scene
        assert len(game_scenario.scene_dict) == 1
        assert game_scenario.scene_dict[start_scene].to_dict() == game_scene.to_dict()


class TestGameScenarioToDict:
    """
    Test class for `qadventure.domain.GameScenario.to_dict` method.
    """

    def test_to_dict(self):
        """
        Assert that object is correctly dumped to dictionary.
        """
        # Preparation
        name = "name"
        description = "description"
        image = b"image"
        start_scene = "scene_id"
        game_scene = GameScene(
            id=start_scene,
            text="text",
            image=None,
            set_variable=None,
            options=[]
        )
        scene_dict = {
            start_scene: game_scene
        }

        # Test
        game_scenario = GameScenario(
            name=name,
            description=description,
            image=image,
            start_scene=start_scene,
            scene_dict=scene_dict,
        )

        # Asserts
        exp_dict = {
            "name": name,
            "description": description,
            "image": image,
            "start_scene": start_scene,
            "scene_dict": {start_scene: game_scene.to_dict()},
        }


        assert exp_dict == game_scenario.to_dict()
