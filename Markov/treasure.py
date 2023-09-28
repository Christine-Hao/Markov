#Clycine Yuaniqng Hao
#ID:261053765

                                                #Treasure Hunt
import doctest



#Helper function 1
def write_strings_to_file(string_list, filename):
    """(list<str>,str) -> NoneType 
    Writes each string from the string_list onto a new line in the file at the
    given name
    
    >>> write_strings_to_file(['2','...','p'], 'random_map.txt')
    >>> f = open('random_map.txt', 'r')
    >>> text_list = []
    >>> for line in f:
            text_list.append(line.strip())
    >>> f.close()
    >>> text_list == ['2','...','p']
    True
    
    >>> write_strings_to_file(['2','%','p'], 'random_map1.txt')
    >>> f = open('random_map1.txt', 'r')
    >>> text_list = []
    >>> for line in f:
            text_list.append(line.strip())
    >>> f.close()
    >>> text_list == ['2','%','p']
    True
    
    >>> write_strings_to_file(['<*123','.....','|*>>>'], 'random_map2.txt')
    >>> f = open('random_map2.txt', 'r')
    >>> text_list = []
    >>> for line in f:
            text_list.append(line.strip())
    >>> f.close()
    >>> text_list == ['<*123','.....','|*>>>']
    True
    
    """
    fobj = open(filename, 'w') #open a file of the given name
    characters = '\n'.join(string_list) #join the characters together 
    fobj.write(characters)
    fobj.close() #CLOSE THE FILEEE
    
    
#Function 1
# Opens the treasure map at that filename and loads the treasure map into a list of lists,
#then returns said list of lists.
# You can assume that the file will exist. Note that the treasure map could have any number
# of rows and columns.
# If there is any issue with the format of the file (e.g., it is not a matrix, or contains any invalid
# characters), then raise an AssertionError with an appropriate error message. Note that an 'X' in
# a file is valid.
def load_treasure_map(filename):
    """(str) -> list
    Returns the list of lists(matrix) that represent the elements in the given file
    Raise an AssertionError with an appropriate error message, if there is any issue with the
    format of the file (e.g., it is not a matrix, or contains any invalid
    characters)
    >>> load_treasure_map('map0.txt')
    [['>', '>', '>', 'v', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'v', '.', '.', '.', '<', '<', '.'], ['.', '.', '.', 'v', '.', '.', '.', '.', '.', '.'], ['v', '.', '.', 'v', '.', '.', '.', '.', '^', '.'], ['v', '.', '.', '>', '>', '*', '.', '.', '^', '.'], ['v', '.', '.', '.', '.', '.', '.', '.', '^', '.']]
    
    >>> write_strings_to_file(['<*123','.....','|*>>>'], 'random_map2.txt')
    >>> load_treasure_map('random_map2.txt')
    [['<', '*', '1', '2', '3'], ['.', '.', '.', '.', '.'], ['|', '*', '>', '>', '>']]
    
    >>> write_strings_to_file(['2','...','p'], 'random_map.txt')
    >>> load_treasure_map('random_map.txt')
    Traceback (most recent call last):
    AssertionError: The text cannot be returned as a matrix
    
    >>> write_strings_to_file(['2','%','p'], 'random_map1.txt')
    >>> load_treasure_map('random_map1.txt')
    Traceback (most recent call last):
    AssertionError: The file conatains an invalid character
    
    """
    accepted_characters = ['.', '^', '>', '<', 'v', 'X', '*', '|', '0', '1', '2', '3', '4'
                           '5', '6', '7', '8', '9']
    fobj = open(filename, 'r')
     
    matrix = []   #the final matrix 
    for line in fobj:
        line = line.strip()
        sublist = [] #each sublist in the the final matrix 
        for element in line:
            sublist.append(element)
        matrix.append(sublist)
    
    fobj.close()
    
    #To raise exceptions
    standard_length = len(matrix[0])
    for elements in matrix:
        #1) the file is not a matrix
        if len(elements) != standard_length:
            raise AssertionError("The text cannot be returned as a matrix")
        #2) If the files conatains invalid characters
        for char in elements:
            if char not in accepted_characters:
                raise AssertionError("The file conatains an invalid character")
            
    return matrix



