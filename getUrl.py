#!/usr/bin/python3
import requests
import sys
import argparse
import re
import os
import string
from bs4 import BeautifulSoup
import subprocess
 

class urls:
    
    extantions= list()
    detectDuplicate = list()
    def test(self,url):
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')       
        urls = []
        for link in soup.find_all('a'):
            print(link.get('href'))
            
    def checkDomain(self,url,urlForCheck):
        # domain = os.popen(f"echo \"{url}\" | sed -e 's/[^/]*\/\/\([^@]*@\)\?\([^:/]*\).*/\2/'").read()#.replace(" ","").replace("\n","")
        url = re.match(r"^[a-z]+://([^/:]+)", url).group(1).replace("www.","")
        if url not in urlForCheck:
            print(f"{urlForCheck} <==== out of domain")
            return False
        return True
        
    def extract_urls(self,url):
        req = requests.get(url,verify=False)
                   
        if req.status_code != "404":
            print(f"{req.status_code} ===> {url}")
            # allUrls = "\n".join(re.findall('src="(.*?)"',req.text))+"\n".join(re.findall('href="(.*?)"',req.text))+"\n".join(re.findall(r'http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', req.text))   
            allUrls = re.findall('src="(.*?)"',req.text) + re.findall('href="(.*?)"',req.text) + re.findall(r'http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', req.text)
            self.fillter(allUrls)
            return allUrls
        else:
            print(f"{req.status_code}  ==> {url}")
            
            return "False"

    def deepSearch(self,originalUrl,urls):
        for url in urls:
            if  "https" and "http" not in url:
                # self.extract_urls(url)
                # print("ok " + url)
                
                urlResutl = self.extract_urls(originalUrl+url)
                self.fillter(urlResutl)
            elif self.checkDomain(originalUrl,url):
                urlResutl = self.extract_urls(originalUrl+url)
                self.fillter(urlResutl)
                print(f"{url} <==== ok")  
            else:
                print(f"{url}  <======= out of domain ")      
        
    def fillter(self,urls):
        charactar = string.ascii_letters + string.ascii_uppercase + string.digits 
        extantions= self.extantions
        detectDuplicate = self.detectDuplicate
        with open("allurl.txt",'w') as file:
            for char in charactar:
                for char2 in charactar: 
                    for char3 in charactar:
                        filtter = f".{char}{char2}{char3}"
                        # filtter2 = f".{char}{char2}"
                        for url in urls:
                            if filtter in url[-4:]:
                                if url not in detectDuplicate:
                                    if  filtter not in extantions:
                                        print(f"======{filtter}======")
                                        file.write(f"======{filtter}======\n")
                                        extantions.append(filtter)
                                    print(url) 
                                    file.write(url+"\n") 
                                    detectDuplicate.append(url)
                            elif filtter in url[:-9]:
                                if url not in detectDuplicate:
                                    if  filtter not in extantions:
                                        print(f"======{filtter}======")
                                        file.write(f"======{filtter}======\n")
                                        extantions.append(filtter)
                                    print(url) 
                                    file.write(url+"\n") 
                                    detectDuplicate.append(url)
                            elif filtter in url:
                                if url not in detectDuplicate:
                                    if  filtter not in extantions:
                                        print(f"======{filtter}======")
                                        file.write(f"======{filtter}======\n")
                                        extantions.append(filtter)
                                    print(url) 
                                    file.write(url+"\n")  
                                    detectDuplicate.append(url) 
            for url in urls:
                if url not in detectDuplicate:
                    if url not in detectDuplicate:
                        filtter = "others"
                        if  filtter not in extantions:
                            print(f"======{filtter}======")
                            file.write(f"======{filtter}======\n")
                            extantions.append(filtter)
                        print(url) 
                        file.write(url+"\n")  
                        detectDuplicate.append(url)     
                           

def main(url):
    start = urls()
    # start.test(url)
    # start.checkDomain(url,"https://support.chess.com/category/135-membership-and-billing")
    extractUrls = start.extract_urls(url)
    print("deeep ==============================================================================>")
    start.deepSearch(url,extractUrls)
    # print(start.extantions)
    # print(start.detectDuplicate)


if __name__ == "__main__":
    main()        
