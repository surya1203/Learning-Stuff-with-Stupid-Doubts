# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.
 
 
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
 
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "S": 4, "N": 5, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"S": 1, "W": 2, "Q": 0}}

descriptions = {0: 'Exit Game', 1: 'Road', 2: 'Hill', 3: 'Building', 4: 'Valley', 5: 'Forest'}

user = int(input('Enter a value: '))
# while user != 0:
#     option = []
#     print(locations.get(user))
#     paths = exits.get(user)
#     for key in paths.keys():
#         option.append(key)
#     print('Paths you can take: {}'.format(option))
#     user = int(input('What path will you take?\n'))
#
while user != 0:
    # options = []
    print(locations.get(user))
    exit_values = exits.get(user)
    # print(exit_values)
    # options = [x for x in exit_values.values()]
    # print(options)
    # opt_des = [(value, descriptions.get(value)) for value in exit_values.values()]
    opt_des = [(xit, locations[xit]) for xit in exit_values.values()]
    # choice = [x for x in opt_des]
    print('Places you can go from here: {}'.format(opt_des))
    # paths = [(exit, descriptions[exit]) for exit in exits if exits[exit] == exits[user]]
    # print(paths)
    user = int(input('What path will you take?\n'))

print('Thank you for playing this lame ass game.')


