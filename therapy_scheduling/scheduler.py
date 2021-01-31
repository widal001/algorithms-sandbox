def check_scheduling_exists(inputs):

    block_count = len(inputs["blocks"])

    # calculate avialable room blocks
    rooms = inputs["rooms"]
    total_rooms = len(rooms.keys())
    group_rooms = len([r for r, types in rooms.items() if "group" in types])
    ind_rooms = len([r for r, types in rooms.items() if "individual" in types])

    room_total = total_rooms * block_count
    room_group = group_rooms * block_count
    room_individual = ind_rooms * block_count
    print("Available group rooms")
    print(room_group)

    # calculate number of required sessions
    patients = inputs["patients"]
    groups = inputs["groups"]
    individual = inputs["individual"]

    session_group = sum(len(g) for g in groups.values())
    session_individual = patients * sum(individual.values())
    session_total = session_group + session_individual
    print("group sessions")
    print(session_group)

    if session_total > room_total:
        error = "There aren't enough rooms to schedule all required sessions"
        return False, error
    elif session_group > room_group:
        error = "There aren't enough group rooms to schedule all group sessions"
        return False, error
    elif session_individual > room_individual:
        error = (
            "There aren't enough individual rooms to schedule all individual sessions"
        )
        return False, error

    message = "A valid schedule is possible with the given inputs"
    return True, message
