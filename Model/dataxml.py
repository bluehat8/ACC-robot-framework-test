import xml.etree.cElementTree as ET
import pandas as pd


arbol = ET.parse('Model/output.xml')
raiz = arbol.getroot()
    
# Una vez hecho esto, puedes empezar a iterar mediante raiz.iter() o raiz.findall(). Ej.
def imprime():
    escenario=[]
    
    for hijo in raiz.findall('./suite/test/kw/status'):
        escenario.append([hijo.attrib.get('status'), hijo.attrib.get('starttime'), hijo.attrib.get('endtime')])
        
    
   # df = pd.DataFrame(escenario)
    
    df = pd.DataFrame(escenario,
                  columns=['Estado','Starttime', 'Endtime'],
                  )

    print(df)
    print("\nTotal de casos de prueba: ", len(escenario))
    
    dpass=df.value_counts(df['Estado']=='PASS')
    dfail=df.value_counts(df['Estado']=='FAIL')
    
    print("\nTotal de casos de prueba aprobados: ", dpass)
    
    print("\nTotal de casos de prueba fallidos: ", dfail)


imprime()  