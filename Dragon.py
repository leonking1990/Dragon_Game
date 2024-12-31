import random
import battleMenu
import Screen


class NormalDragon:

  def __init__(self, dragonLevel):
    self.DragonLevel = dragonLevel
    self.name = "Normal Dragon"
    self.HP = round(round(180 * (self.DragonLevel / 0.926), -3))
    self.MaxHP = self.HP
    self.magic = 50 + round(50 * (self.DragonLevel / .8))
    self.attack_strength = round(10 * (self.DragonLevel / 0.3))
    self.defenses_strength = (self.DragonLevel * 13)

  #calcultes the dragon's damage returns total damage valuse
  def attack(self, player):
    attackStr = round((3 * (random.randrange(1, self.attack_strength) / 5)))

    return player.takeDamage(attackStr)

  #once dragon is defeated calculats the dragon's rewards and returns the rewards earned
  def defeated(self, player):
    leveledUp = False
    earnedEXP = round(
      2 * (5 *
           ((self.DragonLevel * player.getLevel()) / player.getLevel() + 4)))
    earnedCoin = round(5 * (self.DragonLevel * 100) / player.getLevel() + 2)
    leveledUp = player.addEXP(earnedEXP)
    if leveledUp:
      battleMenu.levelUp(player)
    player.addCoin(earnedCoin)
    return (player.name + " has earned " + str(earnedEXP) + " EXP and " +
            str(earnedCoin) + " coin!")

  #subtracts HP from the dragon and returns the damage dealt
  def takeDamage(self, attackStr):
    attackValue = self.defend(attackStr)
    try:
      self.HP -= attackValue
      if self.HP <= 0:
        self.HP = 0
    except:
      print("An error occurred")
      input("Press Enter to return...")
      return
    return attackValue

  #takes attack value from the player and subtracts from the player's defencive strength and return the new damage value
  def defend(self, attackValue):
    attackValue = (attackValue -
                   round(2 *
                         (random.randrange(1, self.defenses_strength) / 10)))
    if attackValue < 0:
      return 0
    else:
      return attackValue

  #dislays the player's stats
  def InstanceProperties(self):
    Screen.clear()
    print("Name: " + self.name)
    print("Dragon Level: " + str(self.DragonLevel))
    print("HP: " + str(self.HP) + "/" + str(self.MaxHP))
    print("Magic: " + str(self.magic))
    print("Attack Strength: " + str(self.attack_strength))
    print("Defenses Strength: " + str(self.defenses_strength))
    print("")
    input("Press Enter to return...")

  def ID(self):
    return str(self.name) + " - HP: " + str(self.HP) + "/" + str(self.MaxHP)


#Below are the dragons that inherite from normal dragon with individual special attack (coming soon) that the player can fight
class FireDragon(NormalDragon):

  def __init__(self, dragonLevel):
    super().__init__(dragonLevel)
    self.DragonLevel = dragonLevel
    self.name = "Fire Dragon"
    self.HP = round(180 * (self.DragonLevel / 0.926), -3)

  def SpecAttack(self):
    return round((self.specAttack_strength * (random.randrange(5, 10) / 10)))


class RubyDragon(NormalDragon):

  def __init__(self, dragonLevel):
    super().__init__(dragonLevel)
    self.DragonLevel = dragonLevel
    self.name = "Ruby Deagon"
    self.specAttack_strength = 30 + round(15 * (self.DragonLevel / 0.3))
    self.HP = round(180 * (self.DragonLevel / 0.926), -3)

  def SpecAttack(self):
    return round((self.specAttack_strength * (random.randrange(5, 10) / 10)))


class WaterDragon(NormalDragon):

  def __init__(self, dragonLevel):
    super().__init__(dragonLevel)
    self.DragonLevel = dragonLevel
    self.name = "Water Dragon"
    self.HP = round(180 * (self.DragonLevel / 0.926), -3)

  def SpecAttack(self):
    return round((self.specAttack_strength * (random.randrange(5, 10) / 10)))


class WindDragon(NormalDragon):

  def __init__(self, dragonLevel):
    super().__init__(dragonLevel)
    self.DragonLevel = dragonLevel
    self.name = "Wind Dragon"

  def SpecAttack(self):
    return round((self.specAttack_strength * (random.randrange(5, 10) / 10)))


class ShadowDragon(NormalDragon):

  def __init__(self, DragonLevel):
    self.DragonLevel = DragonLevel
    super().__init__(self.DragonLevel)
    self.name = "Shadow Dragon"

  def SpecAttack(self):
    return round((self.specAttack_strength * (random.randrange(5, 10) / 10)))


class WhiteDragon(NormalDragon):

  def __init__(self, DragonLevel):
    self.DragonLevel = DragonLevel
    super().__init__(self.DragonLevel)
    self.name = "White Dragon"

  def SpecAttack(self):
    return round((self.specAttack_strength * (random.randrange(5, 10) / 10)))
