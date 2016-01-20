import openpyxl as pxl
import logging as log
from os.path import exists
from os import replace
import active_check as AC
from active_check import run as active_run

def compare_checks():
    print('Run compare checks')

def find_active_file(active_file='active_file.xlsx'):
    if exists(active_file):
        compare_checks()
    else:
        active_run()
        compare_checks()

def write_blank(fout='master_file.xlsx'):
    newWB = pxl.Workbook()
    newWB.save(fout)

def master_check(master_file='master_file.xlsx'):
    if exists(master_file):
        find_active_file()
    else:
        write_blank()
        
def run():
    master_check()
    
if __name__ == '__main__':
    run()