def get_length(file_info):
    return file_info.get('length')

def get_data(files_list):
    files_info = []
    for file_current in files_list:
        #print(file_current)
        with open(file_current, encoding='utf-8') as file:
            files_dict = {}
            text = file.readlines()
            files_dict['name'] = file_current
            files_dict['length'] = len(text)
            files_dict['content'] = text
            files_info.append(files_dict)
    files_info.sort(key=get_length)
    return files_info

def write_data(files_info, new_file='result.txt'):
    with open(new_file, 'w', encoding='utf-8') as file:
        for line in files_info:
            file.write(line['name'] + '\n')
            file.write(str(line['length']) + '\n')
            for string in line['content']:
                file.write(string)
            file.write('\n')


files_list = ['1.txt', '2.txt', '3.txt']
result = get_data(files_list)
write_data(result)