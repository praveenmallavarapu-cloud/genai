'''Income range	Tax rate
Up to ₹4,00,000	        NIL
₹4,00,001 - ₹8,00,000	5%
₹8,00,001 - ₹12,00,000	10%
₹12,00,001 - ₹16,00,000	15%
₹16,00,001 - ₹20,00,000	20%
₹20,00,001 - ₹24,00,000	25%
Above ₹24,00,000	    30% '''


salary = int(input("Enter your salary: "))
if salary <= 400000:
    tax = 0
elif salary <= 800000:
    tax = (salary - 400000) * 0.05
elif salary <= 1200000:
    tax = (salary - 800000) * 0.10 + 20000  
elif salary <= 1600000:
    tax = (salary - 1200000) * 0.15 + 60000
elif salary <= 2000000:
    tax = (salary - 1600000) * 0.20 + 120000
elif salary <= 2400000:
    tax = (salary - 2000000) * 0.25 + 200000
else:
    tax = (salary - 2400000) * 0.30 + 300000
    
print("Your tax liability is: ₹", tax)
