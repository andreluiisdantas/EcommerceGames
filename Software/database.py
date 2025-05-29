import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect("data/database.db")
    cursor = conexao.cursor()

    cursor.execute("DROP TABLE IF EXISTS vendas")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        cpf TEXT NOT NULL,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL CHECK (tipo IN ('administrador', 'vendedor', 'comprador'))
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL CHECK (preco >= 0),
        estoque INTEGER NOT NULL CHECK (estoque >= 0),
        estoque_minimo INTEGER NOT NULL CHECK (estoque_minimo >= 0)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INTEGER NOT NULL,
        id_vendedor INTEGER NOT NULL,
        quantidade INTEGER NOT NULL CHECK (quantidade > 0),
        data TEXT NOT NULL,
        valor_total REAL NOT NULL CHECK (valor_total >= 0),
        FOREIGN KEY (id_produto) REFERENCES produtos(id),
        FOREIGN KEY (id_vendedor) REFERENCES usuarios(id)
    );
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO usuarios(nome, email, cpf, senha, tipo)
    VALUES(
        'admin',
        'admin@admin.com',
        '00000000000',
        '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
        'administrador'
    );
    """)

    conexao.commit()
    conexao.close()

inicializar_banco()
