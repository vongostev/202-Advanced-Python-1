def parse(logstring):

    if (logstring.find('-', 10) == -1) or (logstring.find('[') == -1) or (logstring.find(']') == -1):
        return None

    date = logstring[:logstring.find('-', 10) - 1]
    module = logstring[logstring.find('-', 10) + 2: logstring.find('[') - 1]
    type = logstring[logstring.find('[') + 1: logstring.find(']')].strip()
    message = logstring[logstring.find(']') + 1:].strip()

    return date, module, type, message


log = open("log.txt", "r")
modes_number_list = []
format_string = '{}Found {} modes {}'

for line in log:
    parsing_result = parse(line)
    if parsing_result is None:
        continue
    message = parsing_result[3]

    if ('Found' in message) and ('modes' in message):
        modes_number_list.append(int(message[message.find('Found') + 6:message.find('modes') - 1]))

print(modes_number_list)
log.close()