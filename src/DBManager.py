class DBManager:
    def __init__(self, dbname, user, password, port='5432', host='localhost'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.host = host

    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self):
        pass
