import openpyxl as pxl
import logging as log
from os.path import exists
from os import replace
from master_check import master_check as mstr_check
from master_check import compare_checks as find_active

def get_new_ids():
    mstr_check()
    
    new_ids = find_active()
    print(new_ids)

def run():
    get_new_ids()

if __name__ == '__main__':
    run()