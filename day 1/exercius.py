'''1. Write scripts that prompt users for structured input (e.g., temperature, distance, currency).
2. Format output using print() with sep= and end= to simulate clean data logging.
3. Read string input and cast to numeric types (int, float) for calculations.
'''

print("Please Provide Temperature in Celsius")
#tempInCelsius = input("Temperature In Celsius:")
#tempInCelsius = int(tempInCelsius)
tempInCelsius = 40
def convertToFarenhite(tempInCensius: int) -> int:
    tempInFarenhite = (tempInCensius * 9/5) + 32
    return tempInFarenhite


print(f"Temperatur in Farenhite is {convertToFarenhite(tempInCelsius)}",)



#Format output using print() with sep= and end= to simulate clean data logging.
#give me random string for working here.     
print("This is a random string for working here.", "What","Are","You","Doing",sep="-")
print("This is the second part of the random string.", sep=" ", end="\n")

#3. Read string input and cast to numeric types (int, float) for calculations.
print("Please Provide Distance in Kilometers")
distanceInKilometers = input("Distance In Kilometers:")
distanceInKilometers = float(distanceInKilometers)
def convertToMiles(distanceInKilometers: float) -> float:
    distanceInMiles = distanceInKilometers * 0.621371
    return distanceInMiles

print(f"Distance in Miles is {convertToMiles(distanceInKilometers)}",)
