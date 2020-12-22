# Ok people, don't get too picky.  This is my first python program from scratch, so I'm sure there is a hot mess of
# stupid in here, but a lot of learning.

# The end result is supposed to be an ordered list of my tshirts where no shirt is adjacent to a similar
# shirt based on either theme or color

import numpy as np
import random

random.seed()

DEBUG = 0
SHIRT_FILE = 'shirts.csv'

# Here is a list of my shirts

# Translate the array into actual counts of shirts per category
# Here is what I suspect, but do not know:
#  This is a hard math problem masquerading as an interesting programming problem.  Given a collection of items
#  with N (=2) dimensions, how can you sort those items so that no two dimensions are adjacent to each other
#  in the final list?  I suspect there is some interesting set theory math, or ... but it's outside of my
#  level, so here we are.

# Also, if I may, I'm sure there is a good reason, but array indices in numpy are counterintuitive for me.
# One dimensional array:  initial is on the X axis
# two dimensional array:  initial is on the Y axis and second is on the X axis
# Huh?  Maybe just thinking about it wrong.
# This was the original setup, before I got the file reading working
tshirt = np.array([[0, 1, 0, 5, 4], [1, 2, 0, 0, 0], [1, 2, 3, 1, 0], [3, 0, 0, 0, 1], [0, 1, 3, 0, 0],
                   [0, 0, 0, 0, 2]])
if DEBUG == 1: print("Prior: tshirts is ", tshirt)

# Ok, listen.  I know having these on one line isn't the python way.  My syntax is pretty clean otherwise, but this
# is just too friggin simple and readable, so deal with it
if DEBUG == 1: print(shirts)

# File should look like:
# HEADER, color, company, run, ohack, fatty, other
# black/grey, 0, 1, 0, 5, 4
# light grey, 1, 2, 0, 0, 0
# ROP, 1, 2, 3, 1, 0
# blue, 3, 0, 0, 0, 1
# green, 0, 1, 3, 0, 0
# other, 0, 0, 0, 0, 2

# If I get adventurous I could put this into a google sheet and work on figuring out how to read it all
# from an API.  :)


def read_shirts(shirt_file, lthemes, lcolors):  # ltheme = local theme, lcolors = local colors
    with open(shirt_file, 'r') as file:
        for line in file:
            new_list = []  # I'm going to need a temporary list that gets wiped every time
            line = line.strip('\n')
            if DEBUG == 1: print("|", line, "|")
            # Need to pull out the header row
            line_list = line.split(", ")
            if DEBUG == 1: print("line_list = ", line_list)
            if line_list[0] == "HEADER":
                line_list.pop(0)    # get rid of header element
                line_list.pop(0)    # get rid of the color portion that is just for readability
                lthemes = line_list
                if DEBUG == 1: print("lthemes = ", lthemes)
            else:   # Now we have an element starting with a color
                lcolors.append(line_list.pop(0))  # pop the color off and add it to our color list
                if DEBUG == 1: print("List of colors is", line_list)

                # The line list has the elements as strings.  I need them to be ints so put them in my
                # temporary list as ints.
                for color in line_list:
                    new_list.append(int(color))
                if DEBUG == 1: print("new list of colors is", new_list)
                try:  # let's see if we haven't defined this. If it is, add
                    tshirt = np.append(tshirt, [new_list], axis=0)
                    if DEBUG == 1: print("tshirt array added and now is ", tshirt, line_list)
                except NameError:   # otherwise we initialize it
                    tshirt = np.array([new_list])
                    if DEBUG == 1: print("first tshirt assignment = ", tshirt)
    if DEBUG == 1: print("tshirt array finishes as ", tshirt)
    if DEBUG == 1: print("colors finish as", lcolors)
    if DEBUG == 1: print("themes finish as", lthemes)

    file.close()    # Good idea to cleanup
    return tshirt, lthemes, lcolors


def print_array(label, array):  # Subroutine to print arrays for me.  Probably a python builtin for this.
    for i in range(0, len(array) - 1):
        print(label, array[i])
    return 1


