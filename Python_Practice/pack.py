n = int(input("enter order of matrix = "))
def diagonal_diff():
    a1=int(input()), a2=int(input()), a3=int(input()) b1=int(input()), b2=int(input()), b3=int(input()) c1=int(input()), c2=int(input()), c3=int(input())

    sum1=a1+b2+c3
    sum2=a3+b2+c1

    if sum1>sum2:
        print(sum1-sum2)
    else:
        print(sum2-sum1) 


diagonal_diff()
