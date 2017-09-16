# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:52:08 2016

@author: Josue
"""

class primo():
    def __init__(self,num):
        self.num=num
    
    def primo1(self):
        for i  in range(2,self.num):
             
            if self.num%i==0:
                print "El numero no es primo"
                break
                 
        if(self.num==i+1):
            print "el numero es primo"
          
            
            
a=primo(11)           
a.primo1()                
           
            
            
                
            