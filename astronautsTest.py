import datetime
from astronautsData import sampleAstronauts, sampleShips
from astronauts import assignToSpaceships, formatNotification

expeditionDate = datetime.datetime(2022, 1, 1)

def testFirstChoiceAdd():
    spaceships = [
        { 'name': "Space A", 'capacity': 1, 'assignedAstronauts': [], 'expeditionDate': expeditionDate },
        { 'name': "Space B", 'capacity': 1, 'assignedAstronauts': [], 'expeditionDate': expeditionDate }
    ]

    astronauts = [
        {
            'name': "Astro 1",
            'applicationReceived': datetime.datetime(2020, 1, 2),
            'preferredShip': ["Space A", "Space B"]
        },
        {
            'name': "Astro 2",
            'applicationReceived': datetime.datetime(2020, 1, 1),
            'preferredShip': ["Space B", "Space A"]
        }
    ]

    assignToSpaceships(astronauts, spaceships)
    assert len(spaceships[0]['assignedAstronauts']) == 1, "Should be 1"
    assert spaceships[0]['assignedAstronauts'][0]['name'] == "Astro 1", "Should be Astro 1"
    assert len(spaceships[1]['assignedAstronauts']) == 1, "Should be 1"
    assert spaceships[1]['assignedAstronauts'][0]['name'] == "Astro 2", "Should be Astro 2"

def testSecondChoiceIfFirstFull():
    spaceships = [
        { 'name': "Space A", 'capacity': 1, 'assignedAstronauts': [], 'expeditionDate': expeditionDate },
        { 'name': "Space B", 'capacity': 2, 'assignedAstronauts': [], 'expeditionDate': expeditionDate }
    ]

    astronauts = [
        {
            'name': "Astro 1",
            'applicationReceived': datetime.datetime(2020, 1, 2),
            'preferredShip': ["Space A", "Space B"]
        },
        {
            'name': "Astro 2",
            'applicationReceived': datetime.datetime(2020, 1, 1),
            'preferredShip': ["Space B", "Space A"]
        },
        {
            'name': "Astro 3",
            'applicationReceived': datetime.datetime(2020, 1, 3),
            'preferredShip': ["Space A", "Space B"]
        }
    ]

    assignToSpaceships(astronauts, spaceships)
    assert len(spaceships[0]['assignedAstronauts']) == 1, "Should be 1"
    assert spaceships[0]['assignedAstronauts'][0]['name'] == "Astro 3", "Should be Astro 3"
    assert len(spaceships[1]['assignedAstronauts']) == 2, "Should be 2"
    assert spaceships[1]['assignedAstronauts'][0]['name'] == "Astro 2", "Should be Astro 2"
    assert spaceships[1]['assignedAstronauts'][1]['name'] == "Astro 1", "Should be Astro 1"

def testFirstChoiceFullButAppliedFirstAssignedToNextAvailableChoice():
    spaceships = [
        { 'name': "Space A", 'capacity': 1, 'assignedAstronauts': [], 'expeditionDate': expeditionDate },
        { 'name': "Space B", 'capacity': 1, 'assignedAstronauts': [], 'expeditionDate': expeditionDate },
        { 'name': "Space C", 'capacity': 1, 'assignedAstronauts': [], 'expeditionDate': expeditionDate }
    ]

    astronauts = [
        {
            'name': "Astro 1",
            'applicationReceived': datetime.datetime(2021, 1, 1),
            'preferredShip': ["Space A", "Space B", "Space C"]
        },
        {
            'name': "Astro 2",
            'applicationReceived': datetime.datetime(2020, 1, 2),
            'preferredShip': ["Space A", "Space B", "Space C"]
        },
        {
            'name': "Astro 3",
            'applicationReceived': datetime.datetime(2020, 1, 3),
            'preferredShip': ["Space B", "Space A", "Space C"]
        }
    ]

    assignToSpaceships(astronauts, spaceships)
    assert len(spaceships[0]['assignedAstronauts']) == 1, "Should be 1"
    assert spaceships[0]['assignedAstronauts'][0]['name'] == "Astro 1", "Should be Astro 1"
    assert len(spaceships[1]['assignedAstronauts']) == 1, "Should be 1"
    assert spaceships[1]['assignedAstronauts'][0]['name'] == "Astro 2", "Should be Astro 2"
    assert len(spaceships[2]['assignedAstronauts']) == 1, "Should be 1"
    assert spaceships[2]['assignedAstronauts'][1]['name'] == "Astro 3", "Should be Astro 3" 

def testFormatNotificationShouldFormatMessage():
    astronaut = { 'name': "Astro 1" }
    spaceship = { 'name': "Space A", 'expeditionDate': datetime.datetime(2025, 6, 14) }

    message = formatNotification(astronaut, spaceship)

    assert message == "Congratulations Astro 1. You have been assigned to journey into the heart of the universe on the Spaceship Space A. Please be prepared to start your journey on 06/14/2025."

if __name__ == "__main__":
    print("assignToSpaceships should add astronauts to their first choices")
    testFirstChoiceAdd()
    print("testFirstChoiceAdd passed")
    print("assignToSpaceships should add astronauts to their second choices only if the first is at capacity")
    testSecondChoiceIfFirstFull()
    print("testSecondChoiceIfFirstFull passed")
    print("assignToSpaceships should assign an astronaut whose first choice spaceship is full but applied first to their next capacity spaceship before any other spaceship")
    testFirstChoiceFullButAppliedFirstAssignedToNextAvailableChoice()
    print("testFirstChoiceFull... passed")
    print("test formatNotification should format a message to the astronaut")
    testFormatNotificationShouldFormatMessage()
    print("testFormatNotificationShouldFormatMessage passed")
    print("All tests passed!")
