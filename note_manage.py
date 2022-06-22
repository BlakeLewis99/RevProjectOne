import os

from connector import mydb


def login():
    username = input("username: ")
    password = input("password: ")
    my_cursor = mydb.cursor()

    my_cursor.execute("SELECT user_id, if(username = '" + username + "' AND password = '" + password + "', TRUE, FALSE) FROM user WHERE username = '" + username + "' AND password = '" + password + "';")

    my_result = my_cursor.fetchone()
    try:
        login_check = my_result[1]
        user_id = str(my_result[0])
        return login_check, user_id
    except TypeError:
        print("invalid login")
    return 0, 0


def create_account():
    username = input("create username: ")
    password = input("create password: ")
    first = input("enter your first name: ")
    last = input("enter your last name: ")
    mydb.cursor().execute(
        "INSERT INTO user(username, password, first_name, last_name) VALUES ('" + username + "', '" + password + "', '" + first + "', '" + last + "');")
    mydb.commit()


def open_a_note(user_id):
    title = str(input()+".csv")
    if os.path.exists(title):
        f = open(title, "rt")
        print(f.read())
    return


def create_a_note(user_id):
    title = str(input("Please enter a title for the note: "))
    content = str(input("Please enter the content of the note: "))
    try:
        f = open(title + ".csv", "x")
    except FileExistsError:
        print("You cannot use the same name as an existing note")
    else:
        f.write(content)
        f.close()
        mydb.cursor().execute(
            "INSERT INTO note(title, content, created, last_edit, user_id) VALUES ('" + title + "', '" + title + ".txt', DEFAULT, DEFAULT, "+ user_id+");")
        mydb.commit()
    return


def view_all_notes(user_id):
    my_cursor = mydb.cursor()

    my_cursor.execute("SELECT title FROM note WHERE user_id = " + user_id)

    my_result = my_cursor.fetchall()
    print("Note Titles:")
    for x in my_result:
        print(x[0])
    return


def delete_a_note(user_id):
    title = str(input())
    if os.path.exists(title + ".csv"):
        os.remove(title + ".csv")
        mydb.cursor().execute("DELETE FROM note WHERE title = '" + title + "';")
        mydb.commit()
    else:
        print("No such file exists")
    return
