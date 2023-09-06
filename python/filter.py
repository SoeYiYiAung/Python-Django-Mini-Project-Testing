nums=[1,2,3,4,5,6,7,8,9,10]

def even(num) :
    return (num%2)==0

even_num=list(filter(even,nums))          #filter(function,list)
print(even_num)


nums=[num for num in nums if (num%2)==0] #comprehension
print(nums)

evenNums=[]             #traditional way
for num in nums:
    if (num%2)== 0 :
        evenNums.append(num)
print(evenNums)