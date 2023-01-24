def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content

def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()
    
def format_data(text):
    students_d = {} 
    list_f = []  
    lines = text.split('\n')
    for line in lines:
        line_l = line.split()  
        name_f = line_l[1] + " " + line_l[2].strip(":") 
        mark = line_l[3]
        students_d.update({name_f : mark})
        list_f.append(name_f )
    sorted_list_f = sorted(list_f)  
    final_output = "name,grade\n"
    for name in sorted_list_f:
        pattern = '{},{}\n'  
        final_output += pattern.format(name, students_d.get(name))
    return str(final_output)
write_data('output.csv', format_text(read_data('data.txt')))
