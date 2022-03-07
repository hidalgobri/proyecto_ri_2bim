import funciones as fnc

pathDocs = 'docs/'


def main():
    #Leer docs
    docs_dic = fnc.leerDocs(pathDocs)
    stop_words = fnc.stopWords()
    lemas = fnc.palabras_lematizadas_dic()
    
    #limpieza
    clean_docs_dic = fnc.limpia_string(docs_dic, stop_words, lemas)
    
    #creacion del vocabularioList
    vocabularioList = fnc.crearVocabularioList(clean_docs_dic)
    print(vocabularioList)
    #creacion del diccionario
    #crearDiccionario(dic_docs, vocabularioList )

if __name__ == "__main__":
    main()