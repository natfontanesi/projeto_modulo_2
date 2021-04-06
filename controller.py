from model import Bit_bucket_Model

class Requisition_Bit_Controller:
    def __init__(self):
        self.model = Bit_bucket_Model()

    def get_user(self, user, rtrn_type):
        rtrn_obj=[]
        if rtrn_type=="csv":
            rtrn_obj = self.model.make_csv(user)

        elif rtrn_type=="json":
            rtrn_obj = self.model.make_json(user)

        return rtrn_obj
    
    def get_status_controller(self):
        self.retorno = self.model.get_status()
        if self.retorno == 200:
            return("Funciona!")
        elif self.retorno == 404:
            return ("Não encontrado!")
        elif self.retorno == 500:
            return("Servidor fora do ar")
        elif self.retorno == 401:
            return("Não autorizado")
        elif self.retorno == 400:
            return("Bad request")