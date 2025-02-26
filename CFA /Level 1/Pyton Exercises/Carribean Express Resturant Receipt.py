# Exercise 1: Go on a big shopping spree!
# Pretend you can buy anything you want no matter the cost. Buy at least 3 items. 
# 1. Make variables for each of the items with price values as floats
# 2. Calculate the before tax subtotal and print it
# 3. Add a shipping charge and print it
# 4. Calculate the tax, add it, and print the tax amount
# 5. Print the final receipt
title = "Carribean Express Resturant Receipt"
print(title)
rice_and_peas = 6.00
curry_goat = 12.00
rum_puch = 2.00

subtotal = rice_and_peas + curry_goat + rum_puch
print(f"subtotal (before tax): {subtotal:.2f}")

dlivery_charge = 5.00
subtotal_with_delivery = subtotal + dlivery_charge
print(f"subtotal with dilvery charge : $ {subtotal_with_delivery:.2f}")

tax_rate = 1.00
subtotal_with_tax = subtotal_with_delivery * tax_rate
print(f"subtotal with tax charge : $ {subtotal_with_tax:.2f}")

total_cost = subtotal_with_delivery + tax_rate
print(f"Final total: $ {total_cost:.2f}")

# Exercise 2: Calculate the perimeter and area of a circle
# 1. Create a valiable called pi and give it the float value of pi
# 2. Get the radius of the circle from the user, and convert it to a float
# 3. Using pi and radius, perform the calculation for finding the perimeter of a circle
# and print it, concat the output with a string like: "The perimeter of your circle is:"
# 4. Using pi and radius, perform the calculation for finding the area of a circle 
# and print it, concat the output with a string like: "The area of your circle is:"
print("Finding radius , Perimeter and Area")
pi = 4.00

radius = float(input("Enter the radius of the circle here: "))

perimeter = 2 * pi * radius
print("The perimeter of the circle is : ", perimeter)

area = pi * ( radius ** 2)
print("The area of the circle is : ", area)

