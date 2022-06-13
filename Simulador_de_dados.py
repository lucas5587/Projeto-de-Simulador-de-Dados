# simulador de dado
# Simular o uso de um dado, gerando um valor de 1 ate 6 
import random 
import PySimpleGUI as  sg

class SimuladorDeDado: # aqui foi criada a base. no caso chamada de classe 
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #self.mensagem = 'Voce gostaria de gerar um novo valor para o dado?'
        #oque tem que fazer com o pysimplegui e 
        #criar um Layout
        self.layout = [
            [sg.Text('Vamos Jogar o dado?')],
            [sg.Button('sim'),sg.Button('nao')]
        ]
        
            
     
    
    def Iniciar(self):
          #Criar uma janela
        self.janela = sg.Window('Simulador De Dado',layout=self.layout)
    
      
        #ler os valores na tela
        self.eventos, self.valores = self.janela.read()
        
         
        # vamos fazer alguma coisa com esses valores 
                
        
       
        
        try: # se for digitado algo que nao esteja programado ou seja nao e o correto ele vai dar essa exceção  
            
            if self.eventos == 'sim' or self.eventos == 's':  # ele vai responder esses dois tipos de respostas  
              self.GerarValordoDado()
              print('Obrigado por jogar!')        
            elif self.eventos == 'nao' or self.eventos == 'n': # ele vai responder esses dois tipos de respostas 
              print('Agradecemos a sua participação')               
            else:
              print('Favor digitar sim ou não')
        except: #esse comando faz parte do try, no caso ele diz se ocorrer alguma exceção ele pode ate escrever algo
            print('Ocorreu um erro ao receber sua resposta') # essa vai ser a resposta se tiver alguma exceçao
                       

    def GerarValordoDado(self):
        
        print(random.randint(self.valor_minimo,self.valor_maximo))
        
    
simulador = SimuladorDeDado()
simulador.Iniciar()              