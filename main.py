import funciones as fnc

pathDocs = 'docs/'


def main():
    #Leer docs
    docsDic = fnc.leerDocs(pathDocs)
    stopWords = fnc.stopWords()
    lemas = fnc.palabras_lematizadas_dic()
    
    #limpieza
    cleanDocsDic = fnc.limpia_string(docsDic, stopWords, lemas)

    #creacion del vocabularioList
    vocabularioList = fnc.crearVocabularioList(cleanDocsDic)

    #creacion del diccionario
    dicc = fnc.crearDiccionario(cleanDocsDic, vocabularioList )
    

if __name__ == "__main__":
    main()