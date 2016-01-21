import openpyxl as pxl
import logging as log
from os.path import exists
from os import replace
from active_check import run as active_run

def compare_checks():
    '''
    Compares data from active_file to data in master_file and removes duplications from active_file.
    '''
    print('Run compare checks')

def find_active_file(active_file='active_file.xlsx'):
    '''Checks that active_file exists and proceeds or creates active_file and proceeds.
    
    Args:
        active_file (str) = File name of active data from user feed. Should end with '.xlsx'. Defaults to 'active_file.xlsx'.
    '''
    if exists(active_file):
        compare_checks()
    else:
        active_run()
        compare_checks()

def write_blank(fout='master_file.xlsx'):
    '''Writes blank file and saves it to 'fout'.
    
    Args:
        fout (str): File name to save the blank Excel master_file as. Should end with '.xlsx'. Defaults to 'master_file.xlsx'.
    '''
    newWB = pxl.Workbook()
    newWB.save(fout)

def master_check(master_file='master_file.xlsx'):
    '''Checks that master_file exists and proceeds or creates master_file and proceeds.
    
    Args:
        master_file (str) = File name of master data repository. Should end with '.xlsx'. Defaults to 'master_file.xlsx'.
    '''
    if exists(master_file):
        find_active_file()
    else:
        write_blank()
        find_active_file()
        
def run():
    master_check()
    
if __name__ == '__main__':
    run()