from model import Bit_Bucket_Model

class Bit_Bucket_Controller:
    def __init__(self):
        self.model = Bit_Bucket_Model()

    def get_user(self, user, rtrn_type):
        rtrn_obj=[]
        if rtrn_type=="csv":
            rtrn_obj = self.model.convert_csv(user)

        elif rtrn_type=="json":
            rtrn_obj = self.model.make_json(user)

        return rtrn_obj
    
    def get_status_controller(self):
        self.retorno= self.model.get_status()
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
        