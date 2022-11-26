log = open("log.txt", "r")

substring_counter = 0
substring = 'fun:'

for line in log:
    if substring in line:
        substring_counter += 1

print(substring_counter)
log.close()