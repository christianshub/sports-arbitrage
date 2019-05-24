import sqlite3

from Calculator.calcs import sameNames  # Compare names
from Calculator.calcs import o1o2       # Compare AO_odd1 | XB_odd2
from Calculator.calcs import o2o1       # Compare AO_odd2 | XB_odd1

""""""""""""""""""""""""""""""""""""""""""
"""    HANDICAPS GOAL DIFFERENCE: 1    """
""""""""""""""""""""""""""""""""""""""""""


def HDP_GD_1():

    conn = sqlite3.connect("Live.db", timeout=30)
    for AO_list in list(conn.execute("SELECT * FROM {}".format("AO_HDP"))):
        AO_scoreH = int(AO_list[2])
        AO_scoreA = int(AO_list[3])
        AO_team1  = AO_list[0]
        AO_team2  = AO_list[1]
        AO_info   = AO_list[4]
        AO_odd1   = round(float(AO_list[5]), 2)
        AO_odd2   = round(float(AO_list[7]), 2)

        if (AO_scoreH - AO_scoreA == 1) or (AO_scoreA - AO_scoreH == 1):

            # HOMETEAM FØRER
            if (AO_scoreH > AO_scoreA):

                """"""""""""""""""""""""""""""""""""""""""
                """   HANDICAP VS. DOUBLE CHANCE, 0.5  """
                """"""""""""""""""""""""""""""""""""""""""
                for XB_list in list(conn.execute("SELECT * FROM {}".format("XB_DC"))):

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info  = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_odd2  = round(float(XB_list[7]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):

                        """ AH1 +0.5 vs. DC 2 """
                        if (AO_info == '+0.5'):
                            o1o2("AO: AH1 +0.5", AO_team1, AO_team2, AO_odd1, "XB: DC 2", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 0.5     """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):
                        """ AH1 -0.5 vs. AH2 +1.5 """
                        if (AO_info == '-0.5') and (XB_info2 == '+1.5'):
                            o1o2("AO: AH1 -0.5", AO_team1, AO_team2, AO_odd1, "XB: AH2 +1.5", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 0.75    """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):
                        """ AH1 +0.75 vs. AH2 -1.75 """
                        if (AO_info == '+0.75') and (XB_info2 == '-1.75'):
                            o1o2("AO: AH1 +0.75", AO_team1, AO_team2, AO_odd1, "XB: AH2 -1.75", XB_team1, XB_team2, XB_odd2)

                        """ AH1 -0.75 vs. AH2 +1.75 """
                        if (AO_info == '-0.75') and (XB_info2 == '+1.75'):
                            o1o2("AO: AH1 -0.75", AO_team1, AO_team2, AO_odd1, "XB: AH2 +1.75", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 1.25    """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):
                        """ AH1 +1.25 vs. AH2 -2.25 """
                        if (AO_info == '+1.25') and (XB_info2 == '-2.25'):
                            o1o2("AO: AH1 +1.25", AO_team1, AO_team2, AO_odd1, "XB: AH2 -2.25", XB_team1, XB_team2, XB_odd2)

                        """ AH1 -1.25 vs. AH2 +2.25 """
                        if (AO_info == '-1.25') and (XB_info2 == '+2.25'):
                            o1o2("AO: AH1 -1.25", AO_team1, AO_team2, AO_odd1, "XB: AH2 +2.25", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 1.5     """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):
                        """ AH1 +1.5 vs. AH2 -2.5 """
                        if (AO_info == '+1.5') and (XB_info2 == '-2.5'):
                            o1o2("AO: AH1 +1.5", AO_team1, AO_team2, AO_odd1, "XB: AH2 -2.5", XB_team1, XB_team2, XB_odd2)

                        """ AH1 -1.5 vs. AH2 +2.5 """
                        if (AO_info == '-1.5') and (XB_info2 == '+2.5'):
                            o1o2("AO: AH1 -1.5", AO_team1, AO_team2, AO_odd1, "XB: AH2 +2.5", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 1.75    """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):
                        """ AH1 +1.75 vs. AH2 -2.75 """
                        if (AO_info == '+1.75') and (XB_info2 == '-2.75'):
                            o1o2("AO: AH1 +1.75", AO_team1, AO_team2, AO_odd1, "XB: AH2 -2.75", XB_team1, XB_team2, XB_odd2)

                        """ AH1 -1.75 vs. AH2 +2.75 """
                        if (AO_info == '-1.75') and (XB_info2 == '+2.75'):
                            o1o2("AO: AH1 -1.75", AO_team1, AO_team2, AO_odd1, "XB: AH2 +2.75", XB_team1, XB_team2, XB_odd2)


            # AWAYTEAM FØRER
            elif (AO_scoreA > AO_scoreH):

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 0.5     """
                """"""""""""""""""""""""""""""""""""""""""

                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):
                        """ AH1 +0.5 vs. AH2 -1.5 """
                        if (AO_info == '+0.5') and (XB_info2 == '-1.5'):
                            o1o2("AO: AH1 +0.5", AO_team1, AO_team2, AO_odd1, "XB: AH2 -1.5", XB_team1, XB_team2, XB_odd2)


                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. FULLTIME, 0.5     """
                """"""""""""""""""""""""""""""""""""""""""
                for XB_list in list(conn.execute("SELECT * FROM {}".format("XB_FT"))):

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info  = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_odd2  = round(float(XB_list[7]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):

                        """ AH1 -0.5 vs. FT 2 """
                        if (AO_info == '-0.5'):
                            o1o2("AO: AH1 -0.5", AO_team1, AO_team2, AO_odd1, "XB: FT 2", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 0.75    """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):
                        """ AH1 +0.75 vs. AH2 -1.75 """
                        if (AO_info == '+0.75') and (XB_info2 == '-1.75'):
                            o1o2("AO: AH1 +0.75", AO_team1, AO_team2, AO_odd1, "XB: AH2 -1.75", XB_team1, XB_team2, XB_odd2)

                        """ AH1 -0.75 vs. AH2 -0.25 """
                        if (AO_info == '-0.75') and (XB_info2 == '-0.25'):
                            o1o2("AO: AH1 -0.75", AO_team1, AO_team2, AO_odd1, "XB: AH2 -0.25", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 1.25    """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):
                        """ AH1 +1.25 vs. AH2 -2.25 """
                        if (AO_info == '+1.25') and (XB_info2 == '-2.25'):
                            o1o2("AO: AH1 +1.25", AO_team1, AO_team2, AO_odd1, "XB: AH2 -2.25", XB_team1, XB_team2, XB_odd2)

                        """ AH1 -1.25 vs. AH2 +0.25 """
                        if (AO_info == '-1.25') and (XB_info2 == '+0.25'):
                            o1o2("AO: AH1 -1.25", AO_team1, AO_team2, AO_odd1, "XB: AH2 +0.25", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 1.5     """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):

                        """ AH1 +1.5 vs. AH2 -2.5 """
                        if (AO_info == '+1.5') and (XB_info2 == '-2.5'):
                            o1o2("AO: AH1 +1.5", AO_team1, AO_team2, AO_odd1, "XB: AH2 -2.5", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """  HANDICAP VS. DOUBLE CHANCE, 1.5   """
                """"""""""""""""""""""""""""""""""""""""""
                for XB_list in list(conn.execute("SELECT * FROM {}".format("XB_DC"))):

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info  = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_odd2  = round(float(XB_list[7]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):

                        """ AH1 -1.5 vs. DC 2 """
                        if (AO_info == '-1.5'):
                            o1o2("AO: AH1 -1.5", AO_team1, AO_team2, AO_odd1, "XB: DC 2", XB_team1, XB_team2, XB_odd2)

                """"""""""""""""""""""""""""""""""""""""""
                """     HANDICAP VS. HANDICAP, 1.75    """
                """"""""""""""""""""""""""""""""""""""""""
                XB_HDP = list(conn.execute("SELECT * FROM {}".format("XB_HDP")))
                for XB_list in XB_HDP:

                    XB_team1 = XB_list[0]
                    XB_team2 = XB_list[1]
                    XB_info1 = XB_list[4]
                    XB_odd1  = round(float(XB_list[5]), 2)
                    XB_info2 = XB_list[7]
                    XB_odd2  = round(float(XB_list[8]), 2)

                    if sameNames(AO_team1, AO_team2, XB_team1, XB_team2):

                        """ AH1 +1.75 vs. AH2 -2.75 """
                        if (AO_info == '+1.75') and (XB_info2 == '-2.75'):
                            o1o2("AO: AH1 +1.75", AO_team1, AO_team2, AO_odd1, "XB: AH2 -2.75", XB_team1, XB_team2, XB_odd2)

                        """ AH1 -1.75 vs. AH2 +0.75 """
                        if (AO_info == '-1.75') and (XB_info2 == '+0.75'):
                            o1o2("AO: AH1 -1.75", AO_team1, AO_team2, AO_odd1, "XB: AH2 +0.75", XB_team1, XB_team2, XB_odd2)
