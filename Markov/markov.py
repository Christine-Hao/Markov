#Christine Yuanqing Hao
#ID:261053765

                                                 #Markov
import doctest
import random 

#Fucntion 1
# Do not form k-grams for the last k characters of the text.
def get_grams(text, k):
    """ (str, int) -> dict
    Returns a dictionary of k-grams as described above, using the input string
    text and the given positive integer k. 
    >>> get_grams('gagggagaggcgagaaa', 2)
    {'ga': {'g': 4, 'a': 1}, 'ag': {'g': 2, 'a': 2}, 'gg': {'g': 1, 'a': 1, 'c': 1}, 'gc': {'g': 1}, 'cg': {'a': 1}, 'aa': {'a': 1}}
    
    >>> get_grams("She sells sea shells by the sea shore.", 1)
    {'S': {'h': 1}, 'h': {'e': 3, 'o': 1}, 'e': {' ': 2, 'l': 2, 'a': 2, '.': 1}, ' ': {'s': 5, 'b': 1, 't': 1}, 's': {'e': 3, ' ': 2, 'h': 2}, 'l': {'l': 2, 's': 2}, 'a': {' ': 2}, 'b': {'y': 1}, 'y': {' ': 1}, 't': {'h': 1}, 'o': {'r': 1}, 'r': {'e': 1}}
    
    >>> get_grams('aaoaaobo', 3)
    {'aao': {'a': 1, 'b': 1}, 'aoa': {'a': 1}, 'oaa': {'o': 1}, 'aob': {'o': 1}}
    
    >>> get_grams('I, i, ', 2)
    {'I,': {' ': 1}, ', ': {'i': 1}, ' i': {',': 1}, 'i,': {' ': 1}}
    
    >>> get_grams('aasd', 2)
    {'aa': {'s': 1}, 'as': {'d': 1}}
    
    get_grams('sdaaa', 2)
    {'sd': {'a': 1}, 'da': {'a': 1}, 'aa': {'a': 1}}
    """
    
    final_dict = {} #create an empty dictionnary 

    end = len(text)-k#To avoid looping through the last k characters 
    
    i = 0
    #To loop thorugh the text except the last k characters 
    while i < end: 
        key = text[i:i+k] #to find one possible key 
        
        if key not in final_dict: #If the key is not contained already in the fianl_dict
            final_dict[key] = {} #put the key in the final dictionnary
            
            
        subkey = text[i+k] #find what occurs next to the key 
        
        if subkey in final_dict[key]: #If the subkey is already contained in the dict of the given key 
            final_dict[key][subkey] += 1 #Add one occurence to the subkey
        
        else: # If the subkey is not contained in the dict of the given key 
            final_dict[key][subkey] = 1 #create a new subkey and paire it with the value of 1 (its occurence)
        i+=1
    return final_dict
            


#Function 2
# Takes two k-gram dictionaries and combines them, returning the
# new combined dictionary. All key-value pairs from both dictionaries should be added into the new
# dictionary. If a key exists in both dictionaries, then combine the values (if the two values are
# dictionaries, then combine the dictionaries as above; if the two values are integers, then add them
# together). The input dictionaries should not be modified.
    
