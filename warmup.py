"""
to solve the task:
https://www.hackerrank.com/challenges/bigger-is-greater
"""
def bigger_is_greater():
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
        line = line.rstrip()
        next_line = None
        for i in range(len(line)):

        print "src line: {:s} handled line: {:s}".format(line, next_line)
        line = data_in_fh.readline()
        if testcases_handled == number_of_testcases:
            print "Have analysed: {:d} testcases, exiting".format(testcases_handled)
            break
        testcases_handled += 1

    return
