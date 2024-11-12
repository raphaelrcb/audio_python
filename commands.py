import subprocess
import os
from time import process_time_ns


class Commander:
    def __init__(self):
        self.confirm = ["sim", "sí", "yes", "confirma", "confirmado", "positivo", "positivo e operante", "claro", "óbvio"]
        self.cancel = ["não", "nunca", "cancela", "negativo", "nao", "para agora", "espera", "cancelar", "de novo", "repete"]


    def discover(self, text):
        if ("qual" or "Qual") in text and "nome" in text:
            if "meu" in text:
                self.respond("não sei")
            elif "seu" in text:
                self.respond("Meu nome é PythonVoz")

    def respond(self, response):
        call_string = "echo " + response + " | cscript \"C:\\Program Files\\Jampal\\ptts.vbs\""
        print(call_string)
        subprocess.call(call_string, shell=True)