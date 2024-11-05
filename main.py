from database import Database
from teacher_crud import TeacherCRUD, CLI
from query import Query

db = Database("bolt://44.194.183.145:8576", "neo4j", "cake-car-bell")

query_database = Query(db)

# questão 1

# a.
print(query_database.renzo())
# b.
print(query_database.m())
# c.
print(query_database.city())
# d.
print(query_database.school())

# questão 2

# a.
print(query_database.ano())
# b.
print(query_database.media())
# c.
print(query_database.cep())
# d.
print(query_database.terceira_letra())

# questão 03

# instância da classe TeacherCRUD
teacher = TeacherCRUD(db)

# criação de um teacher
teacher.create('Chris Lima', '1956', '189.052.396-66')

# pesquisando o professor Chris Lima
print(teacher.read('Chris Lima'))

# alterando o cpf do "teacher" de nome "Chris Lima" para "162.052.777-77"
teacher.update('Chris Lima', '162.052.777-77')

# instanciando um CLI
cli = CLI(teacher)

# rodando O CLI
cli.run()

# fechando a conexão com o db
db.close()