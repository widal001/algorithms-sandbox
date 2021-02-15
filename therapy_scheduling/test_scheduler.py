from copy import deepcopy

from therapy_scheduling.data import INPUTS
from therapy_scheduling.scheduler import check_scheduling_exists


class TestCheckValidScheduling:
    def test_possible(self):
        """Tests that check_scheduling_exists() passes with valid inputs"""
        # setup
        inputs = INPUTS["one category"]
        exp_message = "A valid schedule is possible with the given inputs"

        # execution
        exists, message = check_scheduling_exists(inputs)

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
        exists, message = check_scheduling_exists(inputs)

        # validation
        assert exists is False
        assert message == error

    def test_individual_room_shortage(self):
        """Tests that check_scheduling_exists() fails when the number of rooms
        available for a particular session type exceeds the number of sessions
        required for that type
        """
        # setup
        inputs = deepcopy(INPUTS["one category"])
        inputs["rooms"]["Room 2"].remove("individual")
        del inputs["rooms"]["Room 3"]
        assert inputs["rooms"]["Room 2"] == ["group"]
        error = (
            "There aren't enough individual rooms to schedule all individual sessions"
        )

        # execution
        exists, message = check_scheduling_exists(inputs)

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
        assert inputs["rooms"]["Room 2"] == ["individual"]
        error = "There aren't enough group rooms to schedule all group sessions"

        # execution
        exists, message = check_scheduling_exists(inputs)

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
        exists, message = check_scheduling_exists(inputs)

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
        exists, message = check_scheduling_exists(inputs)

        # validation
        assert exists is False
        assert message == error
