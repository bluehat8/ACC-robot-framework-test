import xml.etree.ElementTree as etree
from io import StringIO
import dataxml as dataxml


from charts import create_chart


def data_calculator(file_name):

    """
    :param file_name: Output.xml
    :return:
    """
    with open(file_name) as f:
        xml = f.read()
    context = etree.iterparse(StringIO(xml))
    overall_result = dict()
    list_of_tags = []
    tag_results = {}
    execution_time = ''

    for action, elem in context:
        if elem.tag == 'tag':
            list_of_tags.append(elem.text)
        if elem.tag == 'stat':
        
            try:
                if elem.text == 'All Tests':
                    if elem.attrib.items()[0][0] == "fail":
                        overall_result['fail'] = elem.attrib.items()[0][1]
                    if elem.attrib.items()[1][0] == "pass":
                        overall_result['pass'] = elem.attrib.items()[1][1]
                if elem.text in list_of_tags:
                    tag_results[elem.text] = {}
                    if elem.attrib.items()[0][0] == "fail":
                        tag_results[elem.text]["fail"] = int(elem.attrib.items()[0][1])
                    if elem.attrib.items()[1][0] == "pass":
                        tag_results[elem.text]["pass"] = int(elem.attrib.items()[1][1])
            except:
                continue

    return overall_result,tag_results







def data_extractor(file_name):
    arbol = etree.parse('Model/output.xml')
    raiz = arbol.getroot()
    with open(file_name) as f:
        xml = f.read()
    context = etree.iterparse(StringIO(xml))
    overall_result = dict()
    list_of_tags = []
    tag_results = {}
    execution_time = ''
    escenario=[]
    
    
    for hijo in raiz.findall('./statistics'):
        testAprobados=hijo.find('total/stat').attrib.get('pass')
        testFallidos=hijo.find('total/stat').attrib.get('fail')
       
        print('Steps aprobados: ', testAprobados)
        print('Steps fallidos: ', testFallidos)
    escenario.append(testAprobados)
    escenario.append(testFallidos)
    return escenario
           
    


