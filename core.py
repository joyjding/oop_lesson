class GameElement(object):
    IMAGE = "StoneBlock"
    SOLID = False
    
    def __init__(self):
        self.sprite = None
        self.board = None
        self.x = None
        self.y = None
        self.last_time = 0
        self.mark=0
        self.end=False

    def interact(self, player):
        pass

    def __str__(self):
        return "<%s located at %r, %r>"%(type(self).__name__, self.x, self.y)

    def update(self, dt):      
        pass

