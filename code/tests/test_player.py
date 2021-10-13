import sys
sys.path.append("../")

from player import Player

player1 = Player("QB", skill_level = 60)

assert player1.get_position() == "QB"
assert player1.get_skill_level() == 60

player2 = Player("RB")

assert player2.get_position() == "RB"
assert player2.get_skill_level() == 50