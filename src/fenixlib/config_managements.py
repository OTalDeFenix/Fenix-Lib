import configparser
import tkinter as tk
from tkinter import filedialog
import os

def OpenFileMemory():
	config = configparser.ConfigParser()
	if os.path.exists("config.ini"):
		config.read('config.ini')
		path = config.get('EXCEL', 'Local_da_tabela')
		return path
	else:
		config.add_section('CONFIGS')
		config.add_section('EXCEL')
		config.set('EXCEL', 'Local_da_tabela', filedialog.askopenfilename())
		with open('config.ini', 'w') as config_file:
			config.write(config_file)
		config.read('config.ini')
		path = config.get('EXCEL', 'Local_da_tabela')
		return path