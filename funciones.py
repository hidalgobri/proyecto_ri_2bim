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

def crearDiccionario(dic_docs, v_list ):
  #recibe una lista del contenido de los docs en string
  #devuelve {bicicleta': {'doc_3': 1, 'doc_4': 1, 'n': 2}}
  diccionario = dict()
  contador = 0

  for idx,term in enumerate(v_list):#recorro terminos totales

    for clave, valor in dic_docs.items():#recorro term por doc
  
      if term in valor:

        frec_term_doc = valor.count(term)
          
        if diccionario.get(term,-1) == -1: #si no hay una clave con term, return -1
          dic = {}
          dic[clave] = frec_term_doc
          diccionario[term] = dic

        else:  #si hay una clave con term
          
          diccionario[term][clave] = frec_term_doc
        contador = contador +1 
      
    diccionario[term]['n'] = contador      
    contador = 0
  return diccionario

#vocabularioList = lista con todos los terminos de todos los documentos
  def crearVocabularioList(diccionario):
    listDesordenada = list(diccionario.values())
    listUnidimensional =[item for sublist in listDesordenada for item in sublist ]
    listAux = list(set(listUnidimensional))
    return listaAux.sort()


