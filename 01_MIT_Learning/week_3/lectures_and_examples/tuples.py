

def get_data(data):
    nums = ()
    words = ()

    for i in data:
        nums = nums + (i[0],)      # use comma at end to signify tuple
        if i[1] not in words:
            words = words + (i[1],)

    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


(small, large, words) = get_data((
                    (1, 'mine'),    # t[0], t[1]
                    (3, 'yours'),
                    (5, 'ours'),
                    (7, 'mine')
                    ))

data = ((
        (1, 'mine'),    # t[0], t[1]
        (3, 'yours'),
        (5, 'ours'),
        (7, 'mine')
       ))




print (small)
print (large)
print (words)
print ()
print (get_data(data))


# test = get_data((
#                     (1, 'mine'),
#                     (3, 'yours'),
#                     (5, 'ours'),
#                     (7, 'mine')
#                     ))

# _________________________-
# x = (1, 2, (3, 'John', 4), 'Hi')

# print (x[0])
# print (x[2])
# print (x[-1])

# print (x[2][2])
# print (x[2][-1])
# print (x[-1][-1])
# # print (x[-1][2])      # out of range

# print (x[0:1])
# print (x[0:-1])
# print (len(x))

# print (2 in x)
# print (3 in x)
# print (x[0] == 8)