def combine_grams(grams1, grams2):
    """ (dict, dict) -> dict
    Takes two k-gram dictionaries and combines them, returning the
    new combined dictionary.
    
    >>> combine_grams({'a': {'b': 3, 'c': 9}, 'b': {'a': 10}}, {'b': {'a': 5, 'c': 5}, 'c': {'d': 4}})
    {'a': {'b': 3, 'c': 9}, 'b': {'a': 15, 'c': 5}, 'c': {'d': 4}}
    
    >>> combine_grams({'a': {'b': 3, 'c': 9}}, {'c': {'d': 4}})
    {'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}
    
    #To verify that I don't modify the inputs 
    >>> grams1 = {'a': {'b': 3, 'c': 9}, 'b': {'a': 10}}
    >>> grams2 = {'b': {'a': 5, 'c': 5}, 'c': {'d': 4}}
    >>> x = combine_grams(grams1, grams2)
    >>> print(x)
    {'a': {'b': 3, 'c': 9}, 'b': {'a': 15, 'c': 5}, 'c': {'d': 4}}
    >>> x['b'] = 4
    >>> print(x)
    {'a': {'b': 3, 'c': 9}, 'b': 4, 'c': {'d': 4}}
    >>> print(grams1)
    {'a': {'b': 3, 'c': 9}, 'b': {'a': 10}}
    >>> print(grams2)
    {'b': {'a': 5, 'c': 5}, 'c': {'d': 4}}
    
    >>> combine_grams({'d': {'b': 3, 'c': 9}}, {'d': {'b': 2}})
    {'d': {'b': 5, 'c': 9}}
    
    >>> x = get_grams('aasd', 2)
    >>> y = get_grams('sdaaa', 2)
    >>> combine_grams(x, y)
    {'aa': {'s': 1, 'a': 1}, 'as': {'d': 1}, 'sd': {'a': 1}, 'da': {'a': 1}}
    
    """
    
    #deep copy grams1
    keys = list(grams1.keys()) #retrive all the keys in grams1 
    final_dict = dict.fromkeys(keys) #create a new dictionnary with retrieved keys 
    
    for key in grams1: #loop through every elements in grams 1
        sub_keys = list(grams1[key].keys()) #retrieve all the sub_keys in grams1[key]
        final_dict[key] = dict.fromkeys(sub_keys) #create a new sub dictionnary in final_dict[key]
        
        for sub_key in grams1[key]: #loop through sub_dict in grams1[key]
            final_dict[key][sub_key] = grams1[key][sub_key] #pair the correspondent value to the subkey 
    
    #compare in grams2 
    for key in grams2:
        if key in final_dict: #if the key in grams 2 is in the final dict
            for sub_key in grams2[key]: #loop through subkeys in each of the keys in grams2
                if sub_key in final_dict[key]:
                    final_dict[key][sub_key] += grams2[key][sub_key] #add the occurrence of each of the same subkey
                else:
                    final_dict[key][sub_key] = grams2[key][sub_key] #create a subkey paired with its corrurence in grams 2
                    
                
        else: #if the key in grams 2 is not in the final dict
            final_dict[key] = {}
            for sub_key in grams2[key]: #loop through subkeys in grams 2 and add then to the final dict[key]
                final_dict[key][sub_key] = grams2[key][sub_key]           
        
    return final_dict
    
    
    
    
#Function 3
# This function will 
# Note: When opening the files, use the keyword argument encoding='utf-8', which tells Python to
# interpret the text file using a particular character encoding. Otherwise, Python may use a different
# encoding depending on your OS which can result in errors.
# The following example uses files provided to you along with this PDF.

def get_grams_from_files(filenames, k):
    """ (list, int) -> dict
    Takes a list of strings filenames and a positive integer k, reads in
    the files at the given filenames, and creates a k-grams dictionary for each file.
    It will combine all such k-grams dictionaries and return the combined dictionary.
    >>> grams = get_grams_from_files(['raven.txt'], 4)
    >>> len(grams)
    3023
    >>> grams['drea']
    {'r': 1, 'm': 4}
    
    >>> grams = get_grams_from_files(['beowulf.txt'], 2)
    >>> len(grams)
    2255
    >>> grams['PR']
    {'E': 2, 'O': 5, 'I': 1}
    
    >>> grams = get_grams_from_files(['holmes.txt'], 1)
    >>> len(grams)
    96
    
    >>> grams = get_grams_from_files(['beowulf.txt'], 1)
    >>> len(grams)
    107
    >>> grams['\ufeff']
    {'P': 1}
    
    >>> grams = get_grams_from_files(['raven.txt'], 5)
    >>> len(grams)
    3960
    >>> grams['Once ']
    {'u': 1}
    
    >>> grams = get_grams_from_files(['raven.txt'], 2)
    >>> len(grams)
    516
    >>> grams['On']
    {'c': 1, 'l': 1, ' ': 4}
    
    """
    
    dict_in_lst = []
    
    for text in filenames: #loop through every text
        f = open(text, 'r', encoding='utf-8')
        text = f.read()
        sub_dict = get_grams(text, k) #get grams for the text
        f.close()
        dict_in_lst.append(sub_dict) #append the obtained dict to the list 
    
    final_dict = {}
    for i in range(len(dict_in_lst)):
        final_dict = combine_grams(final_dict, dict_in_lst[i]) #combine all the dictionnaries together 
        
    return final_dict



