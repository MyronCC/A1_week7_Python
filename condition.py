print("This is the condition file")

Current_temp = False

while Current_temp is False:
	Current_temp = input("Enter a temperature: \n")
	print(Current_temp)

	if(int(Current_temp) < 0) or (int(Current_temp == 0)):
		print("water is a solid. icy!")
		Current_temp = False

	elif(int(Current_temp) < 100):
		print("water is a liquid. profit!")

	elif(int(Current_temp > 100)) or (int(Current_temp == 100)):
		print("water is vapor. cuz it's HOT!")
		Current_temp = False