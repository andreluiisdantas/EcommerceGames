import sqlite3

class Produto:
    def __init__(self, nome, preco, estoque, estoque_minimo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.estoque_minimo = estoque_minimo

    def salvar_no_banco(self):
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                INSERT INTO produtos (nome, preco, estoque, estoque_minimo)
                VALUES (?, ?, ?, ?)
            """, (self.nome, self.preco, self.estoque, self.estoque_minimo))
            conexao.commit()
            print("Produto cadastrado com sucesso!")
        except sqlite3.Error as e:
            print("Erro ao salvar produto:", e)
        finally:
            conexao.close()