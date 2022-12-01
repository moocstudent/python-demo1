# def fb(n):
def nth_fib(n):
    print("just in :",n)
    if n <= 2:
        print("return :",n)
        return n - 1
    return nth_fib(n - 1) + nth_fib(n - 2)
    # 9 8
    #

if __name__ == '__main__':
    print(nth_fib(10))
