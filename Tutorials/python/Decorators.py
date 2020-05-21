def printMatrix(fn):
    def inner(*args):
        fn(*args)
        for arr in args:
            if type(arr) == list:
                print(arr)
    return inner

def printShape(fn):
    def outter(*args):
        if len(args) < 1: return
        print(len(args), ' x ', len(args[0]))
        fn(*args)
        return
    return outter


@printShape
@printMatrix
def printA(*args):
    return

printA([1,2,3], [4,5,6], [7,8,9])