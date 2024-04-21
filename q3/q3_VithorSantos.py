import psycopg2

connect_to_database = lambda: psycopg2.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    database="mydatabase"
)

insert_user = lambda id, name, country, id_console: (
    "INSERT INTO USERS (id, name, country, id_console) VALUES (%s, %s, %s, %s)",
    (id, name, country, id_console)
)

remove_user = lambda user_id: (
    "DELETE FROM USERS WHERE id = %s",
    (user_id,)
)

get_all_users = lambda: (
    "SELECT * FROM USERS",
    ()
)

insert_videogame = lambda id_console, name, id_company, release_date: (
    "INSERT INTO VIDEOGAMES (id_console, name, id_company, release_date) VALUES (%s, %s, %s, %s)",
    (id_console, name, id_company, release_date)
)

remove_videogame = lambda game_id: (
    "DELETE FROM VIDEOGAMES WHERE id_console = %s",
    (game_id,)
)

get_all_videogames = lambda: (
    "SELECT * FROM VIDEOGAMES",
    ()
)

insert_game = lambda id_game, title, genre, release_date, id_console: (
    "INSERT INTO GAMES (id_game, title, genre, release_date, id_console) VALUES (%s, %s, %s, %s, %s)",
    (id_game, title, genre, release_date, id_console)
)

remove_game = lambda game_id: (
    "DELETE FROM GAMES WHERE id_game = %s",
    (game_id,)
)

get_all_games = lambda: (
    "SELECT * FROM GAMES",
    ()
)

insert_company = lambda id_company, name, country: (
    "INSERT INTO COMPANY (id_company, name, country) VALUES (%s, %s, %s)",
    (id_company, name, country)
)

remove_company = lambda company_id: (
    "DELETE FROM COMPANY WHERE id_company = %s",
    (company_id,)
)

get_all_companies = lambda: (
    "SELECT * FROM COMPANY",
    ()
)

execute_query = lambda query, values: (
    cursor.execute(query, values)
)

fetch_results = lambda: (
    cursor.fetchall()
)

#-------------- usabilidade

connection = connect_to_database()
cursor = connection.cursor()


execute_query(*insert_user(2, 'usuario_teste', 'BR', 1))
connection.commit()

execute_query(*get_all_users())
users = fetch_results()
print("Users:")
for user in users:
    print(user)

# execute_query(*get_all_videogames())
# videogames = fetch_results()
# print("Videogames:")
# for videogame in videogames:
#     print(videogame)

# execute_query(*get_all_games())
# games = fetch_results()
# print("Games:")
# for game in games:
#     print(game)

# execute_query(*get_all_companies())
# companies = fetch_results()
# print("Companies:")
# for company in companies:
#     print(company)

# Fechar conexão com o banco de dados
cursor.close()
connection.close()
