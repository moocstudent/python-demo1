def doors(n):
  # 声明doors的初始化都为closed
  allDoors = []
  for i in range(0, n):
    allDoors.append("closed")
  # 声明第一名到最后一名学生的学号number，也就是门该按什么区间来进行状态变更
  for kid in range(1, n+1):
    # 因为更改门状态时，学号越大的学生，只更改equal或bigThan学号的门
    # 这里将内层range的初始使用kid-1，即对应了这个第一个应该被该学生修改状态的门
    # 而门有n个循环到n，步进则使用kid，即每按该学生学号进行门状态更改
    # 下面的if else都是对门的状态的变更，如果当时是关闭则打开，打开则关闭
    for door in range(kid-1, n, kid):
        if allDoors[door] == "closed":
          allDoors[door] = "open"
        else:
          allDoors[door] = "closed"

  count = 0
  # 计算门状态为open的门的数量
  for j in range(0, len(allDoors)):
    if allDoors[j] == "open":
      count+=1
  return count


if __name__ == '__main__':
    result = doors(8)
    print('result %s' % result)
