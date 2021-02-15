INPUTS = {
    "one category": {
        "rooms": {
            "Room 1": ["individual", "group"],
            "Room 2": ["individual", "group"],
            "Room 3": ["individual"],
        },
        "blocks": ["Morning", "Afternoon"],
        "staff": {"Therapy": ["Alice", "Bob"]},
        "groups": {"Therapy": ["Body Image"]},
        "individual": {"Therapy": 1},
        "patients": ["Dana", "Eddie", "Francine"],
    },
}

SCHEDULES = {
    "one_category": {
        "Morning": {
            "Room 1": {
                "type": "group",
                "group": "Body Image",
                "staff": "Alice",
                "patients": ["Dana", "Eddie"],
            },
            "Room 2": {
                "type": "individual",
                "staff": "Bob",
                "patients": ["Francine"],
            },
            "Room 3": {
                "type": None,
                "group": None,
                "staff": None,
                "patients": None,
            },
        },
        "Afternoon": {
            "Room 1": {
                "type": "individual",
                "group": None,
                "staff": "Alice",
                "patients": ["Dana"],
            },
            "Room 2": {
                "type": "individual",
                "staff": "Bob",
                "patients": ["Eddie"],
            },
            "Room 3": {
                "type": None,
                "group": None,
                "staff": None,
                "patients": None,
            },
        },
    },
}
