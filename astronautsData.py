import datetime

sampleAstronauts = [
    {
        'name': "Michelle Diaz",
        'applicationReceived': datetime.datetime(2025, 3, 22),
        'preferredShip': ["Nammu", "Abzu", "Ki"]
    },
    {
        'name': "Alexis Ha",
        'applicationReceived': datetime.datetime(2025, 3, 30),
        'preferredShip': ["Abzu", "Ki", "Nammu"]
    },
    {
        'name': "Judson Colomb",
        'applicationReceived': datetime.datetime(2025, 5, 2),
        'preferredShip': ["Ki", "Abzu", "Nammu"]
    },
    {
        'name': "Evia Rosalez",
        'applicationReceived': datetime.datetime(2025, 3, 22),
        'preferredShip': ["Ki", "Abzu", "Nammu"]
    },
    {
        'name': "Danille Bedrosian",
        'applicationReceived': datetime.datetime(2025, 4, 18),
        'preferredShip': ["Abzu", "Nammu", "Ki"]
    },
    {
        'name': "Verlene Brozena",
        'applicationReceived': datetime.datetime(2025, 3, 6),
        'preferredShip': ["Nammu", "Abzu", "Ki"]
    },
    {
        'name': "Taylor Kilfoyle",
        'applicationReceived': datetime.datetime(2025, 1, 10),
        'preferredShip': ["Nammu", "Abzu", "Ki"]
    },
    {
        'name': "Jonas Violett",
        'applicationReceived': datetime.datetime(2025, 3, 9),
        'preferredShip': ["Abzu", "Ki", "Nammu"]
    }
]

sampleShips = [
    { 'name': "Nammu", 'capacity': 5, 'expeditionDate': datetime.datetime(2025, 6, 1), 'assignedAstronauts': [] },
    { 'name': "Ki", 'capacity': 2, 'expeditionDate': datetime.datetime(2025, 9, 15), 'assignedAstronauts': [] },
    { 'name': "Abzu", 'capacity': 2, 'expeditionDate': datetime.datetime(2025, 6, 12), 'assignedAstronauts': [] }
]
