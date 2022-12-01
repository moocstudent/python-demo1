# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def largest(n, xs):
    l = len(xs)
    # 遍历所有数组元素
    for i in range(l):
        if i == n:
            break
        # Last i elements are already in place
        for j in range(0, l - i - 1):
            left = xs[j]
            right = xs[j + 1]
            if left > right:
                temp = right
                xs[j + 1] = left
                xs[j] = temp
            print('left: {left}, right: {right}'.format(left=left, right=right))
    print(xs)
    return xs[l-n:l]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = largest(2, [9, 1, 50, 22, 3, 13, 2, 63, 5])
    print('result %s' % result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
