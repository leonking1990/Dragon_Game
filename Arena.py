import random
import Screen
import time
import battleMenu
import MatchMaking


#arena object that take in player obejcts
class arena:

  def __init__(self, player):
    self.player = player
    dragons = []
    playerLevel = self.player.getLevel()
    #playerLevel = int(playerLevel)
    minLevel = playerLevel - 2
    maxLevel = playerLevel + 2
    if minLevel <= 0:
      minLevel = 1

    traveling = True

    Screen.clear()
    print()

    while traveling:

      #determains if the player unlocked the legendary arena
      if self.player.isLegendary() == True:
        lArena = 'Legindary Arena'

        while not (lArena == 'Y' or lArena == 'N'):
          Screen.clear()
          print("You have unlocked the arena of legends!")
          print("would You like to travel to the arena of legends?")
          lArena = input("(Y/N)")
          lArena = lArena.upper()
          if not lArena.isalpha() or not (lArena == 'Y' or lArena == 'N'):
            print("Please enter a valid input")
            time.sleep(1.5)

        #if the player chose to travel to the legendary arena allows them to pick the dificulty
        if lArena == "Y":
          command = 0
          while command <= 0 or command > 5:
            Screen.clear()
            print("pick a challange " + self.player.getName() + "!")
            print("1. Special")
            print("2. Epic")
            print("3. Legendary")
            print("4. Impossible")
            print('5. Back')
            command = input()
            command = int(command)
            if (command <= 0 or command > 5):
              print("Please enter a valid input")
              time.sleep(1.5)
          if command == 1:
            dragons = MatchMaking.special(playerLevel)

          elif command == 2:
            dragons = MatchMaking.epic()

          elif command == 3:
            dragons = MatchMaking.legendary()

          elif command == 4:
            dragons = MatchMaking.impossible()

          elif command == 5:
            traveling = False

        else:
          dragons = MatchMaking.findDragons(playerLevel)

      else:
        dragons = MatchMaking.findDragons(playerLevel)

      #while there is still dragons in the list
      while len(dragons) > 0:

        battleMenu.DisplayCommand(dragons, self.player)

        command = input()

        command = int(command)
        if command == 1:
          if len(dragons) > 1:
            command = 0
            while command <= 0 or command > len(dragons):
              battleMenu.DisplayMessage(dragons, self.player,
                                        'Choose which to attack!')
              command = input()
              command = int(command)
              damage = self.player.attack(dragons[command - 1])
              if damage == 0:
                message = 'Attack missed!'
                battleMenu.DisplayMessageAlert(dragons, self.player, message)
              else:
                message = self.player.name + " attacked causing " + str(
                  damage) + " damage!"
                battleMenu.DisplayMessageAlert(dragons, self.player, message)
          else:
            damage = self.player.attack(dragons[command - 1])
            if damage == 0:
              message = 'Attack missed!'
              battleMenu.DisplayMessageAlert(dragons, self.player, message)
            else:
              message = self.player.name + " attacked causing " + str(
                damage) + " damage!"
              battleMenu.DisplayMessageAlert(dragons, self.player, message)

          if dragons[command - 1].HP <= 0:
            message = dragons[command - 1].defeated(self.player)
            battleMenu.DisplayMessageAlert(dragons, self.player, message)
            dragons.remove(dragons[command - 1])

            if len(dragons) <= 0:
              deceion = "deceion"
              print('You defeated all of the dragons!')
              while not (deceion == 'Y' or deceion == 'N'):
                print('You defeated all of the dragons!')

                deceion = input('Keep walking deeper? (Y/N)')
                deceion = deceion.title()

                if not arena.isalpha() or not (arena == 'Y' or arena == 'N'):
                  print("Please enter a valid input")
                  time.sleep(1.5)

              if deceion == 'N':
                traveling = False

          if len(dragons) > 0:

            damage = dragons[command - 1].attack(self.player)
            if damage == 0:
              message = 'Attack missed!'
              battleMenu.DisplayMessageAlert(dragons, self.player, message)
            else:
              message = dragons[command - 1].name + " attacked causing " + str(
                damage) + " damage!"
              battleMenu.DisplayMessageAlert(dragons, self.player, message)
            if self.player.HP <= 0:
              self.player.defeated()
              dragons.clear()
              traveling = False

        #diplay magic menu and get command
        elif command == 2:
          command = 0
          while command <= 0 or command > 2:
            battleMenu.DisplayMagicMenu(dragons, self.player)
            command = input()
            command = int(command)

          if command == 1:
            if len(dragons) > 1:
              command = 0
              while command <= 0 or command > len(dragons):
                battleMenu.DisplayMessage(dragons, self.player,
                                          'Choose which to attack!')
                command = input()
                command = int(command)
                dragons[command - 1].InstanceProperties()
            else:
              dragons[command - 1].InstanceProperties()

        #give player a 1 in 3 chance to excape battle
        elif command == 3:
          if random.randrange(1, 3) > 2:
            message = "You escaped!"
            battleMenu.DisplayMessageAlert(dragons, self.player, message)
            dragons.clear()
          else:
            message = "Couldn't escape!"
            battleMenu.DisplayMessageAlert(dragons, self.player, message)
        Screen.clear()
        print()
