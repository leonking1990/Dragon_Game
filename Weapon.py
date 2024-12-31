#                     02/18/2024
# ---------------------------------------------------
#|  Going to work this Weapon class into the player  |
#|      and market class and remove the current      |
#|            way Weapons are handeled               |
# ---------------------------------------------------


class Weapon:

  def __init__(self, name, attack_strength, special_attack_strength, value):
    self.name = name
    self.attack_strength = attack_strength
    self.special_attack_strength = special_attack_strength
    self.value = value

  def Attack(self):
    return self.attack_strength

  def getName(self):
    return self.name

  def getValue(self):
    return self.value


class RustySword(Weapon):

  def __init__(self):
    super().__init__("Rusty Sword", 3, 5, 150)


class OldSword(Weapon):

  def __init__(self):
    super().__init__("Old Sword", 5, 7, 1200)


class SteelSword(Weapon):

  def __init__(self):
    super().__init__("Steel Sword", 7, 9, 4200)


class MasterSword(Weapon):

  def __init__(self):
    super().__init__("Master Sword", 10, 15, 7800)


class LegendarySword(Weapon):

  def __init__(self):
    super().__init__("Legendary Sword", 15, 25, 10000)
