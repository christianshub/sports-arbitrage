def FT_AOU(soup, tag, tbl, home, away):

    over = ('Total Over ')
    under = ('Total Under ')
    nullodd = '1.00'
    _025, _075, _125, _175 = [], [], [], []
    _225, _275, _325, _375 = [], [], [], []
    _425, _475, _525, _575 = [], [], [], []
    _625, _675, _725, _775 = [], [], [], []
    _825, _875, _925, _975 = [], [], [], []

    try:
        for i in soup.find(tag, tbl):

            odd = i.find('span', 'koeff').text
            bet_type = i.find('span', 'bet_type').text

            info = '0.25'
            if bet_type == (over + info):
                _025.insert(1, home)
                _025.insert(0, info)
                _025.insert(2, odd)
                _025.insert(3, nullodd)
            if bet_type == (under + info):
                _025.insert(4, odd)
                _025.insert(5, away)

            info = '0.75'
            if bet_type == (over + info):
                _075.insert(1, home)
                _075.insert(0, info)
                _075.insert(2, odd)
                _075.insert(3, nullodd)
            if bet_type == (under + info):
                _075.insert(4, odd)
                _075.insert(5, away)

            info = '1.25'
            if bet_type == (over + info):
                _125.insert(1, home)
                _125.insert(0, info)
                _125.insert(2, odd)
                _125.insert(3, nullodd)
            if bet_type == (under + info):
                _125.insert(4, odd)
                _125.insert(5, away)

            info = '1.75'
            if bet_type == (over + info):
                _175.insert(1, home)
                _175.insert(0, info)
                _175.insert(2, odd)
                _175.insert(3, nullodd)
            if bet_type == (under + info):
                _175.insert(4, odd)
                _175.insert(5, away)

            info = '2.25'
            if bet_type == (over + info):
                _225.insert(1, home)
                _225.insert(0, info)
                _225.insert(2, odd)
                _225.insert(3, nullodd)
            if bet_type == (under + info):
                _225.insert(4, odd)
                _225.insert(5, away)

            info = '2.75'
            if bet_type == (over + info):
                _275.insert(1, home)
                _275.insert(0, info)
                _275.insert(2, odd)
                _275.insert(3, nullodd)
            if bet_type == (under + info):
                _275.insert(4, odd)
                _275.insert(5, away)

            info = '3.25'
            if bet_type == (over + info):
                _325.insert(1, home)
                _325.insert(0, info)
                _325.insert(2, odd)
                _325.insert(3, nullodd)
            if bet_type == (under + info):
                _325.insert(4, odd)
                _325.insert(5, away)

            info = '3.75'
            if bet_type == (over + info):
                _375.insert(1, home)
                _375.insert(0, info)
                _375.insert(2, odd)
                _375.insert(3, nullodd)
            if bet_type == (under + info):
                _375.insert(4, odd)
                _375.insert(5, away)

            info = '4.25'
            if bet_type == (over + info):
                _425.insert(1, home)
                _425.insert(0, info)
                _425.insert(2, odd)
                _425.insert(3, nullodd)
            if bet_type == (under + info):
                _425.insert(4, odd)
                _425.insert(5, away)

            info = '4.75'
            if bet_type == (over + info):
                _475.insert(1, home)
                _475.insert(0, info)
                _475.insert(2, odd)
                _475.insert(3, nullodd)
            if bet_type == (under + info):
                _475.insert(4, odd)
                _475.insert(5, away)

            info = '5.25'
            if bet_type == (over + info):
                _525.insert(1, home)
                _525.insert(0, info)
                _525.insert(2, odd)
                _525.insert(3, nullodd)
            if bet_type == (under + info):
                _525.insert(4, odd)
                _525.insert(5, away)

            info = '5.75'
            if bet_type == (over + info):
                _575.insert(1, home)
                _575.insert(0, info)
                _575.insert(2, odd)
                _575.insert(3, nullodd)
            if bet_type == (under + info):
                _575.insert(4, odd)
                _575.insert(5, away)

            info = '6.25'
            if bet_type == (over + info):
                _625.insert(1, home)
                _625.insert(0, info)
                _625.insert(2, odd)
                _625.insert(3, nullodd)
            if bet_type == (under + info):
                _625.insert(4, odd)
                _625.insert(5, away)

            info = '6.75'
            if bet_type == (over + info):
                _675.insert(1, home)
                _675.insert(0, info)
                _675.insert(2, odd)
                _675.insert(3, nullodd)
            if bet_type == (under + info):
                _675.insert(4, odd)
                _675.insert(5, away)

            info = '7.25'
            if bet_type == (over + info):
                _725.insert(1, home)
                _725.insert(0, info)
                _725.insert(2, odd)
                _725.insert(3, nullodd)
            if bet_type == (under + info):
                _725.insert(4, odd)
                _725.insert(5, away)

            info = '7.75'
            if bet_type == (over + info):
                _775.insert(1, home)
                _775.insert(0, info)
                _775.insert(2, odd)
                _775.insert(3, nullodd)
            if bet_type == (under + info):
                _775.insert(4, odd)
                _775.insert(5, away)

            info = '8.25'
            if bet_type == (over + info):
                _825.insert(1, home)
                _825.insert(0, info)
                _825.insert(2, odd)
                _825.insert(3, nullodd)
            if bet_type == (under + info):
                _825.insert(4, odd)
                _825.insert(5, away)

            info = '8.75'
            if bet_type == (over + info):
                _875.insert(1, home)
                _875.insert(0, info)
                _875.insert(2, odd)
                _875.insert(3, nullodd)
            if bet_type == (under + info):
                _875.insert(4, odd)
                _875.insert(5, away)

            info = '9.25'
            if bet_type == (over + info):
                _925.insert(1, home)
                _925.insert(0, info)
                _925.insert(2, odd)
                _925.insert(3, nullodd)
            if bet_type == (under + info):
                _925.insert(4, odd)
                _925.insert(5, away)

            info = '9.75'
            if bet_type == (over + info):
                _975.insert(1, home)
                _975.insert(0, info)
                _975.insert(2, odd)
                _975.insert(3, nullodd)
            if bet_type == (under + info):
                _975.insert(4, odd)
                _975.insert(5, away)

        for _list in (_025, _075, _125, _175, _225, _275, _325, _375, _425,
                      _475, _525, _575, _625, _675, _725, _775, _825, _875,
                      _925, _975):
            if len(_list) == 6:
                # print("*** ASIAN OVER/UNDER ***")
                print(tuple([(_list)]))
                XB_Db.w('XB_OU', tuple([(_list)]))

    except AttributeError:
        pass
    except TypeError:
        pass


if __name__ == 'bettypes.FT_AOU':
    from XBdatabase import XB_Db
elif __name__ == 'XB.bettypes.FT_AOU':
    from XB.Database import XB_Db
