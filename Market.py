import Screen
import time
import Shield
import Weapon


class Market:

  def __init__(self, player):
    self.player = player
    items = [[
      Weapon.RustySword(),
      Weapon.OldSword(),
      Weapon.SteelSword(),
      Weapon.MasterSword(),
      Weapon.LegendarySword()
    ],
             [
               Shield.RustyShield(),
               Shield.IronShield(),
               Shield.SteelShield(),
               Shield.MasterShield(),
               Shield.LegendaryShield()
             ]]

    inTown = True
    while inTown:
      Chos = 0
      while Chos < 1 or Chos > 3:
        Screen.clear()
        print(self.player.ID())
        print()
        print("Welcome to the plaza.")
        print("1. Shops")
        print("2. Inn")
        print("3. Leave")
        Chos = input()
        Chos = int(Chos)

      if Chos == 1:
        shopping = True

        while shopping:
          Screen.clear()
          print(self.player.ID())
          print()
          print("What would you like to buy?\n")
          print(((" ") * 7) + "Name" + ((" ") * 16) + "Value")
          print("-" * 35)
          print("1.  " + items[0][0].getName() +
                (" " * (20 - len(items[0][0].getName()))) + "- " +
                str(items[0][0].getValue()) + "   coin")
          print("2.  " + items[0][1].getName() +
                (" " * (20 - len(items[0][1].getName()))) + "- " +
                str(items[0][1].getValue()) + "  coin")
          print("3.  " + items[0][2].getName() +
                (" " * (20 - len(items[0][2].getName()))) + "- " +
                str(items[0][2].getValue()) + "  coin")
          print("4.  " + items[0][3].getName() +
                (" " * (20 - len(items[0][3].getName()))) + "- " +
                str(items[0][3].getValue()) + "  coin")
          print("5.  " + items[0][4].getName() +
                (" " * (20 - len(items[0][4].getName()))) + "- " +
                str(items[0][4].getValue()) + " coin")
          print("6.  " + items[1][0].getName() +
                (" " * (20 - len(items[1][0].getName()))) + "- " +
                str(items[1][0].getValue()) + "   coin")
          print("7.  " + items[1][1].getName() +
                (" " * (20 - len(items[1][1].getName()))) + "- " +
                str(items[1][1].getValue()) + "  coin")
          print("8.  " + items[1][2].getName() +
                (" " * (20 - len(items[1][2].getName()))) + "- " +
                str(items[1][2].getValue()) + "  coin")
          print("9.  " + items[1][3].getName() +
                (" " * (20 - len(items[1][3].getName()))) + "- " +
                str(items[1][3].getValue()) + " coin")
          print("10. " + items[1][4].getName() +
                (" " * (20 - len(items[1][4].getName()))) + "- " +
                str(items[1][4].getValue()) + " coin")
          print("-" * 35)
          print("0. Exit")
          chos2 = input()
          chos2 = int(chos2)
          if (
              chos2 == 1 and self.player.wallet() >=
            (items[0][0].getValue())):  #working on a new way to handle wepons
            ()
            # self.player.spendCoin(150)
            # self.player.changeSword(items[0][0])
          elif (chos2 == 2 and self.player.wallet() >= items[0][1].getValue()):
            self.player.spendCoin(580)
            self.player.changeSword('Steel Sword', 15)
          elif (chos2 == 3 and self.player.wallet() >= items[0][2].getValue()):
            self.player.spendCoin(1200)
            self.player.changeSword('Master Sword', 25)
          elif (chos2 == 4 and self.player.wallet() >= items[0][3].getValue()):
            self.player.spendCoin(7600)
            self.player.changeSword('Legedary Sword', 50)
          elif (chos2 == 5 and self.player.wallet() >= items[0][4].getValue()):
            self.player.spendCoin(150)
            self.player.changeShield('Rusty Shield', 10)
          elif (chos2 == 6 and self.player.wallet() >= items[1][0].getValue()):
            self.player.spendCoin(370)
            self.player.changeShield('Rusty Shield', 15)
          elif (chos2 == 7 and self.player.wallet() >= items[1][1].getValue()):
            self.player.spendCoin(820)
            self.player.changeShield('Master Shield', 25)
          elif (chos2 == 8 and self.player.wallet() >= items[1][2].getValue()):
            self.player.spendCoin(5500)
            self.player.changeShield('Legedary Shield', 50)
          elif (chos2 == 9 and self.player.wallet() >= items[1][3].getValue()):
            self.player.spendCoin(5500)
            self.player.changeShield('Legedary Shield', 50)
          elif (chos2 == 10
                and self.player.wallet() >= items[1][4].getValue()):
            self.player.spendCoin(5500)
            self.player.changeShield('Legedary Shield', 50)
          elif (chos2 == 0):
            shopping = False
          else:
            print("you do not have enough coins!")
            time.sleep(3)
      elif Chos == 2:
        Screen.clear()
        print(self.player.ID())
        print()
        print("Would you like a room for the night? (Y/N)")
        sleep = input()
        sleep = sleep.title()
        while not (sleep == 'Y' or sleep == 'N'):
          Screen.clear()
          print(self.player.ID())
          print()
          print("invalid choice!")
          print("Would you like a room for the night: 100 coin? (Y/N)")
          sleep = input()
          sleep = sleep.title()
        if sleep == 'Y':
          if (self.player.wallet() >= 100):
            self.player.spendCoin(100)
            self.player.recover()
          else:
            print("you do not have enough coins!")
            time.sleep(3)

      elif Chos == 3:
        inTown = False
