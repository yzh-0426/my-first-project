# 输入任意多个数字
numbers = list(map(int, input("请输入多个整数（空格分隔）：").split()))
numbers.sort()
print(f"从小到大为：{numbers}")