#Function 4
 
def generate_next_char(grams, cur_gram):
    """ (dict, str) -> str 
    Returns the prediction of the next character
    >>> random.seed(9001)
    >>> generate_next_char({'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}, 'a')
    'b'
    >>> generate_next_char({'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}, 'a')
    'c'
    >>> random.seed(1337)
    >>> grams = get_grams_from_files(['raven.txt'], 4)
    >>> generate_next_char(grams, 'drea')
    'm'
    
    >>> random.seed(2001)
    >>> grams = get_grams_from_files(['raven.txt'], 5)
    >>> generate_next_char(grams, 'Once ')
    'u'
    
    >>> random.seed(2002)
    >>> grams = get_grams_from_files(['raven.txt'], 5)
    >>> generate_next_char(grams, 'Once ')
    'u'
    
    >>> random.seed(2002)
    >>> grams = get_grams_from_files(['raven.txt'], 2)
    >>> generate_next_char(grams, 'On')
    ' '
    
    
    #Error raising
    >>> generate_next_char({'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}, 'p')
    Traceback (most recent call last):
    AssertionError: The chosen combination does not exist in the previous text
    
    >>> generate_next_char({'a': {'b': 3, 'c': 9}, 'c': {'d': 4}}, 'll')
    Traceback (most recent call last):
    AssertionError: The chosen combination has a diffrent number of characters than the k-grams in the dictionary.
    
    """
    #Raising errors
    if len(grams) == 0:#if the given gram(dict) has no elements inside
        raise AssertionError('The given dictionnary(grams) is empty')
        
    keys_in_grams = list(grams.keys()) #To have a list of keys
    if len(cur_gram) != len(keys_in_grams[0]): #Ifhe chosen combination has a diffrent number of characters than the k-grams in the dictionary
        raise AssertionError("The chosen combination has a diffrent number of characters than the k-grams in the dictionary.")

    
    elif cur_gram not in keys_in_grams: #If the chosen combination does not exist in the previous text
        raise AssertionError("The chosen combination does not exist in the previous text")
    
    dict_cur_grams = grams[cur_gram] #accessing the sub dictionnary 
    total_occurrence = 0 #the total occurence of the chosen curgrams
    
    #list 1 : list of items (that follows cur_gram) to be chosen from at random 
    choices = list(dict_cur_grams)
    
    for key in dict_cur_grams: #to determine the number of total occurence of the character
        total_occurrence += dict_cur_grams[key]
    
    weight = [] #list 2 : probability of occurence of the character next to cur_grams 
    for key in dict_cur_grams: #to determine the probability of a character to occur next to the cur_gram
        probability = dict_cur_grams[key]/total_occurrence
        weight.append(probability)
        
    prediction = random.choices(choices, weight) #to determine the prediction 
    
    return prediction[0]
    
    

#Function 5

# This function generates a piece of text of length n (a
# positive integer), given the k-grams dictionary grams, the positive integer k, and the starting kgram start_gram. That is, starting with the start_gram, continue generating characters until you
# have a text of length k. Then, cut off the text at the last empty whitespace (space or newline
# character), and return the text. (Cutting off the text may result in the text being a few characters
# smaller than n, but that’s OK.)

