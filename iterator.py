mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

  iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)
 
while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        break
