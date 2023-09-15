import math

### 1. 正弦函数（sine）：可以使用math.sin()函数来计算正弦值。
angle = 45  # 角度（单位为度）
#sin Return the sine of x (measured in radians). 返回x的正弦值(以弧度为单位)。
sin_value = math.sin(math.radians(angle))  #radians 将角度转换为弧度 # Convert angle x from degrees to radians.
print(sin_value)


### 2. 余弦函数（cosine）：可以使用math.cos()函数来计算余弦值。
angle = 60  # 角度（单位为度）
#cos Return the cosine of x (measured in radians). 返回x的余弦值(以弧度为单位)。
cos_value = math.cos(math.radians(angle))  # 将角度转换为弧度
print(cos_value)


### 3. 正切函数（tangent）：可以使用math.tan()函数来计算正切值。
angle = 30  # 角度（单位为度）
#tan Return the tangent of x (measured in radians). 返回x的正切(以弧度测量)。
tan_value = math.tan(math.radians(angle))  # 将角度转换为弧度
print(tan_value)
