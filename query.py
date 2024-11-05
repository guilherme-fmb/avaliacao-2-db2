class Query:
    def __init__ (self,db):
        self.db = db
    
# questão 01
# a.
    def renzo(self):
        print("1-1)")
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.ano_nasc"],result["t.cpf"]) for result in results]

# b.
    def m(self):
        print("1-2)")
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.name"],result["t.cpf"]) for result in results]

# c.
    def city(self):
        print("1-3)")
        query = "MATCH (c:City) RETURN c.name"
        results = self.db.execute_query(query)
        return [result["c.name"] for result in results]

# d.
    def school(self):
        print("1-4)")
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        results = self.db.execute_query(query)
        return [(result["s.name"],result["s.address"],result["s.number"]) for result in results]

# questão 02
# a.
    def ano(self):
        print("2-1)")
        query = "MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc ASC LIMIT 1"
        results = self.db.execute_query(query)
        return [result["t.ano_nasc"] for result in results]

# b. 
    def media(self):
        print("2-2)")
        query = "MATCH (c:City) RETURN AVG(c.population)"
        results = self.db.execute_query(query)
        return [result["AVG(c.population)"] for result in results]

# c.
    def cep(self):
        print("2-3)")
        query = "MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A')"
        results = self.db.execute_query(query)
        return [result["REPLACE(c.name, 'a', 'A')"] for result in results]

# d.
    def terceira_letra(self):
        print("2-4)")
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1)"
        results = self.db.execute_query(query)
        return [result["SUBSTRING(t.name, 2, 1)"] for result in results]