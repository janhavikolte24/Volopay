# Count of seats
aisle_seats = 0
window_seats = 0
centre_seats = 0

# List of seats 
aisle =[]
centre =[]
window = []

# input matrix
matrix = []

for i in range(4):
  
   row = []
   for j in range(2):

      el = int(input())

      row.append(el)

   matrix.append(row)

print(matrix)

passenger_count = int(input("No of passengers :"))

for i in range(4):
    
    
        if matrix[i][0] > 2 and (i==0 or i==3):
            window_seats  += matrix[i][1]
            aisle_seats += matrix[i][1] 
            centre_seats += ((matrix[i][0]*matrix[i][1])-(matrix[i][1]*2) )
            
            
        else :
            if matrix[i][0] >2 :
                aisle_seats += matrix[i][1]*2 
                centre_seats += ((matrix[i][0]*matrix[i][1])-(matrix[i][1]*2) )
                
            else:
                aisle_seats += (matrix[i][0]*matrix[i][1])
                
# current passenger filled             
current_passenger = 0
                
for i in range(1,aisle_seats+1):
    if(passenger_count!=0):
        aisle.append(i)
        passenger_count -=1
current_passenger +=len(aisle)
for i in range(1,window_seats+1):
    if(passenger_count!=0):
        window.append(current_passenger+i)
        passenger_count -=1
current_passenger +=len(window)
for i in range(1,centre_seats+1):
    if(passenger_count!=0):
        centre.append(current_passenger+i)
        passenger_count -=1
            
                
print('Window seats count : ',window_seats)
print('Centre seats count : ',centre_seats)
print('Aisle seats count : ',aisle_seats)

# Passenger no in the lists :
print("aisle list :\n")
for i in range(len(aisle)):
    print(aisle[i])

print("window list :\n")
for i in range(len(window)):
    print(window[i])
    
print("centre list :\n")
for i in range(len(centre)):
    print(centre[i])
        
            
