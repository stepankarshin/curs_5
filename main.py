import psycopg2
from src.get_company import get_employers

conn = psycopg2.connect(
    dbname='cursework_5',
    user='postgres',
    password='12345',
    port='5432',
    host='localhost'
)
curr = conn.cursor()
curr.execute('''
                    CREATE TABLE IF NOT EXISTS comp (
                    company_id VARCHAR PRIMARY KEY,
                    company_name VARCHAR,
                    open_vacancies INT
                    );
                    ''')
employers = get_employers()
for f in employers:
    curr.execute('INSERT INTO comp (company_id, company_name, open_vacancies) VALUES (%s, %s, %s);', (f[0], f[1], f[2]))

curr.close()
conn.commit()
conn.close()
