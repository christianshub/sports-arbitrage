from fuzzywuzzy    import fuzz      # sameNames()
from decimal       import Decimal   # calcNumbers()
from Calculator.db import AR_Db     # AR_Db.w()


""""""""""""""""""""""""""""""""""""""""""
"""          NAME COMPARISON           """
""""""""""""""""""""""""""""""""""""""""""
def sameNames(bookie1_hometeam, bookie1_awayteam, bookie2_hometeam, bookie2_awayteam):

    team1s = fuzz.ratio(bookie1_hometeam, bookie2_hometeam)
    team2s = fuzz.ratio(bookie1_awayteam, bookie2_awayteam)

    if (team1s >= 50) and (team2s >= 50):

        print("SameNames: Comparison found 50/50! \n")
        print("Bookie1 HomeTeam ...", bookie1_hometeam, "|", bookie2_hometeam, "... Bookie2 HomeTeam", "ratio:", team1s)
        print("Bookie1 AwayTeam ...", bookie1_awayteam, "|", bookie2_awayteam, "... Bookie2 AwayTeam", "ratio:", team1s)
        print("----------------------------------------")

        return True

    elif (team1s >= 60) and (team2s >= 20):

        print("SameNames: Comparison found! 60/20 \n")
        print("Bookie1 HomeTeam ...", bookie1_hometeam, "|", bookie2_hometeam, "... Bookie2 HomeTeam", "ratio:", team1s)
        print("Bookie1 AwayTeam ...", bookie1_awayteam, "|", bookie2_awayteam, "... Bookie2 AwayTeam", "ratio:", team1s)
        print("----------------------------------------")

        return True

    elif (team1s >= 20) and (team2s >= 60):

        print("SameNames: Comparison found! 20/60 \n")
        print("Bookie1 HomeTeam ...", bookie1_hometeam, "|", bookie2_hometeam, "... Bookie2 HomeTeam", "ratio:", team1s)
        print("Bookie1 AwayTeam ...", bookie1_awayteam, "|", bookie2_awayteam, "... Bookie2 AwayTeam", "ratio:", team2s)
        print("----------------------------------------")

        return True
    else:
        return False


""""""""""""""""""""""""""""""""""""""""""
"""          ODDS CALCULATOR           """
""""""""""""""""""""""""""""""""""""""""""
def calcNumbers(AO_odd, XB_odd):

    invest = Decimal(1000)

    odd1 = ( Decimal(1.00) / Decimal(AO_odd) )
    odd2 = ( Decimal(1.00) / Decimal(XB_odd) )

    arb    = ( odd1 + odd2 )

    roi    = round((( invest / arb) - invest ), 2)

    placeA = round((( invest * odd1) / arb ), 2)
    placeB = round((( invest * odd2) / arb ), 2)

    if (roi >= 0):
        return { 'bool': 'true', 'roi': str(roi), 'AO_odd': str(AO_odd), 'XB_odd': str(XB_odd), 'placeA': str(placeA), 'placeB': str(placeB) }
    else:
        return { 'bool': 'false', 'roi': str(roi), 'AO_odd': str(AO_odd), 'XB_odd': str(XB_odd), 'placeA': str(placeA), 'placeB': str(placeB) }

""""""""""""""""""""""""""""""""""""""""""
"""          DB & CALC HELPER          """
""""""""""""""""""""""""""""""""""""""""""
# AO_ODD1 VS. XB_ODD2 (ONLY)
def o1o2(AO_text, AO_team1, AO_team2, AO_odd1, XB_text, XB_team1, XB_team2, XB_odd2):

    c = calcNumbers(AO_odd1, XB_odd2)
    if c['bool'] == 'true':
        _L = ([(c['roi'], str(AO_text), ("AO: " + AO_team1), ("AO: " + c['AO_odd']), ("AO: " + c['placeA']),
                          str(XB_text), ("XB: " + XB_team2), ("XB: " + c['XB_odd']), ("XB: " + c['placeB']) )])
        print(_L)
        AR_Db.w('Arbitrages', _L)
    else:
        _L = ([(c['roi'], str(AO_text), ("AO: " + AO_team1), ("AO: " + c['AO_odd']), ("AO: " + c['placeA']),
                          str(XB_text), ("XB: " + XB_team2), ("XB: " + c['XB_odd']), ("XB: " + c['placeB']) )])
        AR_Db.w('Calculations', _L)

# AO_ODD2 VS. XB_ODD1 (ONLY)
def o2o1(AO_text, AO_team1, AO_team2, AO_odd2, XB_text, XB_team1, XB_team2, XB_odd1):

    c = calcNumbers(AO_odd2, XB_odd1)
    if c['bool'] == 'true':
        _L = ([(c['roi'], str(AO_text), ("AO: " + AO_team1), ("AO: " + c['AO_odd']), ("AO: " + c['placeA']),
                          str(XB_text), ("BE: " + XB_team2), ("XB: " + c['XB_odd']), ("XB: " + c['placeB']) )])
        AR_Db.w('Arbitrages', _L)
    else:
        _L = ([(c['roi'], str(AO_text), ("AO: " + AO_team1), ("AO: " + c['AO_odd']), ("AO: " + c['placeA']),
                          str(XB_text), ("XB: " + XB_team2), ("XB: " + c['XB_odd']), ("XB: " + c['placeB']) )])
        AR_Db.w('Calculations', _L)