import os

def leerTxt(path):
    file = open(path, 'r', encoding="utf-8")
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
        documentos[doc[0:doc.find('.')]] = leerTxt(path + doc).strip()
    return documentos

def stopWords():
    file = open('stop_words.txt','r', encoding="utf-8")
    lineas = file.readlines()
    stop_words = []
    for linea in lineas:
        stop_words.append(linea.strip())
    return stop_words

def palabras_lematizadas_dic():
  lemat_palabras = {'casa': ['refugio','hogar', 'casas'], 'estar':['estamos'], 'vacio':['vacia'], 'grande':['enorme','grandes'],'foraneo':['extranjero', 'foraneos'],
                  'seleccionar':['selecciono'],'directivo':['directivos'],'convertir':['convirtio'],'compañia':['compañias'],'determinar':['determina'],
                  'tener':['tiene', 'tuvo', 'tendra'],'reconocer':['reconoce', 'reconocio'],'juzgar':['juzgada'],'cien':['cientos'],'mil':['miles'],
                  'proceso':['procesos'],'resolver':['resueltos', 'resolucion'],'conjuez':['conjueces'],'temporal':['temporales'],'juez':['jueces'],
                  'nacional':['nacionales'],'designar':['designados', 'designacion'],'reemplazar':['reemplazado','reemplazo'],'algun':['algunos', 'algunas'],
                  'profesional':['profesionales'],'experto':['expertos', 'expertas'],'mineria':['minerias'],'capacitar':['capacitacion','capacitados', 'capacitan'],
                  'miembro':['miembros'],'fuerza':['fuerza'],'armada':['armadas'],'arquitectura':['arquitecturas', 'arquitecto', 'arquitecta'],
                  'bombero':['bomberos', 'bomberas'],'policia':['policias'],'entrenar':['entrenamiento', 'entrenamientos'],
                  'enfocar':['enfoque','enfocan'],'riesgo':['riesgos', 'peligros'],'mina':['minas'],'ilegal':['ilegales'],
                  'tecnica':['tecnicas'],'ascender':['ascenso'],'galeria':['galerias'],'vertical':['verticales'],
                  'literal':['literatura'],'ruido':['ruidoso', 'ruidos'],'habitar':['habitantes', 'habitaban'],
                  'mirar':['mirada'],'quien':['quienes'],'demandar':['demandaban','demandados'],'entretener':['entretenimiento'],
                  'ciudad':['ciudades'],'sobrar':['sobra', 'sobrando'],'construir':['construyo', 'construyendo'],
                  'campo':['campos'],'relacionar':['relacionada'],'alimentar':['alimento', 'alimentacion'],'poder':['poderes'],
                  'adquirir':['adquisitivo'],'disminuir':['disminuido'],'considerar':['considerablemente'],'sistema':['sistemas'],
                  'salud':['saludable'],'brindar':['brindan', 'brindaron'],'servicio':['servicios'],'obra':['obras'],
                  'realizar':['realizadas', 'realizacion'],'necesidad':['necesidades'],'ciudadano':['ciudadania', 'ciudadanos'],
                  'calle':['calles', 'avenida'],'luz':['luces','focos'],'blanca':['blancas'],'color':['colores'],'tienda':['tiendas'],
                  'decorar':['decoracion', 'decoradas'],'figura':['figuras'],'roja':['rojas'],'verde':['verdes'],'persona':['personas'],
                  'ir':['van', 'vienen'],'salir':['salen', 'saliendo'],'arbol':['arboles', 'arbolitos'],'bola':['bolas'],
                  'brillar':['brillantes', 'brilos'],'guirnalda':['guirnaldas'],'estrella':['estrellas'],
                  'restaurante':['restaurantes'],'parque':['parques'],'mito':['mitos'],
                  'narrar':['narraciones', 'narracion'],'transmitir':['transmision', 'transmitio'],'aparecer':['aparecen','aparecio'],
                  'suceso':['sucesos'],'personaje':['personajes'],'surgir':['surgieron'],
                  'explicar':['explicacion', 'explico'],'existir':['existencia', 'existo'],'relatar':['relatos', 'relata'],
                  'crear':['creacion', 'creados'],'comprender':['comprension'],'coleccionar':['coleccion','coleccionamos', 'coleccionismo', 'coleccionistas'],
                  'objeto':['objetos'],'estudiar':['estudian', 'estudiaron', 'estudiante'],'conservar':['conservacion','conservar'],
                  'invertir':['invierten', 'inversion'],'aquel':['aquellos','aquellas']}
  return lemat_palabras

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


