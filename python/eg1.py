person={}

while True :
    name=input('name :');
    age=input('age :');
    person[name]=age

    another=input('another y/n :' )
    if another=='y':
        continue;
    else :
        break;

ages=list(person.values())
for age in set(ages) : #unit age value #set <- print equal number one time
    count=ages.count(age)
    print(f'{age} years old - {count}')


for (key,value) in person.items():
    print(f'{key} is {value} years old')