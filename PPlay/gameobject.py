# coding= utf-8


class GameObject:
    """
    The most basic game class
    Creates a GameObject in X, Y co-ords, with Width x Height
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.sound = None

    def collided(self, obj):
        # Module import
        from . import collision
        return collision.Collision.collided(self, obj)

    def load_sound(self, sound_file):
        # Module import
        from . import sound
        self.sound = sound.Sound(sound_file)
