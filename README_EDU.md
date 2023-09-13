# Instalación

1. Inst. Miniconda
    1. wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    1. chmod +x Miniconda3-latest-Linux-x86_64.sh
    1. bash Miniconda3-latest-Linux-x86_64.sh
1. Crear env. python 3.8.13
    1. Abrir nueva terminal
    1. conda create --name demml python=3.8.13
    1. conda activate demml
    1. pip install kedro kedro-viz
1. Crear proyecto kedro
    1. kedro new --starter=pyspark
    1. cd iris-pyspark/
1. Configuración git
    1. git config --global init.defaultBranch main
    1. git branch -m main
    1. git init
    1. Creo el repo en Github con el nombre "iris-pyspark"
    1. git remote add origin https://github.com/eromerobilbomatica/iris-pyspark.git
    