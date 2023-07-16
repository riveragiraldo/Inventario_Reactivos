# Inventario_Reactivos

## Windows Instructions 
### PostgreSQL
First check the installation of PostgreSQL 15.2 Version<br>
Also Create a Empty Database with the Name Reactivos<br>
Modify the inventariosreac/settings.py  line 82 and 83  to your user name and password of Database<br>


## Linux Instructions 

In case of you want to perform the installation in a linux operating enviroment follow these steps<br>

### PostgreSQL 
The installation instructions depend on the Linux distribution, however to start the env that allows you to run pgadmin4 follow these steps<br>
* To start the enviroment type on terminal source env/bin/activate <br>
* Go to pgadmin4 by cd pgadmin4 <br>
* Execute pgadmin4 and wait <br>
**Note that the secure protocol generally does not allow to open pgamind 4 verifies http and not https**<br>

### Virtual Enviroment
Note that linux executions usually take place in virtual environments <br>
* Execute the start enviroment on terminal  env/bin/activate <br>
* Go to The folder where the repo was cloned usually follow Documents/GitHub/Inventario_Reactivos/<br>

# General Instructions 

## Install Requirements
→ On terminal execute the command pip install -r ./requirements.txt <br>
## Create User
→ Next Create a Super User python manage.py createsuperuser<br>

## Execute the Enviroment
→ Run python manage.py runserver<br>


