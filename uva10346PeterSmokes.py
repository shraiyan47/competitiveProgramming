while True:
    try:
        n,k=map(int,input().split())
        # print("n", n)
        # print("k", k)
        result = int((k*n-1)/(k-1))
        print(result)

    except EOFError:
        break

# n = int(input())
# k = int(input())
# result = int((k*n-1)/(k-1))
# print(format(result)+"\n")