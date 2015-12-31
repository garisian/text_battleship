from math import sqrt
import random
import copy
import time


class board():

    def __init__(self, board_size):
        self.board_size = board_size
        self.the_board = []
        self.other_board = []

    def make_the_board(self):
        '''Create a list with the the elements of each row as a sub-list.
        Create two copies; one for player 1(other_board), one for player 2
        (the_board)'''
        temporary_list = []
        #Make the list which contains x (# of rows) number of \
        #items, and in each
        #x contains y (number of columns) number of items
        for item in range(0, self.board_size):
            for item in range(0, self.board_size):
                temporary_list.append('-')
            self.the_board.append(temporary_list)
            temporary_list = []
        #Make another copy. One is for player 1 while the other is player 2\
        #computer
        self.other_board = copy.deepcopy(self.the_board)

    def print_the_board(self, x):
        '''Print the board for current situation of the battleship game. If
        parameter x is 1: display player_one's board. Else, display player_two
        board. Return the board with borders.'''

        #if it's player 1....
        if x == 1:
            self.print_string = "\n|"
            for item in self.the_board:
                for thing in item:
                    #Print a "|" inbetween each spot, to \
                    #give a board like image
                    self.print_string += thing + "|"
                self.print_string += "\n|"

            #cut last element out. It is an extra "|" that we dont' need
            return self.print_string[:-1]
        # if it's player 2 / computer...
        else:
            self.print_string = "\n|"
            for item in self.other_board:
                for thing in item:
                    #Print a "|" inbetween each spot, to give a \
                    #board like image
                    self.print_string += thing + "|"
                self.print_string += "\n|"

            #cut last element out. It is an extra "|" that we dont' need
            return self.print_string[:-1]

    def make_full_number_list(self):
        '''Return a list that contains numbers starting from 0 till n-1. n is
        the total number of spots on the battleship board. '''
        final_list = []
        #board_size^2 indicates the number of spots that are on the board
        for item in range(self.board_size ** 2):
            #label each box by numbering them from 0 ---> board_size^2-1
            final_list.append(item)
        return final_list

    def add_boats(self, the_list):
        '''Update the current board by replacing all points in "the_list" with
        'B' on "the_board". Updates the board such that it contains the
        locations of the boats'''
        for item in the_list:
            #each item represents a coordinate in the form [a,b]
            for thing in item:
                x = thing[0]
                y = thing[1]
                #Replace the point on the board by 'B' which indicates that
                #There is a boat there
                self.the_board[y][x] = 'B'

    def hit_ship(self, x_coordinates, y_coordinates):
        '''Update the board such that if the [x_coordinates, y_coordinates] has
        a boat (indicated by 'B'), change to '*' (hit). Otherwise, update the
        point with 'M' (missed)'''
        # if the spot already has a boat, replace it by "*" meaning that it got
        #hit by the opponent
        if self.the_board[y_coordinates][x_coordinates] == 'B':
            self.the_board[y_coordinates][x_coordinates] = '*'
            self.other_board[y_coordinates][x_coordinates] = '*'
        # If there is nothing on the spot, indicated by "-", replace it by 'M',
        # meaning that the attack missed
        elif self.the_board[y_coordinates][x_coordinates] == '-':
            self.the_board[y_coordinates][x_coordinates] = 'M'
            self.other_board[y_coordinates][x_coordinates] = 'M'
