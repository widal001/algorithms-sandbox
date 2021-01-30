ROOMS = {
    "Room A": 10,
    "Room B": 10,
    "Room C": 10,
}

STAFF = {
    "Alice": {
        "Category": "Therapy",
        "Groups": {"Eligible": [], "Assigned": []},
        "Sessions": {},
        "Patients": {},
    },
    "Bob": {},
    "Charlie": {},
}

GROUPS = [
    "Therapy 1",
    "Therapy 2",
    "Therapy 3",
    "Therapy 4",
    "Nutrition 5",
    "Nutrition 6",
]

BLOCKS = [
    "Session 1A",
    "Session 1B",
    "Session 1C",
    "Session 2A",
    "Session 2B",
    "Session 2C",
    "Session 3A",
    "Session 3B",
    "Session 3C",
]

DECISION_VARIABLES = [
    {
        "Rooms": 1,
        "Capacity": 20,
        "Blocks": 2,
        "Staff": {"A": 1},
        "Groups": 1,
        "Patients": 1,
    }
]
