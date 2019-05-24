def FT_DC(soup, tag, tbl, home, away):

    info = ('DC')
    _lst = []

    try:
        for i in soup.find(tag, tbl):

            odd = i.find('span', 'koeff').text
            data_type = i.find('span', 'bet_type').get('data-type')

            if data_type == '4':
                _lst.insert(1, home)
                _lst.insert(0, info)
                _lst.insert(2, odd)
            if data_type == '5':
                _lst.insert(3, odd)
            if data_type == '6':
                _lst.insert(4, odd)
                _lst.insert(5, away)

        if len(_lst) == 6:
            # print("*** DOUBLE CHANCE *** ")
            print(tuple([(_lst)]))
            XB_Db.w('XB_DC', tuple([(_lst)]))

    except AttributeError:
        pass
    except TypeError:
        pass


if __name__ == 'bettypes.FT_DC':
    from XBdatabase import XB_Db
elif __name__ == 'XB.bettypes.FT_DC':
    from XB.Database import XB_Db
