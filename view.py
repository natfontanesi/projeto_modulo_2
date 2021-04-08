from controller import Bit_Bucket_Controller

class Bit_Bucket_View:
    def __init__(self):
        self.controller = Bit_Bucket_Controller                           ()
        
    def set_user(self, user):
        self.user = user    
        
    def set_type(self, type):
        self.type = type

    def response(self):
        return self.controller.get_user(self.user,self.type)
    
    def get_status_view(self):
        return self.controller.get_status_controller()
        