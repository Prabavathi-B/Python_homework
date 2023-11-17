from datetime import datetime

# Get input from the user
entry_time = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")


# Convert time strings to datetime objects
time1 = datetime.strptime(entry_time, "%H:%M")
time2 = datetime.strptime(exit_time, "%H:%M")

# Subtract time2 from time1
time_difference = time2 - time1

# Extract hours and minutes from the time difference
hours, remainder = divmod(time_difference.seconds, 3600)
minutes = remainder // 60

# Print the hours and minutes
print(f"The time difference is {hours} hours and {minutes} minutes.")

if hours >0 and hours <1:
    hours_fee = 100

else:
    hours_fee = 100 + (hours - 1) * 150

# Additional fees based on minutes
if minutes<= 15:
    min_fee = 0

elif minutes>= 15 and minutes <=30:
    min_fee = 50
    
else:
    min_fee = 100
    
parkingGarage = (hours_fee + min_fee)

print(parkingGarage)