import mysql.connector


def create_connection(host_name, user_name):
    current_connection = None
    try:
        current_connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
        )
        print("Connection to MySQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")

    return current_connection


connection = create_connection(
    host_name="localhost",
    user_name="jonas"
)

cursor = connection.cursor()

cursor.execute("select * from schule.fahrzeug")

result = cursor.fetchall()

for x in result:
    print(x)