# Ok, so this where I do the initial sort of dealing with the data as a matrix and things start to get funny
def matrix_shirts(shirt_matrix):
    shirt = 0
    shirt_list = []

    # Probably not the first hack.  Use counters to prevent infinite looping.
    max_counter = 50
    base_counter = 30
    counter = 0
    lastcolor = ncolors  # just an initial
    lasttheme = nthemes

    # I initially did this with for loops, because that made sense.  Then I learned that python for loops
    # are really for X in Y loops, and you can't do all the fun you can do with for(i=0;i<X;i++) loops, so it
    # had to be whiles, or at least not for.
    while shirt <= shirts and counter < max_counter:
        random.seed()
        color = random.randint(0, ncolors - 1)  # start in a random place to work through local maxima
        # So what does that mean?  You can imagine a matrix where you walk it every time and it can never
        # be solved if you always start from the same place.  So, let's start someplace random.
        while color < ncolors and counter < max_counter:
            theme = 0
            counter += 1
            if DEBUG == 1: print("in color", color, theme)
            while theme < nthemes and counter < max_counter:
                if DEBUG == 1: print("in theme", color, theme, shirt, counter, max_counter)
                if counter > base_counter:  # if we've iterated a lot, use random to try to avoid local maxima
                    if DEBUG == 1: print("Randomizing")
                    random.seed()
                    color = random.randint(0, ncolors - 1)
                    theme = random.randint(0, nthemes - 1)
                if shirt_matrix[color, theme] > 0 and color != lastcolor and theme != lasttheme:
                    counter += 1
                    # Move this to putting in an array so we can try to slot other shirts in at the end
                    if DEBUG == 1: print("Success:", colors[color], themes[theme], shirt)
                    shirt_list.append([colors[color], themes[theme]])
                    shirt_matrix[color, theme] -= 1
                    lastcolor = color
                    lasttheme = theme
                    shirt += 1
                    # Now we don't want the next to be same theme or color, so increment both
                    # I think this is sort of clever, without being a sort.  In a matrix, if I increment both
                    # x and y, there is no way for it to be adjacent.
                    theme += 1
                    color += 1
                else:
                    theme += 1
                if theme > nthemes:  # check to see if we marched it off the end, so let's wrap it
                    theme = 0
        color += 1
        if color >= ncolors:
            color = 0
        if DEBUG == 1: print("color increment", color)

    # Return the number of shirts I found
    return shirt_list, shirt_matrix

# Ok, so now we have an array of shirts that are sorted, and all the crap in tshirt.numpy that we want to put into
# an array to allow us to iterate


def matrix_to_array(sorted_shirts):
    list_of_shirts = []

    # build an array of the remaining shirts
    for color in range(0, ncolors):
        for theme in range(0, nthemes):
            if sorted_shirts[color, theme] > 0:
                for f in range(0, sorted_shirts[color, theme]):  # there could be a bunch of them
                    list_of_shirts.append([colors[color], themes[theme]])

    return list_of_shirts


# This takes the array of sorted shirts, and a single new shirt color/theme combination and sees if it can
# stash it into the array

def insert_shirt(finished_shirts, color, theme):

    prev_color = "undef"
    prev_theme = "undef"

    if DEBUG > 0: print_array("Insert shirt started with", finished_shirts)
    for shirt in range(0, len(finished_shirts)):
        if DEBUG > 0: print("shirt number:", shirt)
        if color != prev_color and theme != prev_theme:
            if finished_shirts[shirt][0] != color and finished_shirts[shirt][1] != theme:
                if DEBUG > 0: print(prev_color, prev_theme, '<-', color, theme, '->',
                                    finished_shirts[shirt][0],  finished_shirts[shirt][1])
                finished_shirts.insert(shirt, [color, theme])
                if DEBUG > 0: print_array("Insert shirt finished with", finished_shirts)
                return 1, finished_shirts
        prev_color = finished_shirts[shirt][0]
        prev_theme = finished_shirts[shirt][1]
    return 0, finished_shirts


# Press the green button in the gutter to run the script, because this is what pycharms tells you.  :P

if __name__ == '__main__':

    themes = []
    colors = []
    sorted_shirt_list = []
    (tshirt, themes, colors) = read_shirts(SHIRT_FILE, themes, colors)
    shirts = tshirt.sum()
    more_shirts = 0

    print("Total shirts we started with ", shirts)

    if DEBUG == 1: print("Main: tshirts is ", tshirt)
    if DEBUG == 1: print("Main: themes are ", themes)
    if DEBUG == 1: print("Main: colors are ", colors)
    ncolors = len(colors)
    nthemes = len(themes)
    if DEBUG == 1: print(ncolors)
    if DEBUG == 1: print(nthemes)

    # do the matrix analysis of the shirts, pass in empty array
    # ok, I think this is wrong.  I should pass in the matrix and return the sorted_shirt_list
    (sorted_shirt_list, tshirt) = matrix_shirts(tshirt)
    num_sorted = len(sorted_shirt_list) - 1
    if DEBUG > 0: print("Matrix took care of", num_sorted, "shirts")
    if DEBUG > 0: print_array("From matrix", sorted_shirt_list)

    if (shirts - num_sorted) > 0:
        # if there are shirts left (hint, there probably will be), turn those into an array
        remaining_shirts = matrix_to_array(tshirt)
        if DEBUG > 0: print_array("Left over", remaining_shirts)

        for rshirt in range(0, len(remaining_shirts)):
            single_shirt = remaining_shirts.pop()
            shirt_color = single_shirt[0]
            shirt_theme = single_shirt[1]
            if DEBUG > 0: print("Shirt to fix is", shirt_color, shirt_theme)
            (retval, sorted_shirt_list) = insert_shirt(sorted_shirt_list, shirt_color, shirt_theme)

            if retval == 0:
                print("We failed")

    print_array("Final", sorted_shirt_list)
