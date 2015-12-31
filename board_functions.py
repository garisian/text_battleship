from math import sqrt
import random
import copy
import time


class board_functions():
    def __init__(self):
        pass

    def convert(self, num, num_of_blocks):
        '''Return the coordinates representation of a box number so it fits
        on the board'''
        if num < num_of_blocks:
            return [num, 0]
        else:
            x = 0
            while num + 1 > num_of_blocks:
                num -= num_of_blocks
                x += 1
            return [num, x]

    def converted_perm(self, converting, num_of_blocks):
        '''Return a list that converts the stuff in the list 
        based on the num_of_blocks'''
            s = copy.deepcopy(converting)
            for item in s:
                if len(item) == 2:
                    item[0] = self.convert(item[0], num_of_blocks)
                    item[1] = self.convert(item[1], num_of_blocks)
                elif len(item) == 3:
                    item[0] = self.convert(item[0], num_of_blocks)
                    item[1] = self.convert(item[1], num_of_blocks)
                    item[2] = self.convert(item[2], num_of_blocks)
                elif len(item) == 4:
                    item[0] = self.convert(item[0], num_of_blocks)
                    item[1] = self.convert(item[1], num_of_blocks)
                    item[2] = self.convert(item[2], num_of_blocks)
                    item[3] = self.convert(item[3], num_of_blocks)
                elif len(item) == 5:
                    item[0] = self.convert(item[0], num_of_blocks)
                    item[1] = self.convert(item[1], num_of_blocks)
                    item[2] = self.convert(item[2], num_of_blocks)
                    item[3] = self.convert(item[3], num_of_blocks)
                    item[4] = self.convert(item[4], num_of_blocks)
            return s

    def get_x_coordinates(self, board_length):
        '''Returns the x coordinate which is given by the user'''
        try:
            #make sure the x coordinate is a valid input
            d = int(raw_input("What is the x-coordinate of your attack spot?"))
            if d > board_length - 1 or d < 0:
                print "THAT COORDINATE IS OUT OF THE BOARD"
                return self.get_x_coordinates(board_length)
            return d
        #If the coordinate wasn't number....
        except ValueError:
            print "TYPE A NUMBER YOU IDIOT!!"
            return self.get_x_coordinates(board_length)

    def get_y_coordinates(self, board_length):
        '''Returns the y coordinate which is given by the user'''
        try:
            #make sure the y coordinate is a valid input
            d = int(raw_input("What is the y-coordinate of your attack spot?"))
            if d > board_length - 1 or d < 0:
                print "THAT COORDINATE IS OUT OF THE BOARD"
                return self.get_y_coordinates(board_length)
            return d
        #If the coordinate wasn't number....
        except ValueError:
            print "TYPE A NUMBER FOOL!!"
            return self.get_y_coordinates(board_length)

    def compt_or_player(self):
        '''Returns the number 1 or 2 which indicates if it's player vs player
        or player vs computer'''
        try:
            #checks if the value is either 1 or 2, representing one of 2
            #options
            d = int(raw_input(\
            "Enter 1 for Player Vs \
            Player or Enter 2 for Player Vs Computer: "))
            if d == 1 or d == 2:
                return d
            #if it's neither, rerun the method
            else:
                raise ValueError
        except ValueError:
            print "TYPE A 1 OR 2!!!!"
            return self.compt_or_player()

    def set_board_size(self):
        '''Return the size of the board. Raw input is called and vale of the
        board size is evaluated'''
        try:
            #Check if the size of the board entered is a number. Equate it to
            #num_of_boxes
            num_of_boxes = \
                int(raw_input("Please enter the size of the board: "))
            if num_of_boxes < 2:
                #Can't have a 1 by 1 board or anything less. Call method again
                # if The value of num_of_boxes is less than 2
                print "Board length cannot be less than 2"
                num_of_boxes = self.set_board_size()
            return num_of_boxes
        except ValueError:
            #If it failed, type a message indicating why it failed and recall
            #the method until you get a valid value
            print "Type a legit number fool"
            return self.set_board_size()

    def kinds_of_boats(self, the_boats, board_size):
        '''Return a dict with the keys in "the_boats" and assign a value to it.
        Value represents the number of boats that boat_size has'''
        kinds_of_pieces_dict = {}
        try:
            # Iterate through the_boats (2, 3, 4, 5) \
            #and indicate how many boats of
            # each you want
            for item in the_boats:
                num_of_boats = raw_input("How many pieces of " + str(item) + \
                                         " sized boats:")
                num_of_boats = int(num_of_boats)
                if item > board_size:
                    print "BOAT SIZE " + str(item)\
                          + " WONT FIT ON THE BOARD. SET TO 0"
                    kinds_of_pieces_dict[item] = 0
                else:
                    # add the key and it's value to the kinds_of_pieces_dict
                    kinds_of_pieces_dict[item] = num_of_boats
            sum_val = 0
            #Find the number of squares that will be occupied by the boats
            for item in kinds_of_pieces_dict:
                sum_val += item * kinds_of_pieces_dict[item]
            #Rule: The number of squares occupied by the boat must be less than
            # half of the total number of spots on the box
            if sum_val > board_size ** 2 / 2:
                print "TOO MANY BOATS!! LESS BOATS!!!"
                print \
            "Total area used by boats must be less than 50% of the game board"
                return self.kinds_of_boats(the_boats, board_size)
            # You must have at least one boat. you cannot have 0 \
            #boats and play
            # the game
            elif sum_val == 0:
                print "YOU NEED AT LEAST ONE BOAT FOOL! "
                return self.kinds_of_boats(the_boats, board_size)
            return kinds_of_pieces_dict
        # except these errors and call the method again if any inproper values
        # were entered
        except ValueError:
            print "Not a valid input"
            kinds_of_pieces_dict = {}
            return self.kinds_of_boats(the_boats, board_size)

    def list_remover(self, list1, list2):
        '''Return a list that takes has every item in list1 \
        removed.If list1 has
        [1,2], every item in list2 that has either \
        a '1' or a '2' is completely
        removed. Helps manage with coordinates are occupied on the board'''
        p = []
        for item in list1:
            for thing in list2:
                if item in thing:
                    if thing not in p:
                        p.append(thing)
        for thing in p:
            list2.remove(thing)
        return list2

    def random_choosing_of_boats(self, two, \
                                 three, four, five, kinds_of_pieces_dict):
        '''Return a list that contains all the coordinates of the ships that
         needs to be placed on the board. The coordinates will be randomly
        chosen from the two, three four, five parameters (lists), with the help
         of kinds_of_pieces_dict (indicates how many of each boat is needed'''
        list_of_coordinates_for_all = []
        #Once a coordinate has been used, it is added to this list so that it
        #won't be overwritten by another boat
        removed_items = []
        #these variable contain the number of pieces we need for each kind of
        #boat
        num_of_five_ships = kinds_of_pieces_dict[5]
        # boats which is 5
        num_of_four_ships = kinds_of_pieces_dict[4]
        # boats which are 4
        num_of_three_ships = kinds_of_pieces_dict[3]
        # boats which is 3
        num_of_two_ships = kinds_of_pieces_dict[2]
        thing = five
        for item in range(0, num_of_five_ships):
            t = random.randint(0, len(five) - 1)
            # we are randomly choosing a possible boat orientation \
            #from the list
            # and are adding those coordinates \
            #to removed_items so they can't be
            # used again
            sample_1 = thing[t]
            list_of_coordinates_for_all.append(sample_1)
            thing = self.list_remover(sample_1, five)
            # if random item was already in removed_items, don't \
            #use it and get
            # another coordinate
            for item in sample_1:
                if item not in removed_items:
                    removed_items.append(item)
        #Make sure that none of the other boat occupy the boats \
        #that the 5 piece
        #boats are. So remove all occurances of their coordinates in four
        four = self.list_remover(removed_items, four)
        thing2 = four
        for item in range(0, num_of_four_ships):
            a = random.randint(0, len(four) - 1)
            # we are randomly choosing a possible boat \
            #orientation from the list
            # and are adding those coordinates
            #to removed_items so they can't be
            # used again
            sample_1 = thing2[a]
            list_of_coordinates_for_all.append(sample_1)
            thing2 = self.list_remover(sample_1, four)
            for item in sample_1:
                # if random item was already in removed_items, \
                #don't use it and
                # getanother coordinate
                if item not in removed_items:
                    removed_items.append(item)
        #Make sure that none of the other boats occupy the boats that the e
        #5-piec boats are. So remove all occurances of their \
        #coordinates in four
        three = self.list_remover(removed_items, three)
        thing3 = three
        for item in range(0, num_of_three_ships):
            b = random.randint(0, len(three) - 1)
            # we are randomly choosing a possible \
            #boat orientation from the list
            # and are adding those coordinates
            #to removed_items so they can't be
            # used again
            sample_1 = thing3[b]
            list_of_coordinates_for_all.append(sample_1)

            thing3 = self.list_remover(sample_1, three)
            # if random item was already in removed_items, don't use it and get
            # another coordinate
            for item in sample_1:
                if item not in removed_items:
                    removed_items.append(item)
        #Make sure that none of the other boats occupy the boats that the
        #5-piece boats are. So remove all occurances of their coordinates in
        #four
        two = self.list_remover(removed_items, two)
        thing9 = two
        for item in range(0, num_of_two_ships):
            v = random.randint(0, len(two) - 1)
            # we are randomly choosing a possible boat orientation \
            #from the list
            # and are adding those coordinates to \
            #removed_items so they can't be
            # used again
            sample_1 = thing9[v]

            list_of_coordinates_for_all.append(sample_1)
            # if random item was already in removed_items, \
            #don't use it and get
            # another coordinate
            thing9 = self.list_remover(sample_1, two)
            if sample_1 not in removed_items:
                removed_items.append(sample_1)
            #no need to add it to the remove list. NO more \
            #boats needed. so just
            #return the list with the boat coordinates
        return list_of_coordinates_for_all
