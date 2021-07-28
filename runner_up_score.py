#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

#Input Format

#The first line contains . The second line contains an array   of  integers each separated by a space.

#Constraints

#Output Format

#Print the runner-up score.

#Sample Input 0

#5
#2 3 6 6 5
#Sample Output 0

#5

#Here is the solution

#solution1
n = int(input())
a = [int(x) for x in input().split()]
largest = secondlargest = -100
for x in a:
    if x > largest:
        tmp = largest
        largest = x
        secondlargest = tmp
    elif x > secondlargest and x != largest:
        secondlargest = x
print(secondlargest)


# Second solution

i = int(input())
lis = list(input())
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)

        


