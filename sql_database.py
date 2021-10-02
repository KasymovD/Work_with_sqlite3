import sqlite3

db = sqlite3.connect('Dosa.db') #- Создание или Подключение базы данных

sql = db.cursor() #- Наведение таблицы для дальнешего действия

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT 
)""") #- Создание колонок

db.commit() #- Подвердить создание таблицы

user_login = input('Login: ')
user_password = input('Password: ')

sql.execute("SELECT login FROM users")
a = sql.fetchall()

z = [] 
for val in a:
    f = ''.join(map(''.join,val))
    # print(f)
    z.append(f)


if user_login in z:
    print('Такая запись уже имеется!')
else:
    sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
    db.commit()

# print(z)
# for v in sql.execute("SELECT * FROM users"):
#     print(v[0])