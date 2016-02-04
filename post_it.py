import openpyxl as pxl
import logging as log
from os.path import exists
from os import replace
from master_check import master_check as mstr_check
from master_check import compare_checks as find_active
import datetime
import time

def get_new_ids():
'''Runs check scripts and returns the unique IDs for new and active jobs only.
'''
    mstr_check()
    
    new_ids = find_active()
    print(new_ids)
    
def init_service_timer():
'''Initializes a time check loop that checks if it is midnight every fifteen minutes.
'''
    counter = 1
    while counter <= 10: # Change to while True for continual check
        ct = datetime.datetime.now()
        ct = ct.timetuple()
        
        if ct[3] == 24:
            get_new_ids()
        else:
            print('Ran service check at', datetime.datetime.now())
            time.sleep(20)
            counter += 1
            
def run():
    init_service_timer()

if __name__ == '__main__':
    run()