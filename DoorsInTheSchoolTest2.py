def doors(n):
    return int(n**.5)
    # return sum([1 for i in range(1, n + 1) if (i ** 0.5).is_integer()])


if __name__ == '__main__':
    result = doors(8)
    print('result %s' % result)
