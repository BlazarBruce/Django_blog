from django.test import TestCase

# Create your tests here.
# 参考链接; https://blog.csdn.net/lyq_12/article/details/81260427
li = [[1, 0, -1], [2], [3], [-1, 0, 1]]
# l2 = []
# l3 = []
# rst = [l2.append(item) if item not in l2 and len(item)==1
#        else l3.append(item) for item in li if item not in l3]
# print(l2)
# # list_temp = list(set(rst))
# q = [x if x%3==0 else -x for x in range(1,101)]
#
# t1 = [1, 0, -1]
# t2 = [1, 0, -1]
# print(sorted(t1))
# print(sorted(t2))


def filter(alist):
    "去重复函数"
    rst_liat = []
    sort_list = []
    for i in range(len(alist)):
        if alist[i] not in rst_liat:
            temp = sorted(alist[i])
            if temp not in sort_list:
                sort_list.append(temp)
                rst_liat.append(alist[i])
    return rst_liat

rst = filter(li)
print(rst)


