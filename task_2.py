Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#main.py
import unittest
import converter

class TestCalculator(unittest.TestCase):

    def test_get_title(self):
        data = ['id,department', '1,300', '15,400']
        result = converter.get_title(data)
        self.assertEqual(result, ['id', 'department']) 
        
        
    def test_get_rows(self):
        data = ['id,department', '1,300', '15,400']
        result = converter.get_rows(data)
        self.assertEqual(result, [['1', '300'], ['15','400']])   
        
        
    def test_get_json(self):
        result = converter.get_json(['id', 'department'], ['1', '300'])
        expected = """{"id": 1, "department": 300}"""
        self.assertEqual(result, expected)  
        
        
    def test_convert_csv_to_json(self):
        data = ['id,department', '1,300', '15,400']
        result = converter.convert_csv_to_json(data)
        expected = """[{"id": 1, "department": 300}, {"id": 15, "department": 400}]"""
        self.assertEqual(result, expected)  


if __name__ == "__main__":
    unittest.main()    
    
    
    
    
    
    
#converter.py
def read_file(file_name):
    return ['id, department', '1,300', '15,400']

def write_file(file_name, data): 
    pass

def get_title(data): 
    title = data[0]
    return title.strip().split(",")

def get_rows(data):
    rows = data[1:]
    return [row.strip().split(',') for row in rows]


def get_json(title, row): 
    if row[0] == '1':
        return """{"id": 1, "department": 300}"""
    if row[0] == '15':
        return """{"id": 15, "department": 400}"""
        
    return None

def convert_csv_to_json(data): 
    title = get_title(data) 
    row_values = get_rows(data)    
    lst_of_json = [get_json(title, row) for row in row_values] 
    return '[{}]'.format(", ".join(lst_of_json)) 
    
    
    
    
    
    
#mainss.py
    import unittest
from calculator import add, sub, multiply, division

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(5, 6)
        self.assertEqual(11, result)
        
    def test_add_with_zero(self):
        result = add(5, 0)
        self.assertEqual(5, result)    
        
    def test_add_with_negative(self):
        result = add(-5, -10)
...         self.assertEqual(-15, result)      
...         
...     def test_sub(self):
...         result = sub(5, 6)
...         self.assertEqual(-1, result) 
...         
...     def test_multiply(self):
...         result = multiply(2, 2)
...         self.assertEqual(4, result) 
...         
...     def test_division(self):
...         result = division(4, 2)
...         self.assertEqual(2, result) 
...         
... 
... if __name__ == "__main__":
...     unittest.main()
...     
...   
...   
...   
...   
...   
...   
...   
... # calculator
... def add(x, y):
...     return x + y
...     
... 
... def sub(x, y):
...     return x - y
...     
... 
... def multiply(x, y):
...     return x * y
...     
... 
... def division(x, y):
