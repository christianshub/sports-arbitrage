from AO.Database import AO_Db

def FT(soup, H, A):
    FT_1 = soup.find('span', class_='FTHomeOdd BetItem').text
    FT_2 = soup.find('span', class_='FTAwayOdd BetItem').text
    FT_X = soup.find('span', class_='FTDrawOdd BetItem').text

    scr_raw = soup.find('span', class_='ScoreOrStartTime samehidegroup0').text
    scoreH  = scr_raw.split(":")[0].strip()
    scoreA  = scr_raw.split(":")[1].strip()

    if len(FT_1) > 0:
        _FT = ([(H, A, scoreH, scoreA, "FT", FT_1, FT_X, FT_2)])
        AO_Db.w('AO_FT', _FT)
