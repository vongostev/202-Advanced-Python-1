import re

dictionary = {}
fun_counter = 0
list_of_found_modes = []
string_format_for_dict = r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\s-\s(\w*\.\w*)\s\[(\w*)\s*\]'
string_format_for_fun = r'.*fun:.*'
string_format_for_modes = r'.*Found (\d+) modes.*'

if __name__ == "__main__":
    with open('log.txt', 'r') as parsed_file:
        for string in parsed_file:

            module_and_type_list = re.findall(string_format_for_dict, string) #task №1
            if (module_and_type_list != []):
                module, type_ = module_and_type_list[0][0], module_and_type_list[0][1]
                try: 
                    dictionary[module][type_] += 1
                except KeyError:
                    dictionary[module] = {'DEBUG': 0, 'INFO': 0, 'WARNING': 0, 'ERROR': 0}
                    dictionary[module][type_] += 1
                    
            fun = re.match(string_format_for_fun, string) #task №2
            if fun:
                fun_counter += 1

            found_mode = re.match(string_format_for_modes, string)
            if found_mode:
                print(found_mode.group(1))
                list_of_found_modes.append(int(found_mode.group(1)))

    print('Составлен словарь: ', dictionary)
    print('fun is found ', fun_counter, ' times')
    print('list of found modes: ', list_of_found_modes)             

