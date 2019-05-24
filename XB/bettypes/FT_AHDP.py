def FT_AHDP(soup, tag, tbl, home, away):

    _0, _1, _2, _3 = [], [], [], []
    _4, _5, _6, _7 = [], [], [], []
    _8, _9, _10, _11 = [], [], [], []
    _12, _13, _14 = [], [], []

    try:
        for i in soup.find(tag, tbl):

            nullodd = '1.00'
            odd = i.find('span', 'koeff').text
            bet_type = i.find('span', 'bet_type').text
            data_type = i.find('span', 'bet_type').get('data-type')

            """ Home -, Away + """
            info = '(-3.75)'
            if info in bet_type and data_type == '3829':
                _0.insert(1, home)
                _0.insert(0, info.replace('(', '').replace(')', ''))
                _0.insert(2, odd)
                _0.insert(3, nullodd)
            info = '(+3.75)'
            if info in bet_type and data_type == '3830':
                _0.insert(4, odd)
                _0.insert(5, away)

            info = '(-3.25)'
            if info in bet_type and data_type == '3829':
                _1.insert(1, home)
                _1.insert(0, info.replace('(', '').replace(')', ''))
                _1.insert(2, odd)
                _1.insert(3, nullodd)
            info = '(+3.25)'
            if info in bet_type and data_type == '3830':
                _1.insert(4, odd)
                _1.insert(5, away)

            info = '(-2.75)'
            if info in bet_type and data_type == '3829':
                _2.insert(1, home)
                _2.insert(0, info.replace('(', '').replace(')', ''))
                _2.insert(2, odd)
                _2.insert(3, nullodd)
            info = '(+2.75)'
            if info in bet_type and data_type == '3830':
                _2.insert(4, odd)
                _2.insert(5, away)

            info = '(-2.25)'
            if info in bet_type and data_type == '3829':
                _3.insert(1, home)
                _3.insert(0, info.replace('(', '').replace(')', ''))
                _3.insert(2, odd)
                _3.insert(3, nullodd)
            info = '(+2.25)'
            if info in bet_type and data_type == '3830':
                _3.insert(4, odd)
                _3.insert(5, away)

            info = '(-1.75)'
            if info in bet_type and data_type == '3829':
                _4.insert(1, home)
                _4.insert(0, info.replace('(', '').replace(')', ''))
                _4.insert(2, odd)
                _4.insert(3, nullodd)
            info = '(+1.75)'
            if info in bet_type and data_type == '3830':
                _4.insert(4, odd)
                _4.insert(5, away)

            info = '(-1.25)'
            if info in bet_type and data_type == '3829':
                _5.insert(1, home)
                _5.insert(0, info.replace('(', '').replace(')', ''))
                _5.insert(2, odd)
                _5.insert(3, nullodd)
            info = '(+1.25)'
            if info in bet_type and data_type == '3830':
                _5.insert(4, odd)
                _5.insert(5, away)

            info = '(-0.75)'
            if info in bet_type and data_type == '3829':
                _6.insert(1, home)
                _6.insert(0, info.replace('(', '').replace(')', ''))
                _6.insert(2, odd)
                _6.insert(3, nullodd)
            info = '(+0.75)'
            if info in bet_type and data_type == '3830':
                _6.insert(4, odd)
                _6.insert(5, away)

            info = '(-0.25)'
            if info in bet_type and data_type == '3829':
                _7.insert(1, home)
                _7.insert(0, info.replace('(', '').replace(')', ''))
                _7.insert(2, odd)
                _7.insert(3, nullodd)
            info = '(+0.25)'
            if info in bet_type and data_type == '3830':
                _7.insert(4, odd)
                _7.insert(5, away)

            """ Home +, Away - """
            info = '(+0.25)'
            if info in bet_type and data_type == '3829':
                _8.insert(1, home)
                _8.insert(0, info.replace('(', '').replace(')', ''))
                _8.insert(2, odd)
                _8.insert(3, nullodd)
            info = '(-0.25)'
            if info in bet_type and data_type == '3830':
                _8.insert(4, odd)
                _8.insert(5, away)

            info = '(+1.25)'
            if info in bet_type and data_type == '3829':
                _9.insert(1, home)
                _9.insert(0, info.replace('(', '').replace(')', ''))
                _9.insert(2, odd)
                _9.insert(3, nullodd)
            info = '(-1.25)'
            if info in bet_type and data_type == '3830':
                _9.insert(4, odd)
                _9.insert(5, away)

            info = '(+1.75)'
            if info in bet_type and data_type == '3829':
                _10.insert(1, home)
                _10.insert(0, info.replace('(', '').replace(')', ''))
                _10.insert(2, odd)
                _10.insert(3, nullodd)
            info = '(-1.75)'
            if info in bet_type and data_type == '3830':
                _10.insert(4, odd)
                _10.insert(5, away)

            info = '(+2.25)'
            if info in bet_type and data_type == '3829':
                _11.insert(1, home)
                _11.insert(0, info.replace('(', '').replace(')', ''))
                _11.insert(2, odd)
                _11.insert(3, nullodd)
            info = '(-2.25)'
            if info in bet_type and data_type == '3830':
                _11.insert(4, odd)
                _11.insert(5, away)

            info = '(+2.75)'
            if info in bet_type and data_type == '3829':
                _12.insert(1, home)
                _12.insert(0, info.replace('(', '').replace(')', ''))
                _12.insert(2, odd)
                _12.insert(3, nullodd)
            info = '(-2.75)'
            if info in bet_type and data_type == '3830':
                _12.insert(4, odd)
                _12.insert(5, away)

            info = '(+3.25)'
            if info in bet_type and data_type == '3829':
                _13.insert(1, home)
                _13.insert(0, info.replace('(', '').replace(')', ''))
                _13.insert(2, odd)
                _13.insert(3, nullodd)
            info = '(-3.25)'
            if info in bet_type and data_type == '3830':
                _13.insert(4, odd)
                _13.insert(5, away)

            info = '(+3.75)'
            if info in bet_type and data_type == '3829':
                _14.insert(1, home)
                _14.insert(0, info.replace('(', '').replace(')', ''))
                _14.insert(2, odd)
                _14.insert(3, nullodd)
            info = '(-3.75)'
            if info in bet_type and data_type == '3830':
                _14.insert(4, odd)
                _14.insert(5, away)

        for _list in (_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11,
                      _12, _13, _14):
            if len(_list) == 6:
                print(tuple([(_list)]))
                XB_Db.w('XB_HDP', tuple([(_list)]))

    except AttributeError:
        pass
    except TypeError:
        pass


if __name__ == 'bettypes.FT_AHDP':
    from XBdatabase import XB_Db
elif __name__ == 'XB.bettypes.FT_AHDP':
    from XB.Database import XB_Db
