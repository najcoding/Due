Bill_Amount = float(input("Enter total bill amount"))
Paid_Amount= float(input("Enter amount paid"))
Due_Amount = Bill_Amount - Paid_Amount
if Due_Amount > 0:
    print("Your due is ", Due_Amount)
elif Due_Amount == 0:
    print("Your bill is fully paid")
else:
    print("Extra amount paid")
