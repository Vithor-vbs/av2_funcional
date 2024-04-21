import psycopg2

connect_to_database = lambda: psycopg2.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    database="mydatabase"
)

generate_inner_join = lambda table1, table2, column1, column2: (
    f"INNER JOIN {table2} ON {table1}.{column1} = {table2}.{column2}",
)

generate_select = lambda columns: (
    f"SELECT {', '.join(columns)}",
)

# Example usage:
join_statement1 = generate_inner_join('GAMES', 'VIDEOGAMES', 'id_console', 'id_console')
join_statement2 = generate_inner_join('VIDEOGAMES', 'COMPANY', 'id_company', 'id_company')
select_statement = generate_select(['GAMES.title', 'GAMES.release_date', 'COMPANY.name', 'VIDEOGAMES.name'])

generate_query = lambda select_statement, join_statement1, join_statement2: (
    f"{select_statement[0]} FROM GAMES {join_statement1[0]} {join_statement2[0]}"
)

query = generate_query(select_statement, join_statement1, join_statement2)

conn = connect_to_database()

cur = conn.cursor()

cur.execute(query)

results = cur.fetchall()
print(results)

for result in results:
    print(result)

cur.close()
conn.close()