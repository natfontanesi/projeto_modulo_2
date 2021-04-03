from model import Bit_bucket_Model

class Requisicao_Bit:
    def __init__(self):
        self.model = Bit_bucket_Model()

    def get_user(self, user, retorna_tipo):
        retorna_objeto=[]
        if retorna_tipo=="csv":
            retorna_objeto = self.model.make_csv(user)

        elif retorna_tipo=="json":
            retorna_objeto = self.model.make_json(user)

        return retorna_objeto
    
    def get_status_controller(self):
        return self.model.get_status()
        