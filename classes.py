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



aplanet = Planet()
print(f'Name is: {aplanet.name}')
print(f'Radius is: {aplanet.radius}')
print(f'The gravity is: {aplanet.gravity}')
print(aplanet.orbit())
print(Planet.planetshape())
print(aplanet.planetshape())