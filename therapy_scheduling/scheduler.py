from pprint import pprint
from collections import defaultdict


def inverse(dict_in, duplicates=False):
    dict_out = {}
    for k, v in dict_in.items():
        for x in v:
            if duplicates:
                dict_out.setdefault(x, []).append(k)
            else:
                dict_out[x] = k
    return dict_out


def count(_dict, type):
    return len([k for k, v in _dict.items() if type in v])


class Practice:
    def __init__(self, input):
        self.blocks = input["blocks"]
        self.rooms = input["rooms"]
        self.private = input["private"]
        self.groups = inverse(input["groups"])
        self.categories = list(set(input["groups"]) | set(input["private"]))
        self.staff = inverse(input["staff"], duplicates=True)
        self.patients = {p: {} for p in input["patients"]}

        self.get_counts()

    def get_counts(self):

        block_count = len(self.blocks)
        patient_count = len(self.patients)
        self.block_count = block_count
        self.patient_count = patient_count

        # count rooms
        rooms = self.rooms
        self.room_count = {
            "total": len(rooms) * block_count,
            "group": count(rooms, "group") * block_count,
            "private": count(rooms, "private") * block_count,
        }

        # count staff
        staff = self.staff
        self.staff_count = {"total": len(staff) * block_count, "category": {}}
        for c in self.categories:
            cat_count = count(staff, c) * block_count
            self.staff_count["category"][c] = cat_count

        # count sessions
        groups = self.groups
        session_private = patient_count * sum(self.private.values())
        session_group = len(groups)
        self.session_count = {
            "total": session_private + session_group,
            "group": session_group,
            "private": session_private,
            "category": {},
        }
        for c in self.categories:
            cat_count = count(groups, c) + (self.private[c] * patient_count)
            self.session_count["category"][c] = cat_count

    def check_scheduling_exists(self):

        # get counts
        sessions = self.session_count
        rooms = self.room_count
        staff = self.staff_count

        # error statements
        def staff_error(x=""):
            return f"There aren't enough {x}staff to lead all {x}sessions"

        def room_error(x=""):
            return f"There aren't enough {x}rooms to schedule all {x}sessions"

        # check room and total staff capacity
        if sessions["total"] > rooms["total"]:
            return False, room_error()
        elif sessions["group"] > rooms["group"]:
            return False, room_error("group ")
        elif sessions["private"] > rooms["private"]:
            return False, room_error("private ")
        elif sessions["total"] > staff["total"]:
            return False, staff_error()

        # check staff capacity by category
        for c in self.categories:
            if sessions["category"][c] > staff["category"][c]:
                return False, staff_error(c + " ")

        message = "A valid schedule is possible with the given inputs"
        return True, message
