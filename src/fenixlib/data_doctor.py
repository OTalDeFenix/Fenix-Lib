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

def WriteForDebug(VaribleToDebug, FileNameForDebug):	
	FileDebug = FileNameForDebug
	config = configparser.ConfigParser()
	config.add_section('DEBUG')
	config.set('DEBUG', 'variavel', VaribleToDebug)
	with open(FileDebug, 'w') as DebugFile:
		config.write(DebugFile)
    
#def QuickSwap(Urls, Swaps):
#    Replaces = []
#    for item in Urls:
#        replaced_item = item  # Inicializa replaced_item com item original
#        for Key_url, Name in Swaps:
#            if Key_url in replaced_item:
#                replaced_item = replaced_item.replace(Key_url, Name)
#        Replaces.append(replaced_item)  # Adiciona o item substituído à lista Replaces
#    return Replaces
