import sqlite3

class Db():

    def __init__(self):
        self.DB_FILENAME = 'Arbitrages.db'
        self.conn = sqlite3.connect(self.DB_FILENAME, timeout=300000)
        self.cursor = self.conn.cursor()

    def tbl(self, tbl):

        self.cursor.execute('''DROP TABLE IF EXISTS {}'''.format(tbl))
        self.cursor.execute('''CREATE TABLE {}
        (ROI text, AO_INFO text, AO_TEAM text, AO_ODD text, AO_PLACE text,
                   XB_INFO text, XB_TEAM text, XB_ODD text, XB_PLACE text)'''.format(tbl))

    def tblTime(self, tbl):

        self.cursor.execute('''DROP TABLE IF EXISTS {}'''.format(tbl))
        self.cursor.execute('''CREATE TABLE {}
        (LastUpdatedTime text, CurrentDate text)'''.format(tbl))

    def create_tbls(self):

        self.tblTime('LastUpdated')
        self.tbl('Arbitrages')
        self.tbl('Calculations')

        self.conn.commit()

    def w(self, tablename, _listname):

        self.cursor.executemany(('INSERT INTO {} VALUES (?,?,?,?,?,?,?,?,?)'
                                 .format(tablename)), _listname)

        self.conn.commit()

    def wTime(self, tablename, _listname):

        self.cursor.executemany(('INSERT INTO {} VALUES (?,?)'
                                 .format(tablename)), _listname)

        self.conn.commit()


AR_Db = Db()
