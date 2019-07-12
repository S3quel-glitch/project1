class table: 
#Main Class
		
	def __init__(self,number = "0",status = "Свободен", time = "0:00"):
		self.number = number #Номер стола
		self.status = status #Статус стола
		self.time = time #Время резервирования (только для зарезервированных столов)
	
	#Объявление столиков 
	#Making tables
	
table1 = table() #Table 1
table1.number = "1"
table2 = table() #Table 2
table2.number = "2"
table3 = table() #Table 3
table3.number = "3"
table4 = table() #Table 4
table4.number = "4"
table5 = table() #Table 5
table5.number = "5"
table6 = table()#Table 6 
table6.number = "6"
table7 = table() #Table 7
table7.number = "7"
table8 = table() #Table 8
table8.number = "8"
table9 = table() #Table 9
table9.number = "9"
table10 = table() #Table 10
table10.number = "10"


#Начало программы 
#Start of the programm

print("Программа \"Без названия\". 2019-2020©\n")
print("Данная программа была сделана одним человеком.\n\n")

while True:
	#Ввод команды пользователем
	command = input("Доступные команды:\n\n1.List(Открывает весь список) Пример: List\n2.Edit(Внести изменения в список) Пример: Edit №_стола Новый_параметр\n3.Info(Информация о столике) Пример: Info №_стола\n4.Reserve(Зарезервировать стол) Пример: Reserve №_стола время_резервирования\nНаберите Exit или Выход, чтобы выйти из программы.\n\nВведите команду: ")
	command_list = command.split() #Разделение ввода пользователя
	
###########################

	#Команда выхода 
	#Exit command
	if command == "Exit" or command == "EXIT" or command == "Выход" or command == "ВЫХОД":
		break
	
	#Обработка исключений 
	#Exceptions
	elif command == "":
		print("Ошибка ввода: пустой запрос. Повторите ввод. Подсказка: для выхода из программы напиши: Exit\n")
	
	elif command == "Edit":
		print("Ошибка ввода: неверное/неверные значение/значения параметра Edit.")

	elif command == "Info":
		print("Ошибка ввода: неверное значение параметра Info.")
		
	elif command == "Reserve":
		print("Ошибка ввода: неверное значение/значения параметра Reserve.")
	
		
###########################

