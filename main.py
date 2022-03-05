import funciones as fnc

pathDocs = 'docs/'


def main():
    #Leer docs
    docs_dic = fnc.leerDocs(pathDocs)
    stop_words = fnc.stopWords()
    lemas = fnc.palabras_lematizadas_dic()
    
    #limpieza
    #...

    #creacion del vocabularioList
    #vocabularioList = crearVocabularioList(diccionario)

    #creacion del diccionario
    #crearDiccionario(dic_docs, vocabularioList )

if __name__ == "__main__":
    main()