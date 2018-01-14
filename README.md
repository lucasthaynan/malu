# Maju
A nossa robô do tempo Maju é especialista em previsão do tempo, e com uma ajudinha dos dados do Instituto Nacional de Pesquisas Espaciais (Inpe), ela escreve uma pequena matéria sobre o tempo de qualquer um dos 5.570 municípios brasileiros. Legal, né?

E tem mais. Ela faz questão de detalhar como está previsto o tempo, com informações sobre as temperaturas mínima e máxima, e também qual é a probabilidade de chover naquele município.

Dentro da matéria, ela descreve a previsão do tempo sempre do dia seguinte ao da busca, ou seja, se eu rodo o programa hoje (dia 14), ela vai me retornar com a previsão do tempo de amanhã (dia 15), e se rodar amanhã retornará o tempo do outro dia. E assim vai...

O script em Python pode ser visualizado no arquivo Maju_robo_tempo.py

# Arquivo CSV
Ao iniciar o script percebi, que no site do INPE, cada município brasileiro era representado, na url de busca, por um código. Por exemplo, Maceió é o 233, já São Paulo é o número 244. 

Então, para que eu pudesse fazer uma busca por um determinado município, dentro do programa que criei, era preciso apenas associar o nome ao número. Assim, utilizei a extensão Web Scraper do Google Chrome para fazer isso para mim. E ela me gerou uma linda tabela CSV que pode ser consultada no arquivo tempo_cidades_br.csv

# Como o programa funciona?
É super fácil. Basta rodá-lo em seu diretório Python e digitar um nome de um município de sua preferência. E aí a nossa Maju entra em ação, e rapidinho vai escrever uma matéria para você sobre a previsão do tempo, sempre para amanhã, daquele município. 

Sim, e se você errar o nome ela vai pedir que você digite novamente até que acerte.
 
# Rodando o programa
Para rodar o script é necessário ter o Python 3.6 instalando, além das bibliotecas csv, request e  BeautifulSoup.