#Далее проверка на ввод 

	
	#__EDIT__ 
	#If command is Edit
	elif command_list[0] == "Edit":
		
		#1 стол 
		#1 table
		if command_list[1] == "1":
			table1.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table1.number, " изменён на ", table1.status)
		#2 стол	
		#2 table
		elif command_list[1] == "2":
			table2.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table2.number, " изменён на ", table2.status)
		#3 стол	
		#3 table
		elif command_list[1] == "3":
			table3.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table3.number, " изменён на ", table3.status)
		#4 стол	
		#4 table
		elif command_list[1] == "4":
			table4.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table4.number, " изменён на ", table4.status)
		#5 стол	
		#5 table
		elif command_list[1] == "5":
			table5.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table5.number, " изменён на ", table5.status)
		#6 стол	
		#6 table
		elif command_list[1] == "6":
			table6.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table6.number, " изменён на ", table6.status)
		#7 стол	
		#7 table
		elif command_list[1] == "7":
			table7.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table7.number, " изменён на ", table7.status)
		#8 стол	
		#8 table
		elif command_list[1] == "8":
			table8.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table8.number, " изменён на ", table8.status)
		#9 стол	
		#9 table
		elif command_list[1] == "9":
			table9.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table9.number, " изменён на ", table9.status)
		#10 стол	
		#10 table
		elif command_list[1] == "10":
			table10.status = command_list[2]
			print("\n", command_list[2])
			print("\n", "Статус столика ", table10.number, " изменён на ", table10.status)
			
	#Если ввод не равен ни одному заданному значению:	
	#If command is wrong
		else:
			print("Ошибка ввода. Повторите ввод.")
			
			
	#__INFO__	
	#If command is Info	
	elif command_list[0] == "Info":
		#Стол 1
		#Table 1
		if command_list[1] == "1":  
			if table1.status == "Зарезервирован":	#Checking status of the table 1
				print("\n", table1.number, table1.status, table1.time, "\n")
			else: #If table 1 isn't reserved
				print("\n", table1.number, table1.status, "\n")
		#Стол 2
		#Table 2		
		elif command_list[1] == "2":
			if table2.status == "Зарезервирован":	#Checking status of the table 2
				print("\n", table2.number, table2.status, table2.time, "\n")
			else: #If table 2 isn't reserved
				print("\n", table2.number, table2.status, "\n")
		#Стол 3
		#Table 3		
		elif command_list[1] == "3":
			if table3.status == "Зарезервирован":	#Checking status of the table 3
				print("\n", table3.number, table3.status, table3.time, "\n")
			else: #If table 3 isn't reserved
				print("\n", table3.number, table3.status, "\n")
		#Стол 4
		#Table 4		
		elif command_list[1] == "4":
			if table4.status == "Зарезервирован":	#Checking status of the table 4
				print("\n", table4.number, table4.status, table4.time, "\n")
			else: #If table 4 isn't reserved
				print("\n", table4.number, table4.status, "\n")
		#Стол 5
		#Table 5		
		elif command_list[1] == "5":
			if table5.status == "Зарезервирован":	#Checking status of the table 5
				print("\n", table5.number, table5.status, table5.time, "\n")
			else: #If table 5 isn't reserved
				print("\n", table5.number, table5.status, "\n")
		#Стол 6
		#Table 6		
		elif command_list[1] == "6":
			if table6.status == "Зарезервирован":	#Checking status of the table 6
				print("\n", table6.number, table6.status, table6.time, "\n")
			else: #If table 6 isn't reserved
				print("\n", table6.number, table6.status, "\n")
		#Стол 7
		#Table 7		
		elif command_list[1] == "7":
			if table7.status == "Зарезервирован":	#Checking status of the table 7
				print("\n", table7.number, table7.status, table7.time, "\n")
			else: #If table 7 isn't reserved
				print("\n", table7.number, table7.status, "\n")
		#Стол 8
		#Table 8		
		elif command_list[1] == "8":
			if table8.status == "Зарезервирован":	#Checking status of the table 8
				print("\n", table8.number, table8.status, table8.time, "\n")
			else: #If table 8 isn't reserved
				print("\n", table8.number, table8.status, "\n")
		#Стол 9
		#Table 9		
		elif command_list[1] == "9":
			if table9.status == "Зарезервирован":	#Checking status of the table 9
				print("\n", table9.number, table9.status, table9.time, "\n")
			else: #If table 9 isn't reserved
				print("\n", table9.number, table9.status, "\n")
		#Стол 10
		#Table 10		
		elif command_list[1] == "10":
			if table10.status == "Зарезервирован":	#Checking status of the table 10
				print("\n", table10.number, table10.status, table10.time, "\n")
			else: #If table 10 isn't reserved
				print("\n", table10.number, table10.status, "\n")
		else:
			print("Ощибка в вводе команды. Попробуйте заново.")
			
			
			
	#Вывод листа 
	#List printing		
			
	#__LIST__ 
	#If command is List		
	elif command == "List":
		
		
		#Вывод стола 1 
		#Printing table 1
		if table1.status == "Зарезервирован":	#Checking status of the table 1
			print(table1.number, table1.status, table1.time, "\n")
		else:
			print(table1.number, table1.status, "\n")
		#Вывод стола 2	
		#Printing table 2
		if table2.status == "Зарезервирован":	#Checking status of the table 2
			print(table2.number, table2.status, table2.time, "\n")
		else:
			print(table2.number, table2.status, "\n")	
		#Вывод стола 3	
		#Printing table 3
		if table3.status == "Зарезервирован":	#Checking status of the table 3
			print(table3.number, table3.status, table3.time, "\n")
		else:
			print(table3.number, table3.status, "\n")	
		#Вывод стола 4	
		#Printing table 4
		if table4.status == "Зарезервирован":	#Checking status of the table 4
			print(table4.number, table4.status, table4.time, "\n")
		else:
			print(table4.number, table4.status, "\n")	
		#Вывод стола 5	
		#Printing table 5
		if table5.status == "Зарезервирован":	#Checking status of the table 5
			print(table5.number, table5.status, table5.time, "\n")
		else:
			print(table5.number, table5.status, "\n")
		#Вывод стола 6	
		#Printing table 6
		if table6.status == "Зарезервирован":	#Checking status of the table 6
			print(table6.number, table6.status, table6.time, "\n")
		else:
			print(table6.number, table6.status, "\n")
		#Вывод стола 7	
		#Printing table 7
		if table7.status == "Зарезервирован":	#Checking status of the table 7
			print(table7.number, table7.status, table7.time, "\n")
		else:
			print(table7.number, table7.status, "\n")
		#Вывод стола 8	
		#Printing table 8
		if table8.status == "Зарезервирован":	#Checking status of the table 8
			print(table8.number, table8.status, table8.time, "\n")
		else:
			print(table8.number, table8.status, "\n")
		#Вывод стола 9	
		#Printing table 8
		if table9.status == "Зарезервирован":	#Checking status of the table 9
			print(table9.number, table9.status, table9.time, "\n")
		else:
			print(table9.number, table9.status, "\n")
		#Вывод стола 10	
		#Printing table 10
		if table10.status == "Зарезервирован":	#Checking status of the table 10
			print(table10.number, table10.status, table10.time, "\n")
		else:
			print(table10.number, table10.status, "\n")
			

	#__RESERVE__
	#If command is Reserve
	elif command_list[0] == "Reserve":
		#Резервация стола 1 
		#Reservation of the table 1
		if command_list[1] == "1":
			table1.status = "Зарезервирован"
			table1.time = command_list[2]
			print(table1.status)
			print("Статус столика ", table1.number, "изменён на ", table1.status, ". Время резервирования: ", table1.time)
		#Резервация стола 2	
		#Reservation of the table 2
		if command_list[1] == "2":
			table2.status = "Зарезервирован"
			table2.time = command_list[2]
			print(table2.status)
			print("Статус столика ", table2.number, "изменён на ", table2.status, ". Время резервирования: ", table2.time)
		#Резервация стола 3	
		#Reservation of the table 3
		if command_list[1] == "3":
			table3.status = "Зарезервирован"
			table3.time = command_list[2]
			print(table3.status)
			print("Статус столика ", table3.number, "изменён на ", table3.status, ". Время резервирования: ", table3.time)
		#Резервация стола 4	
		#Reservation of the table 4
		if command_list[1] == "4":
			table4.status = "Зарезервирован"
			table4.time = command_list[2]
			print(table4.status)
			print("Статус столика ", table4.number, "изменён на ", table4.status, ". Время резервирования: ", table4.time)
		#Резервация стола 5	
		#Reservation of the table 5
		if command_list[1] == "5":
			table5.status = "Зарезервирован"
			table5.time = command_list[2]
			print(table5.status)
			print("Статус столика ", table5.number, "изменён на ", table5.status, ". Время резервирования: ", table5.time)
		#Резервация стола 6	
		#Reservation of the table 6
		if command_list[1] == "6":
			table6.status = "Зарезервирован"
			table6.time = command_list[2]
			print(table6.status)
			print("Статус столика ", table6.number, "изменён на ", table6.status, ". Время резервирования: ", table6.time)
		#Резервация стола 7	
		#Reservation of the table 7
		if command_list[1] == "7":
			table7.status = "Зарезервирован"
			table7.time = command_list[2]
			print(table7.status)
			print("Статус столика ", table7.number, "изменён на ", table7.status, ". Время резервирования: ", table7.time)
		#Резервация стола 8	
		#Reservation of the table 8
		if command_list[1] == "8":
			table8.status = "Зарезервирован"
			table8.time = command_list[2]
			print(table8.status)
			print("Статус столика ", table8.number, "изменён на ", table8.status, ". Время резервирования: ", table8.time)
		#Резервация стола 9	
		#Reservation of the table 9
		if command_list[1] == "9":
			table9.status = "Зарезервирован"
			table9.time = command_list[2]
			print(table9.status)
			print("Статус столика ", table9.number, "изменён на ", table9.status, ". Время резервирования: ", table9.time)
		#Резервация стола 10 
		#Reservation of the table 10	
		if command_list[1] == "10":
			table10.status = "Зарезервирован"
			table10.time = command_list[2]
			print(table10.status)
			print("Статус столика ", table10.number, "изменён на ", table10.status, ". Время резервирования: ", table10.time)
	
	
	
	#Если введённая команда является неправильной 
	#If command is wrong
	else:
		print("Ошибка ввода. Повторите ввод.")
			
			
			
			
