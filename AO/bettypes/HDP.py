from AO.Database import AO_Db

def HDP(soup, H, A):

    HomeText = soup.find('span', class_='FTHDPHome').text
    AwayText = soup.find('span', class_='FTHDPAway').text
    HomeOdd  = soup.find('span', class_='FTHDPHomeOdd BetItem').text
    AwayOdd  = soup.find('span', class_='FTHDPAwayOdd BetItem').text

    scr_raw  = soup.find('span', class_='ScoreOrStartTime samehidegroup0').text
    scoreH   = scr_raw.split(":")[0].strip()
    scoreA   = scr_raw.split(":")[1].strip()

    if (len(HomeOdd) > 0) and (len(AwayOdd) > 0):
        # 0.25
        if '0-0.5' == HomeText:
            _list = ([(H, A, scoreH, scoreA, '-0.25', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)
        if '0-0.5' == AwayText:
            _list = ([(H, A, scoreH, scoreA, '+0.25', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)

        # 0.5
        if '0.5' == HomeText:
            _list = ([(H, A, scoreH, scoreA, '-0.5', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)
        if '0.5' == AwayText:
            _list = ([(H, A, scoreH, scoreA, '+0.5', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)

        # 0.75
        if '0.5-1' == HomeText:
            _list = ([(H, A, scoreH, scoreA, '-0.75', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)
        if '0.5-1' == AwayText:
            _list = ([(H, A, scoreH, scoreA, '+0.75', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)

        # 1
        if '1' == HomeText:
            _list = ([(H, A, scoreH, scoreA, '-1', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)
        if '1' == AwayText:
            _list = ([(H, A, scoreH, scoreA, '+1', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)

        # 1.25
        if '1-1.5' == HomeText:
            _list = ([(H, A, scoreH, scoreA, '-1.25', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)
        if '1-1.5' == AwayText:
            _list = ([(H, A, scoreH, scoreA, '+1.25', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)

        # 1.5
        if '1.5' == HomeText:
            _list = ([(H, A, scoreH, scoreA, '-1.5', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)
        if '1.5' == AwayText:
            _list = ([(H, A, scoreH, scoreA, '+1.5', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)

        # 1.75
        if '1.5-2' == HomeText:
            _list = ([(H, A, scoreH, scoreA, '-1.75', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)
        if '1.5-2' == AwayText:
            _list = ([(H, A, scoreH, scoreA, '+1.75', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)

        # 2
        if '2' == HomeText:
            _list = ([(H, A, scoreH, scoreA, '-2', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)
        if '2' == AwayText:
            _list = ([(H, A, scoreH, scoreA, '+2', HomeOdd, '1.0', AwayOdd)])
            AO_Db.w('AO_HDP', _list)

        # # 2.25
        # if '2-2.5' == HomeText:
        #     _list = ([(H, A, scoreH, scoreA, '-2.25', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)
        # if '2-2.5' == AwayText:
        #     _list = ([(H, A, scoreH, scoreA, '+2.25', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)

        # # 2.5
        # if '2.5' == HomeText:
        #     _list = ([(H, A, scoreH, scoreA, '-2.5', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)
        # if '2.5' == AwayText:
        #     _list = ([(H, A, scoreH, scoreA, '+2.5', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)

        # # 2.75
        # if '2.5-3' == HomeText:
        #     _list = ([(H, A, scoreH, scoreA, '-2.75', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)
        # if '2.5-3' == AwayText:
        #     _list = ([(H, A, scoreH, scoreA, '+2.75', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)

        # # 3
        # if '3' == HomeText:
        #     _list = ([(H, A, scoreH, scoreA, '-3', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)
        # if '3' == AwayText:
        #     _list = ([(H, A, scoreH, scoreA, '+3', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)

        # # 3.25
        # if '3-3.5' == HomeText:
        #     _list = ([(H, A, scoreH, scoreA, '-3.25', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)
        # if '3-3.5' == AwayText:
        #     _list = ([(H, A, scoreH, scoreA, '+3.25', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)

        # # 3.5
        # if '3.5' == HomeText:
        #     _list = ([(H, A, scoreH, scoreA, '-3.5', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)
        # if '3.5' == AwayText:
        #     _list = ([(H, A, scoreH, scoreA, '+3.5', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)

        # # 3.75
        # if '3.5-4' == HomeText:
        #     _list = ([(H, A, scoreH, scoreA, '-3.75', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)
        # if '3.5-4' == AwayText:
        #     _list = ([(H, A, scoreH, scoreA, '+3.75', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)

        # # 4
        # if '4' == HomeText:
        #     _list = ([(H, A, scoreH, scoreA, '-4', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)
        # if '4' == AwayText:
        #     _list = ([(H, A, scoreH, scoreA, '+4', HomeOdd, '1.0', AwayOdd)])
        #     AO_Db.w('AO_HDP', _list)

