def gst(amount, percent):
    gst_amount = amount * percent / 100
    total = amount + gst_amount
    return total


amount = float(input("Enter amount: "))
percent = float(input("Enter GST percent: "))

result = gst(amount, percent)

print("Total amount with GST:", result)