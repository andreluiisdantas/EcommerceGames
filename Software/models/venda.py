import sqlite3
from datetime import datetime

class Venda:
    def __init__(self, id_produto, id_vendedor, quantidade, valor_unitario):
        self.id_produto = id_produto
        self.id_vendedor = id_vendedor
        self.quantidade = quantidade
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.valor_total = quantidade * valor_unitario

    def registrar_venda(self):
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()
        try:
            cursor.execute("SELECT estoque FROM produtos WHERE id = ?", (self.id_produto,))
            resultado = cursor.fetchone()
            if not resultado or resultado[0] < self.quantidade:
                print("Produto não encontrado ou estoque insuficiente.")
                return
            novo_estoque = resultado[0] - self.quantidade
            cursor.execute("UPDATE produtos SET estoque = ? WHERE id = ?", (novo_estoque, self.id_produto))
            cursor.execute("""
                INSERT INTO vendas (id_produto, id_vendedor, quantidade, data, valor_total)
                VALUES (?, ?, ?, ?, ?)
            """, (self.id_produto, self.id_vendedor, self.quantidade, self.data, self.valor_total))
            conexao.commit()
            print("Venda registrada com sucesso.")
        except sqlite3.Error as e:
            print("Erro ao registrar venda:", e)
        finally:
            conexao.close()
