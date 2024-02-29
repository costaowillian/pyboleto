from decimal import Decimal

from cnab240.tipos import Arquivo
from cnab240.bancos import itau

class gerar_remessa():
    """Geração do arquivo (.txt) de remessa do banco Itaú com a biblioteca CNAB240

    Esta classe é responsável por gerar a remessa em formato .txt para o banco Itaú.

    Ela foi desenvolvida exclusivamente para a geração de remessas do banco Itaú. 

    Caso deseje implementar funcionalidades para outros bancos, é possível reutilizar a 
    classe, modificando apenas o método gerar_arquivo_remessa(), que é responsável pela 
    escrita dos dados de acordo com o banco desejado.
    """

    def __init__(self):
        """Método não precisa ser iniciado
        """
        pass

    def gerar_dict_arquivo(self, data_arquivo):
        return {
            'cedente_inscricao_tipo': data_arquivo.cedente_inscricao_tipo,
            'cedente_inscricao_numero': data_arquivo.cedente_inscricao_numero,
            'cedente_agencia': data_arquivo.cedente_agencia,
            'cedente_conta': data_arquivo.cedente_conta,
            'cedente_agencia_conta_dv': data_arquivo.cedente_agencia_conta_dv,
            'cedente_nome': data_arquivo.cedente_nome,
            'arquivo_data_de_geracao': data_arquivo.arquivo_data_de_geracao,
            'arquivo_hora_de_geracao': data_arquivo.arquivo_hora_de_geracao,
            'arquivo_sequencia': data_arquivo.arquivo_sequencia
        }
        
    def gerar_arquivo_remessa(self, data, data_arquivo):
        if(not data):
            raise ValueError("Sem dados para escrever")
        
        dict_arquivo = self.gerar_dict_arquivo(data_arquivo)

        arq = Arquivo(itau, **dict_arquivo)

        header = {}

        for dados in data:
            arq.incluir_cobranca(header, **dados)
        
        self.escrever_arquivo_remessa(arq)

    
    def escrever_arquivo_remessa(self, arq):
        with open('meu_arquivo.txt', 'w') as arquivo:
            print("veio aqui no with")
            # Escrevendo o conteúdo no arquivo
            arquivo.write(str(arq))
