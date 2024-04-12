import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    user = os.environ.get('DBUSER'),
    password = os.environ.get('DBPASS'),
    database =os.environ.get('DATABASE')
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS areas
             (area_id SERIAL PRIMARY KEY,
             area_name TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
             (employee_ID SERIAL PRIMARY KEY,
             employee_name TEXT NOT NULL,
             employee_age INTEGER,
             area_ID INTEGER,
             CONSTRAINT fk_areas
                FOREIGN KEY(area_id) 
                    REFERENCES areas(area_id)
             )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS TASKS
             (task_id SERIAL PRIMARY KEY,
             task_name TEXT NOT NULL,
             completed BOOLEAN,
             due_date DATE,
             completion_date DATE,
             priority INTEGER,
             employee_ID INTEGER,
             CONSTRAINT fk_employees
                FOREIGN KEY(employee_ID) 
                    REFERENCES EMPLOYEES(employee_ID)
             )''')

# Insert sample tasks into the areas table
cursor.execute("INSERT INTO AREAS (area_name) VALUES (%s)",
               ('Soporte Usuarios',))
cursor.execute("INSERT INTO AREAS (area_name) VALUES (%s)",
               ('Soporte Internos',))

# Insert sample tasks into the employees table
cursor.execute("INSERT INTO EMPLOYEES (employee_name, employee_age, area_ID) VALUES (%s, %s, %s)",
               ('Joaquin', 30, 1))
cursor.execute("INSERT INTO EMPLOYEES (employee_name, employee_age, area_ID) VALUES (%s, %s, %s)",
               ('Pedro', 25, 2))
cursor.execute("INSERT INTO EMPLOYEES (employee_name, employee_age, area_ID) VALUES (%s, %s, %s)",
               ('Alonso', 30, 1))
cursor.execute("INSERT INTO EMPLOYEES (employee_name, employee_age, area_ID) VALUES (%s, %s, %s)",
               ('Brenda', 24, 2))


# Insert sample tasks into the tasks table
cursor.execute("INSERT INTO tasks (task_name, completed, due_date, completion_date, priority, employee_ID) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Complete the web page design', True, '2023-05-01', '2023-05-03', 1, 1))
cursor.execute("INSERT INTO tasks (task_name, completed, due_date, completion_date, priority, employee_ID) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Create login and signup pages', True, '2023-05-03', '2023-05-05', 2, 2))
cursor.execute("INSERT INTO tasks (task_name, completed, due_date, completion_date, priority, employee_ID) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Product management', False, '2023-05-05', None, 3, 3))
cursor.execute("INSERT INTO tasks (task_name, completed, due_date, completion_date, priority, employee_ID) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Cart and wishlist creation', False, '2023-05-08', None, 4, 4))
cursor.execute("INSERT INTO tasks (task_name, completed, due_date, completion_date, priority, employee_ID) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Payment gateway integration', False, '2023-05-10', None, 5, 4))
cursor.execute("INSERT INTO tasks (task_name, completed, due_date, completion_date, priority, employee_ID) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Order management', False, '2023-05-10', None, 6, 1))

# Commit the changes and close the connection
conn.commit()
conn.close()