# -*- coding: utf-8 -*-
###############################################################
# Máster de Ciencia de Datos - UOC                            #
# M2.851 - Tipología y ciclo de vida de los datos             #
# Práctica 1 - Web Scraping                                   #
# constants.py                                                #  
#                                                             #
# Autores:                                                    #
#   Azucena González (azucenagm)                              #
#   Jesús Márquez (jmarquez01)                                #
###############################################################

# Fichero que contiene un conjunto de constantes de utilidad para el web scraper

# Campos básicos de un alimento
BASIC_LIST = ('f_id', 'f_ori_name', 'sci_name', 'edible_portion')

# Campos de detalle de un alimento
DETAIL_LIST = ('alcohol (etanol)', 'energía, total', 'grasa, total (lipidos totales)',
               'proteina, total', 'agua (humedad)', 'carbohidratos', 'fibra, dietetica total',
               'ácido graso 22:6 n-3 (ácido docosahexaenóico)', 'ácido graso 20:5 (ácido eicosapentaenóico)',
               'ácido graso 12:0 (láurico)', 'ácido graso 14:0 (ácido mirístico)',
               'ácido graso 16:0 (ácido palmítico)', 'ácido graso 18:0 (ácido esteárico)',
               'ácido graso 18:1 n-9 cis (ácido oléico)', 'ácido graso 18:2',
               'ácido graso 18:3', 'ácido graso 20:4 n-6  (ácido araquidónico)',
               'ácidos grasos, monoinsaturados totales',
               'ácidos grasos, poliinsaturados totales',
               'ácidos grasos saturados totales','ácidos grasos, trans totales',
               'colesterol',
               'Vitamina A equivalentes de retinol de actividades de retinos y carotenoides',
               'Vitamina D',
               'Viamina E equivalentes de alfa tocoferol de actividades de vitámeros E',
               'folato, total', 'equivalentes de niacina, totales', 'riboflavina',
               'tiamina', 'Vitamina B-12', 'Vitamina B-6, Total',
               'Vitamina C (ácido ascórbico)', 'calcio', 'hierro, total', 'potasio',
               'magnesio', 'sodio', 'fósforo', 'ioduro', 'selenio, total', 'zinc (cinc)')

# Nombre del fichero CSV de salida que contendrá la información nutricional de los alimentos
CSV_OUTPUT_FILE = "nutritional-info.csv"

# Cabecera para el fichero CSV de salida
CSV_HEADER = BASIC_LIST + DETAIL_LIST

# Valor utilizado para campos sin información
EMPTY = 'NA'

# URl sobre la que se realizarán las peticiones de la página web de BEDCA
URL = "http://www.bedca.net/bdpub/procquery.php"

# Cabeceras de la petición: se indica que el texto es XML y se facilita un user-agent
HEADERS = {'Content-Type':'text/xml', 'User-Agent':'ws-uoc-pra1'}

# Factor de retardo entre peticiones
DELAY_FACTOR = 2

# Petición de los ids del total de alimentos 
IDS_REQUEST = """<foodquery>
	<type level="1"/>
	<selection>
		<atribute name="f_id"/>
	</selection>
	<condition>
		<cond1>
			<atribute1 name="f_origen"/>
		</cond1>
		<relation type="EQUAL"/>
		<cond3>BEDCA</cond3>
	</condition>
	<order ordtype="ASC">
		<atribute3 name="f_id"/>
	</order>
</foodquery>"""

# Primer fragmento de la petición de información detallada para un alimento concreto
DETAILS_REQUEST_INI = """<foodquery>
	<type level="2"/>
	<selection>
		<atribute name="f_id"/>
		<atribute name="f_ori_name"/>
		<atribute name="sci_name"/>
		<atribute name="f_des_esp"/>
		<atribute name="edible_portion"/>
		<atribute name="f_origen"/>
		<atribute name="c_id"/>
		<atribute name="c_ori_name"/>
		<atribute name="eur_name"/>
		<atribute name="componentgroup_id"/>
		<atribute name="best_location"/>
		<atribute name="v_unit"/>
		<atribute name="u_id"/>
		<atribute name="u_descripcion"/>
		<atribute name="value_type"/>
		<atribute name="vt_descripcion"/>
		<atribute name="mu_id"/>
		<atribute name="mu_descripcion"/>
	</selection>
	<condition>
		<cond1>
			<atribute1 name="f_id"/>
		</cond1>
		<relation type="EQUAL"/>
		<cond3>"""
        
# Segundo fragmento de la petición de información detallada
DETAILS_REQUEST_FIN = """</cond3>
	</condition>
	<condition>
		<cond1>
			<atribute1 name="publico"/>
		</cond1>
		<relation type="EQUAL"/>
		<cond3>1</cond3>
	</condition>
	<order ordtype="ASC">
		<atribute3 name="componentgroup_id"/>
	</order>
</foodquery>"""


