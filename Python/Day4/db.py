import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="summer_course",
    user="iti",
    password="iti"
)
curso = conn.cursor()

def register():
    name = input("Enter your name: ")
    emil = input("Enter your email: ")
    password = input("Enter your password: ")
    get_tracks = """
    select id,name from track;
    """
    curso.execute(get_tracks)
    for track in curso.fetchall():
        print(track)
    track = input("Choose your track: ")
    sql = f"insert into students(fname,email,password,track_id) values('{name}','{emil}','{password}',{int(track)});"
    curso.execute(sql)
    conn.commit()
    print("====== Registered successfully ========")
    return True

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    sql = f"select * from students where email = '{email}' and password = '{password}'"
    curso.execute(sql)
    result = curso.fetchone()
    if result:
        print("====== Login successfully ========")
        return True, result
    else:
        print("====== Login failed ========")
        return False , None
while True:
    result = input("Choose \n 1)Register \n 2)Login \n 3)Exit \n")
    if result == '1':
        register()
        continue
    elif result == '2':
        ret , user = login()
        if ret:
           print("========= Congratulations Welcome To our site ==========")
           while True:
               res = input("Do you want to \n 1) Show Profile \n 2) Update Profile \n 3)Delete Profile \n 4) Exit \n")
               if res == '1':
                   show_profile = f"select students.fname,students.email,track.name from students  inner join track on track.id = students.track_id and students.id = {user[0]};"
                   curso.execute(show_profile)
                   result_show = curso.fetchone()
                   print("--------------------------------")
                   print('Name: ', result_show[0])
                   print('Email: ', result_show[1].strip())
                   print('Track: ', result_show[2])
                   print("--------------------------------")
                   continue
               elif res == '2':
                   name = input("Enter your name: ")
                   email = input("Enter your email: ")
                   password = input("Enter your password: ")
                   update_profile = f"update students set fname = '{name}',email = '{email}',password = '{password}' where id = {user[0]};"
                   curso.execute(update_profile)
                   conn.commit()
                   print("====== Profile updated successfully ========")
                   continue
               elif res == '3':
                   delete_profile = f"delete from students where id = {user[0]};"
                   curso.execute(delete_profile)
                   conn.commit()
                   print("====== Profile deleted successfully ========")
                   break
               elif res == '4':
                   break
        else:
            continue
    elif result == '3':
        break

conn.close()