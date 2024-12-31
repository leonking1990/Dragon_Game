import Screen
import time


#display battle arena
def displayBattleArena(dragons, player):
  Screen.clear()
  count = 0
  print()

  for dragon in dragons:
    count += 1
    if (count % 2) == 0:
      print(str(count) + ': ' + dragon.ID())
    else:
      print(str(count) + ': ' + dragon.ID(), end="   "),

  print('\n'*10)
  print(player.ID())


#displays the magic menu
def DisplayMagicMenu(dragons, player):
  displayBattleArena(dragons, player)

  print('1: Scan')
  print('2: Return')


#displays dragons, player and the battle menu
def DisplayCommand(dragons, player):
  displayBattleArena(dragons, player)

  print('1: Attack!')
  print('2: Magic')
  print('3: Run!')


#displays the any message to the player
def DisplayMessage(dragons, player, message):
  displayBattleArena(dragons, player)

  print(message)


#displays and ugent message to the player
def DisplayMessageAlert(dragons, player, alert):
  space = " "
  virLine = '-'
  horLine = '|'
  messageSpace = len(horLine + (space * 2) + alert + (space * 2) + horLine)

  displayBattleArena(dragons, player)

  print(virLine * (messageSpace + 6))
  print(horLine + (space * (messageSpace + 4)) + horLine)
  print(horLine + (space * (messageSpace + 4)) + horLine)
  print(horLine + (space * 5) + alert + (space * 5) + horLine)
  print(horLine + (space * (messageSpace + 4)) + horLine)
  print(horLine + (space * (messageSpace + 4)) + horLine)
  print(virLine * (messageSpace + 6))
  time.sleep(3)


#display that player level up and player's new stats
def levelUp(player):
  Screen.clear()
  print()
  space = " "
  virLine = '-'
  horLine = '|'

  print('\n\n')
  print((space * 16) + virLine * 48)
  print((space * 15) + horLine + (space * 19) + "**LEVEL UP**" + (space * 17) +
        horLine)
  print((space * 15) + horLine + (space * 48) + horLine)
  if player.getLevel() >= 10:
    print((space * 15) + horLine + (space * 15) + "You are now level " +
          str(player.getLevel()) + (space *
                                    (15 - len(str(player.level)))) + horLine)
  else:
    print((space * 15) + horLine + (space * 14) + "You are now level: " +
          str(player.getLevel()) + (space *
                                    (16 - len(str(player.level)))) + horLine)
  print((space * 15) + horLine + (space * 15) + "Max HP is now: " +
        str(player.MaxHP) + (space * (18 - len(str(player.MaxHP)))) + horLine)
  print((space * 15) + horLine + (space * 15) + "Strength is now: " +
        str(player.attack_strength) +
        (space * (16 - len(str(player.attack_strength)))) + horLine)
  print((space * 15) + horLine + (space * 15) + "Defenses is now: " +
        str(player.defenses_strength) +
        (space * (16 - len(str(player.defenses_strength)))) + horLine)
  print((space * 16) + virLine * 48)
  time.sleep(8)
