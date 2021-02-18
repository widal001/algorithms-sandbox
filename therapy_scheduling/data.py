INPUTS = {
    "one category": {
        "rooms": {
            "Room 1": ["private", "group"],
            "Room 2": ["private", "group"],
            "Room 3": ["private"],
        },
        "blocks": ["Morning", "Afternoon"],
        "staff": {"Therapy": ["Alice", "Bob"]},
        "groups": {"Therapy": ["Body Image"]},
        "private": {"Therapy": 1},
        "patients": ["Dana", "Eddie", "Francine"],
    },
}

SCHEDULES = {
    "one category": {
        "Morning": {
            "Room 1": {
                "type": "group",
                "category": "Therapy",
                "group": "Body Image",
                "staff": "Alice",
                "patients": ["Dana", "Eddie"],
            },
            "Room 2": {
                "type": "private",
                "category": "Therapy",
                "group": None,
                "staff": "Bob",
                "patients": ["Francine"],
            },
            "Room 3": {
                "type": None,
                "category": None,
                "group": None,
                "staff": None,
                "patients": None,
            },
        },
        "Afternoon": {
            "Room 1": {
                "type": "private",
                "category": "Therapy",
                "group": None,
                "staff": "Alice",
                "patients": ["Dana"],
            },
            "Room 2": {
                "type": "private",
                "category": "Therapy",
                "staff": "Bob",
                "patients": ["Eddie"],
            },
            "Room 3": {
                "type": None,
                "category": None,
                "group": None,
                "staff": None,
                "patients": None,
            },
        },
    },
}

SCHEDULE_OBJECTS = {
    "available": {
        "staff": {
            "Alice": ["Morning", "Afternoon"],
            "Bob": ["Morning", "Afternoon"],
        },
        "rooms": {
            "Room 1": ["Morning", "Afternoon"],
            "Room 2": ["Morning", "Afternoon"],
        },
    },
    "to schedule": {
        "groups": {
            "Body Image": None,
        },
        "patients": {
            "Dana": {
                "blocks": ["Morning", "Afternoon"],
                "group": [],
                "private": {"Therapy": {"staff": None, "count": 0}},
            },
            "Eddie": {
                "blocks": ["Morning", "Afternoon"],
                "groups": [],
                "privates": {"Therapy": {"staff": None, "count": 0}},
            },
            "Francine": {
                "blocks": ["Morning", "Afternoon"],
                "groups": [],
                "privates": {"Therapy": {"staff": None, "count": 0}},
            },
        },
    },
}

""
