# f =open("./look_texts", "r")
# str = f.readlines()
# # print(str)
# url_list = []
# for s in str:
#     url_list.append(s.rstrip())
# print(url_list)

#
# url_list = []
# list = ["dsada", "", " ", "dasfs"]
# for s in list:
#     if s != "" and s != " ":
#         url_list.append(s.rstrip())
# print(url_list)

# def add(n, i):
#     return n + i
#
#
# def test():
#     for i in range(4):
#         yield i
#
#
# g = test()
#
# for n in [1, 10, 5]:
#     g = (add(n, i) for i in g)
#
# print(list(g))  # 结果是 [15, 16, 17, 18]
# l = ['da', 'fs', 3, 4]
# print(type(l[2]))
import time

get_time = time.strftime("%Y_%m_%d_%H_%M_%S")
print(get_time)


a = input("请输入需要循环的次数：")
a = int(a)
print(type(a))

