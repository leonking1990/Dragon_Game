#Stevie D Littleton
#Final Project : Creating your own Python Project
#Date: April 12, 2021
#Description: This simple text based game that allows the user to battling enemies and defeating them while gaining XP and gold.
#https://replit.com/@stevielittleton/dragon-game#main.py
import Market
import Arena
import Player
import json
import Screen
import time


#this methos is used to takes player data and stor it in a json file
def save(player):
  saveData = {
    "No": player.number,
    "Name": player.getName(),
    "Level": player.getLevel(),
    "Coin": player.wallet(),
    "EXP": player.exp,
    "EXP_to_next_level": player.nextLevel,
    "Legendary": player.isLegendary(),
    "Sword": player.weapon,
    "Shield": player.shield
  }

  with open("saveFile.json", "r+") as out_file:
    data = json.load(out_file)
    #print(data)
    #input("Press Enter to continue...")
    data['Save ' + str(player.number)] = saveData
    out_file.seek(0)
    #print(data)
    #input("Press Enter to Continue")
    json.dump(data, out_file, indent=6)
    out_file.truncate()


def Start(play):
  #opens json file and loads data
  with open("saveFile.json", "r") as openfile:
    json_object = json.load(openfile)
    # Reading from json file

  #prints the list of save data in the json file
  print()
  print("Who is standing before us? ")
  print("1: " + json_object['Save 1']['Name'])
  print("2: " + json_object['Save 2']['Name'])
  print("3: " + json_object['Save 3']['Name'])
  print()

  select = input()
  Screen.clear()
  print()

  #determins if new player is selected and if so prompts for player to enter name then creates object player.
  if json_object['Save ' + select]['Name'] == 'New Challenger':
    playerNum = json_object['Save ' + select]['No']
    weapon = json_object['Save ' + select]['Sword']
    shield = json_object['Save ' + select]['Shield']
    print("Ah a new challenger!")
    print()
    print("What shall I call you?")
    name = input()
    name = name.title()

    #creates new player object
    player = Player.Player(playerNum, name, 1, 100, 0, 1000, weapon, shield,
                           False)

  #if player is selected from the list of save data then it loads the player data form json file into the player object
  else:
    playerNum = json_object['Save ' + select]['No']
    name = json_object['Save ' + select]['Name']
    level = json_object['Save ' + select]['Level']
    coin = json_object['Save ' + select]['Coin']
    exp = json_object['Save ' + select]['EXP']
    exp_to_next_level = json_object['Save ' + select]['EXP_to_next_level']
    weapon = json_object['Save ' + select]['Sword']
    shield = json_object['Save ' + select]['Shield']
    legendary = json_object['Save ' + select]['Legendary']

    print("Welcome Back " + name + "!")
    time.sleep(1.5)
    player = Player.Player(playerNum, name, level, coin, exp,
                           exp_to_next_level, weapon, shield, legendary)

  while play:
    Chos = 0

    while Chos < 1 or Chos > 4:
      Screen.clear()
      print(player.ID())
      print()
      print("Where would you like to go?")
      print("1. Town")
      print("2. Caves")
      print("3. Status")
      print("4. Save/Exit")
      Chos = input()
      Chos = int(Chos)
      if (Chos <= 0 or Chos > 4):
        print("Please enter a valid input")
        time.sleep(1.5)

    if Chos == 1:
      Market.Market(player)
    elif Chos == 2:
      Arena.arena(player)
    elif Chos == 3:
      player.InstanceProperties()
    elif Chos == 4:
      save(player)
      print("Until next time " + player.name + "!")
      play = False


Start(True)
