class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        current_mass = mass
        for asteroid in asteroids:
            if current_mass < asteroid:
                return False
            current_mass += asteroid
        return True