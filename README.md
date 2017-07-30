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

# Nuevo Servicio
Para que el bot conozca un nuevo servicio, se agrega una entrada en la base de datos. 
* En la tabla web_services ejecutamos la siguiente linea:
  * INSERT INTO leviathan.web_services (endpoint,name,keywords,datekeyword) VALUES ('servicesName:port','helloWorld',"{'hola':0}",now())

Gracias a la sentencia anterior, el bot puede entender lo siguiente: Si en el texto que escribio el usuario se encuentra un "hola" entonces debe mandarl al servicio con url "servicesName:port" el texto ingresado. El name es un simple nombre para definir los servicios; en el parametro 3 {'hola':0} se pueden agregar mas palabra si se desea como por ejemplo {'hola':0,'adios':0} y es posible porque un mismo endpoint puede contener varios microservicios.
