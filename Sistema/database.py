import sqlite3

conexao = sqlite3.connect("data/database.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    cpf TEXT NOT NULL,
    senha TEXT NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('administrador', 'vendedor', 'comprador'))
);
""")

cursor.execute("""
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK (preco >= 0),
    estoque INTEGER NOT NULL CHECK (estoque >= 0),
    estoque_minimo INTEGER NOT NULL CHECK (estoque_minimo >= 0)
);
""")

cursor.execute("""
CREATE TABLE vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    id_vendedor INTEGER NOT NULL,
    id_comprador INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    data TEXT NOT NULL,
    valor_total REAL NOT NULL CHECK (valor_total >= 0),

    FOREIGN KEY (id_produto) REFERENCES produtos(id),
    FOREIGN KEY (id_vendedor) REFERENCES usuarios(id),
    FOREIGN KEY (id_comprador) REFERENCES usuarios(id)
);
""")

conexao.close()