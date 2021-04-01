from controller import Requisicao_Bit

class userView:
    def __init__(self):
        self.controller = Requisicao_Bit()
        
    def set_user(self, user):
        self.user = user    
        
    def resposta(self):
        return self.controller.get_user(self.user,"json")