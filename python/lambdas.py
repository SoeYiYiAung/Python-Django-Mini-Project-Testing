def add(n1,n2):             #traditional way
    return n1+n2
print(add(2,3))

#using lambdas in small function
addition=lambda n1,n2:n1+n2  #small function -> lambda parameter:function
print(addition(4,5))

nums=[1,2,3,4,5,6,7]
even=list(filter(lambda num:(num%2)==0 , nums))
print(even)


nums=list(map(lambda num:num*2,nums))
print(nums)