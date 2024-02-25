# thelist = ["apple", "banana", "Cherry", "Pineapple", "Cherry"]
# print(thelist)

#List length
# print(len(thelist))

#Data Structures in Python, List, Tuple, Dictionary, Set
# print(type(thelist))

#List Constructor : the bracket is called constructors ()
# thislist = list(("apple", "banana", "Cherry"))
# print (thislist)

# for x in thislist:
#     print(x)


# mylist = ["apple", "banana", "Cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist[1]) #or print(mylist[-2])  - (negative indexing)
# print(mylist[2:5])
# for x in mylist[2:5]:
#     print(x)


# numlist = [0,1,2,3,4,5,6,7,8,9]
# for y in numlist[0:5]:
#     print(y)

# numlist = [0,1,2,3,4,5,6,7,8,9]
# for y in numlist[-5:-1]:
#     print(y)

#Nested Loop
print("result")
response = int(input()) 
thislist = [0,1,2,3,4,5,6,7,8,9]
nxt = [0,1,2,3,4,5,6,7,8,9]
for x in thislist[-5:-1]:
    for y in nxt:
        #print(f"{x} - {y})
        scores = x-y 
        while response == scores:
            print("You win!!!")
            break
        else:
            print("You loose!!!")