def robo_graph_generator():



    overall_result,tag_results = data_calculator(r"C:\Users\Usuario\Documents\python testing\ACC-Robot-Framework-Testing\Model\output.xml")
    overall_result=data_extractor(r"C:\Users\Usuario\Documents\python testing\ACC-Robot-Framework-Testing\Model\output.xml")
    total_pass = int(overall_result[0])
    total_fail = int(overall_result[1])
    total_result = total_pass + total_fail
    datosXml=dataxml.obtener_xml_robot('results/output.xml')
    suitesXml=dataxml.obtener_lst_suites('results/output.xml')


    all_test_case_data ="""<body class='extent standard default hide-overflow bdd'>
		<div id='theme-selector' alt='Click to toggle theme. To enable by default, use theme configuration.' title='Click to toggle theme. To enable by default, use theme configuration.'>
			<span><i class='material-icons'>desktop_windows</i></span>
		</div>

		<nav>
    <div class="nav-wrapper">
        <a href="http://extentreports.relevantcodes.com" class="brand-logo blue darken-3">Extent</a>

        <!-- slideout menu (para barra lateral izquierda)-->
        <ul id='slide-out' class='side-nav fixed hide-on-med-and-down'>
            <li class='waves-effect active'><a href='#!' view='test-view' onclick="configureView(0);chartsView('test');"><i class='material-icons'>dashboard</i></a></li>
                        <li class='waves-effect'><a href='#!' onclick="configureView(-1);chartsView('dashboard');" view='dashboard-view'><i class='material-icons'>track_changes</i></i></a></li>
        </ul>

        <!-- report name -->
        <span class='report-name'>Casos de pruebas automatizados</span>

        <!-- report headline -->
        <span class='report-headline'></span>

        <!-- nav-right -->
        <!-- <ul id='nav-mobile' class='right hide-on-med-and-down nav-right'>

            <a>
                <span class='suite-start-time label blue darken-3'>1/30/2023 2:39:08 PM Coordinated Universal Time</span>
            </a>
            <a>
                <span class="label blue darken-3">3.1.0</span>
            </a>
        </ul> -->
    </div>
</nav> 

<div class='container'>

            
<div id='test-view' class='view'>

    <div align="center" style="vertical-align:bottom">
<div align="center" style="vertical-align:bottom">
<table border="1" align="center">
<tr bgcolor = 0CE36B align="center"><th>Total Test Cases</th><th>Passed</th><th>Failed</th></tr>
<tr><th>"""+str(total_result)+"""</th><th>"""+ str(total_pass) +"""</th><th>"""+ str(total_fail) +"""</th></tr>
</table></div></div>
"""

    for i in range(len(suitesXml)):
        all_test_case_data=all_test_case_data+"""<div class='subview-left left'>
        <div class='view-summary'>
            <h5>Tests</h5>
            <ul id='test-collection' class='test-collection'>  
    <li class='test displayed active has-leaf pass' status='pass' bdd='bdd' test-id='1'>
                        <div class='test-heading'>
                            <span class='test-name'>"""+str(i)+"."+suitesXml[i]['Nombre']+"""</span>
                            <span class='test-time'>"""+str(suitesXml[i]['Tiempo'])+"""</span>
                            <span class='test-status right pass'>"""+suitesXml[i]['Status']+"""</span>
                        </div>
        <div class='test-content'>
"""
                        
        for i in range(len(datosXml)):
            all_test_case_data=all_test_case_data+"""<div class='scenario node' test-id='2' status='pass'>
                                        <span class='scenario-duration right label'>"""+str(datosXml[i]['elapsed-time'])+"""</span>
                                        <div class='scenario-desc'>
                                            <b>Scenario</b>
                                            1.01. """+datosXml[i]['nombre_test']+"""

                                            
                                        </div>
                                            <ul class='steps'>
                                                    <li test-id='3' class='node given pass' status='given pass'>
                                                        <b>Given</b>
                                                        """+datosXml[i]['keywords'][0]+""""
                                                        <div class='pre'><pre><b>Text Output</b><hr>"""+datosXml[i]['info_mensajes'][0]+""""</pre></div>
                                                    </li>
                                                    <li test-id='4' class='node then pass' status='then pass'>
                                                        <b>Then</b>
                                                         """+datosXml[i]['keywords'][1]+"""
                                                        <div class='pre'><pre><b>Text Output</b><hr>"""+datosXml[i]['info_mensajes'][1]+"""</pre></div>
                                                    </li>
                                            </ul>
                                    </div>"""
        all_test_case_data=all_test_case_data+"</div> </li>"                            

    all_test_case_data=all_test_case_data+"""</ul>
        </div>
    </div>
    
    <div class='subview-right left'>
        <div class='view-summary'>
            <h5 class='test-name'></h5>

        </div>
    </div>
    
     </div>
    </div>
    """
    
    #html_data = create_chart(overall_result,tag_results)
    html= "<html><head><meta charset=\"utf-8\" /> <link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600' rel='stylesheet' type='text/css'><link href='https://fonts.googleapis.com/icon?family=Material+Icons' rel='stylesheet'> <link href='https://cdn.rawgit.com/anshooarora/extentreports-csharp/3b6cc04fd241b9782606e57fc5e84f0e42172c08/dist/css/extent.css' type='text/css' rel='stylesheet' /></head><body>"+all_test_case_data+"<script type=\"text/javascript\">/**" + "<h1>naruto</h1>*/" + "</script></body></html>"
    f = open("graph.html",'w+', encoding="utf-8")
    f.write(html)
    f.close()
    print('HTML CREADO')
    print(tag_results)


#if __name__ == "__main__":
robo_graph_generator()


           
data_extractor(r"C:\Users\Usuario\Documents\python testing\ACC-Robot-Framework-Testing\Model\output.xml")