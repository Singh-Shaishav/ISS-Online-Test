import datetime

with open("data.txt", "r") as f:
    
    highest_temperature, lowest_temperature = float("-inf"), float("inf")
    highest_temperature_date, lowest_temperature_date = None, None

    for line in f:
        date, temperature = line.strip().split(",")
        day = int(date[:2])
        month =int(date[2:4])
        year = int(date[4:])
        temperature = int(temperature)


        if temperature > highest_temperature:
            highest_temperature = temperature
            highest_temperature_date = "{}/{}/{}".format(year,month,day)
        if temperature < lowest_temperature:
            lowest_temperature = temperature
            lowest_temperature_date = "{}/{}/{}".format(year,month,day)

current_date = datetime.datetime.now().strftime('%Y/%m/%d')
current_time = datetime.datetime.now().strftime('%H:%M:%S')

print("Name: Shaishav Singh")
print("Date: {}".format(current_date))
print("Time: {}".format(current_time))
print("Results")
print("Highest Temperature 20{}  {} degrees centigrade".format(highest_temperature_date,highest_temperature))
print("Lowest Temperature 20{}  {} degrees centigrade".format(lowest_temperature_date,lowest_temperature))


# Name:Shaishav Singh
# Date:12/05/2023
# TIme:03:30:PM
