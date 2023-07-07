#1259 팰린드롬
#1259 팰린드롬
my_list = []
pringLst = []
while True:
    nums = list(input())
    if nums == ['0']:
        break
    else:
        while True:
            if len(nums) <= 1:
                pringLst.append('yes')
                break
            if nums[0] == nums[-1]:
                del nums[0]
                del nums[-1]
            else:
                pringLst.append('no')
                break
for a in pringLst:
    print(a)



