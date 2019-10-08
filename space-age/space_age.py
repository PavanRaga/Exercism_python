orbital_sec = {
    "earth": 31557600,
    "mercury": 0.2408467*31557600,
    "venus": 0.61519726*31557600,
    "mars": 1.8808158*31557600,
    "jupiter": 11.862615*31557600,
    "saturn": 29.447498*31557600,
    "uranus": 84.016846*31557600,
    "neptune": 164.79132*31557600
}

class SpaceAge(object):
    def __init__(self, seconds):
        self.age = seconds
    def on_earth(self):
        return round(self.age/orbital_sec["earth"],2)
    def on_mercury(self):
        return round(self.age/orbital_sec["mercury"],2)
    def on_venus(self):
        return round(self.age/orbital_sec["venus"],2)
    def on_mars(self):
        return round(self.age/orbital_sec["mars"],2)
    def on_jupiter(self):
        return round(self.age/orbital_sec["jupiter"],2)
    def on_saturn(self):
        return round(self.age/orbital_sec["saturn"],2)
    def on_uranus(self):
        return round(self.age/orbital_sec["uranus"],2)
    def on_neptune(self):
        return round(self.age/orbital_sec["neptune"],2)

