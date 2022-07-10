from calendar import c
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Biggolfer07",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):

   cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
 
   players = cursor.fetchall()

   print("\n --{}--".format(title))

   for player in players:
        print("    Player ID: {}\n   First Name: {}\n  Last Name: {}\n  Team Names: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    show_players(cursor, "DISPLAYING PLAYERS BEFORE INSERT")

    add_player = ("INSERT INTO player(first_name, last_name, team_id)" "VALUES(%s, %s, %s)" )

    player_data = ("Bill", "Thomas", 1)

    cursor.execute(add_player, player_data)

    db.commit()

    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    update_player = ("UPDATE player SET team_id = 2, first_name = 'William', last_name = 'Adams' WHERE first_name = 'Bill' ")

    cursor.execute(update_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    delete_player = ("DELETE FROM player WHERE first_name = 'William'")

    cursor.execute(delete_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue...")

   
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close