from copy import deepcopy

from therapy_scheduling.data import INPUTS, SCHEDULES
from therapy_scheduling.scheduler import Practice


class TestCheckSchedulingExists:
    def test_possible(self):
        """Tests that check_scheduling_exists() passes with valid inputs"""
        # setup
        inputs = INPUTS["one category"]
        exp_message = "A valid schedule is possible with the given inputs"

        # execution
        p = Practice(inputs)
        exists, message = p.check_scheduling_exists()

        # validation
        assert exists
        assert message == exp_message

    def test_total_room_shortage(self):
        """Tests failure case where total number of required sessions exceeds
        the total number of available room blocks"""
        # setup
        inputs = deepcopy(INPUTS["one category"])
        del inputs["rooms"]["Room 2"]
        del inputs["rooms"]["Room 3"]
        error = "There aren't enough rooms to schedule all sessions"

        # execution
        p = Practice(inputs)
        exists, message = p.check_scheduling_exists()

        # validation
        assert exists is False
        assert message == error

    def test_private_room_shortage(self):
        """Tests that check_scheduling_exists() fails when the number of rooms
        available for a particular session type exceeds the number of sessions
        required for that type
        """
        # setup
        inputs = deepcopy(INPUTS["one category"])
        inputs["rooms"]["Room 2"].remove("private")
        del inputs["rooms"]["Room 3"]
        assert inputs["rooms"]["Room 2"] == ["group"]
        error = "There aren't enough private rooms to schedule all private sessions"

        # execution
        p = Practice(inputs)
        exists, message = p.check_scheduling_exists()

        # validation
        assert exists is False
        assert message == error

    def test_group_room_shortage(self):
        """Tests that check_scheduling_exists() fails when the number of rooms
        available for a particular session type exceeds the number of sessions
        required for that type
        """
        # setup
        inputs = deepcopy(INPUTS["one category"])
        inputs["groups"]["Therapy"].extend(["Communication", "Nutrition"])
        inputs["rooms"]["Room 2"].remove("group")
        assert inputs["rooms"]["Room 2"] == ["private"]
        error = "There aren't enough group rooms to schedule all group sessions"

        # execution
        p = Practice(inputs)
        print(p.room_count)
        print(p.session_count)
        exists, message = p.check_scheduling_exists()

        # validation
        assert exists is False
        assert message == error

    def test_total_staff_shortage(self):
        """Tests that check_scheduling_exists() fails when total number
        of required sessions exceeds the total number of staff, even when one
        staff member is listed under multiple categories
        """
        # setup
        inputs = deepcopy(INPUTS["one category"])
        inputs["staff"]["Therapy"].remove("Bob")
        assert inputs["staff"]["Therapy"] == ["Alice"]
        inputs["staff"]["Nutrition"] = ["Alice"]  # tests double counting
        error = "There aren't enough staff to lead all sessions"

        # execution
        p = Practice(inputs)
        exists, message = p.check_scheduling_exists()

        # validation
        assert exists is False
        assert message == error

    def test_staff_category_shortage(self):
        """Tests that check_scheduling_exists() fails when the number of staff
        available for a particular category exceeds the number of sessions
        required for that category
        """
        # setup
        inputs = deepcopy(INPUTS["one category"])
        inputs["staff"]["Therapy"].remove("Bob")
        assert inputs["staff"]["Therapy"] == ["Alice"]
        inputs["staff"]["Nutrition"] = ["Charlie"]
        error = "There aren't enough Therapy staff to lead all Therapy sessions"

        # execution
        p = Practice(inputs)
        exists, message = p.check_scheduling_exists()

        # validation
        assert exists is False
        assert message == error


class TestPractice:
    def test_read_inputs_one(self):
        # setup
        inputs = INPUTS["one category"]
        patients = ["Dana", "Eddie", "Francine"]
        groups = ["Body Image"]
        staff = ["Alice", "Bob"]
        rooms = ["Room 1", "Room 2", "Room 3"]
        blocks = ["Morning", "Afternoon"]
        categories = ["Therapy"]

        # setup counts
        room_count = {"group": 4, "private": 6, "total": 6}
        session_count = {
            "private": 3,
            "group": 1,
            "total": 4,
            "category": {"Therapy": 4},
        }
        staff_count = {"total": 4, "category": {"Therapy": 4}}

        # execution
        p = Practice(inputs)

        # validation - inputs
        assert list(p.patients.keys()) == patients
        assert list(p.groups.keys()) == groups
        assert list(p.staff.keys()) == staff
        assert list(p.rooms.keys()) == rooms
        assert p.blocks == blocks
        assert p.categories == categories

        # validation - counts
        assert p.patient_count == 3
        assert p.block_count == 2
        assert p.room_count == room_count
        assert p.staff_count == staff_count
        assert p.session_count == session_count
