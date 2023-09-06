nums=[2,5,6,7,8,9,10]

def mapfunction(num):
    return num*2

nums=list(map(mapfunction,nums)) #use map-> map(function,list)
print(nums)

nums=[num*2 for num in nums] #comprehension
print(nums)