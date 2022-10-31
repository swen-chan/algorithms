running time:0.01s

def change(money):
    # write your code here
    v=[0 for k in range(money+1)]
    coins=[1,3,4]
    n=len(coins)

    for i in range(n):
        for j in range(coins[i],money+1):
            if v[j]==0 :
                v[j]=v[j-coins[i]]+1
            elif v[j-coins[i]]+1<v[j]:
                v[j]=v[j-coins[i]]+1
    return v[money]

if __name__ == '__main__':
    m = int(input())
    print(change(m))
