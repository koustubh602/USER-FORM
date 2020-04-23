

#!C:\Users\koustubh pal\AppData\Local\Programs\Python\Python37\python.exe


print('Content-Type :text/html\r\n\r\n')
#import some packages for Form Handling
#Adding Bs 
print("<meta name='viewport' content='width=device-width,initial-scale=1.0'/>")
print("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css'>")
print("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>")
print("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js'></script>")
import cgi,cgitb,mysql.connector

cgitb.enable() #Debugging 

form = cgi.FieldStorage()

name    = form.getvalue('t1')
age     = int(form.getvalue('t2'))
gender  = form.getvalue('r1')
city    = form.getvalue('t4')
email   = form.getvalue('t5')
phone   = form.getvalue('t6')

#print('You have entered :{}'.format(name))
#print('Name is {} Age is {} Gender is {} from {}'.format(name,age,gender,city))

con = mysql.connector.connect(
      host='localhost',
      database='testdb',
      user='root',
      password=''  
      )
cursor = con.cursor()
SQL ="insert into contacts(name,age,gender,city,email,phone)values('%s','%d','%s','%s','%s','%s')"%(name,age,gender,city,email,phone)
cursor.execute(SQL)
r=cursor.rowcount
if(r==1):
 print("<div class='alert alert-success'>")	
 print('Record Added')
 print("</div>")
else:
 print("<div class='alert alert-danger'>")	
 print('Error')
 print("</div>")
con.commit()
con.close()
#Providing Back Link
print('<br>')
print('<br>')
print("<a href='form.html'>Back</a>")

