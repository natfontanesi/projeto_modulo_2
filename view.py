from controller import Requisition_Bit_Controller

class userView:
    def __init__(self):
        self.controller = Requisition_Bit_Controller                            ()
        
    def set_user(self, user):
        self.user = user    
        
    def set_type(self, type):
        self.type = type

    def response(self):
        return self.controller.get_user(self.user,self.type)
    
    def get_status_view(self):
        self.retorno = self.controller.get_status_controller()
        if self.retorno == 200:
            return("Requisição bem sucedida.")
        elif self.retorno == 404:
            return ("O servidor não encontrou o recurso solicitado.")
        elif self.retorno == 500:
            return("Servidor fora do ar.")
        elif self.retorno == 401:
            return("Não autorizado.")
        elif self.retorno == 400:
            return("Bad request.")
        else:
            return("Erro desconhecido.")