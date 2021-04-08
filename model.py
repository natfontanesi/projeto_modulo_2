import requests 
import pandas
import json
from termcolor import cprint 

class Bit_Bucket_Model():
    def __init__(self):
        self.url='https://api.bitbucket.org/2.0/repositories'

    def get(self,user):
        self.request = requests.get(f'{self.url}/{user}')
        return self.request
    
    def get_status(self):
        return self.request.status_code

    def make_json(self,user):
        response = self.get(user)
        resposta =response.json()
        json_str = json.dumps(resposta)
        json_dict = json.loads(json_str)
        with open('saida.json', 'w') as arq:
            json.dump(json_dict, arq, indent=4)
        
        return cprint(json.dumps(json_dict, indent = 4),'green')

    def convert_csv(self,user):
        response = self.get(user)
        arquivo = pandas.read_json(response.content)
        csv= pandas.DataFrame(arquivo)
        print(csv)
        return arquivo.to_csv('bitbucket.csv')


