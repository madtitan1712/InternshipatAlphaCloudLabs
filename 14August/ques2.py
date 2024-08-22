a=int(input())
x={}
for i in range(a):
    name=input("Enter name ")
    mark=int(input("Enter Mark"))
    x[name]=mark
def sort_key(item):
    marks = item[1]
    name = item[0]
    return (marks, name)
sorted_dict = dict(sorted(x.items(), key=sort_key))
print(sorted_dict)