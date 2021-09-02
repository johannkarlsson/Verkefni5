# 1,2,3,6,11,20,37,_,_,_,....
# finna ut leið til að gera reikna sequencið með breytum
# finna leið til að leggja saman og á sama tíma geyma eldri númer fyrir næstu summu.
#laga username

#a = 1
#b = a+a
#c = a+b
#d = a+b+c

current_number = 1
prev_number = 0
prev_number2 = 0
prev_number3 = 0

n = int(input("Enter the length of the sequence: ")) # Do not change this line


for i in range (0,n):
   if current_number == 1:
      print(current_number)
      prev_number = current_number
      current_number = prev_number + prev_number
   elif current_number == 2:
      print(current_number)
      prev_number2 = prev_number
      prev_number = current_number
      current_number = prev_number + prev_number2
   else:
      print(current_number)
      prev_number3 = prev_number2
      prev_number2 = prev_number
      prev_number = current_number
      current_number = prev_number + prev_number2 + prev_number3



   



