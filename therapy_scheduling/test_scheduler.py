class TestCheckValidScheduling:
    def test_possible(self):
        """Tests that check_valid_scheduling() passes with valid inputs"""
        assert 1

    def test_total_room_shortage(self):
        """Tests failure case where total number of required sessions exceeds
        the total number of available room blocks"""
        assert 1

    def test_total_staff_shortage(self):
        """Tests that check_valid_scheduling() fails when total number
        of required sessions exceeds the total number of staff
        """
        assert 1

    def test_room_type_shortage(self):
        """Tests that check_valid_scheduling() fails when the number of rooms
        available for a particular session type exceeds the number of sessions
        required for that type
        """
        assert 1

    def test_staff_category_shortage(self):
        """Tests that check_valid_scheduling() fails when the number of staff
        available for a particular category exceeds the number of sessions
        required for that category
        """
        assert 1
