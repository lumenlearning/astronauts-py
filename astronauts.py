import datetime
from astronautsData import sampleAstronauts, sampleShips

def lookupSpaceship(spaceships, spaceshipName):
    for s in spaceships:
        if s['name'] == spaceshipName:
            return s

def assignToSpaceships(astronauts, spaceships):
    notYetAssigned = [];
    sortedAstronauts = sorted(astronauts, key = lambda i: i['applicationReceived'], reverse=True)
    # print("sorted astros:", sortedAstronauts)
    for a in sortedAstronauts:
        firstChoiceShip = lookupSpaceship(spaceships, a['preferredShip'][0])
        if (firstChoiceShip['capacity'] == len(firstChoiceShip['assignedAstronauts'])):
            notYetAssigned.append(a)
        else:
            firstChoiceShip['assignedAstronauts'].append(a)

    for a in notYetAssigned:
        secondChoiceShip = lookupSpaceship(spaceships, a['preferredShip'][1])
        if (secondChoiceShip['capacity'] == len(secondChoiceShip['assignedAstronauts'])):
            thirdChoiceShip = lookupSpaceship(spaceships, a['preferredShip'][2])
            thirdChoiceShip['assignedAstronauts'].append(a)
        else:
            secondChoiceShip['assignedAstronauts'].append(a)

def formatNotification(astronaut, spaceship):
    message = "Congratulations " + astronaut['name']
    message += ". You have been assigned to journey into the heart of the universe "
    message += "on the Spaceship " + spaceship['name'] + ". Please be prepared to "
    message += "start your journey on " + (spaceship['expeditionDate']).strftime("%m/%d/%Y") + "."
    return message

def notifySpaceshipAssignments():
    assignToSpaceships(sampleAstronauts,sampleShips)
    for s in sampleShips:
        for a in s['assignedAstronauts']:
            print(formatNotification(a, s))

# Calling the main function
if __name__ == "__main__":
    notifySpaceshipAssignments()
