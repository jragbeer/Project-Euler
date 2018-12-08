# Project Euler Problem 20

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:

n = [
[75],#0
[95,64],#1
[17,47,82],#2
[18,35,87,10],#3
[20,4,82,47,65],#4
[19,1,23,75,3,34],#5
[88,2,77,73,7,63,67],#6
[99,65,4,28,6,16,70,92],#7
[41,41,26,56,83,40,80,70,33],#8
[41,48,72,33,47,32,37,16,94,29],#9
[53,71,44,65,25,43,91,52,97,51,14],#10
[70,11,33,28,77,73,17,78,39,68,17,57],#11
[91,71,52,38,17,14,91,43,58,50,27,29,48],#12
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],#13
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]#14

def make_bottom_optimized(bot, top, nums):
    new_bottom = [max([nums[top][x]+nums[bot][y] for y in range(len(nums[bot])) if x == y or x+1 ==y]) for x in range(len(nums[top]))]
    nums = nums[:top]
    nums.append(new_bottom)
    return nums

def make_bottom_not_optimized(bot, top, nums):
    newbottom = []
    for x in range(len(nums[top])):
        result = []
        for y in range(len(nums[bot])):
            if x == y or x+1 == y:
                result.append(nums[top][x]+nums[bot][y])
        newbottom.append(max(result))
    nums = nums[:top]
    nums.append(newbottom)
    return nums

for _ in range(len(n)-1):
    n = make_bottom_optimized(len(n)-1, len(n)-2, n)
print(n)