def generate_text(grams, start_gram, k, n):
    """ (dict, str, int, int) -> str

    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt'], 5)
    >>> generate_text(grams, "Once upon", 5, 200)
    Once upon the tempest tossed this desert land enchanted—tell me—tell me, I implore—
    Quoth the Raven, thou,” I cried, “thy God we both adore—
    Tell the floor.
    "'Tis soul with my head at ease
    
    >>> random.seed(200)
    >>> grams = get_grams_from_files(['raven.txt'], 10)
    >>> generate_text(grams, 'Some late ', 10, 100)
    'Some late visitor entreating entrance at my chamber door—\nBird or beast upon the velvet sinking, I'
    
    >>> random.seed(1975)
    >>> grams = get_grams_from_files(['raven.txt'], 9)
    >>> generate_text(grams, 'Nevermore ', 9, 50)
    'Nevermore.\n\n    And the Raven “Nevermore.”\n\n   '
    
    >>> random.seed(2001)
    >>> grams = get_grams_from_files(['holmes.txt'], 7)
    >>> generate_text(grams, 'Holmes ', 7, 50)
    'Holmes clapped the dog, which we were going'
    """
    if len(start_gram) > k: #slice the start grams at k characters
        start_gram = start_gram[:k]
    
    text = start_gram + generate_next_char(grams, start_gram) #generate the first character 
    while len(text) != n: #loop to have n characters in the text 
        text += generate_next_char(grams, text[len(text)-k:])


    remove_blank_index = len(text)
    for i in range(len(text)-1, -1, -1): #loop from the end of the text and find teh first occurence of a space or next line
        if text[i] == ' ' or text[i] == '\n':
            remove_blank_index = i #to obtain the index of the space
            break 
        
        
    text = text[0:remove_blank_index] #slicing the text at the index of the whitespace 
        
    return text 
        

#Function 6
    
#  This function takes a string of text corrupted_text,
# which is a portion of text that has been corrupted. A corrupted text is one where certain characters have been replaced with a certain character (the error_char character). Given a dictionary
# of k-grams grams and integer k, we must fill in the corrupted characters by using the predictions
# of our model. That is, we must give to our model the k-gram preceding each corrupted character,
# and replace said character by the model’s predicted next character. The repaired string will then
# be returned.
# If the preceding k-gram does not exist in our dictionary, then keep the corrupted character as is in
# the string.

def repair_text(corrupted_text, error_char, grams, k):
    """(str, str, dict, int) -> str
    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt', 'beowulf.txt'], 5)
    >>> repair_text('it was th~ bes~ of tim~s, i~ was ~he wo~st of~times', '~', grams, 5)
    'it was the best of times, in was Bhe wolst of times'
    
    >>> random.seed(1330)
    >>> grams = get_grams_from_files(['raven.txt', 'beowulf.txt'], 5)
    >>> repair_text('I/love/you', '/', grams, 5)
    'I/love/you'
    
    >>> random.seed(2001)
    >>> grams = get_grams_from_files(['raven.txt'], 5)
    >>> repair_text('While I ponde*and weary* ~ The Raven * /\ never*****', '*', grams, 5)
    'While I ponderand weary, ~ The Raven o /\\ nevermore.'
    """
    
    final_text = corrupted_text 
    for i, character in enumerate(corrupted_text): #to loop through both carcacters and idex at the same time 
        if character == error_char:
            cur_gram = final_text[i-k:i] #the k charcater before '~'
            if cur_gram not in grams.keys(): #if the previous k characters is not in the dictionnary 
                continue
            replacement = generate_next_char(grams, cur_gram) #replace the corrupted text if the previre k charcaters are found 
            final_text = final_text[:i] + replacement + final_text[i+1:] #slice the final text and insert the replacement 
    
    return final_text 





    
    


