current_year = 2019
alchohol_consumtion_age = 21
print("--------------------------------------")
print("~~~~~~DRINKING AGE CALCULATOR~~~~~~~~~")
print("--------------------------------------")
patron_year = input("What Year Were You Born In, My Friend? ")
print("Ok, so you were born in " + patron_year) 
patron_month = input("What month was that? ")
print("Ok, so it was " + patron_month)
print("I love the weather in " + patron_month)
patron_day = input('And what day might you have joined us on earth? ')
print("Ahhhh, the " + patron_day)
print("I had a cousin, who was born on the very same day! What a small world it is")
print("Hmmmmmmmmm... I come to the conclusion, that:")
if current_year - int(patron_year) <= alchohol_consumtion_age:
	print("You are underage! Tsk, Tsk, no alcohol for you")
else: 
	print("It's Beer O'Clock, my dude or dudette. Please Drink responsibly!") 
print("-------------------------------------")
