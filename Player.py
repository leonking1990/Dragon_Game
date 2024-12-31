import random
import time
import Screen
import battleMenu
import Weapon


class Player():

  def __init__(self, number, name, level, coin, exp, exp_to_next_level, weapon,
               shield, legendary):
    self.number = number
    self.name = name
    self.level = level
    self.HP = round(120 * (self.level / 0.60))
    self.MaxHP = self.HP
    self.attack_strength = round(10 * (self.level / 0.3))
    self.defenses_strength = 5 + round(5 * (self.level / 0.8))
    self.exp = exp
    self.nextLevel = exp_to_next_level
    self.coin = coin
    self.weapon = weapon
    self.shield = shield
    self.legendary = legendary

  #this mehtod increses the player's level and recalculates the stats
  def levelup(self):
    self.level = self.level + 1
    self.HP = round(120 * (self.level / 0.60))
    self.MaxHP = self.HP
    self.attack_strength = round(10 * (self.level / 0.3))
    self.defenses_strength = 5 + round(5 * (self.level / 0.8))

  #this method returns a boolen that determines if the player unlocked legedary battles
  def isLegendary(self):
    return self.legendary

  #returns name of the player
  def getName(self):
    return self.name

  #returns the player's coin balance
  def wallet(self):
    return self.coin

  #adds coins to the player's wallet
  def addCoin(self, coin):
    self.coin += coin

  #subtrs coins from the player's wallet
  def spendCoin(self, coin):
    self.coin -= coin

  #equips the player's weapon
  def changeSword(self, name, strength):
    self.weapon[0] = name
    self.weapon[1] = strength

  #equips the player's shield
  def changeShield(self, name, strength):
    self.shield[0] = name
    self.shield[1] = strength

  #adds experiance to the player and returs True if the player leveled up
  def addEXP(self, addExp):
    if self.level < 100:
      self.exp = self.exp + addExp
      print(str(self.exp) + '/' + str(self.nextLevel))
      if self.exp >= self.nextLevel:

        self.levelup()
        if self.level == 100:
          self.exp = self.nextLevel
        else:
          self.nextLevel += (self.level * 1000)
        return True

  #return player's level
  def getLevel(self):
    return self.level

  #if player is dead, removes cuurent weapon and shield from the player and recovers HP
  def defeated(self):
    self.HP = self.MaxHP
    self.weapon = ['Old Sward', 3]
    self.shield = ['old Shield', 3]
    Screen.clear()
    print("your awake!")
    print("We found you and brought you back here.")
    print("We where unable to recover your gear. ")
    time.sleep(3)

  #calcultes the damage the player does to the enemy and returens the damage valuse
  def attack(self, enemy):
    attackStr = round((3 * (random.randrange(round(self.attack_strength / 2),
                                             self.attack_strength) / 5)))

    return enemy.takeDamage(attackStr)

  #Subtract hp from the enemy and return the damage dealt
  def takeDamage(self, attackStr):
    attackValue = self.defend(attackStr)
    try:
      self.HP -= attackValue
      if self.HP <= 0:
        self.HP = 0
    except:
      print("An error occurred")
      input("Press Enter to return...")
      return 0
    return attackValue

  #takes attack value from the enemy and subtracts from the player's defencive strength and return the new damage value
  def defend(self, attacked):
    damage = (attacked -
              round(2 * (random.randrange(1, self.defenses_strength) / 10) +
                    self.shield[1]))
    if damage < 0:
      return 0
    else:
      return damage

  #reset player's HP to maxHP
  def recover(self):
    self.HP = self.MaxHP

  #dislays the player's stats
  def InstanceProperties(self):
    Screen.clear()
    print("Name: " + self.name)
    print("Level: " + str(self.level))
    print("HP: " + str(self.HP) + "/" + str(self.MaxHP))
    print("Attack Strength: " + str(self.attack_strength))
    print("Defense Strength: " + str(self.defenses_strength))
    print("EXP: " + str(self.exp) + "/" + str(self.nextLevel))
    print("Coin: " + str(self.coin))
    print("Weapon: " + self.weapon[0] + " (" + str(self.weapon[1]) + ")")
    print("Shield: " + self.shield[0] + " (" + str(self.shield[1]) + ")\n")
    input("Press Enter to continue..." + "\n")

  def ID(self):
    return "Name: " + str(self.name) + '   Level: ' + str(
      self.level) + "   HP: " + str(self.HP) + "/" + str(
        self.MaxHP) + "   Coin: " + str(self.coin)
