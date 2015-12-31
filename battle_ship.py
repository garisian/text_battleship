from math import sqrt
import random
import copy
import media
import time
from board import board
import sys
from boats import boats
from board_functions import board_functions

if __name__ == "__main__":

    working_class = board_functions()
    # 'b' either has 1 or 2 which indicate if it's player vs player or player
    # vs computer
    b = working_class.compt_or_player()
    #snd=media.load_sound('battle2.wav')
    #media.play(snd)
    # if it's 1, it's player vs player
    if b == 1:
        #create the boards for both player one and player 2
        board_size = working_class.set_board_size()
        # ask how many ships of each kinds is wanted
        the_boat_numbers = working_class.kinds_of_boats([2, 3, 4, 5], \
                                                        board_size)
        player_one_board = board(board_size)
        player_one_board.make_the_board()
        player_two_board = board(board_size)
        player_two_board.make_the_board()
        # make a list of permutations for each boat and save it to the
        # corresponding list
        the_list = player_one_board.make_full_number_list()
        b = boats(board_size, the_boat_numbers)
        permutation_list5 = b.permutation_list(the_list, 5)
        permutation_list4 = b.permutation_list(the_list, 4)
        permutation_list3 = b.permutation_list(the_list, 3)
        permutation_list2 = b.permutation_list(the_list, 2)
        #randomly choose the coordinates for the wanted ships for player one
        # and player two. NOTE that they will NOT be the same.
        boat_list_1 = \
            working_class.random_choosing_of_boats(permutation_list2,
                    permutation_list3, permutation_list4,\
                    permutation_list5, the_boat_numbers)
        #Converted_lists converts the boat_lists into a coordinate system that
        # is used by the game board
        converted_list_1 = \
            working_class.converted_perm(boat_list_1, board_size)
        boat_list_2 = \
            working_class.random_choosing_of_boats(permutation_list2,
                    permutation_list3, permutation_list4, permutation_list5,\
                    the_boat_numbers)
        converted_list_2 = \
            working_class.converted_perm(boat_list_2, board_size)
        # Take the final list of coordinates and add it to the boards of player
        # one and player two
        player_one_board.add_boats(converted_list_1)
        player_two_board.add_boats(converted_list_2)
        keep_playing = True
        # Keep tracks on which coordinates the player/computer have already
        # attacked. one list is for player 1, while the other is for player2/
        # computer
        hit_points = []
        hit_points1 = []
        # this is the loop that rotates between the two turns
        while keep_playing == True:
            # player one's turn
            print "----------------------------Player 1's move----------------"
            player_one_board.print_the_board(0)
            print player_two_board.print_the_board(0)
            pointer = True
            while pointer == True:
                # choose two coordinates that haven't been entered already
                # by same player
                x = working_class.get_x_coordinates(board_size)
                y = working_class.get_y_coordinates(board_size)
                if [x, y] not in hit_points:
                    pointer = False
                    hit_points.append([x, y])
                else:
                    print "YOU CHOSE THIS POINT ALREADY FOOL!!"
            #updates the screen with how your current board is and status on
            #enemy board
            player_two_board.hit_ship(x, y)
            print "---------------ENEMY BOARD AFTER YOUR MOVE-----------------"
            print player_two_board.print_the_board(0)
            print "---------------MY BOARD RIGHT NOW------------------"
            print player_one_board.print_the_board(1)
            # The conditions for comments if the poitn choosen has a boat
            for item in converted_list_2:
                for thing in item:
                    # if the coordinates are the same, then a boat was there.
                    if [x, y] == thing:
                        item.remove([x, y])
                        print "ENEMY SHIP HAS BEEN HIT!"
                        #media.play(media.load_sound('bigboom.wav'))
                    #else:
                        ##media.play(media.load_sound('pond_splash.wav'))
                # if a boat has been sunk, an empty list would exist. If one is
                # found, delete it and state that a boat has been sunk
                if [] in converted_list_2:
                    print "AN ENEMY BOAT HAS BEEN SUNK!!!!"
                    converted_list_2.remove([])
                # if the whole list is empty, it means all boat locations have
                # been hit. Player One Wins
                if [] == converted_list_2:
                    print "PLAYER ONE HAS WON!!!!!!!!!"
                    keep_playing = False
                    media.stop(snd)
                    break
                break
            print '==========================================================='
            # If player 1 has not won by this point:
            if converted_list_2 != []:
                # now it's player 2's turn
                print "------CHANGE TURNS   LOOK AWAY PLAYER 2--------"
                print "-----------------Player 2's moves--------------------"
                print player_one_board.print_the_board(0)
                # same routine. Choose coordinate that hasn't been picked yet
                pointer = True
                while pointer == True:
                    x2 = working_class.get_x_coordinates(board_size)
                    y2 = working_class.get_y_coordinates(board_size)
                    if [x2, y2] not in hit_points1:
                        pointer = False
                        hit_points1.append([x2, y2])
                    else:
                        print "YOU CHOSE THIS POINT ALREADY FOOL!!"
                # update the board with the coordinates chosen
                player_one_board.hit_ship(x2, y2)
                print "---------------ENEMY BOARD------------------"
                print player_one_board.print_the_board(0)
                print "---------------MY BOARD------------------"
                print player_two_board.print_the_board(1)
                # conditiosn if boat has been hit/sunk/player has won
                for item in converted_list_1:
                    # if coordinates is thing, that means a boat was there.
                    # enemy boat has been hit
                    for thing in item:
                        if [x2, y2] == thing:
                            item.remove([x2, y2])
                            print "ENEMY SHIP HAS BEEN HIT!"
                            #media.play(media.load_sound('bigboom.wav'))
                        #else:
                            #media.play(media.load_sound('pond_splash.wav'))
                    # after removing previous location, if there is an empty
                    # list, that means that the boat was sunk.
                    if [] in converted_list_1:
                        print "AN ENEMY BOAT HAS BEEN SUNK!!!!"
                        converted_list_1.remove([])
                    # after removing the empty list, if the list is empty,
                    # player two has won teh game.
                    if [] == converted_list_1:
                        print "PLAYER TWO HAS WON!!!!!!!!!"
                        keep_playing = False
                        media.stop(snd)
                        break
                    break
            # if no one won, back to player 1...
            print "==========================================================="
    # it can only be 1 or 0, so if it's not 1 it has to be 0, indicating it's
    #  player vs computer. Note this next half is similar to the code from the
    # last half
    else:
        #ask for the size of the board
        board_size = working_class.set_board_size()
        #the number of boat for each sizes is asked
        the_boat_numbers = working_class.kinds_of_boats([2, 3, 4, 5], \
                                                        board_size)
        #create both the boards for player one and player two
        player_one_board = board(board_size)
        player_one_board.make_the_board()
        player_two_board = board(board_size)
        player_two_board.make_the_board()
        # create a full list of coordinates in the board
        the_list = player_one_board.make_full_number_list()
        #creates lists for permutations for each boat size
        b = boats(board_size, the_boat_numbers)
        permutation_list5 = b.permutation_list(the_list, 5)
        permutation_list4 = b.permutation_list(the_list, 4)
        permutation_list3 = b.permutation_list(the_list, 3)
        permutation_list2 = b.permutation_list(the_list, 2)
        #make a list that randomly pulled coordinates for the boat
        boat_list_1 = \
            working_class.random_choosing_of_boats(permutation_list2,\
                    permutation_list3, permutation_list4,\
                    permutation_list5, the_boat_numbers)
        #convert the boat_list to a list that the game board can comprehend
        converted_list_1 = \
            working_class.converted_perm(boat_list_1, board_size)

        #make a list that randomly pulled coordinates for the boat
        boat_list_2 = \
            working_class.random_choosing_of_boats(permutation_list2,\
                        permutation_list3, permutation_list4, \
                        permutation_list5,\
                        the_boat_numbers)
        #convert the boat_list to a list that the game board can comprehend
        converted_list_2 = working_class.converted_perm(boat_list_2, \
                                                        board_size)
        # finally add the coordinates of the boat onto the board
        player_one_board.add_boats(converted_list_1)
        player_two_board.add_boats(converted_list_2)
        # the loop that indicates when to stop rotating turns
        keep_playing = True
        #keeps track of the points that have been hit
        hit_points = []
        hit_points1 = []
        while keep_playing == True:
            #player one's turn
            print "Player 1's Board and Player 2's move"
            #print how your attacking board looks like
            print player_two_board.print_the_board(0)
            pointer = True
            print "----------Your Current Board-------------"
            #prints how your board looks from your oppenent
            print player_one_board.print_the_board(1)
            while pointer == True:
                # use the coordinate an and update the board
                x = working_class.get_x_coordinates(board_size)
                y = working_class.get_y_coordinates(board_size)
                if [x, y] not in hit_points:
                    pointer = False
                    hit_points.append([x, y])
                else:
                    print "YOU CHOSE THIS POINT ALREADY FOOL!!"
            #Enemy turn
            player_two_board.hit_ship(x, y)
            #print the current situation of enemy's board
            print "---------------ENEMY BOARD------------------"
            print player_two_board.print_the_board(0)
            print "---------------MY BOARD------------------"
            print player_one_board.print_the_board(1)
            # commands for if boat has been hit
            for item in converted_list_2:
                for thing in item:
                    # if both items are the same, the boat has been hit
                    if [x, y] == thing:
                        item.remove([x, y])
                        print "ENEMY SHIP HAS BEEN HIT!"
                        #media.play(media.load_sound('bigboom.wav'))
                    #else:
                        #media.play(media.load_sound('pond_splash.wav'))
                # if the list is empty after the removing,
                # it means boat is sunk
                if [] in converted_list_2:
                    print "AN ENEMY BOAT HAS BEEN SUNK!!!!"
                    converted_list_2.remove([])
                # if the overall list is empty, no more spots left. Player one
                # wins
                if [] == converted_list_2:
                    print "PLAYER ONE HAS WON!!!!!!!!!"
                    keep_playing = False
                    #media.stop(snd)
                    break
                break
            #if player one didn't win yet:
            if converted_list_2 != []:
                print "\n" * 5
                #indicates in the shell that turns ended
                print "------CHANGE TURNS--------"
                print "COMPUTER'S TURN"
                player_one_board.print_the_board(0)
                pointer = True
                # random a point that hasn't been randomed already
                while pointer == True:
                    x2 = random.randint(0, board_size - 1)
                    y2 = random.randint(0, board_size - 1)
                    if [x2, y2] not in hit_points1:
                        pointer = False
                        hit_points1.append([x2, y2])
                # attack player one' sboard with the randomed coordinate
                player_one_board.hit_ship(x2, y2)
                print "computer has attacked " + str([x2, y2])
                # if the boat has been hit
                for item in converted_list_1:
                    for thing in item:
                        if [x2, y2] == thing:
                            # if the coordinates are the same, boat is hit
                            item.remove([x2, y2])
                            print "COMPUTER HIT ENEMY SHIP!"
                            ##media.play(media.load_sound('bigboom.wav'))
                        #else:
                            #media.play(media.load_sound('pond_splash.wav'))
                    #if empty list is in the final_list, boat has been sunk
                    if [] in converted_list_1:
                        print "COMPUTER HAS SUNK AN SHIP!!!!"
                        converted_list_1.remove([])
                    # if the list is empty: computer has won
                    if [] == converted_list_1:
                        print "COMPUTER HAS WON!!!!!!!!!"
                        keep_playing = False
                        #media.stop(snd)
                        break
                    break
            print "\n" * 10
