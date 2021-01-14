from random import choice

name = input ("What is your name?")

print ("Welcome to Middle Earth," + name + "!") 

print("")

age = input ("How old are you?")
print("")

if int(age) > 1000:
    description = " an elder "
else:
    description = "a younger one"

print("So you are " + description + "," + name)
print("")


#write each list item and then write prompt. I can put the items in a plot generator so it  creates a random story. Then I will just substitute the items for the variables and finish it.


things = ["goblins", "mines", "chocolate", "rocks", "trees", "pipe"]
friends = ["Bilbo", "Gandalf", "Aragorn", "Galadriel", "Gimli", "Haldir", "Arwen", "Thranduil ", "Legolas", "celeborn", "Glorfindel", "Elrond"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat", "study", "talk with"]
places = ["Old Forrest", "Lothlórien", "Fangorn", "Beleriand", "Valinor"]

friend = choice(friends)
thing = choice(things)
action = choice(actions)
place = choice(places)

story = "Once upon a time, there was an Elf called " + name + ". The Elf was " + description + " in Middle Earth." + " It liked nothing better than to " +  action + " " + thing + ". Sadly, the Elf was so great at this that it ran out of " + thing + " to " + action + " in " + place + ". The Elf became very bored. Luckily the Elf had a friend called " + friend + ". " + friend + " knew where the Elf could find lots of " + thing + " and the two of them travelled far away from " + place + " and found a land filled with lots of lovely " + thing + " to " + action + ". " + name + " and " + friend + " lived happily ever, with all the " + thing + " they wanted."

print(story)




#ver como colocar a lista de opções pra pessoa poder selecionar da list place.
Place = ['Bree', 'The Shire', "Valfenda", (...)] #completar
choose_Place = choice(Place)

food = ["Lamba", "Beer", "Fruit", "Fish", "Vegetables"]
choose_Food = choice(food)

to_Do = ["Hike" + "go fishing" + "Try to get the Ring of Power" + "Go to the tavern", "Smoke tabacco and try to make rings", 'Read by the fire']
choose_to_Do = choice(to_Do)