#Function 2
#  Takes as inputs a list of lists corresponding to a
# treasure map and a string corresponding to a filename. Writes the treasure map to a file at the
# given filename, with a newline after each row of the map. Does not return anything.
#
def write_treasure_map(treasure_map, filename):
    """(list, str) -> NoneType
    Writes the treasure map to a file at the
    given filename, with a newline after each row of the map.
    >>> my_map = load_treasure_map('map0.txt')
    >>> write_treasure_map(my_map, 'new_map.txt')
    >>> my_map2 = load_treasure_map('new_map.txt')
    >>> my_map == my_map2
    True
    
#My own examples 
    >>> my_map = load_treasure_map('map8.txt')
    >>> write_treasure_map(my_map, 'new_map.txt')
    >>> my_map2 = load_treasure_map('new_map.txt')
    >>> my_map == my_map2
    True
    
    >>> my_map = load_treasure_map('map1.txt')
    >>> write_treasure_map(my_map, 'new_map.txt')
    >>> my_map2 = load_treasure_map('new_map.txt')
    >>> my_map == my_map2
    True

    >>> write_strings_to_file([">>>v..","...>>v","......"], "test_map_fxn2.txt")
    >>> my_map = load_treasure_map('test_map_fxn2.txt')
    >>> write_treasure_map(my_map, 'new_map.txt')
    >>> my_map2 = load_treasure_map('new_map.txt')
    >>> my_map == my_map2
    True
    
    """
#Open the file in mode "write"
    fobj = open(filename, 'w')

#Loop through each sublist, join each element together and go to the
    #next line when a sublist ends
    for sublist in treasure_map:
        characters = ''.join(sublist)
        fobj.write(characters + '\n')
        
    fobj.close()
    


#Function 3
#Takes as inputs a string corresponding to a filename, and
# two non-negative integers representing a row and column index. Reads in the map at the given
# filename, inserts an X into the given row and column position, then saves the map to a new file
# with 'new_' prepended to the given filename. You can assume the filename given to the function
# as argument refers to a file that exists.

def write_X_to_map(filename, row, col):
    """(str, int, int)-> NoneType 
    >>> write_X_to_map('map8.txt', 3, 6)
    >>> f = open('new_map8.txt', 'r')
    >>> for line in f: print(line.strip())
    >>v......v
    ..v......v
    ..v.......
    ..>>>>X...
    ..........
    ..^v^...<<
    >>> f.close()
    
    >>> write_X_to_map('map8.txt', 5, 1)
    >>> f = open('new_map8.txt', 'r')
    >>> for line in f: print(line.strip())
    >>v......v
    ..v......v
    ..v.......
    ..>>>>....
    ..........
    .X^v^...<<
    >>> f.close()
    
    >>> write_X_to_map('map1.txt', 5, 9)
    >>> f = open('new_map1.txt', 'r')
    >>> for line in f: print(line.strip())
    .>........
    ......<<..
    ..........
    .....>v...
    .^...^v...
    .^....>>8X
    >>> f.close()
    
    >>> write_X_to_map('map1.txt', 5, 20)
    Traceback (most recent call last):
    AssertionError: Accessed column out of range
    
    >>> write_X_to_map('map1.txt', 20, 20)
    Traceback (most recent call last):
    AssertionError: Accessed row out of range
    """
    
    my_list = load_treasure_map(filename)
    
    if row > len(my_list) - 1: #If the inputed row is not in the map 
        raise AssertionError('Accessed row out of range')
    
    if col > len(my_list[0]) -1 : #If the inputed column is not in the map 
        raise AssertionError('Accessed column out of range')
        
    my_list[row][col] = 'X' #wrtite X
    write_treasure_map(my_list, 'new_'+ filename)
    

