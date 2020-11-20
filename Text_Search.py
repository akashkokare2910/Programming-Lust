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

# Check if string 'at' is found in file 'search.txt'
if check_if_string_in_file('search.txt', 'is'):
    print('Yes, string found in file')
else:
    print('Oops, String not found in file')

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

matched_lines = search_string_in_file('search.txt', 'is')
print('Total Matched lines in the file --> ', len(matched_lines))
for elem in matched_lines:
    print('Line Number is --> ', elem[0], ' :: Line = ', elem[1])

