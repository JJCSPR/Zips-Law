"""
    Jorge Juan Cruz Serralles
"""
def normalize_text(text):
    """Return copy of text in lowercase with punctuation removed.

    Parameters:
    text: str - text to normalize

    Return: str which is copy of text converted to lowercase with
    punctuation (the chars in string.punctuation) removed.
    """
    from string import punctuation
    newText = text.lower()
    return "".join(letter for letter in newText if letter not in punctuation)
def mk_word2count(text):
    """Return a dictionary mapping words in text to their count in text. Be sure to account for newlines in the text!

    Parameters:
    text: str - string containing words separated by spaces

    Return: char_dict: dict - dictionary whose keys are words and
    associated values are the number of times the word appears in text
    """
    splitUp = text.split()
    my_dict = {}
    for word in splitUp:
    	if word in my_dict.keys():
    		my_dict[word] += 1
    	elif word not in my_dict.keys():
    		my_dict[word] = 1
    return my_dict
def dict2tuples(word_dict, key=None):
    """Convert a str:int dictionary to a sorted list of (str, int) tuples, optionally with a key

    Parameters:
    word_dict: dict[str -> int]
    key: (optional) a key function to extract the element of the tuples by which to sort

    Return: a list[(str, int)], sorted in descending order, optionally by a key
    """
    return sorted([(k, v) for k, v in word_dict.items()], key=key, reverse=True)
def normalize_counts(tuples, max_value=100):
    """Normalize the second values in tuples.

    Parameters:
    tuples: Sequence[(str, int)] - (word, count) tuples
    max_value: int - the max value of the normalized counts (min value is 0)

    Return: Sequence[(str, int)] with same first elements as tuples
    but whose second elements are normalized to the range 0 to
    max_value.
    """
    coeff = max_value / max([i[1] for i in tuples])
    return [(word, int(num*coeff)) for word, num in tuples]
def word_hist(bar_list):
    """Create a text-based bar chart from bar_list.

    Parameters:
    bar_list: Sequence[(str, int)] - (label, length) tuples

    Return: list[str] with one line per tuple in bar_list. Each line --
    a str in the returned list -- has the right-aligned label, a |
    character, then length Xs
    """
    max_len = len(max(bar_list, key=lambda t: len(t[0]))[0])
    return ["{word} | {bars}".format(word=w.rjust(max_len), bars="X"*length)
            for w, length in bar_list]
def main(args):
    # code intended to be executed when run as a script
    import os.path
    file_name = args[1] if len(args) > 1 else None
    max_bar_length = int(args[2]) if len(args) > 2 else None
    number_of_lines = int(args[3]) if len(args) > 3 else None

    # Keeps asking the user for a file name if they did not provide one initially, will repeat until it is valid.
    while file_name is None: 
        file_name = input("What is the file's name?")
        if not os.path.exists(file_name):
            file_name = None
            print("Input a valid file name, s'il vous plait.")

    # Exits the function if the path does not exist.
    if not os.path.exists(file_name): 
        exit()

    # Reads the file.
    file = open(file_name, 'r') 

    # Slurps in the text in the file.
    text = file.read()

    # Normalizes the text that we have just slurped in.
    normalized_text = normalize_text(text)

    # Makes a dictionary with Words: Counts mapped.
    frequency_dict = mk_word2count(normalized_text)

    #Converts the dictionary into a list of tuples
    tuples = dict2tuples(frequency_dict)

    #Sorts the tuples i descending orderby using the sorted() method.
    sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse = True)

    #applies normalized_counts on the tuple
    normalized_tuples = normalize_counts(sorted_tuples, max_bar_length) if max_bar_length is not None else normalize_counts(sorted_tuples)
    
    # Generates a histogram when given the normalized tuples
    histogram = word_hist(normalized_tuples)

    # Prints a certain number of lines if given a value for number_of_lines, prints all if else
    if number_of_lines is not None:
        for x in range(number_of_lines):
            print(histogram[x])
    else:
        for line in histogram:
            print(line)

    file.close()
if __name__=="__main__":
    import sys
    main(sys.argv)