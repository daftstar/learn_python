# Implement a function that meets the specifications below.


def max_val(t):
    """ t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t
    e.g. find the largest integer in the entire t """
    # https://stackoverflow.com/questions/10823877/what-is-the-fastest-way-to-flatten-arbitrarily-nested-lists-in-python
    def flatten_helper(obj_to_review):
        for i in obj_to_review:
            if isinstance(i, (list, tuple)):
                for j in flatten_helper(i):
                    # https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
                    yield j
            else:
                yield i

    flat_list = (list(flatten_helper(t)))
    return max(flat_list)


# t = [99, 1, 800, (55, 98, 57), 100, [300, 400, 500], 101, 18, 601]
# t = (5, (1, 2), [[1], [2]])
t = (5, (1, 2), [[1], [9]])


print (max_val(t))
