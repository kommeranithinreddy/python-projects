def outer(num):
    def inner(new_num):
        print(num * new_num) # no need to use extra alignment
    return inner

multi_by_5 = outer(5)
multi_by_5(10)
multi_by_5(9)
multi_by_5(8)
