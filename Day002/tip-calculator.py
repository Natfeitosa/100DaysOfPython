print("Insert value of Bill")
bill=input()
bill=float(bill)
print("how many people?")
people=input()
result=(bill/int(people))*1.12
print("price everyone will pay is %8.2f" % (result))
