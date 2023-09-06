with open ('./about.txt','w') as file:
    file.write("I am soeyiyi")
    file.write("\nI am 20years old")
    

#another work

with open ('./about.txt','a') as file: # 'a' <- 
    file.write("\nI am uni student")


#add to file from list
lists=["I am soeyiyi","I am uni student"]
with open ('./about.txt','a') as file:
    file.writelines(lists)

