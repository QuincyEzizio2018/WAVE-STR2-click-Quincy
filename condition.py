"""
Condition statement are used to handle errors condition
and
or
not
>
<
>=
<=
"""
gender = str(input("What's your gender ?")).lower()

if gender == "male":
    print("You are a He/Him")
elif gender == "female":
    print("You are a She/Her")
else: print ("Invalid request")
