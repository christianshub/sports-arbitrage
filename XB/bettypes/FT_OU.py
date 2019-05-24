def FT_OU(soup, tag, tbl, home, away):

    over = ('Total Over ')
    under = ('Total Under ')
    nullodd = '1.00'
    _050, _100, _150, _200 = [], [], [], []
    _250, _300, _350, _400 = [], [], [], []
    _450, _500, _550, _600 = [], [], [], []
    _650, _700, _750, _800 = [], [], [], []
    _850, _900, _950, _1000 = [], [], [], []

    try:
        for i in soup.find(tag, tbl):

            odd = i.find('span', 'koeff').text
            bet_type = i.find('span', 'bet_type').text

            info = '0.5'
            if bet_type == (over + info):
                _050.insert(1, home)
                _050.insert(0, info)
                _050.insert(2, odd)
                _050.insert(3, nullodd)
            if bet_type == (under + info):
                _050.insert(4, odd)
                _050.insert(5, away)

            info = '1'
            if bet_type == (over + info):
                _100.insert(1, home)
                _100.insert(0, info)
                _100.insert(2, odd)
                _100.insert(3, nullodd)
            if bet_type == (under + info):
                _100.insert(4, odd)
                _100.insert(5, away)

            info = '1.5'
            if bet_type == (over + info):
                _150.insert(1, home)
                _150.insert(0, info)
                _150.insert(2, odd)
                _150.insert(3, nullodd)
            if bet_type == (under + info):
                _150.insert(4, odd)
                _150.insert(5, away)

            info = '2'
            if bet_type == (over + info):
                _200.insert(1, home)
                _200.insert(0, info)
                _200.insert(2, odd)
                _200.insert(3, nullodd)
            if bet_type == (under + info):
                _200.insert(4, odd)
                _200.insert(5, away)

            info = '2.5'
            if bet_type == (over + info):
                _250.insert(1, home)
                _250.insert(0, info)
                _250.insert(2, odd)
                _250.insert(3, nullodd)
            if bet_type == (under + info):
                _250.insert(4, odd)
                _250.insert(5, away)

            info = '3'
            if bet_type == (over + info):
                _300.insert(1, home)
                _300.insert(0, info)
                _300.insert(2, odd)
                _300.insert(3, nullodd)
            if bet_type == (under + info):
                _300.insert(4, odd)
                _300.insert(5, away)

            info = '3.5'
            if bet_type == (over + info):
                _350.insert(1, home)
                _350.insert(0, info)
                _350.insert(2, odd)
                _350.insert(3, nullodd)
            if bet_type == (under + info):
                _350.insert(4, odd)
                _350.insert(5, away)

            info = '4'
            if bet_type == (over + info):
                _400.insert(1, home)
                _400.insert(0, info)
                _400.insert(2, odd)
                _400.insert(3, nullodd)
            if bet_type == (under + info):
                _400.insert(4, odd)
                _400.insert(5, away)

            info = '4.5'
            if bet_type == (over + info):
                _450.insert(1, home)
                _450.insert(0, info)
                _450.insert(2, odd)
                _450.insert(3, nullodd)
            if bet_type == (under + info):
                _450.insert(4, odd)
                _450.insert(5, away)

            info = '5'
            if bet_type == (over + info):
                _500.insert(1, home)
                _500.insert(0, info)
                _500.insert(2, odd)
                _500.insert(3, nullodd)
            if bet_type == (under + info):
                _500.insert(4, odd)
                _500.insert(5, away)

            info = '5.5'
            if bet_type == (over + info):
                _550.insert(1, home)
                _550.insert(0, info)
                _550.insert(2, odd)
                _550.insert(3, nullodd)
            if bet_type == (under + info):
                _550.insert(4, odd)
                _550.insert(5, away)

            info = '6'
            if bet_type == (over + info):
                _600.insert(1, home)
                _600.insert(0, info)
                _600.insert(2, odd)
                _600.insert(3, nullodd)
            if bet_type == (under + info):
                _600.insert(4, odd)
                _600.insert(5, away)

            info = '6.5'
            if bet_type == (over + info):
                _650.insert(1, home)
                _650.insert(0, info)
                _650.insert(2, odd)
                _650.insert(3, nullodd)
            if bet_type == (under + info):
                _650.insert(4, odd)
                _650.insert(5, away)

            info = '7'
            if bet_type == (over + info):
                _700.insert(1, home)
                _700.insert(0, info)
                _700.insert(2, odd)
                _700.insert(3, nullodd)
            if bet_type == (under + info):
                _700.insert(4, odd)
                _700.insert(5, away)

            info = '7.5'
            if bet_type == (over + info):
                _750.insert(1, home)
                _750.insert(0, info)
                _750.insert(2, odd)
                _750.insert(3, nullodd)
            if bet_type == (under + info):
                _750.insert(4, odd)
                _750.insert(5, away)

            info = '8'
            if bet_type == (over + info):
                _800.insert(1, home)
                _800.insert(0, info)
                _800.insert(2, odd)
                _800.insert(3, nullodd)
            if bet_type == (under + info):
                _800.insert(4, odd)
                _800.insert(5, away)

            info = '8.5'
            if bet_type == (over + info):
                _850.insert(1, home)
                _850.insert(0, info)
                _850.insert(2, odd)
                _850.insert(3, nullodd)
            if bet_type == (under + info):
                _850.insert(4, odd)
                _850.insert(5, away)

            info = '9'
            if bet_type == (over + info):
                _900.insert(1, home)
                _900.insert(0, info)
                _900.insert(2, odd)
                _900.insert(3, nullodd)
            if bet_type == (under + info):
                _900.insert(4, odd)
                _900.insert(5, away)

            info = '9.5'
            if bet_type == (over + info):
                _950.insert(1, home)
                _950.insert(0, info)
                _950.insert(2, odd)
                _950.insert(3, nullodd)
            if bet_type == (under + info):
                _950.insert(4, odd)
                _950.insert(5, away)

            info = '10'
            if bet_type == (over + info):
                _1000.insert(1, home)
                _1000.insert(0, info)
                _1000.insert(2, odd)
                _1000.insert(3, nullodd)
            if bet_type == (under + info):
                _1000.insert(4, odd)
                _1000.insert(5, away)

        for _list in (_050, _100, _150, _200, _250, _300, _350, _400, _450,
                      _500, _550, _600, _650, _700, _750, _800, _850, _900,
                      _950, _1000):
            if len(_list) == 6:
                # print("*** OVER/UNDER *** ")
                print(tuple([(_list)]))
                XB_Db.w('XB_OU', tuple([(_list)]))

    except AttributeError:
        pass
    except TypeError:
        pass


if __name__ == 'bettypes.FT_OU':
    from XBdatabase import XB_Db
elif __name__ == 'XB.bettypes.FT_OU':
    from XB.Database import XB_Db
