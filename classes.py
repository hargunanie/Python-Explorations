class Planet:

    shape = 'round'

    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth system'
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
    
    @classmethod
    def planetshape(cls):
        return f'all planets are {cls.shape}'

    @staticmethod
    def planetornot():
        print('am a planet')
