from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text, select, ForeignKey, exc

class DbUtils:
    db_string = "postgresql+psycopg2://postgres:banco@localhost/loja_smartphones"
    db_query = " "

    def createTableProducts(self):
        db = create_engine(self.db_string)
        #self.db_query = "CREATE TABLE IF NOT EXISTS cadastro.usuarios (id_usuario SERIAL PRIMARY KEY, nome VARCHAR(60), idade INT, cidade VARCHAR(40));)"
        try:
            db.execute("CREATE TABLE products (id_produto SERIAL PRIMARY KEY, name VARCHAR(64), price VARCHAR(16), text VARCHAR(1024), urlImage VARCHAR(256));")
            res = True
        except:
            print("Problemas ao criar a tabela\n")
            res = False
        return res
    
    def createTableUsers(self):
        db = create_engine(self.db_string)
        try:
            db.execute("CREATE TABLE users (id_usuario SERIAL PRIMARY KEY, name VARCHAR(64), password VARCHAR(32), email VARCHAR(64));")
            res = True
        except:
            print("Problemas ao criar a tabela\n")
            res = False
        return res

    def addNewProduct(self, name, price, text, urlImage):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO products(name, price, text, urlImage) VALUES (%s, %s, %s, %s)", name, price, text, urlImage)
            res = True
        except Exception as e:
            print("Problemas ao inserir na tabela usuario\n")
            print(e)
            res = False
        return res
    
    def addNewUser(self,name, password, email):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO users(name, password, email) VALUES (%s, %s, %s)", name, password, email)
            res = True
        except Exception as e:
            print("Problemas ao inserir na tabela usuario\n")
            print(e)
            res = False
        return res

    def updateProduct(self, id, name, price, text, urlImage):
        db = create_engine(self.db_string)
        try:
            db.execute("UPDATE usuarios SET name=%s, price=%s, text=%s, urlImage=%s WHERE id_usuario=%s", name, price, text, urlImage, id)
            res = True
        except:
            print("Problemas ao atualizar na tabela usuario\n")
            res = False
        return res

    def selectProducts(self):
        db = create_engine(self.db_string)
        try:
            res = db.execute("select * from products")
        except:
            print("Problemas em importar o produto")
            res = False
        return res
    
    def selectUsers(self, email, password):
        db = create_engine(self.db_string)
        try:
            #select * from users where (email='Maria@ufu.br' and password='1616464686784878787878778')
            res = db.execute("select * from users where (email=%s and password=%s)", email, password)
        except:
            print("Problemas em importar o produto")
            res = False
        return res