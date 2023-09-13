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
    1. **Para poder hacer push he tenido que poner como colaborador a mi usuario de github personal  en el repo que tengo con la cuenta de bilbomática porque 
    no he podido cambiarlo en git, por defecto me está manteniendo el usuario IngTecEduardo y de ahí que haya que darle permisos a este.**
    1. git add .
    1. git commit -m "añado instrucción README_EDU.md"
    1. git push -u origin main
    