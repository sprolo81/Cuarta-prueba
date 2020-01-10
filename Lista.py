  #for i in range(5,50,3):
	#print(f"valor de la variable{i}")


#for i in ["a","b"]:
#	print("HOLA",end="  h  ")

email= False
miEmail=input ("INTRODUCE TU EMAIL")

for x in miEmail:
	if (x=="@"):
		email=True

	if email==True:
		print("tu email es valido")

	else:
		print("tu email es invalido")

		