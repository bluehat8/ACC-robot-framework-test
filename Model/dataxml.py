import xml.etree.cElementTree as ET
import pandas as pd
import datetime as datetime


arbol = ET.parse('results/output.xml')
raiz = arbol.getroot()
    
# Una vez hecho esto, puedes empezar a iterar mediante raiz.iter() o raiz.findall(). Ej.
def imprime():
    escenario=[]
    
    for hijo in raiz.iter('test'):
        
        start_time = datetime.datetime.strptime(hijo.find('status').attrib.get('starttime'), "%Y%m%d %H:%M:%S.%f")
        end_time = datetime.datetime.strptime(hijo.find('status').attrib.get('endtime'), "%Y%m%d %H:%M:%S.%f")
        
        escenario.append([hijo.attrib.get('name'),
                         
                          hijo.find('status').text   
            ,hijo.find('status').attrib.get('status'), hijo.find('status').attrib.get('starttime'), 
            hijo.find('status').attrib.get('endtime'),end_time-start_time])
        
        
    df = pd.DataFrame(escenario,
                  columns=['Caso','then','Estado','Starttime', 'Endtime', 'Elapsed time'],
                  )

    print(df)
    print("\nSteps de casos de prueba: ", len(escenario))
    
   # print(df.iloc[1]['Output'])
    # nombres=[]
    # for hijo in raiz.findall('./suite/test'):
    #     nombres.append(hijo.find('kw/doc').text)
    #     print('Texto de salida: ',nombres)

    # print(nombres)
    
    
    # for nodo in raiz.iter('doc'):
    #     for elemento in nodo.iter():
    #         print("Notas: ", elemento.text)
            
    for test in raiz.iter('test'):
        doc= test.find('status').text
        print("Documentos: ",doc)
        
def obtener_xml_robot(xml):
    arbol = ET.parse(xml)
    raiz = arbol.getroot()
    test_lista = []

    for test in raiz.findall('./suite/test'):
        nombre_test = test.get('name')
        keywords = []
        info_mensajes = []
        start_time = datetime.datetime.strptime(test.find('status').attrib.get('starttime'), "%Y%m%d %H:%M:%S.%f")
        end_time = datetime.datetime.strptime(test.find('status').attrib.get('endtime'), "%Y%m%d %H:%M:%S.%f")
        elapsedtime=end_time-start_time

        for keyword in test.findall('kw'):
            if keyword.get('name').startswith('Given') or keyword.get('name').startswith('Then') or keyword.get('name').startswith('And'):
                keywords.append(keyword.get('name'))

        for mensaje_info in test.findall('kw/msg'):
            info_mensajes.append(mensaje_info.text)
            
        test_dict = {
            'nombre_test': nombre_test,
            'keywords': keywords,
            'info_mensajes': info_mensajes,
            'startime': start_time,
            'endtime': end_time,
            'elapsed-time': elapsedtime
        }
        test_lista.append(test_dict)
    
        
    # df = pd.DataFrame(test_lista)
   # df = pd.DataFrame(df, index=[0], columns=['nombre_test', 'keywords', 'info_mensajes'])
   # print(df)
   # print(df_new)
    

    return test_lista


#imprime()  
#print(obtener_xml_robot('results/output.xml'))
print("Nombre de caso de prueba: ",obtener_xml_robot('results/output.xml')[0]['nombre_test'])
print("Given: ", obtener_xml_robot('results/output.xml')[0]['keywords'][0])
print(obtener_xml_robot('results/output.xml')[0]['info_mensajes'][0])
print("Then: ",obtener_xml_robot('results/output.xml')[0]['keywords'][1])
print(obtener_xml_robot('results/output.xml')[0]['info_mensajes'][1])
print("Start-time: ",obtener_xml_robot('results/output.xml')[0]['startime'])
print("End-time: ", obtener_xml_robot('results/output.xml')[0]['endtime'])
print("Elapsed-time: ",obtener_xml_robot('results/output.xml')[0]['elapsed-time'])
