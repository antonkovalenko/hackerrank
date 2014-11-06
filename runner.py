import sys
import warmup

def main():
    if len(sys.argv) < 2:
        print "first parameter serves as a function name to call"
        return
    print "calling function: {:s}".format(sys.argv[1])
    fname = sys.argv[1]
    if not hasattr(warmup, fname):
        print "Unknown function: {:s}".format(fname)
        return
    f = getattr(warmup, fname)
    f()
    return


if __name__ == '__main__':
    #a = "hefg"
    #print a[3:]
    #print ord(a[3]) - ord(a[1])
    #print a[warmup.get_closest_greater_letter(a, 'g', 2)]
    #print sorted(range(len(a)), reverse=True)
    sys.exit(main())

