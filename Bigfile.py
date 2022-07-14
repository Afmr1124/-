import sqlite3
conn = sqlite3.connect('D.db')

cursor = conn.cursor()
cursor.execute("DROP TABLE  IF EXISTS  away;")
cursor.execute('DROP TABLE  IF EXISTS  home;')

print('D.db created successfully')
conn.commit()
cursor.close()
conn.close()
