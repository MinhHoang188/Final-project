print("Enter the number of Sets (1 to 5): ")
n = int(input())
lst = []

#representing general Sets
for i in range (1, n+1, 1):
  set1 = []
  set1 = [item for item in input("Enter the Sets: ").split()]
  print(set1)
  #counting the element of each set
  num_elm = len(set1)
  print()
  print("The number of element in each Set is: ", num_elm)
  print()
  lst.append(set1)
print()
print("Your general Sets are:")
print(lst)

#counting the element in Sets
def elm_count(elm):
  count = 0
  if isinstance(elm, list):
     for each_elm in elm:
       count += elm_count(each_elm)
  else:
     count += 1 
  return count
print()
print("The number of element in total is: ", elm_count(lst))
print()

#perform the corresponding user-selected operations
while True:
  while True:
    print("Choose the set opereration: ")
    print("1-difference\n2-intersection\n3-symmetric_difference\n4-union")
    y = int(input())

    #calculate the difference
    if y == 1:
        print("Choose the two array number (1 to 5 and do not repeat the selected number): ")
        [s1, s2] = input().split()
        dif = set(lst[int(s1)-1]).difference(set(lst[int(s2)-1]))
        print("The difference is: ", dif)
        break

    #calculate the intersection
    elif y == 2: 
        print("Choose the two array number (1 to 5 and do not repeat the selected number): ")
        [s1, s2] = input().split()
        ints = set(lst[int(s1)-1]).intersection(set(lst[int(s2)-1]))
        print("The intersection is: ", ints)
        break

    #calculate the symmetric difference
    elif y == 3:
        print("Choose the two array number (1 to 5 and do not repeat the selected number): ")
        [s1, s2] = input().split()
        symm = set(lst[int(s1)-1]).symmetric_difference(set(lst[int(s2)-1]))
        print("The symmetric difference is: ", symm)
        break

    #calculate the union
    elif y == 4:
        print("Choose the two array number (1 to 5 and do not repeat the selected number): ")
        [s1, s2] = input().split()
        uni = set(lst[int(s1)-1]).union(set(lst[int(s2)-1]))
        print("The union is: ", uni)
        break

    else:
        print("Your choose is invalid")
  print("Do you want to do other set operation (Y or N): ")
  z = str(input())
  if not (z == "Y" or z == "y"): break
print("Finnish!")

