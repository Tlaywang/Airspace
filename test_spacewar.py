import unittest
from unittest.mock import patch
import pygame
import game

class TestInit(unittest.TestCase):

    @patch('pygame.init')
    def test_pygame_init(self, mock_init):
        game.pygame.init()
        mock_init.assert_called()

    @patch('pygame.mixer.init') 
    def test_mixer_init(self, mock_mixer_init):
        game.pygame.mixer.init()
        mock_mixer_init.assert_called()

    @patch('pygame.mixer.music.load')
    def test_mixer_music_load(self, mock_load):
        game.pygame.mixer.music.load(game.bgm)
        mock_load.assert_called_with(game.bgm)

    @patch('pygame.mixer.music.play')
    def test_mixer_music_play(self, mock_play):
        game.pygame.mixer.music.play(-1) 
        mock_play.assert_called_with(-1)

    def test_screen_creation(self):
        game.screen = game.pygame.display.set_mode((1000, 600))
        self.assertEqual(game.screen.get_size(), (1000,600))

    def test_set_window_title(self):
        game.pygame.display.set_caption('game')
        pygame.display.set_caption.assert_called_with('game')

    def test_set_window_icon(self):
        game.icon = game.pygame.image.load('spaceship.png')
        game.pygame.display.set_icon(game.icon)
        game.pygame.display.set_icon.assert_called_with(game.icon)


class TestEnemyBulletCollision(unittest.TestCase):

    def test_enemy_init(self):
        self.assertGreater(game.enemyX, 0)
        self.assertLess(game.enemyX, 936)
        self.assertEqual(game.enemyY, 300)
        self.assertEqual(game.enemyX_change, -5)

    def test_bullet_init(self):
        self.assertEqual(game.bulletX, 0)
        self.assertEqual(game.bulletY, 480)
        self.assertEqual(game.bulletX_change, 0)
        self.assertEqual(game.bulletY_change, 15)
        self.assertEqual(game.bullet_state, "ready")

    @patch('pygame.mixer.Sound.play')   
    def test_fire_bullet(self, mock_play):
        game.fire_bullet(100, 400)
        self.assertEqual(game.bullet_state, "fire")
        mock_play.assert_called()

    def test_collision_detection(self):
        game.enemyX = 300
        game.enemyY = 300
        game.bulletX = 300
        game.bulletY = 280
        
        self.assertTrue(game.isCollision(game.enemyX, game.enemyY,
                                               game.bulletX, game.bulletY))

        game.bulletY = 600        
        self.assertFalse(game.isCollision(game.enemyX, game.enemyY, 
                                               game.bulletX, game.bulletY))

    def test_scoring(self):
        game.score_value = 0
        game.isCollision(game.enemyX, game.enemyY,
                               game.bulletX, game.bulletY) 
        self.assertEqual(game.score_value, 0)
        
if __name__ == '__main__':
    unittest.main()

