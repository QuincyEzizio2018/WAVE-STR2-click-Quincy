print("Welcome To The EvenOdd Game: ")
username = str(input("What's your name ?  ")).title()

print(f"Hey!, {username} are you ready ?")

reply1 = str(input("Y for Yes and N for No ")).lower()
if reply1 == "y" or reply1 == "yes" :
    print(f"Okay {username}, Let's Start")
elif reply1 == "n" or reply1 == "no" :
    print(f"Okay {username}, Bye")
else:
    print("invalid input")

n=0
while n <= 100 :
    print(f"Hey {username}, \"{n}\" is an Even or Odd number ?")
    print("A. Even")
    print("B. Odd")
    reply2 = str(input()).lower()
    if n == n/2 :
        if reply2 == "a" or reply2 == "even" or reply2 == "even number"  :
            print(f"Correct : The answer is {int(n/2)+1}")
        else:
            print(f"Oh!, Sorry {username} Wrong Answer")
    elif n == n/3 :
        if reply2 == "a" or reply2 == "even" or reply2 == "even number"  :
            print(f"Correct : The answer is {int(n/2)+1}")
        else:
            print(f"Oh!, Sorry {username} Wrong Answer")
    n+=1