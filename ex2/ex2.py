# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:48:14 2021

@author: Егор
"""


class LOG_READER:

    def open(self, file_name):
        self.is_open = False
        if file_name[len(file_name) - 4:len(file_name):1] != ".txt":
            file_name += ".txt"
        try:
            self.file = open(file_name, 'r')
            self.is_open = True
            print("Sucessfully opened! -", file_name)
        except FileNotFoundError:
            print("No such File! -", file_name)
        except Exception as e:
            print(e)

    def __init__(self, file_name):
        self.open(file_name)

    def __del__(self):
        if self.is_open == True:
            self.file.close()
    
    def get_dict(self):
        if self.dict_created == True:
            return self.dict
        else:
            self.create_dict()
        
        if self.dict_created == True:
            return self.dict
        else:
            return {}
            
    def print_dict(self):
        keys = self.dict.keys()
        for key in keys:
            print(key, ": (", end='')
            types = self.dict[key].keys()
            i = 0
            for type_ in types:
                if(i == len(types) - 1):
                    print(type_, ":", self.dict[key][type_], end='')
                else:
                    print(type_, ":", self.dict[key][type_], ", ", end='')
                i += 1
            print(")")
    
    def create_dict(self):

        self.dict = {}
        self.dict_created = False

        if self.is_open != True:
            print("File was not opened!")
            return

        for line in self.file:
            #print("\nLINE:", line)

            temp_split = line.split(' - ')
            #print("   SPLIT: ", temp_split);

            date_str = temp_split[0].strip()
            #print("   Date:\t [", date_str, "]")
            
            try:
                temp_split = temp_split[1].split(' [')
            except:
                continue
            #print("   SPLIT: ", temp_split);

            module_str = temp_split[0].strip()
            #print("   Module:\t [", module_str, "]")
            
            try:
                temp_split = temp_split[1].split('] ')
            except:
                continue
            #print("   SPLIT: ", temp_split);

            type_str = temp_split[0].strip()
            #print("   Type:\t [", type_str, "]")
            
            try:
                message_str = temp_split[1].strip()
            except:
                continue
            #print("   Message:\t [", message_str, "]")
            
            try:
                self.dict[module_str]
            except Exception as e:
                #print("Adding key world to dict :\t\t\t", e)
                self.dict.update({module_str: {}})
                
            try:
                self.dict[module_str][type_str]
            except Exception as e:
                #print("Adding key world to", module_str, ":\t\t\t", e)
                self.dict[module_str].update({type_str : 0})
                
            self.dict[module_str][type_str] += 1

        self.dict_created = True

if __name__ == "__main__":
    logs = LOG_READER("logs")
    logs.create_dict()
    logs.print_dict()
    
