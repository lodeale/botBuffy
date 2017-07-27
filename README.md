# botBuffy
Es un script que permite conectarse a telegram o gmail y pasar información desde una cuenta a servicios rest que están guardados en una base de datos.

# Configuración
1) Ingrese las credenciales de base de datos en _dbData y de la cuenta de telegram o gmail en _data en el archivo config/credential.py
2) En el archivo app.py ingresar si la conexin es por gtalk o telegram comentando y descomentando la linea correspondiente:
* c.setConnect(Telegram())
* c.setConnect(Gtalk())

# Instalación
1) git clone XXXXXX
2) cd ./botBuffy
3) mysql -uroot -p
mysql> create database leviathan;
mysql> use leviathan;
mysql> source leviathan.sql;
mysql> quit;

4) pip install -r requirements.txt

# Uso
python app.py
