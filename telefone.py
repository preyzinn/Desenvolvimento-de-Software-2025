from transitions import Machine

states = ['ocioso', 'discando', 'chamando', 'tocando', 'conectado', 'em_espera', 'finalizando']

class Telefone:
    def __init__(self):
        self.numero = None

    def iniciar_ligacao(self):
        print("Iniciando discagem...")
    
    def discando_numero(self):
        print("Discando o número...")
    
    def chamando_destinatario(self):
        print("Tentando conectar com o destinatário...")
    
    def tocando_destinatario(self):
        print("O telefone do destinatário está tocando...")
    
    def conectado_chamada(self):
        print("Chamada conectada!")
    
    def colocar_em_espera(self):
        print("Chamada em espera...")
    
    def finalizar_chamada(self):
        print("Chamada finalizada.")

telefone = Telefone()

machine = Machine(model=telefone, states=states, initial='ocioso')

machine.add_transition(trigger='iniciar', source='ocioso', dest='discando', before='iniciar_ligacao')
machine.add_transition(trigger='numero_completo', source='discando', dest='chamando', before='discando_numero')
machine.add_transition(trigger='tocando', source='chamando', dest='tocando', before='chamando_destinatario')
machine.add_transition(trigger='atender', source='tocando', dest='conectado', before='conectado_chamada')
machine.add_transition(trigger='espera', source='conectado', dest='em_espera', before='colocar_em_espera')
machine.add_transition(trigger='retomar', source='em_espera', dest='conectado', before='conectado_chamada')
machine.add_transition(trigger='desligar', source=['conectado', 'em_espera', 'tocando', 'chamando', 'discando'], dest='finalizando', before='finalizar_chamada')
machine.add_transition(trigger='resetar', source='finalizando', dest='ocioso')

telefone.iniciar()
telefone.numero_completo()
telefone.tocando()
telefone.atender()
telefone.espera()
telefone.retomar()
telefone.desligar()
telefone.resetar()
