import Dragon
import random


# takes player level and returns the dragon objects
def findDragons(playerLevel):
  minLevel = playerLevel - 2
  maxLevel = playerLevel + 2
  if minLevel < 1:
    minLevel = 1
  Dragons = []

  if playerLevel < 5:
    Dragons.append((Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
    return Dragons

  elif playerLevel >= 5 and playerLevel < 10:
    for x in range(2):
      Dragons.append((Dragon.NormalDragon(random.randrange(minLevel,
                                                           maxLevel))))
      return Dragons

  elif playerLevel >= 10 and playerLevel < 15:
    Dragons.append((Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
    Dragons.append(
      (Dragon.FireDragon(random.randrange(minLevel + 3, maxLevel + 3))))
    return Dragons

  elif playerLevel >= 15 and playerLevel < 20:
    rand = random.randrange(2, 3)
    for x in range(rand):
      pick = random.randrange(1, 2)
      if pick == 1:
        Dragons.append(
          (Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
      elif pick == 2:
        Dragons.append(
          (Dragon.FireDragon(random.randrange(minLevel + 3, maxLevel + 3))))
      return Dragons

  elif playerLevel >= 20 and playerLevel < 25:
    rand = random.randrange(3, 4)
    for x in range(rand):
      pick = random.randrange(1, 2)
      if pick == 1:
        Dragons.append(
          (Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
      elif pick == 2:
        Dragons.append(
          (Dragon.FireDragon(random.randrange(minLevel + 3, maxLevel + 3))))
    return Dragons

  elif playerLevel >= 25 and playerLevel < 30:
    for x in range(1):
      pick = random.randrange(1, 3)
      if pick == 1:
        Dragons.append(
          (Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
      elif pick == 2:
        Dragons.append(
          (Dragon.FireDragon(random.randrange(minLevel + 3, maxLevel + 3))))
      elif pick == 3:
        Dragons.append(
          (Dragon.WaterDragon(random.randrange(minLevel + 5, maxLevel + 5))))
    return Dragons

  elif playerLevel >= 30 and playerLevel < 35:
    rand = random.randrange(2, 3)
    for x in range(rand):
      pick = random.randrange(1, 3)
      if pick == 1:
        Dragons.append(
          (Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
      elif pick == 2:
        Dragons.append(
          (Dragon.FireDragon(random.randrange(minLevel + 3, maxLevel + 3))))
      elif pick == 3:
        Dragons.append(
          (Dragon.WaterDragon(random.randrange(minLevel + 5, maxLevel + 5))))
    return Dragons

  elif playerLevel >= 35 and playerLevel < 40:
    rand = random.randrange(3, 4)
    for x in range(rand):
      pick = random.randrange(1, 3)
      if pick == 1:
        Dragons.append(
          (Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
      elif pick == 2:
        Dragons.append(
          (Dragon.FireDragon(random.randrange(minLevel + 3, maxLevel + 3))))
      elif pick == 3:
        Dragons.append(
          (Dragon.WaterDragon(random.randrange(minLevel + 5, maxLevel + 5))))
    return Dragons

  elif playerLevel >= 40 and playerLevel < 45:
    for x in range(2):
      pick = random.randrange(1, 3)
      if pick == 1:
        Dragons.append(
          (Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
      elif pick == 2:
        Dragons.append(
          (Dragon.FireDragon(random.randrange(minLevel + 3, maxLevel + 3))))
      elif pick == 3:
        Dragons.append(
          (Dragon.WaterDragon(random.randrange(minLevel + 5, maxLevel + 5))))
    Dragons.append(
      (Dragon.WindDragon(random.randrange(minLevel + 10, maxLevel + 10))))
    return Dragons

  elif playerLevel >= 45 and playerLevel < 50:
    for x in range(2):
      pick = random.randrange(1, 3)
      if pick == 1:
        Dragons.append(
          (Dragon.NormalDragon(random.randrange(minLevel, maxLevel))))
      elif pick == 2:
        Dragons.append(
          (Dragon.FireDragon(random.randrange(minLevel + 3, maxLevel + 3))))
      elif pick == 3:
        Dragons.append(
          (Dragon.WaterDragon(random.randrange(minLevel + 5, maxLevel + 5))))
    for x in range(2):
      Dragons.append(
        (Dragon.WindDragon(random.randrange(minLevel + 10, maxLevel + 10))))
    return Dragons

  elif playerLevel >= 50:
    Dragons.append(Dragon.RubyDragon(maxLevel + 20))
    return Dragons


def special(playerLevel):
  minLevel = playerLevel - 2
  maxLevel = playerLevel + 2
  if minLevel < 1:
    minLevel = 1
  Dragons = []
  for x in range(6):
    Dragons.append(Dragon.RubyDragon(maxLevel + 20))
  return Dragons


def legendary():
  Dragons = []
  Dragons.append(Dragon.WhiteDragon(120))
  return Dragons


def impossible():
  Dragons = []
  Dragons.append(Dragon.WhiteDragon(150))
  Dragons.append(Dragon.WhiteDragon(140))
  Dragons.append(Dragon.WhiteDragon(130))
  Dragons.append(Dragon.WhiteDragon(120))
  return Dragons


def epic():
  Dragons = []
  Dragons.append(Dragon.ShadowDragon(130))
  return Dragons
