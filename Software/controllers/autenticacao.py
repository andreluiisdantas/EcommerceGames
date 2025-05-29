import sqlite3
from controllers.criptografia import gerar_hash_senha

def fazer_login():
    email = input("Email: ")
    senha = input("Senha: ")
    senha_hash = gerar_hash_senha(senha)

    conexao = sqlite3.connect("data/database.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cpf, email, senha, tipo FROM usuarios WHERE email=?", (email,))
    usuario = cursor.fetchone()
    conexao.close()

    if usuario and senha_hash == usuario[4]:
        print(f"Bem-vindo, {usuario[1]}! ({usuario[5]})")
        return usuario
    else:
        print("Credenciais inválidas!")
        return None
