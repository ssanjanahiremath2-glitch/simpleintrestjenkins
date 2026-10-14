from simpleintrest import simple_intrest

def test_SI():
    asert simple_intrest(200,60,10) == 1200

    def test_SIZero():
        assert simple_intrest(10000,0,0) == 0