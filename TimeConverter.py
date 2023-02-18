# Using an import because use the tools available to you right? Work smarter not harder or something?
# install to console "pip install num2words"
# I probably could've used a virtual enviroment
from num2words import num2words
def militaryTimeConverter(time):
    timeInWords = ""
    firstHalf = time.split(":")[0]
    secondHalf = (time.split(":")[1])[:2]

    # For AM
    if(time[-2:] == "AM"):
        # First half
        if(len(firstHalf) == 1):
            timeInWords += "Zero "
        timeInWords += num2words(firstHalf) + " "
        # Second half
        if(secondHalf == "00"):
            timeInWords += "hundred hours"
        else:
            timeInWords += num2words(secondHalf)
    # For PM
    elif(time[-2:] == "PM"):
        # First half
        hours = ['', 'thirteen','fourteen','fifteen','sixteen', 'seventeen','eighteen','nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'zero']
        timeInWords+=(hours[int(firstHalf)]) + " "
        # Second Half
        if(secondHalf == "00"):
            timeInWords += "hundred hours"
        else:
            timeInWords += num2words(secondHalf)

    return timeInWords

# Some tests
print(militaryTimeConverter("9:45PM"))
print(militaryTimeConverter("5:00PM"))
print(militaryTimeConverter("11:59PM"))

print(militaryTimeConverter("8:00AM"))
print(militaryTimeConverter("11:11AM"))
print(militaryTimeConverter("12:00AM"))
