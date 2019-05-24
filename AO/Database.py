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
        Info text, Odd1 text, OddX text, Odd2 text)'''.format(tbl))

    def create_tbls(self):

        self.tbl('AO_HDP')
        self.tbl('AO_OU')
        self.tbl('AO_FT')

        self.conn.commit()

    def w(self, tablename, _listname):

        self.cursor.executemany(('INSERT INTO {} VALUES (?,?,?,?,?,?,?,?)'
                                .format(tablename)), _listname)

        self.conn.commit()


AO_Db = Db()
