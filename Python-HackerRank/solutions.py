# Solve Me First: https://www.hackerrank.com/challenges/solve-me-first/problem
def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return a+b

num1 = input()
num2 = input()
res = solveMeFirst(num1,num2)
print res

# A Very Big Sum: https://www.hackerrank.com/challenges/a-very-big-sum
def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

# Staircase: https://www.hackerrank.com/challenges/staircase/problem
def staircase(n):
    for i in range (1, n+1):
        print(" "*(n-i) + "#"*i)
