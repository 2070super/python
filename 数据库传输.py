import MySQLdb
class student:
    def __init__(self, stuName, stuId) -> None:
        self.stuName = stuName
        self.stuId = stuId

sl = [student("studentName" + str(i), i) for i in range(10)]

db = MySQLdb.connect(host="localhost",user= "root", password="live2018", database="test" )
cursor = db.cursor()
for i in sl:
    sql="INSERT INTO a(id, name) VALUES (%s,  %s)"
    cursor.execute(sql,(i.stuId,i.stuName))
    db.commit()
db.close()