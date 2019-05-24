import sqlite3

from Calculator.calcs import sameNames  # Compare names
from Calculator.calcs import o1o2       # Compare AO_odd1 | XB_odd2
from Calculator.calcs import o2o1       # Compare AO_odd2 | XB_odd1

""""""""""""""""""""""""""""""""""""""""""
"""      OVER/UNDER | OVER/UNDER       """
""""""""""""""""""""""""""""""""""""""""""
def OU():

    conn = sqlite3.connect("Live.db", timeout=30)
    for AO_list in list(conn.execute("SELECT * FROM {}".format("AO_OU"))):

        AO_scoreH = int(AO_list[2])
        AO_scoreA = int(AO_list[3])
        AO_team1  = AO_list[0]
        AO_team2  = AO_list[1]
        AO_info   = AO_list[4]
        AO_odd1   = round(float(AO_list[5]), 2)
        AO_odd2   = round(float(AO_list[7]), 2)

        for XB_list in list(conn.execute("SELECT * FROM {}".format("XB_OU"))):

                XB_team1 = XB_list[0]
                XB_team2 = XB_list[1]
                XB_info  = XB_list[4]
                XB_odd1  = round(float(XB_list[5]), 2)
                XB_odd2  = round(float(XB_list[7]), 2)

                if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):

                    # 0.5
                    if (AO_info == '0.5') and (XB_info == '0.5'):

                      o1o2("AO OVER  0.5", AO_team1, AO_team2, AO_odd1, "BE UNDER 0.5", XB_team1, XB_team2, XB_odd2)
                      o2o1("AO UNDER 0.5", AO_team1, AO_team2, AO_odd2, "BE OVER  0.5", XB_team1, XB_team2, XB_odd1)

                    # 1.0
                    if (AO_info == '1') and (XB_info == '1'):

                      o1o2("AO OVER  1", AO_team1, AO_team2, AO_odd1, "BE UNDER 1", XB_team1, XB_team2, XB_odd2)
                      o2o1("AO UNDER 1", AO_team1, AO_team2, AO_odd2, "BE OVER  1", XB_team1, XB_team2, XB_odd1)

                    # 1.5
                    if (AO_info == '1.5') and (XB_info == '1.5'):

                      o1o2("AO OVER  1.5", AO_team1, AO_team2, AO_odd1, "BE UNDER 1.5", XB_team1, XB_team2, XB_odd2)
                      o2o1("AO UNDER 1.5", AO_team1, AO_team2, AO_odd2, "BE OVER  1.5", XB_team1, XB_team2, XB_odd1)

                    # 2
                    if (AO_info == '2') and (XB_info == '2'):

                      o1o2("AO OVER  2", AO_team1, AO_team2, AO_odd1, "BE UNDER 2", XB_team1, XB_team2, XB_odd2)
                      o2o1("AO UNDER 2", AO_team1, AO_team2, AO_odd2, "BE OVER  2", XB_team1, XB_team2, XB_odd1)

                    # 2.5
                    if (AO_info == '2.5') and (XB_info == '2.5'):

                      o1o2("AO OVER  2.5", AO_team1, AO_team2, AO_odd1, "BE UNDER 2.5", XB_team1, XB_team2, XB_odd2)
                      o2o1("AO UNDER 2.5", AO_team1, AO_team2, AO_odd2, "BE OVER  2.5", XB_team1, XB_team2, XB_odd1)
