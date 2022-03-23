from solutions.CHK import checkout_solution

class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("AAAAAAAAB") == 360

    def test_chk(self):
        assert checkout_solution.checkout("AAAAAAAABB") == 375
    
    def test_chk(self):
        assert checkout_solution.checkout("EEB") == 360

