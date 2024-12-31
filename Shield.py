#                     02/18/2024
# ---------------------------------------------------
#|  Going to work this Shield class into the player  |
#|      and market class and remove the current      |
#|            way Shields are handeled               |
# ---------------------------------------------------

import random
import time


class Shield:

  def __init__(self, name, defense_strength, value):
    self.name = name
    self.defense_strength = defense_strength
    self.value = value

  def defend(self, attacked):
    defense = (attacked -
               round(2 * (random.randrange(1, self.defense_strength) / 10) +
                     self.defense_strength))
    if defense < 0:
      return 0
    else:
      return defense

  def getName(self):
    return self.name

  def getValue(self):
    return str(self.value)


class RustyShield(Shield):

  def __init__(self):
    super().__init__("Rusty Shield", 10, 150)


class IronShield(Shield):

  def __init__(self):
    super().__init__("Iron Shield", 15, 2200)


class SteelShield(Shield):

  def __init__(self):
    super().__init__("Steel Shield", 25, 7800)


class MasterShield(Shield):

  def __init__(self):
    super().__init__("Master Shield", 37, 10000)


class LegendaryShield(Shield):

  def __init__(self):
    super().__init__("Legendary Shield", 50, 50000)
