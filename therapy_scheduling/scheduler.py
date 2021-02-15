def check_scheduling_exists(inputs):

    # grab variables from input
    patient_count = len(inputs["patients"])
    groups = inputs["groups"]
    individuals = inputs["individual"]
    rooms = inputs["rooms"]
    staff = inputs["staff"]
    block_count = len(inputs["blocks"])

    # calculate required sessions
    session_group = sum(len(g) for g in groups.values())
    session_individual = patient_count * sum(individuals.values())
    session_total = session_group + session_individual

    # calculate total number of staff and rooms
    unique_staff = set().union(*staff.values())
    staff_total = len(unique_staff) * block_count

    # calculate total number of rooms
    room_count = lambda x: len([r for r, types in rooms.items() if x in types])
    room_total = len(rooms) * block_count
    room_group = room_count("group") * block_count
    room_individual = room_count("individual") * block_count

    # error statements
    def staff_error(x=""):
        return f"There aren't enough {x}staff to lead all {x}sessions"

    def room_error(x=""):
        return f"There aren't enough {x}rooms to schedule all {x}sessions"

    # check room and total staff capacity
    if session_total > room_total:
        return False, room_error()
    elif session_group > room_group:
        return False, room_error("group ")
    elif session_individual > room_individual:
        return False, room_error("individual ")
    elif session_total > staff_total:
        return False, staff_error()

    # check staff capacity by category
    categories = set(groups.keys()) | set(individuals.keys())
    for c in categories:
        staff_count = len(staff[c]) * block_count
        session_count = len(groups[c]) + (individuals[c] * patient_count)
        if session_count > staff_count:
            return False, staff_error(c + " ")

    message = "A valid schedule is possible with the given inputs"
    return True, message


def create_schedule(inputs):
    pass
