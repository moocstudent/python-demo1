import sympy as sp

#### 求导数
# 定义变量
x = sp.Symbol('x')

# 定义函数
f = x**2 + 2*x + 1

# 求导数
f_prime = sp.diff(f, x)

# 打印结果
print("函数f的导数为：", f_prime)


#### 求不定积分
# 定义变量
x = sp.Symbol('x')

# 定义函数
f = x**2 + 2*x + 1

# 求不定积分
f_integral = sp.integrate(f, x)

# 打印结果
print("函数f的不定积分为：", f_integral)


#### 求定积分
# 定义变量
x = sp.Symbol('x')

# 定义函数
f = x**2 + 2*x + 1

# 求定积分
f_def_integral = sp.integrate(f, (x, 0, 1))

# 打印结果
print("函数f在[0, 1]上的定积分为：", f_def_integral)