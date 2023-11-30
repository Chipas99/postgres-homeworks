import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="north",
    user="postgres",
    password="Vhodanet19.",
    host="localhost"
)
cur = conn.cursor()


# Чтение данных из файла customers_data.csv и добавление их в базу данных
with open('north_data/customers_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvreader)  # Пропуск заголовков
    for row in csvreader:
        cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))


# Чтение данных из файла employees_data.csv и добавление их в базу данных
with open('north_data/employees_data.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvreader)  # Пропуск заголовков
    for row in csvreader:
        cur.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))

# Чтение данных из файла orders_data.csv и добавление их в базу данных
with open('north_data/orders_data.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvreader)  # Пропуск заголовков
    for row in csvreader:
        cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))

# Сохранение изменений
conn.commit()

# Закрытие соединения
cur.close()
conn.close()
