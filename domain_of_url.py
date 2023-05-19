def domain_name(url):
    lst=[]
    lst=url.split("/")[2]                      #remove http// or ftb//
                                                         #it will first remove every / and put the between in a list so http://www.youtube.com will become: ['http:', ' ', 'www.youtube.com'] 
                                                         #after that take the second elemnt of this list so ['www.youtube.com']
    anotherlst=[]
    anotherlst=lst.split(".")[-2]           #remove the www. if existed    
                                                           #the lst.split result will be ['www' 'youtube' 'com'] so take not the last element (which is com) but the youtube only
                                            
    return anotherlst

#sadly it wont work with 'http://google.co.jb'



url=str(input("Enter here: "))
print(domain_name(url))
