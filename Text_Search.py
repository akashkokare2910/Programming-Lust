def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False
def search_string_in_file(file_name, string_to_search):

    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results
def search_multiple_strings_in_file(file_name, list_of_strings):
   
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results
def main():
    print('*** Check if a string exists in a file *** ')
    # Check if string 'is' is found in file 'sample.txt'
    if check_if_string_in_file('search.txt', 'is'):
        print('Yes, string found in file')
    else:
        print('Oops, String not found in file')
    print('### Search for a string in file & get all lines containing the string along with line numbers ###')
    matched_lines = search_string_in_file('search.txt', 'is')
    print('Total Matched lines : ', len(matched_lines))
    for elem in matched_lines:
        print('Line Number = ', elem[0], ' :: Line = ', elem[1])
    print('### Search for multiple strings in a file and get lines containing string along with line numbers ###')
    # search for given strings in the file 'sample.txt'
    matched_lines = search_multiple_strings_in_file('search.txt', ['is', 'what'])
    print('Total Matched lines in the file : ', len(matched_lines))
    for elem in matched_lines:
        print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])
if __name__ == '__main__':
    main()
