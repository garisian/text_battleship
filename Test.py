import random
import unittest
from math import sqrt 
from board import board 
from boats import boats


class Testgame(unittest.TestCase):
        
    def setUp(self):
        self.s = board(10)
        self.s.make_the_board() 
        self.t = board(10)
        self.t.make_the_board()
        self.b = boats({2:1,3:1,4:1,5:1},10)
        
    def tearDown(self):
        self.s = None 
        
    def test1_board(self):
        #check if the board is 10 * 10
        self.assertTrue(self.s.the_board == [['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']])

  
    def test2_two_boat_placement(self):
        self.s.add_boats([[[1,2],[1,3]],[[5,3], [4,3]]]) 
        #check if the board has the appropriate number of two size ships without any of them overlapping
        self.assertTrue(self.s.the_board == [['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','B','B','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']])
    
    def test3_three_boat_placement(self):
        self.s.add_boats([[[1,2],[1,3], [1,4]],[[5,3], [4,3], [3,3]]]) 
        #check if the board has the appropriate number of two size ships without any of them overlapping
        self.assertTrue(self.s.the_board == [['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','B','B','B','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']])
        
    def test4_four_boat_placement(self):
        self.s.add_boats([[[1,2],[1,3], [1,4], [1,5]],[[5,3], [4,3], [3,3], [2,3]]]) 
        #check if the board has the appropriate number of two size ships without any of them overlapping
        self.assertTrue(self.s.the_board == [['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','B','B','B','B','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']])
    def test5_five_boat_placement(self):
        self.s.add_boats([[[1,2],[1,3], [1,4], [1,5], [1,6]],[[6,3],[5,3], [4,3], [3,3], [2,3]]]) 
        #check if the board has the appropriate number of two size ships without any of them overlapping
        self.assertTrue(self.s.the_board == [['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','B','B','B','B','B','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']])
    def test6_boat_placement_all_together(self):
        self.s.add_boats([[[1,2],[1,3]], [[1,5], [1,6], [1,7]],[[2,1],[2,2],[2,3],[2,4]],[[3,0],[3,1],[3,2],[3,3],[3,4]]]) 
        #check if the board has the appropriate number of two size ships without any of them overlapping
        self.assertTrue(self.s.the_board == [['-','-','-','B','-','-','-','-','-','-'],['-','-','B','B','-','-','-','-','-','-'],['-','B','B','B','-','-','-','-','-','-'],['-','B','B','B','-','-','-','-','-','-'],['-','-','B','B','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']])
        
    def test7_boat_hit_and_miss(self):
        self.t.the_board = [['-','-','-','B','-','-','-','-','-','-'],['-','-','B','B','-','-','-','-','-','-'],['-','B','B','B','-','-','-','-','-','-'],['-','B','B','B','-','-','-','-','-','-'],['-','-','B','B','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]
        self.t.hit_ship(0,0)
        self.t.hit_ship(3,0)
        self.assertTrue([['M','-','-','*','-','-','-','-','-','-'],['-','-','B','B','-','-','-','-','-','-'],['-','B','B','B','-','-','-','-','-','-'],['-','B','B','B','-','-','-','-','-','-'],['-','-','B','B','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','B','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']] == self.t.the_board)
        
    def test8_permutation_for_two_size_boat(self):
        self.assertEqual(self.b.permutation_list([0,1,2,3,4,5,6,7,8],2),[[0, 1], [1, 2], [3, 4], [4, 5], [6, 7], [7, 8], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]])
        
    def test9_permuation_for_three_size_boat(self):
        self.assertEqual(self.b.permutation_list([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],3),[[0, 1, 2], [1, 2, 3], [4, 5, 6], [5, 6, 7], [8, 9, 10], [9, 10, 11], [12, 13, 14], [13, 14, 15], [0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12], [5, 9, 13], [6, 10, 14], [7, 11, 15]])
    def test10_permutation_for_four_size_boat(self):
        self.assertEqual(self.b.permutation_list([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],4), [[0, 1, 2, 3], [1, 2, 3, 4], [5, 6, 7, 8], [6, 7, 8, 9], [10, 11, 12, 13], [11, 12, 13, 14], [15, 16, 17, 18], [16, 17, 18, 19], [20, 21, 22, 23], [21, 22, 23, 24], [0, 5, 10, 15], [1, 6, 11, 16], [2, 7, 12, 17], [3, 8, 13, 18], [4, 9, 14, 19], [5, 10, 15, 20], [6, 11, 16, 21], [7, 12, 17, 22], [8, 13, 18, 23], [9, 14, 19, 24]])
        
    def test11_permutation_for_five_size_boat(self):
        self.assertEqual(self.b.permutation_list([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35],5), [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [13, 14, 15, 16, 17], [18, 19, 20, 21, 22], [19, 20, 21, 22, 23], [24, 25, 26, 27, 28], [25, 26, 27, 28, 29], [30, 31, 32, 33, 34], [31, 32, 33, 34, 35], [0, 6, 12, 18, 24], [1, 7, 13, 19, 24], [2, 8, 14, 20, 24], [3, 9, 15, 21, 24], [4, 10, 16, 22, 24], [5, 11, 17, 23, 24], [6, 12, 18, 24, 24], [7, 13, 19, 25, 24], [8, 14, 20, 26, 24], [9, 15, 21, 27, 24], [10, 16, 22, 28, 24], [11, 17, 23, 29, 24]])
        
    def test12_list_remover(self):
        pass
    
    def test13_print_the_board(self):
        pass
    
    def test14_add_the_boat(self):
        pass
    
    def test15_make_full_number_list(self):
        pass
    
    
    
    

if __name__ == '__main__':
    unittest.main()