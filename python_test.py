x=[100,110,120,130,140,150]
z=5
for mult in x:
    z*=mult
    print(z)

def divisible_by_seven():
    numbers=range(100,200)
    for x in numbers:
        print(x)
        if x%7==0:
            print("divisible by 7".format(x))



def Students():
    students=[{"age":19,"name":"Eunice"},{"age":21,"name":"Agnes"},{"age":18,"name":"Teresa"},{"age":22,"name":"Asha"}],
    eunice={'age':19,'name':'Eunice'}
    agnes={'age':21,'name':'Agnes'}
    teresa={'age':18,'name':'Tersa'}
    asha={'age':22,'name':'Asha'}
    students=[eunice,agnes,teresa,asha]
    print(students)
    for student in students:
        name=student['name']
        age=student['age']
        sentence="Hello {} you were born in the year{}".format(name,2021-age)

x = {'a','b','a','e','d','b','c','e','f','g','h'}
print(x)
