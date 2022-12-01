

v1='1'
v2='222'
v3='3'
tuple1=()
tuple1+= (v1,v2)
# tuple1+= (v2)

tuple2=()
tuple2+= (v1,v2)
# tuple2+= tuple(v2)

arr=[]
arr.append(tuple1)
arr.append(tuple2)
print(arr)