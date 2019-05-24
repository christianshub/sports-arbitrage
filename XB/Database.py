"""
    Database creation
"""
import sqlite3


class Db():

    def __init__(self):
        self.DB_FILENAME = 'Live.db'
        self.conn = sqlite3.connect(self.DB_FILENAME, timeout=300000)
        self.cursor = self.conn.cursor()

    def tbl(self, tbl):

        self.cursor.execute('''DROP TABLE IF EXISTS {}'''.format(tbl))
        self.cursor.execute('''CREATE TABLE {}
        (HomeTeam text, AwayTeam text, HomeScore text, AwayScore text,
        Info1 text, Odd1 text, OddX text, Odd2 text)'''.format(tbl))

    def tbl_HDP(self, tbl):

        self.cursor.execute('''DROP TABLE IF EXISTS {}'''.format(tbl))
        self.cursor.execute('''CREATE TABLE {}
        (HomeTeam text, AwayTeam text, HomeScore text, AwayScore text,
        Info1 text, Odd1 text, OddX text, Info2 text, Odd2 text)'''.format(tbl))


    def create_tbls(self):

        self.tbl('XB_FT'), self.tbl('XB_DC'),
        self.tbl('XB_OU'), self.tbl_HDP('XB_HDP')

        self.conn.commit()

    def w(self, tablename, _listname):

        self.cursor.executemany(('INSERT INTO {} VALUES (?,?,?,?,?,?,?,?)'
                                .format(tablename)), _listname)

        self.conn.commit()

    def wHDP(self, tablename, _listname):

        self.cursor.executemany(('INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?)'
                                .format(tablename)), _listname)

        self.conn.commit()


XB_Db = Db()
