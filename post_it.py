import openpyxl as pxl
import logging as log
from os.path import exists
from os import replace
from master_check import master_check as mstr_check
from master_check import compare_checks as find_active
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_new_ids():
    '''Runs check scripts and returns the unique IDs for new and active jobs only.
    '''
    mstr_check()
    
    new_ids = find_active()
    #print(new_ids)
    return new_ids

def post_jobs():
    driver = webdriver.Firefox() # use PhantomJS for actual driver once complete and monitoring is not needed
    jobs_to_post = get_new_ids()
    print(jobs_to_post)
    for job in jobs_to_post:
        print(job)
        driver.get(job)
# TODO add distribution function for actual distribution to job boards
# TODO add function that gets called here. Will take the job information from active_file and add it to master_file so that it is not posted multiple times
    driver.close()
    
#def init_service_timer():
#   '''Initializes a time check loop that checks if it is midnight every fifteen minutes.
#   '''
#    counter = 1
#    while counter <= 10: # Change to while True for continual check
#        ct = datetime.datetime.now()
#        ct = ct.timetuple()
#        
#        if ct[3] == 24:
#            post_jobs()
#        else:
#            print('Ran service check at', datetime.datetime.now())
#            time.sleep(20)
#            counter += 1
            
def run():
    #get_new_ids()
    post_jobs()
    #init_service_timer()

if __name__ == '__main__':
    run()