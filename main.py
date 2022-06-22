import note_manage as nm


def login_page():
    print("""
|-----------------------------------|
|-Note Management System Login Page-|
|-----------------------------------|

1 - login
2 - create account
3 - exit
""")
    option = int(input())
    match option:
        case 1:
            login_check, user_id = nm.login()
            if login_check == 1:
                main_page(user_id)
            else:
                login_page()
        case 2:
            nm.create_account()
            login_page()
            pass
        case 3:
            quit()


def main_page(user_id):
    print("""
|----------------------------------|
|-Note Management System Main Page-|
|----------------------------------|

1 - create a note
2 - open a note
3 - delete a note
4 - view all of my notes
5 - logout
6 - close application
""")
    option = int(input())
    match option:
        case 1:
            nm.create_a_note(user_id)
            main_page(user_id)
        case 2:
            nm.open_a_note(user_id)
            main_page(user_id)
        case 3:
            nm.delete_a_note(user_id)
            main_page(user_id)
        case 4:
            nm.view_all_notes(user_id)
            main_page(user_id)
        case 5:
            login_page()
        case 6:
            quit()
    return


class Main:
    def __init__(self):
        return
    login_page()
