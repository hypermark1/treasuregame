import unittest
from main import TreasureMap, Player, Game
from unittest.mock import patch


class TestTreasureMap(unittest.TestCase):
    def test_generate_treasure_location(self):
        treasure_map = TreasureMap(10, 10)
        treasure_location = treasure_map.generate_treasure_location()
        self.assertTrue(1 <= treasure_location[0] <= 10)
        self.assertTrue(1 <= treasure_location[1] <= 10)

    def test_check_treasure(self):
        treasure_map = TreasureMap(10, 10)
        treasure_map.treasure_location = (5, 5)
        self.assertTrue(treasure_map.check_treasure(5, 5))
        self.assertFalse(treasure_map.check_treasure(1, 1))

    def test_get_hint(self):
        treasure_map = TreasureMap(10, 10)
        treasure_map.treasure_location = (5, 5)
        self.assertEqual(treasure_map.get_hint(5, 5), 0)
        self.assertEqual(treasure_map.get_hint(1, 1), 8)

    def test_init_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            TreasureMap(0, 0)  # Width and height are 0
        with self.assertRaises(ValueError):
            TreasureMap(-1, -1)  # Width and height are negative


class TestPlayer(unittest.TestCase):
    def test_choose_coordinates(self):
        player = Player()
        player.choose_coordinates(1, 1)
        self.assertEqual(player.coordinates, [(1, 1)])
        self.assertEqual(player.attempts, 1)


class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['1,A', '2,B', '3,C', '4,D', '5,E', '6,F', '7,G'])
    def test_start_treasure_not_found(self, mock_input):
        player = Player()
        treasure_map = TreasureMap(10, 10)
        treasure_map.treasure_location = (10, 10)  # Set treasure location so it won't be found
        game = Game(player, treasure_map)
        game.start()
        self.assertEqual(player.attempts, player.max_attempts)
        self.assertFalse(treasure_map.check_treasure(*player.coordinates[-1]))

    @patch('builtins.input', side_effect=['1,A', '2,B', '3,C', '4,D', '5,E', '6,F', '10,J'])
    def test_start_treasure_found(self, mock_input):
        player = Player()
        treasure_map = TreasureMap(10, 10)
        treasure_map.treasure_location = (10, 10)  # Set treasure location so it will be found
        game = Game(player, treasure_map)
        game.start()
        self.assertTrue(treasure_map.check_treasure(*player.coordinates[-1]))

    @patch('builtins.input', side_effect=['1.A', '1,A', '2,B', '3,C', '4,D', '5,E', '6,F', '7,G'])
    def test_start_invalid_input(self, mock_input):
        player = Player()
        treasure_map = TreasureMap(10, 10)
        game = Game(player, treasure_map)
        game.start()
        self.assertEqual(player.attempts, player.max_attempts)
        self.assertFalse(treasure_map.check_treasure(*player.coordinates[-1]))

    @patch('builtins.input', side_effect=['1.A', '1,A', '2,B', '3,C', '4,D', '5,E', '6,F', '7,G'])
    def test_start_invalid_input(self, mock_input):
        player = Player()
        treasure_map = TreasureMap(10, 10)
        game = Game(player, treasure_map)
        game.start()
        self.assertEqual(player.attempts, player.max_attempts)
        self.assertFalse(treasure_map.check_treasure(*player.coordinates[-1]))

    @patch('builtins.input',
           side_effect=['11,A', '1,K', '1,A', '2,B', '3,C', '4,D', '5,E', '6,F', '7,G'])  # Out of bounds input
    def test_start_out_of_bounds_input(self, mock_input):
        player = Player()
        treasure_map = TreasureMap(10, 10)
        game = Game(player, treasure_map)
        game.start()
        self.assertEqual(player.attempts, player.max_attempts)
        self.assertFalse(treasure_map.check_treasure(*player.coordinates[-1]))

    @patch('builtins.input', side_effect=['1,A', '2,B', '3,C', '4,D', '5,E', '6,F', '7,G'])  # Treasure not found
    def test_start_max_attempts_reached(self, mock_input):
        player = Player()
        treasure_map = TreasureMap(10, 10)
        treasure_map.treasure_location = (10, 10)  # Set treasure location so it won't be found
        game = Game(player, treasure_map)
        game.start()
        self.assertEqual(player.attempts, player.max_attempts)
        self.assertFalse(treasure_map.check_treasure(*player.coordinates[-1]))

    @patch('builtins.input', side_effect=['1,A', '2,B', '3,C', '4,D', '5,E', '10,J'])  # Treasure found
    def test_start_treasure_found_early(self, mock_input):
        player = Player()
        treasure_map = TreasureMap(10, 10)
        treasure_map.treasure_location = (10, 10)  # Set treasure location so it will be found
        game = Game(player, treasure_map)
        game.start()
        self.assertTrue(treasure_map.check_treasure(*player.coordinates[-1]))
        self.assertLess(player.attempts, player.max_attempts)

    def test_choose_coordinates(self):
        player = Player()
        player.choose_coordinates(1, 1)
        self.assertEqual(player.coordinates, [(1, 1)])
        self.assertEqual(player.attempts, 1)

    def test_check_treasure(self):
        treasure_map = TreasureMap(10, 10)
        treasure_map.treasure_location = (5, 5)
        self.assertFalse(treasure_map.check_treasure(1, 1))
