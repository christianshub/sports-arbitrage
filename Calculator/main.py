import sqlite3

from Calculator.db              import AR_Db
from Calculator.types.HDP_GD_0	import HDP_GD_0
from Calculator.types.HDP_GD_1	import HDP_GD_1
from Calculator.types.HDP_GD_2	import HDP_GD_2
from Calculator.types.HDP_GD_3	import HDP_GD_3
from Calculator.types.HDP_GD_4	import HDP_GD_4
from Calculator.types.HDP_GD_5	import HDP_GD_5
from Calculator.types.OU		import OU
from Calculator.types.FT_DC 	import FT_DC

class Calculator:

    def __init__(self):
        pass

    def compare2ways(self):

        OU()
        FT_DC()
        HDP_GD_0() # HDP goal difference 0
        HDP_GD_1()
        HDP_GD_2()
        HDP_GD_3() # DOBBELTCHECKET
        HDP_GD_4()
        HDP_GD_5()

