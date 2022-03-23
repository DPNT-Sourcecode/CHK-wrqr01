from solutions.CHK import checkout_solution

class TestChk():
    def test_chk1(self):
        o=checkout_solution.checkout()
        assert o.checkout("UUUUUUUU") == 240
    # def test_chk2(self):
    #     assert checkout_solution.checkout("EE")==80
    # def test_chk3(self):
    #     assert checkout_solution.checkout("AAAAAAAAB") == 360

    # def test_chk4(self):
    #     assert checkout_solution.checkout("AAAAAAAABB") == 375
    
    # def test_chk5(self):
    #     assert checkout_solution.checkout("EEB") == 80
    
    # def test_chk6(self):
    #     assert checkout_solution.checkout("EEEEBB") == 160

    # def test_chk7(self):
    #     assert checkout_solution.checkout("O") == 10
    
    # def test_chk8(self):
    #     assert checkout_solution.checkout("RRQR") == 150
    
    # def test_chk9(self):
    #     assert checkout_solution.checkout("F") == 10

    # def test_chk10(self):
    #     assert checkout_solution.checkout("UUU") == 120
    
    # def test_chk11(self):
    #     assert checkout_solution.checkout("UUUU") == 120
    
    # def test_chk12(self):
    #     assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965
    
    # def test_chk13(self):
    #     assert checkout_solution.checkout("VV") == 90
    
    # def test_chk14(self):
    #     assert checkout_solution.checkout("VVV") == 130
    
    # def test_chk15(self):
    #     assert checkout_solution.checkout("VVVV") == 180
    
    # def test_ch16(self):
    #     assert checkout_solution.checkout("AAAAAPPPPPUUUUEEBRRRQAAAHHHHHHHHHHVVVBBNNNMFFFKKQQQVVHHHHH") == 1580

    

