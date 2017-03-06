#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox
import base64
import bson
import pymongo
import time
import requests
from bson.binary import Binary


# Get your acces token from the Dropbox developer website
access_token = ''
dbx = dropbox.Dropbox(access_token)

#Liste des extensions autorisé 
liste = ["pdf", "doc", "docx", "ppt", "pptx", "jpeg", "jpg", "png"]

#chemin de fichier à Synchroniser : 
chemin = "/Docs"

#taille max des fichiers : 
taille = 8000000

# establish a connection to the database
connection = pymongo.MongoClient()
 
#get a handle to the test database
db = connection.dropbox
coll = db.test6
 

#sauvegarder un fichier dropBox à ma BD
def ajouter(folder):
	#list documents in your folder 1
	for entry in dbx.files_list_folder(folder).entries:
		#recuperer le nom du fichier 
		nom = entry.name
		#récupérer l'extension
		ext = nom.split('.')[1]
		#Fichier < 8Mo et a une extenstion autorisée
		if entry.size < taille and ext in liste :
   			t = folder+"/"+entry.name
			#télécharger le fichir
   			f, res = dbx.files_download(t, rev=None)
			#Mettre le contenu sous la forme binaire
      			encoded = Binary(res.content, 0)
			#insérer et mettre à jour
      			coll.update( {"hash": f.content_hash }, {"filename": entry.name , "file": encoded, "hash": f.content_hash } , True)
	

#supprimer un fichier , qui n'existe plus sur dropBox , de ma BD ( selon nom du fichier ) 
def deleteNom(folder):
	ListNom =[] 
	for entry in dbx.files_list_folder(folder).entries:
		ListNom.append(entry.name)
	for doc in coll.find():
		critere = doc["filename"]
		if not (critere in ListNom) :
			coll.remove({"filename": critere })
	print 'hello'

#supprimer un fichier , qui n'existe plus sur dropBox , de ma BD ( en utilisant une fonction prédéfini de Dropbox SDK )
def deleteNomDefini(folder):
	for doc in coll.find():
		critere = doc["filename"]
		s = dbx.files_search(folder,critere,start=0)
		if s.matches == []:
			coll.remove({"filename": critere })
	print 'hi'
	


	
#boucle qui s'excute chaque une minute pour synchroniser les fichiers ( DropBx / BD )
while True :
	ajouter(chemin)
	deleteNomDefini(chemin)
	print coll.count()
	time.sleep(60)




