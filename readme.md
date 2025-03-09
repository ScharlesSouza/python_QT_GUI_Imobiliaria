# python_QT_GUI_Imobiliaria
Projeto de ambientação na biblioteca PyQT e QT Designer

CRIAR O VENV
python -m venv venvThisProject 

#Liberar execução de script no windows
Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned

#Executar um ambiente virtual python
venvThisProject\Scripts\Activate.ps1

PARA EXECUTAR
Criar uma imagem:
docker build -t nome_image .

Criar um container a partir da imagem:
docker run nome_image


Creando uma imagem a partir do Dokerfile

FROM: Especifica a imagem base a ser usado.

RUN:  Os comandos que serão rodados dentro do container Docker durante a construção do projeto

COPY: copia arquivos do sistema de arquivos local para dentro da imagem Docker

WORKDIR: defini o diretorio de trabalho no quais serão executados os comandos dentro do Docker

CMD: especifica os comandos que serão executados quando o container Docker iniciar.

Criar uma imagem:
docker build -t nome_image .

Criar um container a partir da imagem:
docker run nome_image
