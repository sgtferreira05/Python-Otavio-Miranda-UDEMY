#   Ambientes virtuais em Python(venv)
# Um ambiente virtual carrega toda a sua instalação do Python para
#uma pasta no caminho escolhido. Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.
# Venv é o módulo que vamos usar para criar ambientes virtuais. Você pode dar o nome que preferir para um AV, mas os mais comuns são: venv env .venv .env

#       Como criar um AV:
# Abra a pasta do seu projeto no seu terminal e digite:
# python -m venv venv(nome do AV)
#       Como ativar o ambiente virtual:
# venv\Scripts\activate
#       Instalar pips(mysql, ...) e desinstalar
# No terminal digitar o código: pip install (nome do arquivo) ou
# python -m pip install (nome do arquivo)
# No terminal digitar o código: pip uninstall (nome do arquivo)

#       Instalar versões antigas de arquivos:
# pip install pymysql==1.0.2 (Versão escolhida) 

#       Para verificar os arquivos instalados:
# pip freeze

#       Repositório dos arquivos (criar um repositório com os arquivos que vai utilizar, INCLUSIVE PRECISA ATUALIZAR A CADA INSTALAÇÃO NOVA)
# pip freeze > requirements.txt

#       Para instalar os arquivos do repositório num ambiente virtual novo(vai importar tudo do repositório):
# pip install -r .\requirements.txt

