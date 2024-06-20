europe=['greece','italy','france','spain']
asia={"singapore","china","india"}
america={"usa","perou","canada","mexico"}
country=input('give a name of a country:')
new_country=""
if country in europe:
    print(country,"is in europe") 
elif country in asia:
    print(country,"is in asia") 
elif country in america:
    print(country,"is in america")
else:
    new_country=input("does this country belong to europe,asia,america?")
if new_country=="europe":
    europe.append(country)
elif new_country=="asia":
    asia.append(country)
elif new_country=="america":
    america.append(country)
print(europe)
print(asia)
print(america)
