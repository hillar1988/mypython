import pandas as pd
def check(s):
    if len(str(s)) != 11:
        return  False
    elif len(str(s)) == 11 and str(s).strip().startswith('11') is True:
        return  False
    elif len(str(s)) == 11 and str(s).strip().startswith('12') is True:
        return  False
    elif len(str(s)) == 11 and str(s).strip().startswith('14') is True:
        return  False
    elif len(str(s)) == 11 and str(s).strip().startswith('16') is True:
        return  False
    elif len(str(s)) == 11 and str(s).strip().startswith('19') is True:
        return  False
    else:return True

ls = pd.DataFrame(pd.read_excel('duanxin.xlsx', header=None))
ls=ls.drop_duplicates([0])
print(ls)
# phone = []
# info = []
# result = []
# '''ls.shape[0]:取行数；ls[0][i]：第一列的数据'''
# for i in range(0, ls.shape[0]):
#     if  check(ls[0][i]) is True:
#     #if len(str(ls[0][i])) == 11:
#       phone.append(str(ls[0][i]))  # 需转化为字符串
#       info.append(ls[1][i])  # 第二列的数据
#       # print(result)
#     else:
#       print(i+1)
#       break
# result.append(phone)
# result.append(info)
# print(result)