#Function 4
# follow_trail(filename, treasure_map, start_row, start_col): Takes as inputs a string corresponding to a filename,
# a list of lists corresponding to a treasure map, and two non-negative integers
# representing a row and column index. Follows the trail in the given treasure map, starting at the
# given row and column index. Following the trail means to look at each character of the trail and
# # perform the appropriate operation for that character:
def follow_trail(filename, treasure_map, start_row, start_col):
    """(str, list, int, int)-> NoneType

    Follows the trail in the given treasure map, starting at the
    given row and column index.
    
    #Encoutering a '*'
    >>> my_map = load_treasure_map('map0.txt')
    >>> follow_trail('map0.txt', my_map, 0, 0)
    (1, 4, 5)
    
    #Encoutering a number 
    >>> my_map = load_treasure_map('map1.txt')
    >>> follow_trail('map1.txt', my_map, 4, 5)
    (8, 0, 0)
    
    #Encoutering a '.'
    >>> my_map = load_treasure_map('map8.txt')
    >>> follow_trail('map8.txt', my_map, 0, 0)
    (-1, 3, 6)
    
    >>> my_map = load_treasure_map('new_map8.txt')
    >>> my_map[3][6]
    'X'
    
    >>> write_strings_to_file(['>>v', 'v<<', '>>.'], "map3.txt")
    >>> my_map = load_treasure_map("map3.txt")
    >>> follow_trail("map3.txt", my_map, 4, 4)
    Traceback (most recent call last):
    AssertionError: Start point not found : We started from the ouside of the map.
    

#My own examples
    #Writing a 'X' to a '.' at the end od the matrix 
    >>> write_strings_to_file([">>>v..","...>>v","......"], "map6.txt")
    >>> my_map = load_treasure_map("map6.txt")
    >>> follow_trail("map6.txt", my_map, 0, 0)
    (-1, 2, 5)
    
    >>> my_map = load_treasure_map('new_map6.txt')
    >>> my_map[2][5]
    'X'
    
    
    #Encouterig a '|'
    >>> write_strings_to_file([">>>v..","...|>v","......"], "map7.txt")
    >>> my_map = load_treasure_map("map7.txt")
    >>> follow_trail("map7.txt", my_map, 0, 1)
    (6, 1, 3)
    
#AssertionError test
    #trail off the grid by above 
    >>> write_strings_to_file([">>>^..","...|>v","......"], "map9.txt")
    >>> my_map = load_treasure_map("map9.txt")
    >>> follow_trail("map9.txt", my_map, 0, 1)
    Traceback (most recent call last):
    AssertionError: The trail leads off the grid from above
    
    #Trail off the grid form the right 
    >>> write_strings_to_file([">>>>>>","...|>v","......"], "map2.txt")
    >>> my_map = load_treasure_map("map2.txt")
    >>> follow_trail("map2.txt", my_map, 0, 1)
    Traceback (most recent call last):
    AssertionError: The trail leads off the grid from the right
    
    #Invalid trail number
    >>> write_strings_to_file([">>>>>>","...|>v","......"], "mapa.txt")
    >>> my_map = load_treasure_map("mapa.txt")
    >>> follow_trail("mapa.txt", my_map, 0, 1)
    Traceback (most recent call last):
    AssertionError: Invalid map number
    
    >>> write_strings_to_file(['>>v', 'v<<', '>>.'], "map3.txt")
    >>> my_map = load_treasure_map("map3.txt")
    >>> follow_trail("map3.txt", my_map, -1, 4)
    Traceback (most recent call last):
    AssertionError: Start point not found : We started from the ouside of the map.
    
    
    """
    total_elements_in_matrix = len(treasure_map) * len(treasure_map[0]) #total number of characters in the matrix 
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    if start_row > len(treasure_map) or start_col > len(treasure_map[0]) or start_row <0 or start_col<0: #If the index cannot be reached in the matrix
        raise AssertionError("Start point not found : We started from the ouside of the map.")
    
    map_number_without_txt = filename.strip('.txt') #to extract the map number 
    map_number = map_number_without_txt.strip('map') #same as above 
    lst_map_number = list(map_number)
    
    if len(lst_map_number) == 0: #If the map number is not present 
        raise AssertionError("Invalid map number")
    
    for element in lst_map_number: #loop through the numbers to see if there are invalid characters
        if element not in numbers:
            raise AssertionError("Invalid map number")
    map_number = int(map_number) #convert map number to an integer to do operations on it 
    
    loop_timer = 0 #loop timer to notify infinite loops 
    i = start_row
    j = start_col
    while i < len(treasure_map): #looping by rows 
        while j < len(treasure_map[0]): #looping by columns
            if treasure_map[i][j] == ">":
                j += 1
                if j >= len(treasure_map[0]): #if the trail goes beyond the first line of the map
                    raise AssertionError("The trail leads off the grid from the right")
                loop_timer += 1
                
                #If we have loop through every elements in the matrix and the loop continues,
                #it means that the map is infinite 
                if loop_timer > total_elements_in_matrix:
                    raise AssertionError("The map never ends.")
            
            elif treasure_map[i][j] == "v":#we are going down
                i += 1
                if i >= len(treasure_map): #if the trail goes beyond the last line of the map
                    raise AssertionError("The trail leads off the grid at the bottom")
                loop_timer += 1
                if loop_timer > total_elements_in_matrix: #If there is an infinite loop
                    raise AssertionError("The map never ends.")
                
            elif treasure_map[i][j] == "^": #we are going up
                i -= 1
                if i < 0: #if the trail goes above the first line of the map
                    raise AssertionError("The trail leads off the grid from above")
                loop_timer += 1
                if loop_timer > total_elements_in_matrix:
                    raise AssertionError("The map never ends.")
                
            elif treasure_map[i][j] == "<":#we are going to the left 
                j -= 1
                if j < 0: #if the trail goes before the first line of the map
                    raise AssertionError("The trail leads off the grid from the left")
                loop_timer += 1
                if loop_timer > total_elements_in_matrix: 
                    raise AssertionError("The map never ends.")
    
            elif treasure_map[i][j] == '.': #we are writting an X to the position of '.'
                write_X_to_map(filename, i, j)
                return (-1, i, j)
            
            elif treasure_map[i][j] == '*': #going to another map with map number + 1
                map_number += 1
                return (map_number, i, j)
            
            elif treasure_map[i][j] == '|':#going to another map with map number - 1
                map_number -= 1
                return (map_number, i, j)
            
            elif treasure_map[i][j] in numbers: #going to another map that has the same number as indicated 
                return (int(treasure_map[i][j]), 0, 0)
            


