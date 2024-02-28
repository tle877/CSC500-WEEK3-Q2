current_time = int(input("Please enter the time now in hours: "))
wait_time = int (input("Please enter the number of hours to wait for the alarm: "))

result = (current_time + wait_time ) % 24

print("The time when the alarm goes off is: " , result)

