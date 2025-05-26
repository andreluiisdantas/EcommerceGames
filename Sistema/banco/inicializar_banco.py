from conexao import conectar

def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    tabelas = """
    PRAGMA foreign_keys = ON;

    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL,
        tipo TEXT NOT NULL,
        ativo INTEGER NOT NULL DEFAULT 1
    );

    CREATE TABLE produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade_estoque INTEGER NOT NULL DEFAULT 0,
        estoque_minimo INTEGER NOT NULL DEFAULT 0
    );

    CREATE TABLE fornecedores (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        contato TEXT,
        avaliacao_media REAL
    );

    CREATE TABLE compras (
        id INTEGER PRIMARY KEY,
        id_comprador INTEGER NOT NULL,
        id_fornecedor INTEGER NOT NULL,
        data TEXT NOT NULL,
        valor_total REAL NOT NULL,
        FOREIGN KEY (id_comprador) REFERENCES usuarios(id),
        FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id)
    );

    CREATE TABLE itens_compra (
        id INTEGER PRIMARY KEY,
        id_compra INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        preco_unitario REAL NOT NULL,
        FOREIGN KEY (id_compra) REFERENCES compras(id),
        FOREIGN KEY (id_produto) REFERENCES produtos(id)
    );

    CREATE TABLE vendas (
        id INTEGER PRIMARY KEY,
        id_vendedor INTEGER NOT NULL,
        data TEXT NOT NULL,
        desconto_total REAL DEFAULT 0,
        valor_total REAL NOT NULL,
        FOREIGN KEY (id_vendedor) REFERENCES usuarios(id)
    );

    CREATE TABLE itens_venda (
        id INTEGER PRIMARY KEY,
        id_venda INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        preco_unitario REAL NOT NULL,
        FOREIGN KEY (id_venda) REFERENCES vendas(id),
        FOREIGN KEY (id_produto) REFERENCES produtos(id)
    );

    CREATE TABLE movimentos_estoque (
        id INTEGER PRIMARY KEY,
        id_produto INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        data TEXT NOT NULL,
        observacao TEXT,
        FOREIGN KEY (id_produto) REFERENCES produtos(id)
    );

    CREATE TABLE movimentos_caixa (
        id INTEGER PRIMARY KEY,
        data TEXT NOT NULL,
        tipo TEXT NOT NULL,
        origem TEXT NOT NULL,
        referencia_id INTEGER,
        valor REAL NOT NULL,
        descricao TEXT
    );

    CREATE TABLE logs_atividade (
        id INTEGER PRIMARY KEY,
        id_usuario INTEGER NOT NULL,
        acao TEXT NOT NULL,
        data TEXT NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
    );
    """

    cursor.executescript(tabelas)
    conexao.commit()
    conexao.close()

criar_banco()
