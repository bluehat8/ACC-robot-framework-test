import xml.etree.cElementTree as ET
import pandas as pd
import datetime as datetime
import xml.etree.ElementTree as etree
from io import StringIO



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
    with open(xml) as f:
        xml = f.read()
    parser = ET.XMLParser(encoding="utf-8")
    arbol = etree.iterparse(StringIO(xml))
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
            
        #if keyword.get('name') == "Log":
        

        
        # for mensaje_info in test.iter('kw'):
        #     info_mensajes.append(mensaje_info.find('doc').text)

        # for mensaje_info in test.iter('kw'):
        #     if mensaje_info.get('name')=='Log':                  
        #          info_mensajes.append(mensaje_info.find('msg').text)
            
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


def obtener_lst_suites(xml):
    rbol = ET.parse(xml)
    raiz = arbol.getroot()
    test_lista = []


    for test in raiz.findall('suite'):
        suiteName=test.get('name')
        suiteTime=test.find('status').get('endtime')
        testNuevo= raiz.findall('./statistics')
        suitePass=testNuevo[0].find('total/stat').attrib.get('pass')
        suiteFail=testNuevo[0].find('total/stat').attrib.get('fail')
        suiteStatus='FAIL'
        if suiteFail=='0':
            suiteStatus='PASS'
        
        test_dict={
            'Nombre':suiteName,
            'Tiempo':suiteTime,
            'Pass': suitePass,
            'Fail': suiteFail,
            'Status': suiteStatus
        }
        test_lista.append(test_dict)

    
    return test_lista




print(obtener_lst_suites('results/output.xml'))



def extraer_texto_falla(archivo_xml):
    tree = ET.parse(archivo_xml)
    root = tree.getroot()
    for child in root:
        if child.tag == 'suite':
            for subchild in child:
                if subchild.tag == 'test':
                    for subsubchild in subchild:
                        if subsubchild.tag == 'status':
                            if subsubchild.attrib['status'] == 'FAIL':
                                for subsubsubchild in subchild:
                                    if subsubsubchild.tag == 'kw':
                                        for subsubsubsubchild in subsubsubchild:
                                            if subsubsubsubchild.tag == 'kw':
                                                #return subsubsubsubchild.text
                                                
                                                for subsubsubsubchild2 in subsubsubsubchild:
                                                    if subsubsubsubchild2.tag == 'msg':
                                                        subsubsubsubchild2.get('timestamp')

# print(extraer_texto_falla('results/output.xml'))

#imprime()  
print(obtener_xml_robot('results/output.xml'))
# print("Nombre de caso de prueba: ",obtener_xml_robot('results/output.xml')[0]['nombre_test'])
# print("Given: ", obtener_xml_robot('results/output.xml')[0]['keywords'][0])
# print(obtener_xml_robot('results/output.xml')[0]['info_mensajes'])
# print("Then: ",obtener_xml_robot('results/output.xml')[0]['keywords'][1])
# print(obtener_xml_robot('results/output.xml')[0]['info_mensajes'])
# print("Start-time: ",obtener_xml_robot('results/output.xml')[0]['startime'])
# print("End-time: ", obtener_xml_robot('results/output.xml')[0]['endtime'])
# print("Elapsed-time: ",obtener_xml_robot('results/output.xml')[0]['elapsed-time'])


def extraer_xml_datatest(xmla):
    with open(xmla) as f:
        xml = f.read()
    parser = ET.XMLParser(encoding="utf-8")
    context = etree.iterparse(StringIO(xml))
    list=[]
        
    for action, elem in context:
        if elem.tag=='msg':
            
            if elem.attrib['level']=="FAIL":
                #print(elem.text)
                list.append(elem.text)
    return list           
                
print(extraer_xml_datatest('results/output.xml'))
        
