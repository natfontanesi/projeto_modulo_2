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
        return self.controller.get_status_controller()
        