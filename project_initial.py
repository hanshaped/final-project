# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:32:37 2020

@author: black
"""
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from multiprocessing import Pool

def transcription():
    sentences = input('Type or paste your sentence(s) below:\n')
    print(sentences)

#def main():
    #print('Getting staff urls ...')

    #staff_url='http://wa.amu.edu.pl/wa/en/staff_list'
   # staff_content = get_content(staff_url)
    
   # links = staff_content.find_all('a')    

   # urls = []

#    for link in links:
  #      if len(link.get_text()) > 1:
   #         base_url = 'http://wa.amu.edu.pl'
   #         url= urllib.parse.urljoin(base_url, link['href'])
    #        encoded_url = fix_encoding(url)
     #       urls.append(encoded_url)
    
#    print('Staff emails found:')    
    

#    mypool = Pool()
 #   mypool.map(print_details, urls)



#def fix_encoding(url):
#     components = urllib.parse.urlsplit(url)
 #    components = list(components)
 #    components[2] = urllib.parse.quote(components[2])
 #    return urllib.parse.urlunsplit(components)
 
#def get_content(url):
 #   response = urllib.request.urlopen(url)
 #   data= response.read()
  #  doc = BeautifulSoup(data, 'html.parser')
  #  return doc.find(id = 'tresc_wlasciwa')    

transcription()