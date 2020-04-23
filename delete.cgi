#C:\Users\koustubh pal\AppData\Local\Programs\Python\Python37\python.exe
import mysql.connector
import cgi,cgitb
print('Content-Type :text/html\r\n\r\n')
cgitb.enable() #Debugging 

form = cgi.FieldStorage()
id  = int(form.getvalue('id'))
con = mysql.connector.connect(
      host='localhost',
      database='testdb',
      user='root',
      password=''  
      )
cursor = con.cursor()
cursor.execute("delete from contacts where id = '%d'"%(id))
r = cursor.rowcount
if r==1:
	print("<meta http-equiv='refresh' content = '0,view.cgi'/>")
else :
	print('Unable to Remove Record !!')
con.commit()
con.close()