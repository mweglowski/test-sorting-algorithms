import importlib
import sys

folder = 'c:\\Learning\\clean\\projects\\python-sorting-app\\algorithms'
sys.path.append(folder)
file = 'bubble_sort'

m = importlib.__import__(file)
print(m.sort_set([2, 1,2, 3]))