

#perguntar em qual formato o usuário deseja a resposta
resposta = user.resposta()
json_str = json.dumps(resposta)
json_dict = json.loads(json_str)

print(json.dumps(json_dict, indent = 3))






