# -*- coding: utf-8 -*-
###############################################################
# Máster de Ciencia de Datos - UOC                            #
# M2.851 - Tipología y ciclo de vida de los datos             #
# Práctica 1 - Web Scraping                                   #
# main.py                                                     #  
#                                                             #
# Autores:                                                    #
#   Azucena González (azucenagm)                              #
#   Jesús Márquez (jmarquez01)                                #
###############################################################

# Programa para lanzar la ejecución del web scraper nutriScraper
from nutriscraper import NutriScraper
import datetime
import time

# Creación del objeto
webScraper = NutriScraper()

print("Inicio de la ejecución: " + str(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")))
initialTime = time.time()

# Ejecución
webScraper.execute()

print("Final de la ejecución: " + str(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")))
print("Tiempo total: " + str(time.time() - initialTime))
