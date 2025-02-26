
name_of_the_show = "BatMan"
number_of_tickets = "2"
tickets_price = "2.00"

show_name = "BatMan"
message = "I am exsited to go see BatMan in theater"
number_of_tickets = int(input ("How many tickets are you buying? : "))
ticket_price = float(input("What is the price of a single ticket? :"))
subtotal = number_of_tickets * ticket_price 
tax = 0.10 * subtotal
order_total = subtotal + tax
print(f"subtotal : {subtotal:.2f}")
print (f"tax : {tax:.2f}")
print (f" Order total : {order_total : 2f}")

print(message)
print("It will cost you $" + str(order_total))
def show_review(show_name , ticket_price):
    review = (f""" 
    This is the review of {show_name} : 
    "An unforgettable experience The performace is great and 
    every momment was filled with exsitment and wonder! 
    The ticket price is {ticket_price:.2f}""")
    print(review)
show_review(show_name , ticket_price)

additional = int(input("How many tickets do you want?"))
print = (f"you have requested {additional}tickets.")

def calculate_total(num_tickets):
    global number_of_tickets
    number_of_tickets += additional

subtotal = number_of_tickets * ticket_price 
tax = 0.10 * subtotal
order_total = subtotal + tax

print(f"subtotal : {subtotal: .2f}")
print (f"tax : {tax: .2f}")
print (f" Order total : {order_total: .2f}")

calculate_total(additional)