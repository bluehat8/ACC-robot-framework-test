import xml.etree.cElementTree as ET
import pandas as pd


arbol = ET.parse('Model/output.xml')
raiz = arbol.getroot()
    
# Una vez hecho esto, puedes empezar a iterar mediante raiz.iter() o raiz.findall(). Ej.
def imprime():
    escenario=[]
    
    for hijo in raiz.findall('./suite/test/kw'):
        escenario.append([hijo.attrib.get('name'),
                          hijo.text   
            ,hijo.find('status').attrib.get('status'), hijo.find('status').attrib.get('starttime'), 
            hijo.find('status').attrib.get('endtime')])
        
        
    df = pd.DataFrame(escenario,
                  columns=['Caso','Output','Estado','Starttime', 'Endtime'],
                  )

    print(df)
    print("\nSteps de casos de prueba: ", len(escenario))
    
    nombres=[]
    for hijo in raiz.findall('./suite/test'):
        nombres.append(hijo.find('kw/doc').text)
        print('Texto de salida: ',nombres)

    print(nombres)
    
    
    for nodo in raiz.iter('doc'):
        for elemento in nodo.iter():
            print("Notas: ", elemento.text)


imprime()  