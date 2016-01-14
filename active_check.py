from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl as pxl
import random
import time
from collections import OrderedDict
from os.path import exists
from os import replace
import pickle
import logging as log
import urllib.request
import xml.etree.ElementTree as ET

def pull_feed(feed_url = 'http://cepamerica.force.com/careers/ts2__apply_to_job?nostate=1&tSource=a0dG0000002vObVIAU&showJobs=500', filename = 'active_check.xml'):
    '''
    Retrieves data from a URL and stores it as a file.
    
    Args:
        URL : Location that contains the data the user is pulling.
        Filename : Filename where the pulled data will be dumped.
    
    Returns:
        The file type and name per user specification.
    '''
    feed_data_pull = urllib.request.urlretrieve(feed_url, filename)
    print('inside pull_feed')
    
def parse_xml(filename = 'active_check.xml'):
    feed = ET.parse(filename)
    root = feed.getroot()
    print('inside parse_xml')

    print('inside feed_elements')
    
    elements = []
    
    for root_elements in root: #channel
        #print('root elem', root_elements.tag)
        for branch_elements in root_elements: #title, description, language, item
            #print ('branch elem', branch_elements.tag)
            post_elements = []
            for leaf_elements in branch_elements: #title, link, description, pubdate
                #print('leaf elem', leaf_elements.tag)
                post_elements.append(leaf_elements.text)
            #print(post_elements)
            elements.append(post_elements)
            #print(elements)
        #elements = elements
    print('END OF FX')
    #print(elements[0:5])
    return elements
        
def clean_parse_data():
    #check items in elements and delete those from list that are 0
    elements = parse_xml()
    print('BEGIN CLEAN FX')
    print(elements[0:3])
    for item in elements:
        #print(item)
        if item == []:
            elements.remove(item)
        #for i in item:
        #    #print(i)
        #    if i == None:
        #        print('I blank found')
        #        elements.remove(item[i])
    #print(elements)
    print(elements[0:3])
    return elements

def write_master(sname = 'master_file.xlsx'):
    master_data = clean_parse_data()
    newWB = pxl.Workbook()
    sheet = newWB.active
    print('MASTER DATA')
    #print(master_data)
    
    headers = ['Title', 'Link', 'Description', 'Pub Date']
    
    for h in range(len(headers)):
        sheet.cell(row = 1, column = h + 1).value = headers[h]
    
    row_index = 2
    for job in master_data:
        #row_index = master_data.index(job) + 2
        #print(row_index)
        for j in job:
            col_index = job.index(j) + 1
            #print(col_index)
            #print(type(row_index))
            #print(type(col_index))
            #for j in job:
            sheet.cell(row = row_index, column = col_index).value = j
        row_index += 1

    newWB.save(sname)
    
    
def run():
    pull_feed()
    #parse_xml()
    #clean_parse_data()
    write_master()

if __name__ == '__main__':
    run()