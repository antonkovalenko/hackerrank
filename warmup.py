def bigger_is_greater():
    """
    to solve the task:
    https://www.hackerrank.com/challenges/bigger-is-greater
    """
    testdata_filename = 'testdata/input01.txt'
    try:
        data_in_fh = open(testdata_filename, 'r')
    except IOError as e:
        print "Unable to open {:s} because: {:s}".format(testdata_filename, e.message)
        return

    line = data_in_fh.readline()
    number_of_testcases = int(line.rstrip())

    if number_of_testcases < 1 or number_of_testcases > pow(10, 5):
        #print "number of testcases={:d} for bigger_is_greater isn't within boundaries".format(number_of_testcases)
        return
    #print "have to handle {:d} testcases".format(number_of_testcases)
    testcases_handled = 0
    line = data_in_fh.readline()
    line = line.rstrip()
    while len(line) > 0:
        next_line = inc_string_lexically(line)
        #print "src line: {:s} handled line: {:s}".format(line, next_line)
        print next_line
        if testcases_handled == number_of_testcases:
            #print "Have analysed: {:d} testcases, exiting".format(testcases_handled)
            break
        testcases_handled += 1
        line = data_in_fh.readline()
        line = line.rstrip()
    return


def inc_string_lexically(src_line):
    """
    return a string that is lexically next one after the src_line
    https://www.hackerrank.com/challenges/bigger-is-greater
    :param src_line:
    :return str:
    """
    result_line = "no answer"
    for i in sorted(range(len(src_line)), reverse=True):
        if i == 0:
            break
        if src_line[i-1] < src_line[i]:
            #print "swapping at: {:d} tail: {:s}".format(i, src_line[i-1:])
            result_line = swap_letters(src_line, i-1, get_closest_greater_letter(src_line, src_line[i-1], i-1))
            head = result_line[:i]
            tail = ''.join(sorted(result_line[i:]))
            return head + tail
    return result_line


def get_closest_greater_letter(l_string, l_char, l_lookup_start_idx):
    """
    :param l_string: string containing characters that are supposed to be looked up
    :param l_char: character we have to find a greater character for
    :param l_lookup_start_idx: position to start out search process from
    :return int: returns an index of the character in l_string that is greater than l_char, but with the smallest difference
    in comparison to all the other characters
    :raise Exception:
    """
    if len(l_char) > 1:
        raise TypeError("l_char has to be 1 character long")
    if l_lookup_start_idx >= len(l_string):
        raise Exception("l_lookup_start_idx must be less than length of l_string")
    closest_letter = None
    for i in range(l_lookup_start_idx, len(l_string)):
        if ord(l_string[i]) <= ord(l_char):
            continue
        if (closest_letter is None) or (ord(l_string[i]) - ord(l_char)) < (ord(l_string[closest_letter]) - ord(l_char)):
            closest_letter = i
    return closest_letter


def swap_letters(string_to_mod, index_a, index_b):
    string_result = str()
    symbol_at_index_a = string_to_mod[index_a]
    symbol_at_index_b = string_to_mod[index_b]
    for k in range(len(string_to_mod)):
        current_symbol = string_to_mod[k]
        if k == index_a:
            current_symbol = symbol_at_index_b
        if k == index_b:
            current_symbol = symbol_at_index_a
        string_result += current_symbol
    #print "swap: from {:s} {:d} {:d} to {:s}".format(string_to_mod, index_a, index_b, string_result)
    return string_result