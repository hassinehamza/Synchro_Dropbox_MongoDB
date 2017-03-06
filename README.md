# Synchro_Dropbox_MongoDB
synchroniser un dossier sous DROPBOX avec une  base mongoDB

##Install

installer python : 
>sudo apt-get install python python-pip

installer dropbox for python:
>pip install dropbox
		
installer requests :
>pip install requests

installer pymongo :
>pip install pymongo

installer mongodb : 
(https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

##How to Use : 

###Configuration Basique 

1- D'abord , vous devez creer une application dropbox et générer votre *acces token*

2- Ensuite vous devez configurer votre code (test.py): 
```
# Get your acces token from the Dropbox developer website
access_token =  <your access token > 
```
```
#Liste des extensions autorisées 
liste = ["pdf", "doc", "docx", "ppt", "pptx", "jpeg", "jpg", "png", .....]
```
```
#chemin de votre dossier sur dropBox (exple "/Docs" , sans '/' à la fin )
chemin = "/Docs"
```
```
#taille de fichhier  ( exple 8Mo ) 
taille = 8000000
```

###Overview 

1. Se Connecter avec votre compte DropBox 

2. Se Connecter avec votre base de Données 

3. Les Methodes : 
	 
	 *ajouter(chemin) : permet de parcourir le fichier dropbox : si on trouve un fichier < taille et d'une extension autorisée , on l'enregistre à notre base de données sous forme bianire
	 
	 *deleteNom(chemin) : permet de supprimer un fichier , qui n'exite plus sur dropbox , de notre BD ( en utilisant une recherche personalisée ) 
	 
	 *deleteNomDéfini(chemin) : permet de supprimer un fichier , qui n'exite plus sur dropbox , de notre BD ( en utilisant une recherche prédéfinie  ) 

4. une boucle while : 
	 
	 *parcourir notre fichier dropbox et ajouter ( et / ou mise à jour ) les fichiers de notre BD 
	 
	 *parcourir notre BD et supprimer les fichiers qui n'exite plus sur notre dropBox
	 
	 *attendre une minute et réexcuter le process 
	 
## Testing 
> python test.py

## creer un service linux ( daemon ) : 
###configurer le fichier test.sh

```
# Change the next 3 lines to suit where you install your script and what you want to call it
DIR=/home/lenovo #chemin de votre fichier code
DAEMON=$DIR/test.py #nom de votre fichier code
DAEMON_NAME=test #nom de service
```

### lancer le service 

copier le script .sh en /etc/init.d et donner les autorisations necessaires 
>sudo cp test.sh /etc/init.d/
>sudo chmod 755 test.sh 

lancer le script 
>sudo /etc/init.d/test.sh start

on peut aussi essayer : status , stop , restart









