def parse(logstring):

    if (logstring.find('-', 10) == -1) or (logstring.find('[') == -1) or (logstring.find(']') == -1):
        return None

    date = logstring[:logstring.find('-', 10) - 1]
    module = logstring[logstring.find('-', 10) + 2: logstring.find('[') - 1]
    type = logstring[logstring.find('[') + 1: logstring.find(']')].strip()
    message = logstring[logstring.find(']') + 1:].strip()

    return date, module, type, message


log = open("log.txt", "r")
output_dict = dict()

for line in log:

    parsing_result = parse(line)
    if parsing_result is None:
        continue

    date = parsing_result[0]
    module = parsing_result[1]
    type = parsing_result[2]
    message = parsing_result[3]

    output_dict[module] = output_dict.get(module, {'DEBUG': 0, 'INFO': 0, 'WARNING': 0, 'ERROR': 0})
    output_dict[module][type] = output_dict[module].get(type, 0) + 1

print(output_dict)
log.close()