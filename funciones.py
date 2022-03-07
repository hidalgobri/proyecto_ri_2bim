import os
import unidecode


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
  lemat_palabras = {'casa': ['refugio','hogar', 'casas'], 'estar':['estamos','están','estan','estaremos'], 'vacio':['vacia'], 'grande':['enorme','grandes'],'foraneo':['extranjero', 'foraneos'],
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
                  'campo':['campos'],'relacionar':['relacionada','relacionan'],'alimentar':['alimento', 'alimentacion'],'poder':['poderes'],
                  'adquirir':['adquisitivo'],'disminuir':['disminuido'],'considerar':['consideremos','considera'],'sistema':['sistemas'],
                  'salud':['saludable'],'brindar':['brindan', 'brindaron'],'servicio':['servicios'],'obra':['obras'],
                  'realizar':['realizadas', 'realizacion'],'necesidad':['necesidades'],'ciudadano':['ciudadania', 'ciudadanos','ciudadana'],
                  'calle':['calles', 'avenida'],'luz':['luces','focos'],'blanco':['blancas','blanca'],'color':['colores'],'tienda':['tiendas'],
                  'decorar':['decoracion', 'decoradas'],'figura':['figuras'],'rojo':['rojas','rojos','roja'],'verde':['verdes'],'persona':['personas'],
                  'ir':['van', 'vienen','va'],'salir':['salen', 'saliendo'],'arbol':['arboles', 'arbolitos','árboles','arboleda'],'bola':['bolas'],
                  'brillar':['brillantes', 'brillos'],'guirnalda':['guirnaldas'],'estrella':['estrellas'],
                  'restaurante':['restaurantes'],'parque':['parques'],'mito':['mitos'],
                  'narrar':['narraciones', 'narracion'],'transmitir':['transmision', 'transmitio','transmisión'],'aparecer':['aparecen','aparecio'],
                  'suceso':['sucesos'],'personaje':['personajes'],'surgir':['surgieron'],
                  'explicar':['explicacion', 'explico'],'existir':['existencia', 'existo'],'relatar':['relatos', 'relata'],
                  'crear':['creacion', 'creados'],'comprender':['comprension'],'coleccionar':['coleccion','coleccionamos', 'coleccionismo', 'coleccionistas'],
                  'objeto':['objetos'],'estudiar':['estudian', 'estudiaron', 'estudiante'],'conservar':['conservacion','conservan'],
                  'invertir':['invierten', 'inversion'],'aquel':['aquellos','aquellas'],'poblacion':['poblaciones','población'],
                  'publico':['publicas','públicas','pública','publica','publicos','público'],'adornado':['adornados','adornada','adornadas'],
                  'distinto':['distinta','distintos','distintas'],'entrar':['entran','entramos','entra'],'caer':['caen','caemos'],'fantastico':['fantásticos','fantástico'],
                  'cosa':['cosas'],'servir':['sirven','servimos','serviremos'],'consistir':['consisten','consistencia'],'reunir':['reunen','reúnen','reuniendo'],
                  'restaurar':['restauran','restauracion'],'exponer':['exponen','exposicion']
                  }
  return lemat_palabras


#si existe, reemplaza la palabra por otra conjugada en presente y singular
def lematizacion ( palabra, dicc_lemat):
  for key, value in dicc_lemat.items():
    if palabra in value:
      return key
  return palabra

#1. V= [todos los términos que haya en el doc]
def crear_v(lista_docs, stop_words, lemat_palabras):
  v_list = []
  for doc in lista_docs:
    doc_limp = limpia_string(doc,stop_words, lemat_palabras)

    v_list_aux = [ palabra for palabra in doc_limp if palabra not in v_list]
    v_list = v_list + v_list_aux
  return v_list

def limpia_string(docs_dic, stop_words, lemat_palabras):
#recibe un string, lo parte, limpia cada palabra y devuelve una lista

  clean_docs_dic = {}
  for indx, value in docs_dic.items():
    
    palabras = value.split()
    lista_palabras = []

    for palabra in palabras:
      palabra_limpia = unidecode.unidecode(palabra.lower().replace(',','').replace('.','').replace("'","")) #quita la tilde, y pone en minúscula
      
      if palabra_limpia not in stop_words and palabra_limpia.isnumeric() == False :
        palabra_lemat = lematizacion(palabra_limpia, lemat_palabras)
        if palabra_lemat not in lista_palabras:
          lista_palabras.append(palabra_lemat)
    lista_palabras.sort()
    clean_docs_dic[indx] = lista_palabras
  return clean_docs_dic



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
  listAux = list(set(listUnidimensional)) #para borrar los repetidos
  listAux.sort()
  return listAux


def docs_term_limpios (docs_list, stop_words, lemat_palabras):
  dic_docs = {}
  nombre_clave = 'doc_'
  for indx,doc in enumerate(docs_list):
    dic_docs[nombre_clave+str(indx)] = limpia_string(doc, stop_words, lemat_palabras)
  return dic_docs

