import pymysql

class mysqlController():
    def __init__(self,username = None,password = None,database = None):
        self.hostname    = "localhost"
        self.username    = username,
        self.password    = password,
        self.database    = database
        self.use_unicode = True
        self.charset     = "utf8"
        self.cursorclass = pymysql.cursors.DictCursor

    def dbconnect(self):
        return pymysql.connect(host=self.hostname, user=self.username[0], passwd=self.password[0], db=self.database, use_unicode=True, charset="utf8",cursorclass=pymysql.cursors.DictCursor)

    def fetchOne(self,query = None,sql = None,args = None):
        db = self.dbconnect()
        cursor = db.cursor()
        if(sql is not None):
            # print(sql)
            cursor.execute(sql)
        else:
            cursor.execute(query = query,args = args)
        outputData = cursor.fetchone()
        db.close()
        return outputData

    def fetchAll(self,query = None,sql = None,args = None):
        db = self.dbconnect()
        cursor = db.cursor()
        if(sql is not None):
            # print(sql)
            cursor.execute(sql)
        else:
            cursor.execute(query = query,args = args)
        outputData = cursor.fetchall()
        db.close()
        return outputData

    def executor(self,sql = None ,query = None,args = None):
        db = self.dbconnect()
        cursor = db.cursor()
        if(sql is not None):
            # print(sql)
            cursor.execute(sql)
        else:
            cursor.execute(query,args)
        return cursor.execute(query,args)

        db.commit()
        db.close()
