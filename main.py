from view import userView
import json

print(
    "Bem-vindo à API Bitbucket! Com esta API:  \n \
\n \
- Acesse informações públicas do usuário;  \n \
- Acesse repositórios públicos ou privados, tags ou branches;  \n \
- Crie, atualize ou exclua um de seus repositórios;  \n \
- Acesse, crie, atualize ou exclua um serviço; \n \
- Acesse, crie ou exclua uma chave SSH; \n \
- Baixe um repositório como um arquivo; \n \
- Acesse, crie, atualize ou exclua um problema; \n \
- Acesse, crie, atualize ou exclua um comentário. \n \
 \n \
Insira um termo de pesquisa: ")

usuario = userView()
usuario.set_user(input())

print("Qual tipo de arquivo, JSON/CSV: ")
usuario.set_type(input())

#perguntar em qual formato o usuário deseja a resposta
resposta = usuario.response()
json_str = json.dumps(resposta)
json_dict = json.loads(json_str)
print(json.dumps(json_dict, indent = 3))

print(f'{usuario.get_status_view()}')




