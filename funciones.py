import os

def leerTxt(path):
    file = open(path, 'r')
    lineas = file.readlines()
    texto = ''
    for linea in lineas:
        if linea.strip() != '':
            texto = texto + linea.strip() + ' '
    return texto

def leerDocs(path):
    docs = os.listdir(path)
    documentos = {}
    for doc in docs:
        documentos[doc[0:doc.find('.')]] = leerTxt(path + doc)
    return documentos

