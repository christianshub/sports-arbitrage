def FT_1X2(soup, tag, tbl, home, away):

    info = ('1x2')
    _lst = []

    try:
        for i in soup.find(tag, tbl):

            odd = i.find('span', 'koeff').text
            data_type = i.find('span', 'bet_type').get('data-type')

            if data_type == '1':
                _lst.insert(1, home)
                _lst.insert(0, info)
                _lst.insert(2, odd)
            if data_type == '2':
                _lst.insert(3, odd)
            if data_type == '3':
                _lst.insert(4, odd)
                _lst.insert(5, away)

        if len(_lst) == 6:
            # print("*** 1X2 *** ")
            print(tuple([(_lst)]))
            XB_Db.w('XB_1x2', tuple([(_lst)]))

    except AttributeError:
        pass
    except TypeError:
        pass


if __name__ == 'bettypes.FT_1X2':
    from XBdatabase import XB_Db
elif __name__ == 'XB.bettypes.FT_1X2':
    from XB.Database import XB_Db
