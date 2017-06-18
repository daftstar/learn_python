
def print_move(fr, to):
    """
    fr, to = strings
    """
    print ('move from: %s to %s' %(fr, to))


def towers(n, fr, to, spare):
    """
    n = integre
    fr, to, spare = strings
    """
    if n == 1:
        print_move(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)
        print ()


print (towers(3, "P1", "P2", "P3"))