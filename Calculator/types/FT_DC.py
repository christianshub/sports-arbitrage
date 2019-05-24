import sqlite3

from Calculator.calcs import sameNames  # Compare names
from Calculator.calcs import o1o2       # Compare AO_odd1 | XB_odd2
from Calculator.calcs import o2o1       # Compare AO_odd2 | XB_odd1

""""""""""""""""""""""""""""""""""""""""""
"""      FULLTIME | DOUBLE CHANCE      """
""""""""""""""""""""""""""""""""""""""""""
def FT_DC():

    conn = sqlite3.connect("Live.db", timeout=30)
    for AO_list in list(conn.execute("SELECT * FROM {}".format("AO_FT"))):

        AO_scoreH = int(AO_list[2])
        AO_scoreA = int(AO_list[3])
        AO_team1  = AO_list[0]
        AO_team2  = AO_list[1]
        AO_info   = AO_list[4]
        AO_odd1   = round(float(AO_list[5]), 2)
        AO_odd2   = round(float(AO_list[7]), 2)

        for XB_list in list(conn.execute("SELECT * FROM {}".format("XB_DC"))):

            XB_team1 = XB_list[0]
            XB_team2 = XB_list[1]
            XB_info  = XB_list[4]
            XB_odd1  = round(float(XB_list[5]), 2)
            XB_odd2  = round(float(XB_list[7]), 2)

            if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):

                o1o2("AO FT 1", AO_team1, AO_team2, AO_odd1, "XB DC 2", XB_team1, XB_team2, XB_odd2)
                o2o1("AO FT 2", AO_team1, AO_team2, AO_odd2, "XB DC 1", XB_team1, XB_team2, XB_odd1)

