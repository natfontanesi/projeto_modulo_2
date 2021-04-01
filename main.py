from view import userView

print("Insira um termo de pesquisa: ")
user = userView()
user.set_user(input())
print(user.resposta())