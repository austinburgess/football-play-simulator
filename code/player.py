# player.py
#
# Creates Player object.

class Player:
    def __init__(self, position, skill_level = 50):
        self.position = position
        self.skill_level = skill_level
        
    def get_position(self):
        return self.position
    
    def get_skill_level(self):
        return self.skill_level
        