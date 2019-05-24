from AO.Database import AO_Db

def OU(soup, H, A):

    Goal    = soup.find('span', class_='FTGoal').text
    Over    = soup.find('span', class_='FTOver BetItem').text
    Under   = soup.find('span', class_='FTUnder BetItem').text

    scr_raw = soup.find('span', class_='ScoreOrStartTime samehidegroup0').text
    scoreH  = scr_raw.split(":")[0].strip()
    scoreA  = scr_raw.split(":")[1].strip()

    if (len(Over) > 0) and (len(Under) > 0):
        if '0-0.5' == Goal:
            _025 = ([(H, A, scoreH, scoreA, '0.25', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _025)

        if '0.5' == Goal:
            _050 = ([(H, A, scoreH, scoreA, '0.5', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _050)

        if '0.5-1' == Goal:
            _075 = ([(H, A, scoreH, scoreA, '0.75', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _075)

        if '1' == Goal:
            _100 = ([(H, A, scoreH, scoreA, '1', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _100)

        if '1-1.5' == Goal:
            _125 = ([(H, A, scoreH, scoreA, '1.25', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _125)

        if '1.5' == Goal:
            _15 = ([(H, A, scoreH, scoreA, '1.5', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _15)

        if '1.5-2' == Goal:
            _175 = ([(H, A, scoreH, scoreA, '1.75', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _175)

        if '2' == Goal:
            _200 = ([(H, A, scoreH, scoreA, '2', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _200)

        if '2-2.5' == Goal:
            _225 = ([(H, A, scoreH, scoreA, '2.25', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _225)

        if '2.5' == Goal:
            _25 = ([(H, A, scoreH, scoreA, '2.5', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _25)

        if '2.5-3' == Goal:
            _275 = ([(H, A, scoreH, scoreA, '2.75', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _275)

        if '3' == Goal:
            _300 = ([(H, A, scoreH, scoreA, '3', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _300)

        if '3-3.5' == Goal:
            _325 = ([(H, A, scoreH, scoreA, '3.25', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _325)

        if '3.5' == Goal:
            _35 =([(H, A, scoreH, scoreA, '3.5', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _35)

        if '3.5-4' == Goal:
            _375 = ([(H, A, scoreH, scoreA, '3.75', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _375)

        if '4' == Goal:
            _400 = ([(H, A, scoreH, scoreA, '4', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _400)

        if '4-4.5' == Goal:
            _425 = ([(H, A, scoreH, scoreA, '4.25', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _425)

        if '4.5' == Goal:
            _45 = ([(H, A, scoreH, scoreA, '4.5', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _45)

        if '4.5-5' == Goal:
            _475 = ([(H, A, scoreH, scoreA, '4.75', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _475)

        if '5' == Goal:
            _500 = ([(H, A, scoreH, scoreA, '5', Over, '1.0', Under)])
            if (Over != '') and (Under != ''):
                AO_Db.w('AO_OU', _500)