#Function 5
# find_treasure(start_map_num): Takes an integer between 0 and 9 as input. Loads the corresponding
# map file, and starts following the trail (at position 0, 0 of that file) as described above. Continues
# following the trail through other map files as needed. Places an 'X' at the conclusion of the trail and
# saves the updated treasure map to a new file with 'new_' prepended to the current map filename.
# Returns a tuple of the row and column index where the 'X' was placed in that file.
def find_treasure(start_map_num):
    """(int) -> tuple
    Returns a tuple of the row and column index where the 'X' was placed in that file.
    >>> find_treasure(0)
    (3, 6)
    >>> my_map = load_treasure_map('new_map8.txt')
    >>> my_map[3][6]
    'X'
    
    >>> find_treasure(1)
    (0, 0)
    >>> my_map = load_treasure_map('new_map1.txt')
    >>> my_map[0][0]
    'X'
    
    find_treasure(8)
    (3,6)
    >>> my_map = load_treasure_map('new_map8.txt')
    >>> my_map[3][6]
    'X'
    """
    
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    filename = 'map'+ str(start_map_num) + '.txt'
    my_list = load_treasure_map(filename)
    start = follow_trail(filename, my_list, 0, 0)
    
    #if we encouter a '.' at the beginning 
    if start[0] == -1:
        return (start[1], start[2])
    
    
    while start[0] != -1: #while we have not found the treasure yet, keep looping 
        new_filename = ''
        for letters in filename: #looping through elements in the filename and reconstruct a map
            if letters not in numbers:
                new_filename += letters
            else: #taking the new map's number 
                new_filename += str(start[0])
    
        my_list = load_treasure_map(new_filename) #reload the new treasure map 
        start = follow_trail(new_filename, my_list, start[1], start[2]) 

    
    return (start[1], start[2])
    




