# 找出最小的硬币个数来实现某个数
import sys

def find_coins(m,n):
    '''
        m: 硬币的种类[1,2,5]
        n: 需要拼凑的数:27
    '''

    # 初始化f[0] = 0
    f = [0]

    for i in range(1,n+1):
        max_int = sys.maxsize
        f.append(max_int)
        for conin in m:
            if conin <=i and f[i-conin] != max_int:
                f[i] = min(f[i-conin]+1,f[i])
        
    return f

def find_coins2(m,n):
    '''
        m: 硬币的种类[1,2,5]
        n: 需要拼凑的数:27
    '''

    # 初始化f[0] = 0
    f = [0]
    f_dict = {}

    for i in range(1,n+1):
        max_int = sys.maxsize
        f.append(max_int)
        f_dict[i] = []
        for conin in m:
            if conin <=i and f[i-conin] != max_int:
                f[i] = min(f[i-conin]+1,f[i])
                if f[i-conin]+1 >f[i]:
                    f_dict[i].append(conin)
        
    return f,f_dict


m = [1,5,7]
n = 27
result,res_dict = find_coins2(m,n)
print("coin number:" + str(result[-1]))
for i in range(1,n+1):
    print(i,":",result[i])
for key,val in res_dict.items():
    print(key,":",val)


