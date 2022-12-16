"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = set()
    for line in open(filename):
        words = line.split("|")

        species.add(words[1])

    return species

#when you call another file as an argument, put it in " "! 
#print(all_species("villagers.csv"))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    #if species name is the argument search_string
            #find all of the villagers who are that species
                #append them to our list villagers
            #return a sorted list of villagers
#create an empty list called villagers that can be returned 
    villagers = []

#iterate through the villagers.csv file line by line 
    for line in open(filename):
        #split the string in each line of the villagers.csv into a list that can be iterated
        words = line.split("|")
    
        #if the species name (which is index 1 in our new list words), is equal to the argument...
        #...of the string search put in in calling the function:
        if words[1] == search_string:
            #append the name of the villager (index 0 in the new list words) to the villagers list.
            villagers.append(words[0])

    #return the list of villagers sorted in alphabetical order. 
    return sorted(villagers)

# print(get_villagers_by_species("villagers.csv", "Goat"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # create an empty list for each hobby: 
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

#   iterate through the villagers.csv file line by line 
    for line in open(filename):
        #split the string in each line of the villagers.csv into a list that can be iterated
        words = line.split("|")
        hobby= words[3]
        name = words[0]

        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)

    return [
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play),
        ]
print(all_names_by_hobby("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
