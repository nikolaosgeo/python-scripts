import re
input_file = 'system_logs.txt'
output_file = 'cell_phones.txt'

# First read the raw input content.
print('\nReading input data from file \'' +  input_file + '\'...')
input_file_stream = open(input_file, 'r')
input_file_content = input_file_stream.read()

# Extract all the phone regex matches from the lines.
phone_regex = re.compile(r'\d{3}[-\.\s]\d{3}[-\.\s]\d{4}\b|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}\b')
cell_phones = phone_regex.findall(input_file_content)

# Combine all occurences into one string.
numbers = ""
for cell_phone in cell_phones:
    numbers += str(cell_phone)+"\n"

# Export all found phones in a target file.
print('Writing output data to file \'' +  output_file + '\'...\n')
with open(output_file, 'w') as output_file_stream:
    output_file_stream.write(numbers)
