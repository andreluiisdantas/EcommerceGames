from banco.conexao import conectar
from interfaces.area_logada import area_logada

def login():
    conexao = conectar()
    cursor = conexao.cursor()

    email = input("Digite o e-mail: ")
    senha = input("Digite sua senha: ")

    cursor.execute("""
        SELECT id, nome, email, senha_hash, tipo, ativo 
        FROM usuarios 
        WHERE email = ?
    """, (email,))
    usuario = cursor.fetchone()
    conexao.close()

    if usuario is None:
        print("Usuário não encontrado.")
        return None

    id_usuario, nome_usuario, email_usuario, senha_armazenada, tipo, ativo = usuario

    if not ativo:
        print("Usuário está desativado.")
        return None

    if senha != senha_armazenada:
        print("Senha incorreta.")
        return None

    usuario_dict = {
        "id": id_usuario,
        "nome": nome_usuario,
        "email": email_usuario,
        "tipo": tipo,
        "ativo": ativo
    }

    area_logada(usuario_dict)
    return usuario_dict
