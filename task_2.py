def read_data(file_name): 
    file = open(file_name) 
    content = file.read() 
    return content


def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data) 
    f.close() 


def prepare_lines(data):
    splitted = data.split('\n') 
    titles, line_1, line_2, line_3 = splitted[0], splitted[1], splitted[2], splitted[3]
    labels = titles.split(',') 
    line_1_formatted = line_1.split(',')
    line_2_formatted = line_2.split(',')
    line_3_formatted = line_3.split(',')
    # print(line_1_formatted)
    one = dict(zip(labels, line_1_formatted)) 
    two = dict(zip(labels, line_2_formatted)) 
    three = dict(zip(labels, line_3_formatted))
    # l = [one, two, three]
    print(one, two, three, sep="\n")
    # print(l)

    return labels, line_1_formatted, line_2_formatted, line_3_formatted, 
def format_text(labels, line_1_formatted, line_2_formatted, line_3_formatted):
    d = dict(zip(labels, line_1_formatted))
    print(d)


content = read_data("input.py")
prepare_lines(content) 

