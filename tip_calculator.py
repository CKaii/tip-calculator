question = input("How much did you pay? ")
amount = int(question)
question = input("How much did you pay? ")
amount = float(question)
round_amount = round(amount, 2)

percent = input("How much would you like to tip? ")
tip_percent = float(percent)

tip_amount = round_amount * (tip_percent/100)
round_tip_amount = round(tip_amount)
total_amount = round_amount + round_tip_amount

print(f"The amount of tip you should give for {percent} percent tip is: {tip_amount}")
print(f"The total amount you should pay is: {total_amount}")

percent = input("How much would you like to tip? ")
tip_percent = int(percent)

tip_amount = amount * (tip_percent/100)

print(f"The amount of tip you should give for {percent} percent tip is: {tip_amount}")
