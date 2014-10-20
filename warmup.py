"""
to solve the task:
https://www.hackerrank.com/challenges/bigger-is-greater
"""
def bigger_is_greater():

    def gen_all_letter_combinations(str_src):
        result = list()
        for i in range(len(str_src)):
            for j in range(len(str_src)):
                if i == j:
                    continue
                result.append(swap_letters(str_src, i, j))
        return result

    testdata_filename = 'testdata/bigger_is_greater.txt'
    try:
        data_in_fh = open(testdata_filename, 'r')
    except IOError as e:
        print "Unable to open {:s} because: {:s}".format(testdata_filename, e.message)
        return

    line = data_in_fh.readline()
    number_of_testcases = int(line.rstrip())

    if number_of_testcases < 1 or number_of_testcases > pow(10, 5):
        print "number of testcases={:d} for bigger_is_greater isn't within boundaries".format(number_of_testcases)
        return
    print "have to handle {:d} testcases".format(number_of_testcases)
    testcases_handled = 0
    while len(line) > 0:
        line = data_in_fh.readline()
        line = line.rstrip()
        next_line = None
        print "src line: {:s} handled line: {:s}".format(line, next_line)
        print gen_all_letter_combinations(line)
        if testcases_handled == number_of_testcases:
            print "Have analysed: {:d} testcases, exiting".format(testcases_handled)
            break
        testcases_handled += 1

    return


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
    print "swap: from {:s} {:d} {:d} to {:s}".format(string_to_mod, index_a, index_b, string_result)
    return string_result