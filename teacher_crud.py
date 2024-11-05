# CRUD de Teacher
class TeacherCRUD():
    def __init__(self, database):
        self.database = database
        
     # cria um novo professor
    def create(self, name, ano_nasc, cpf):
        query = f"CREATE (t:Teacher {{name: '{name}', ano_nasc: '{ano_nasc}', cpf: '{cpf}'}})"
        self.database.execute_query(query)

    def read(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        result = self.database.execute_query(query)
        if result:
            return result[0]
        else:
            return None

    # deleta o professor com base no nome
    def delete(self, name): 
        query = f"MATCH (t:Teacher {{name: '{name}'}}) DETACH DELETE t"
        self.database.execute_query(query)
    
    # atualiza cpf com base no name
    def update(self, name, newCpf): 
        query = f"MATCH (t:Teacher {{name: '{name}'}}) SET t.cpf = '{newCpf}'"
        self.database.execute_query(query)

# Teacher CLI
class CLI:
    def __init__(self, teacher_crud):
        self.teacher_crud = teacher_crud

    def run(self):
        while True:
            print("CLI CRUD Teacher")
            print("1. Create Teacher")
            print("2. Read Teacher")
            print("3. Update Teacher")
            print("4. Delete Teacher")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_teacher()
            elif choice == "2":
                self.read_teacher()
            elif choice == "3":
                self.update_teacher()
            elif choice == "4":
                self.delete_teacher()
            elif choice == "0":
                break

    def create_teacher(self):
        name = input("Enter teacher's name: ")
        ano_nasc = input("Enter teacher's birth year: ")
        cpf = input("Enter teacher's CPF: ")
        self.teacher_crud.create(name, ano_nasc, cpf)
        print("Teacher created successfully!")

    def read_teacher(self):
        name = input("Enter teacher's name: ")
        teacher = self.teacher_crud.read(name)
        if teacher:
            print("Teacher found:")
            print(f"Name: {teacher['name']}")
            print(f"Birth Year: {teacher['ano_nasc']}")
            print(f"CPF: {teacher['cpf']}")
        else:
            print("Teacher not found.")

    def update_teacher(self):
        name = input("Enter teacher's name: ")
        new_cpf = input("Enter new CPF: ")
        self.teacher_crud.update(name, new_cpf)
        print("Teacher updated!")

    def delete_teacher(self):
        name = input("Enter teacher's name: ")
        self.teacher_crud.delete(name)
        print("Teacher deleted!")