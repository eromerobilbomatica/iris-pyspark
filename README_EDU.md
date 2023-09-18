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
1. Instalalo las dependencias
    1. Incluyo pyspark==3.3.1 en el src/requirements.txt
    1. pip install -r src/requirements.txt
<!-- 1. Java: 
    1. Instalación: sudo apt update && sudo apt install openjdk-8-jdk-headless
    1. Desintalación: sudo apt remove openjdk-8-jdk-headless -->
1. Instalo java
    1. wget https://builds.openlogic.com/downloadJDK/openlogic-openjdk/8u362-b09/openlogic-openjdk-8u362-b09-linux-x64.tar.gz
    1. tar -xvzf openlogic-openjdk-8u362-b09-linux-x64.tar.gz
    1. sudo mv openlogic-openjdk-8u362-b09-linux-x64 /usr/lib/jvm/
    1. sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/bin/java 1
    1. sudo update-alternatives --config java
    1. para comprobar que la versión java coincide con el DEMML ``java -version``

    * En el caso de tener que desintalar de esta versión de java por completo
        1. Eliminar el directorio Java: sudo rm -rf /usr/lib/jvm/openlogic-openjdk-8u362-b09-linux-x64
        1. Eliminar los enlaces simbólicos de Java:
            1. sudo rm -f /usr/bin/java
            1. sudo rm -f /usr/lib/jvm/default-java
        1. Eliminar las entradas de Java del menú de actualización de alternativas: sudo update-alternatives --remove-all java


# Correcciones

## Kedro no me cagar el catalog en el jupyterlab

Dentro del jupyterlab levantado con ``kedro jupyter lab`` ejecutar en una celda:

````
%load_ext kedro.extras.extensions.ipython
%reload_kedro
````

## Mapeo de dns en el archivo etc/hosts

### version de linux usada

````
(demml) coder@coder-eromero-eromero-bcfbb95bd-d4kc5:~/eromero/iris-pyspark$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.6 LTS
Release:        20.04
Codename:       focal
````

### instalación nano y ping

* nano: ``sudo apt update && sudo apt install nano``
* ping: ``sudo apt install iputils-ping``