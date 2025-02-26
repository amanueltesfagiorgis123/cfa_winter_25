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

additional = int(input("How many additional tickets do you want to by :"))

def calculate_total(number_of_tickets):
    number_of_tickets += additional

subtotal = number_of_tickets * ticket_price 
tax = 0.10 * subtotal
order_total = subtotal + tax

friends_share = order_total / 2

print(f"Total order cost: ${order_total: .2f}")
print(f"Friend is pating half : ${friends_share:.2f}")
print(f"Each of the remaning friends will owe: ${friends_share:.2f}")

calculate_total(additional)

score = 0 

def play(points):
    global score 
    score += points
    print(f"Your current score is: {score}")

play(10)
play(15)
play(5)
play(20)


