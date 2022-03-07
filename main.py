import funciones as fnc

pathDocs = 'docs/'


def main():
    #Leer docs
    docsDic = fnc.leerDocs(pathDocs)
    docsDic.pop("doc9")
    docsDic.pop("doc8")
    docsDic.pop("doc7")


   
    #crear stop words
    stopWords = fnc.stopWords()
    lemas = fnc.palabras_lematizadas_dic()
    
    #limpieza
    cleanDocsDic = fnc.limpia_string(docsDic, stopWords, lemas)
    
    #creacion del vocabularioList
    vocabularioList = fnc.crearVocabularioList(cleanDocsDic)

    #creacion del diccionario
    dicc = fnc.crearDiccionario(cleanDocsDic, vocabularioList )


    #pedir R al usuario
    R = fnc.pedirR()

    if R is not None:
        
        #creo una lista de los r primeros docs relevantes
        docsConRList = fnc.listaDocsConR( R, cleanDocsDic )

        #calculo de ci
        ciDic = fnc.ci_dicc(vocabularioList, docsConRList, len(cleanDocsDic),dicc )

        print(ciDic)

    else:
        print("El valor solicitado no es el correcto")
    
    

if __name__ == "__main__":
    main()