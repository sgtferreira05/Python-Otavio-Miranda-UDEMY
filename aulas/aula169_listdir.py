# os.listdir to navigate through paths

import os

# "D:\\CURSOS\\python_udemy\\EXEMPLO"
path = os.path.join("\\CURSOS", "python_udemy", "EXEMPLO")
for pasta in os.listdir(path):
    complete_pasta_way = os.path.join(path, pasta)
    print(complete_pasta_way)
    if not os.path.isdir(complete_pasta_way):
        continue
    for image in os.listdir(complete_pasta_way):
        print(image)