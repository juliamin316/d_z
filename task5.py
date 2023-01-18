Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_result(strs_list):
...     result = {}
...     for strs in strs_list:
...         sorted_strs = ''.join(sorted(strs))
...         if sorted_strs in result:
...             result[sorted_strs].append(strs)
...         else:
...             result[sorted_strs] = [strs]
... 
...     result_list = list(map(lambda x: sorted(x), list(result.values())))
...     result_list = sorted(result_list)
...     return result_list
