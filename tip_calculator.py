question = input("How much did you pay? ")
amount = int(question)

percent = input("How much would you like to tip? ")
tip_percent = int(percent)

tip_amount = amount * (tip_percent/100)

print(f"The amount of tip you should give for {percent} percent tip is: {tip_amount}")
