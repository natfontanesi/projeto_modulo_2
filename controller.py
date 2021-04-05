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
        return self.model.get_status()
        