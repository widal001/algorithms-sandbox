from collections import defaultdict


def check_scheduling_exists(inputs):

    counts = {}
    blocks = len(inputs["blocks"])
    counts["blocks"] = blocks

    # calculate number of available rooms
    rooms = inputs["rooms"].items()
    room_count = lambda x: len([r for r, types in rooms if x in types])
    counts["rooms"] = {
        "all": len(rooms) * blocks,
        "group": room_count("group") * blocks,
        "individual": room_count("individual") * blocks,
    }

    # calculate number of required sessions
    patients = inputs["patients"]
    groups = inputs["groups"]
    sessions = inputs["individual"]
    # categories = groups.keys()

    session_group = sum(len(g) for g in groups.values())
    session_individual = patients * sum(sessions.values())
    session_total = session_group + session_individual

    if session_total > counts["rooms"]["all"]:
        error = "There aren't enough rooms to schedule all required sessions"
        return False, error
    elif session_group > counts["rooms"]["group"]:
        error = "There aren't enough group rooms to schedule all group sessions"
        return False, error
    elif session_individual > counts["rooms"]["individual"]:
        error = (
            "There aren't enough individual rooms to schedule all individual sessions"
        )
        return False, error

    message = "A valid schedule is possible with the given inputs"
    return True, message
