from view import userView
import json
import sys
from termcolor import colored, cprint

cprint(
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
Insira um termo de pesquisa: ",'green')

usuario = userView()
usuario.set_user(input())

cprint("Qual tipo de arquivo, JSON/CSV: ",'green')
tipo_arquivo= input().lower()
while tipo_arquivo!="json" and tipo_arquivo!="csv":
    cprint("Tipo inválido, digite novamente!",'green')
    tipo_arquivo= input().lower()
usuario.set_type(tipo_arquivo)


#perguntar em qual formato o usuário deseja a resposta
resposta = usuario.response()
print(f'{usuario.get_status_view()}')

json_str = json.dumps(resposta)
json_dict = json.loads(json_str)
print(json.dumps(json_dict, indent = 3))
