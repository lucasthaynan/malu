
# coding: utf-8

# In[ ]:


def cidade_tempo():

    import csv

    cidade_desejada = input("Qual município você deseja saber a previção do tempo para amanhã? ")
    cidade_desejada = cidade_desejada.upper()
    
    # abrindo planilha csv com os nomes das cidades e código do site do INPE
    
    arquivo = open('tempo_cidades_br.csv', encoding='utf8')

    codigo = 0

    for registro in csv.DictReader(arquivo):
        if registro['cidade'] == cidade_desejada:
            codigo = codigo + int(registro['codigo_cidade'])
            estado = registro['uf']

    if codigo > 0:

        import requests 
        from bs4 import BeautifulSoup

        requisicao = requests.get(f'http://www.cptec.inpe.br/cidades/tempo/{codigo}')

        sopa = BeautifulSoup(requisicao.content, "html.parser")

        # Dados gerais

        informacao_detalhada = sopa.find_all("div", {"class": "previsao deg_azul2"})

        # Data

        data = informacao_detalhada[1].find("div", {"class": "tit"}).text.strip() 

        dia_semana, dia_mes = data.split(' - ')

        dia, mes, ano = dia_mes.split('.')

        dia_semana = dia_semana.lower()

        # Tempo

        tempo = sopa.find_all("div", {"class": "prev"})

        # Temperadtura Mínima
        minima = tempo[1].find("div", {"class": "c2"})

        temperatura_minima = minima.find('b').text.strip()

        # Temperadtura Máxima
        maxima = tempo[1].find("div", {"class": "c3"})

        temperatura_maxima = maxima.find('b').text.strip()

        # Probalidade de chuva
        pro_chuva = tempo[1].find("div", {"class": "c4"})

        pro_chuva = pro_chuva.find('b').text.strip()

        pro_chuva = pro_chuva.strip(" %")

        # Texto de tempo detalhado

        info_tempo = informacao_detalhada[1].find("div", {"class": "c8"}).text.strip()

        info_tempo_resumido, info_tempo_detalhado = (info_tempo.split('-'))
        
        info_tempo_resumido = info_tempo_resumido.lower()

        info_tempo_detalhado = info_tempo_detalhado.lower()


        # Imprimindo matéria final

        titulo = (f"'{info_tempo_resumido.strip()}', indica previsão do tempo para amanhã em {cidade_desejada}")
        print(" ")
        print(titulo.upper())
        print(" ")
        if dia_semana == "sábado" or dia_semana == "domingo":
            print(f"A previsão do tempo para o município de {cidade_desejada.upper()}-{estado} para este {dia_semana.strip()}, dia {dia}, indica{info_tempo_detalhado.strip('.')}. A máxima registrada será de {temperatura_maxima} e a mínima de {temperatura_minima}. A probabilidade de chuva para amanhã é de {pro_chuva}%.")
            print(" ")
            print("As informações desta matéria foram coletadas pela nossa robô do tempo Maju, de modo automatizado, no site do Instituto Nacional de Pesquisas Espaciais (Inpe).")
        else:
            print(f"A previsão do tempo para o município de {cidade_desejada.upper()}-{estado} para esta {dia_semana.strip()}, dia {dia}, indica{info_tempo_detalhado.strip('.')}. A máxima registrada será de {temperatura_maxima} e a mínima de {temperatura_minima}. A probabilidade de chuva para amanhã é de {pro_chuva}%.")
            print(" ")
            print("As informações desta matéria foram coletadas pela nossa robô do tempo Maju, de modo automatizado, no site do Instituto Nacional de Pesquisas Espaciais (Inpe).")

    else:
        print('CIDADE NÃO ENCONTRADA =(')
        print('Tente novamente!')
        cidade_tempo()
        
cidade_tempo()

