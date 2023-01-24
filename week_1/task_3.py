def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content 
    
def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()
    
def format_t(text, symbols_q):    #symbols_q количество символов в строке 
    lines = []
    line = ""
    words = text.split()
    for word in words:
        if len(line + " " + word) <= symbols_q:
            line += " " + word
        else:
            lines.append(line.strip())
            line = word
    lines.append(line.strip())
    finished_t  = "\n".join(lines)   #finished_t обработанный текст
    return finished_t 
  

write_data('output.txt', format_t(read_data('input.txt'), 21))
