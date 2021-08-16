import os

from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv() 

now = datetime.now()
now_date = f'{now.day}/{now.month}/{now.year}'
now_time = f'{now.hour}:{now.minute}'

driver = webdriver.Chrome()
driver.get('https://www.c19.cl/')

# Datos a cargar

last_name = os.environ.get('last_name')
first_name = os.environ.get('first_name')
sex = os.environ.get('sex')
date_of_birth = os.environ.get('date_of_birth')
nationality =  os.environ.get('nationality')
type_dni =  os.environ.get('type_dni')
number_dni = os.environ.get('number_dni')
country_of_residence = os.environ.get('country_of_residence')
type_of_traveler = os.environ.get('type_of_traveler')
type_of_stay_in_Chile = os.environ.get('type_of_stay_in_chile')
email = os.environ.get('email')
phone_to_contact = os.environ.get('phone_to_contact')
type_address = os.environ.get('type_address')
address = os.environ.get('address')
region = os.environ.get('region')
commune = os.environ.get('commune')
transport = os.environ.get('transport')
name_to_control = os.environ.get('name_to_control')
type_transport = os.environ.get('type_transport')

box_internacional = driver.find_element_by_class_name('box-internacional')
box_internacional.click()

box_internacional2 = driver.find_element_by_class_name('box-internacional')
box_internacional2.click()

driver.find_element_by_id('apellidopaterno').send_keys(last_name)
driver.find_element_by_id('nombres').send_keys(first_name)
driver.find_element_by_id('sexo').send_keys(sex)
driver.find_element_by_id('fechanacimiento').send_keys(date_of_birth)
driver.find_element_by_id('nacionalidad').send_keys(nationality)
driver.find_element_by_id('documentodeviaje').send_keys(type_dni)
driver.find_element_by_id('numerodocumentodeviaje').send_keys(number_dni)
driver.find_element_by_id('paisderesidencia').send_keys(nationality)
driver.find_element_by_id('tipopasajero').send_keys(type_of_traveler)
driver.find_element_by_id('tipo_de_permanencia').send_keys(type_of_stay_in_Chile)
driver.find_element_by_id('fecha_estimada_salida').send_keys(now_date)
driver.find_element_by_id('motivodeviaje').send_keys('LABORAL')
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('confirmemail').send_keys(email)
driver.find_element_by_class_name('iti__selected-flag').click()
driver.find_element_by_id('iti-0__item-ar').click()
driver.find_element_by_id('telefono1').send_keys(phone_to_contact)
driver.find_element_by_id('tipoAislamiento').send_keys(type_address)
driver.find_element_by_id('direccion').send_keys(address)
driver.find_element_by_id('numero').send_keys(address)
driver.find_element_by_id('region').send_keys(region)
driver.find_element_by_id('comuna').send_keys(commune)
driver.find_element_by_id('procedencia').send_keys(nationality)
driver.find_element_by_id('controlfronterizo').send_keys(transport)
driver.find_element_by_id('bordercontrolname').send_keys(name_to_control)
driver.find_element_by_id('controlfronterizo').send_keys(type_transport)
driver.find_element_by_id('fecha_estimada_llegada').send_keys(now_date)
driver.find_element_by_id('hora_estimada_llegada').send_keys(now_time)
driver.find_element_by_id('visitedselect').click()
driver.find_element_by_id('visitedselect').send_keys('ARGENTINA')
driver.find_element_by_name('contacto_persona_enferma').send_keys('NO')
driver.find_element_by_name('contacto_estrecho_covid19').send_keys('NO')
driver.find_element_by_name('examen_pcr').send_keys('NO')
driver.find_element_by_id('sintomasNone').click()
driver.find_element_by_id('checkbox_final').click()

print('scraping finalizado con exito')
# driver.find_element_by_id('submit').click()