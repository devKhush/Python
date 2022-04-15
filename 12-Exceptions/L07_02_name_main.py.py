# Ways to import a file
import L07_01_name_main
import L07_01_name_main as file

# Ways to import function and varaible from file
from L07_01_name_main import greet as g
from L07_01_name_main import greet

str = 'Khush Dev'
L07_01_name_main.greet(str)
file.greet(str)
greet(str)
g(str)
