food = str(input("Enter the food item: "))
price = float(input("Enter the price of the food item: "))  
gst = price * 0.18
total_amount = price + gst
print(f"The total amount for {food} including GST is: {total_amount}")