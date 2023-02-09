 
for mensaje_info in test.iter('test'):
            if  mensaje_info.find('status').attrib('status')=='FAIL':
                info_mensajes.append(mensaje_info.find('status').text)
            
            if  mensaje_info.find('status').attrib('status')=='PASS':
     
                if mensaje_info.get('name')=='Log':            
                    info_mensajes.append(mensaje_info.find('kw/msg').text)