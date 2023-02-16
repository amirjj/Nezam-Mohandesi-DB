import time
import urllib.parse
import urllib.request
from utils import logit, make_formfields_config
from config import (
    URI, TOTAL_ENTRY, NUMBER_OF_PAGES, HEADERS, FORM_FIELDS, 
    STATUS_FILE, OUTPUT_DIR, VIEWSTAT_FILE, 
    EVENTVALIDATON_FILE, GET_HEADERS, INITIAL_FIELDS
)
import requests
from dom import pars_and_fetch


class Attacker:
    def __init__(self, page_number=2):
        self.page_number = page_number
        
    def save_status(self):
        """ save the current page_number
        in order to retain progress
        """
        with open(STATUS_FILE, 'a') as f:
            print(self.page_number, file=f)
         
    def save_fetched_data(self, the_page):
        print(OUTPUT_DIR)
        OUTFILE = OUTPUT_DIR + 'out_page%s.html'%self.page_number
        with open(OUTFILE, 'w') as writer:
            writer.write(the_page)

    @staticmethod
    def get_viewstat():
        with open(VIEWSTAT_FILE, "r") as f:
            return f.readline()

    @staticmethod
    def save_viewstat(viewstat):
        with open(VIEWSTAT_FILE, "w") as f:
            return f.write(viewstat)

    @staticmethod
    def get_eventvalidation():
        with open(EVENTVALIDATON_FILE, "r") as f:
            return f.readline()

    @staticmethod
    def save_eventvalidation(eventvalidation):
        with open(EVENTVALIDATON_FILE, "w") as f:
            return f.write(eventvalidation)

    @staticmethod
    def fetch_header_parameters():
        r = requests.get(URI, headers=GET_HEADERS)
        return_string = r.content
        viewstat = pars_and_fetch(return_string, '__VIEWSTATE')
        eventvalidation = pars_and_fetch(return_string, '__EVENTVALIDATION')
        return viewstat, eventvalidation
        
    def single_attack(self, formFields):
        encodedFields = urllib.parse.urlencode(formFields)
        encodedFields = encodedFields.encode('ascii')
        req = urllib.request.Request(URI, encodedFields, HEADERS)

        with urllib.request.urlopen(req) as response:
           the_page = response.read().decode('utf-8')
           print(response.status)
           print(response.reason)
           self.save_fetched_data(the_page)
           return the_page

    def first_search(self):
        viewstat = self.get_viewstat()
        eventvalidation = self.get_eventvalidation()
        
        print("--------first search------------")
        form_fields = make_formfields_config(INITIAL_FIELDS, None, 
                                            viewstat, eventvalidation)
        the_page = self.single_attack(form_fields)
        viewstat = pars_and_fetch(the_page, '__VIEWSTATE')
        eventvalidation = pars_and_fetch(the_page, '__EVENTVALIDATION')
        self.save_viewstat(viewstat)
        self.save_eventvalidation(eventvalidation)
        
    def run(self):
        """Core method, connects to the server and fetch the data, until the last page
        """
        viewstat, eventvalidation = self.fetch_header_parameters()
        self.save_viewstat(viewstat)
        self.save_eventvalidation(eventvalidation)
        print("--------Get-----------")
        print(viewstat)
        print(eventvalidation)
        time.sleep(10)
        print("Get Completed.")
        
        self.first_search()
        time.sleep(10)
        
        for iteration in range(self.page_number + 1, NUMBER_OF_PAGES + 1):
            self.page_number = iteration 
            print(self.page_number)
            viewstat = self.get_viewstat()
            eventvalidation = self.get_eventvalidation()
            
            form_fields = make_formfields_config(FORM_FIELDS, self.page_number, 
                                                viewstat, eventvalidation)
            print("++++++++++++++++form fields+++++++++++++++++")
            the_page = self.single_attack(form_fields)
            print("+++++++++++++++++++++++++++++++++")
            viewstat = pars_and_fetch(the_page, '__VIEWSTATE')
            eventvalidation = pars_and_fetch(the_page, '__EVENTVALIDATION')
            self.save_viewstat(viewstat)
            self.save_eventvalidation(eventvalidation)
            
            self.save_status()
            time.sleep(10)
