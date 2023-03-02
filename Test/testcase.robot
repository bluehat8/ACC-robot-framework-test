*** Settings ***
Library    Selenium2Library
Library    ScreenCapLibrary
#Library    JIRALibrary
Library    ../xmlReader.py
Library    ../Controller/UserController.py
Library    ../Controller/ComentController.py
Library    ../Controller/ApplicantsController.py
Library    ../Controller/TaxpayerController.py
Library    ../Controller/DirController.py
Library    ../Controller/GeneralitiesController.py
Library    ../Controller/MailController.py

*** Keywords ***

Abrir Navegador
    Open Browser    https://almacc.tustributos.com    chrome
    ${browser_info}=    Execute Javascript    return navigator.userAgent;
   # Log        Navegador: ${browser_info.split('/')[2]}       Versión: ${browser_info.split('/')[2]}   
    Maximize Browser Window


Iniciar Grabacion
    [Arguments]    ${testname}
    Start Video Recording    alias=None    name=${testname}   fps=none    size_percentage=1    embed=True    embed_width=100px    monitor=1   


Detener Grabacion
    Stop Video Recording    alias=none

# Pasos inciales para login

Leer username
    ${position}=    Convert To Integer    0
    ${txtUser}=    Get User Attribute    username       ${position}
    [return]    ${txtUser}

Leer password
    ${position}=    Convert To Integer    0
    ${txtPass}=    Get User Attribute    password    ${position}
    [return]    ${txtPass}

Log my username
    ${txtUser}=    Leer username 
    Input Text    name=txtUserName    ${txtUser}    
    Sleep    1s

Log my password    
    ${txtPass}=    Leer password
    Input Text    name=txtUserPassword    ${txtPass}
    Sleep    1s

Login              Click Button    name=linLogin
    Sleep    1s

Login Succesful      Page Should Contain    Identificador:   
    Sleep    1s


Iniciar sesion
    Log my username  
    Log my password
    Login
    Login Succesful

# Accerder al tramite sujeto pasivo

Ir a trámites predeterminados
    ${tempb}=    Get Title
    Log To Console    New windows is: \ ${tempb}
    Select Frame    name=fastway
    Wait Until Element Is Visible    name=textSearchId
    Click Element    name=buttonProceeding
    Sleep     1s

Ingresar al trámite de sujeto pasivo
    ${tempb}=    Get Title
    Unselect Frame
    Log To Console    New windows is: \ ${tempb}
    Select Frame        name=rise_content
    Wait Until Element Is Visible    id=dgTypeProceeding_dvClick_22
    Click Element   id=dgTypeProceeding_dvClick_22
    Sleep     1s

# Empezar a realizar caso de prueba

Validación de creación de Trámite con campos requeridos vacíos
    Unselect Frame
    Select Frame    name=rise_content
    Sleep     1s
    Click Element        name=ibtnCreateProceeding
    Sleep     2s
    Handle Alert    ACCEPT    timeout=3s 
    Sleep    1s
    Alert Should Be Present
    Log To Console    La alerta está presente
    Sleep    2s



Digitar el comentario del trámite
    
    Click Element    name=textProceedingComments
    ${ComentarioTramite}=    ComentController.Get Attribute      comentario    0   
    Input Text    name=textProceedingComments    ${ComentarioTramite}
    Sleep    1s
    

Validación búsqueda de Cédula del solicitante, valor vacío

    Click Element    name=linkShow
    Sleep    1s
    Wait Until Element Is Visible     xpath=//*[@id="tableMessage"]/tbody/tr/td[3]    
    Element Should Contain   xpath=//*[@id="tableMessage"]/tbody/tr/td[3]    El campo Cédula del Solicitante no puede ser vacio
    Sleep    1s

Validación búsqueda de Cédula del Solicitante, valor incorrecto

    Click Element    name=textApplicantIdCard
    Input Text       name=textApplicantIdCard    0011605011026T
    Sleep    1s
    Click Element    name=linkShow
    Wait Until Element Contains    xpath=//*[@id="tableMessage"]/tbody/tr/td[3]   No se ha encontrado el contribuyente
    Sleep    1s

Búsqueda Cédula del solicitante, valor correcto

    Click Element    name=textApplicantIdCard
    ${CedulaSoli}=    ApplicantsController.Get Attribute     cedula    0
    Input Text       name=textApplicantIdCard    ${CedulaSoli}
    Sleep    1s
    Click Element    name=linkShow
    Sleep    2s

Teléfono del solicitante 

    Click Element    name=textApplicantPhone
    ${TelefonoSoli}=   ApplicantsController.Get Attribute    telefono    0
    Input Text       name=textApplicantPhone    ${TelefonoSoli}

Cargo del solicitante

    Click Element    name=textApplicantPosition
    ${CargoSoli}=   ApplicantsController.Get Attribute    cargo    0
    Input Text       name=textApplicantPosition    ${CargoSoli}

Correo del solicitante

    Click Element    name=textApplicantEmail
    ${CorreoSoli}=    ApplicantsController.Get Attribute    correo    0    
    Input Text       name=textApplicantEmail    ${CorreoSoli}
    


Registro de información faltante en la sección Solicitante
    Teléfono del solicitante 
    Cargo del solicitante
    Correo del solicitante   
    Sleep    1s 


Tipo de contribuyente

    Click Element    name=clientControl$ddTypeActor
    ${TipoPersona}=    TaxpayerController.Get Attribute    tipoPersona    0
    Select From List By Label   name=clientControl$ddTypeActor     ${TipoPersona}
    Sleep    1s
    
Primer nombre contribuyente    

    ${primerNombre}=    TaxpayerController.Get Attribute   primerNom     0
    Input Text    name=clientControl$textActorFFNameTradeName    ${primerNombre} 
    
Tipo de docuemnto de identidad

    Click Element    name=clientControl$ddTypeIdCard
    ${tipoDocumento}=    TaxpayerController.Get Attribute    documentoID    0    
    Select From List By Label  name=clientControl$ddTypeIdCard    ${tipoDocumento}

Día de nacimiento del contribuyente

    Click Element    name=clientControl$ddlDayActorBirthday       
    ${diaNaci}=    TaxpayerController.Get Attribute    diaNaci    0
    Select From List By Label  name=clientControl$ddlDayActorBirthday    ${diaNaci}

Mes de nacimiento del contribuyente

    Click Element    name=clientControl$ddlMonthActorBirthday
    ${mesNaci}=    TaxpayerController.Get Attribute    mesNaci    0
    Select From List By Label  name=clientControl$ddlMonthActorBirthday    ${mesNaci}

Año de nacimiento del contribuyente

    Click Element    name=clientControl$ddlYearActorBirthday   
    ${añoNaci}=    TaxpayerController.Get Attribute    añoNaci    0
    Select From List By Label  name=clientControl$ddlYearActorBirthday     ${añoNaci}

Primer apellido del contribuyente

    Click Element    name=clientControl$textActorLFNameCommercialName
    ${primerApellido}=    TaxpayerController.Get Attribute    primerApe    0
    Input Text         name=clientControl$textActorLFNameCommercialName    ${primerApellido}

Número de identificacion del contribuyente

    ${ID}=    TaxpayerController.Get Attribute    identificacion    0
    Click Element    name=clientControl$textActorIdCard
    Input Text    name=clientControl$textActorIdCard    ${ID}
    Sleep    1s

Género del contribuyente

    ${genero}=    TaxpayerController.Get Attribute    genero    0
    Click Element    name=clientControl$ddGenderName
    Select From List By Label    name=clientControl$ddGenderName    ${genero}      
    Wait Until Element Contains    name=clientControl$ddGenderName    ${genero}

Registro de información requerida en la sección Contribuyente
    Tipo de contribuyente
    Primer nombre contribuyente   
    Tipo de docuemnto de identidad
    Día de nacimiento del contribuyente
    Mes de nacimiento del contribuyente
    Año de nacimiento del contribuyente
    Primer apellido del contribuyente
    Número de identificacion del contribuyente
    Género del contribuyente
    Sleep    1s



Segundo nombre del contribuyente
  
    ${segundoNombre}=    TaxpayerController.Get Attribute    segundoNom    0
    Click Element    name=clientControl$textActorFSName
    Input Text     name=clientControl$textActorFSName    ${segundoNombre}

Segundo apellido del contribuyente

    ${comentario}=    TaxpayerController.Get Attribute    segundoApe    0
    Click Element    name=clientControl$textActorLSName
    Input Text     name=clientControl$textActorLSName     ${comentario}

Comentario del contribuyente

    ${primerApellido}=    TaxpayerController.Get Attribute    comentario    0
    Click Element    name=clientControl$textCusPubStatusComment
    Input Text     name=clientControl$textCusPubStatusComment    ${primerApellido}




Registro de información opcional en la sección Contribuyente
    Segundo nombre del contribuyente
    Comentario del contribuyente
    Comentario del contribuyente



Nacionalidad del contribuyente

    ${nacionalidad}=    GeneralitiesController.Get Attribute   nacionalidad     0   
    Click Element    name=clientControl$txtCustNationality
    Input Text     name=clientControl$txtCustNationality    ${nacionalidad}

Profesion del contribuyente

    ${profesion}=    GeneralitiesController.Get Attribute    profesion    0
    Click Element    name=clientControl$txtCustOccupation
    Input Text     name=clientControl$txtCustOccupation   ${profesion}

Numero Nis del contribuyente

    ${numeroNis}=    GeneralitiesController.Get Attribute   numeroNis    0
    Click Element    name=clientControl$txtNisNumber
    Input Text     name=clientControl$txtNisNumber   ${numeroNis}

Estado civil del contribuyente

    ${estadoCivil}=    GeneralitiesController.Get Attribute  estadoCivil    0
    Click Element    name=clientControl$dlMaritalStatus
    Select From List By Label     name=clientControl$txtNisNumber   ${estadoCivil}

Cuenta Enacal del contribuyente

    ${cuentaEnacal}=    GeneralitiesController.Get Attribute   cuentaEnacal    0
    Click Element    name=clientControl$txtCustEnacalNumber
    Input Text     name=clientControl$txtCustEnacalNumber   ${cuentaEnacal}



Registro de informacion de generalidades del contribuyente
    Nacionalidad del contribuyente
    Profesion del contribuyente
    Numero Nis del contribuyente
    Estado civil del contribuyente
    Cuenta Enacal del contribuyente



Tipo de teléfono del contribuyente

    ${tipoTelefono}=    MailController.Get Attribute    tipoTelefono    0
    Click Element    name=clientControl$dlTypePhoneName
    Select From List By Label     name=clientControl$dlTypePhoneName  ${tipoTelefono}

Número de teléfono del contribuyente

    ${numTelefono}=    MailController.Get Attribute    numTelefono    0
    Click Element    name=clientControl$textPhoneNumber
    Input Text     name=clientControl$textPhoneNumber   ${numTelefono}

Correo electrónico del contribuyente

    ${correo}=    MailController.Get Attribute   correo    0
    Click Element    name=clientControl$textEmailDefinition
    Input Text     name=clientControl$textEmailDefinition   ${correo}



Registro de teléfono y correo del contribuyente
    Tipo de teléfono del contribuyente
    Número de teléfono del contribuyente
    Correo electrónico del contribuyente



Tipo de dirección del contribuyente

    ${tipoDireccion}=    DirController.Get Attribute   tipoDireccion    0    
    Click Element    name=clientControl$ddlTypeAddress
    Select From List By Label    name=clientControl$ddlTypeAddress   ${tipoDireccion}    

Edificio / casa del contribuyente

    ${edificio}=    DirController.Get Attribute  edificioCasa    0 
    Click Element    name=clientControl$textAddressRealEstate
    Input Text    name=clientControl$textAddressRealEstate    ${edificio}

Distrito de la dirección

    ${distrito}=    DirController.Get Attribute  distrito    0
    Click Element    name=clientControl$dlHousingDevName
    Select From List By Label    name=clientControl$dlHousingDevName    ${distrito}
    Sleep    1s
   
Barrio de la dirección
    Sleep    1s
    ${barrio}=    DirController.Get Attribute  barrio    0 
    Click Element    name=clientControl$dlZipCodeName
    Select From List By Label    name=clientControl$dlZipCodeName   ${barrio}



Registro de información requerida en la sección dirección
    Tipo de dirección del contribuyente
    Edificio / casa del contribuyente
    Distrito de la dirección
    Barrio de la dirección



Calle a la izquierda del inmueble

    ${calleIzquierda}=    DirController.Get Attribute    calleIzquierda    0
    Click Element    name=clientControl$textRealLeftStreet
    Input Text   name=clientControl$textRealLeftStreet    ${calleIzquierda}

Calle a la derecha del inmueble

    ${calleDerecha}=    DirController.Get Attribute  calleDerecha    0
    Click Element    name=clientControl$textAddressRightStreet
    Input Text    name=clientControl$textAddressRightStreet   ${calleDerecha}

Apartamento de la dirección

    ${apartamento}=    DirController.Get Attribute    apartamento    0
    Click Element    name=clientControl$textAddressApartment
    Input Text    name=clientControl$textAddressApartment    ${apartamento}

Piso de la dirección

    ${piso}=    DirController.Get Attribute    piso    0
    Click Element    name=clientControl$textAddressFloor
    Input Text    name=clientControl$textAddressFloor   ${piso}

Comentario de la dirección

    ${direccion}=    DirController.Get Attribute    direccion    0
    Click Element    name=clientControl$textRealEstateStreet
    Input Text    name=clientControl$textRealEstateStreet    ${direccion}
    Sleep    1s


Registro de información opcional en la sección dirección
    Calle a la derecha del inmueble
    Calle a la izquierda del inmueble
    Apartamento de la dirección
    Piso de la dirección
    Comentario de la dirección
    Sleep    1s

Agregar la direccion en la sección dirección
    Click Element    name=clientControl$btnAddAddress
    Sleep    2s


Creacion del trámite
    Wait Until Element Is Visible    name=ibtnCreateProceeding
    Click Element    name=ibtnCreateProceeding
    Sleep    1s

Aceptar creación del trámite
    Handle Alert    ACCEPT    timeout=3s 
    Sleep    1s

Aprobar el trámite
    Sleep    2s
    Wait Until Element Is Visible    id=rbStatus_0
    Click Element    id=rbStatus_0
    Sleep    1s
    Click Element    name=ibtnSave
    Sleep    3s

Verificar trámite
    Wait Until Element Is Visible    name=clientControl$textAcountNumber 
    ${cuentaFiscal}=    get element attribute    id=clientControl_textAcountNumber    value
    Ingresar Datos De Salida XML    ArchivosXML/contribuNatural.xml    output      numerocontribuyente    ${cuentaFiscal}        
    Log To Console    Cuenta fiscal-Número de contribuyente:    ${cuentaFiscal}    value
    Sleep    3s    


Registrar datos del trámite de sujeto pasivo
    AND Ir a trámites predeterminados
    Sleep    1s
    AND Ingresar al trámite de sujeto pasivo
    Sleep     1s
    AND Validación de creación de Trámite con campos requeridos vacíos
    AND Validación búsqueda de Cédula del solicitante, valor vacío
    AND Validación búsqueda de Cédula del Solicitante, valor incorrecto
    AND Búsqueda Cédula del solicitante, valor correcto
    AND Registro de información requerida en la sección Contribuyente
    AND Registro de información requerida en la sección dirección
    AND Registro de información opcional en la sección dirección
    AND Agregar la direccion en la sección dirección

Crear y aceptar el trámite
    AND Creacion del trámite
    AND Aceptar creación del trámite


*** Variables ***
${URL}      https://jira.com
${USER}     ARI CC Testing
${PASS}     ACT
${tipoPersona}    Natural
${rutaContribuyente}    ArchivosXML/contribuNatural.xml    
${rutaInicioSesion}    ArchivosXML/prueba.xml
${rutaSolicitante}    ArchivosXML/solicitante.xml
${rutaDireccion}    ArchivosXML/direccion.xml
${rutaComentarioTramite}    ArchivosXML/comentarioTramite.xml
${rutaGeneralidadesContribuyente}    ArchivosXML/contribGeneralidades.xml
${rutaTelefono}     ArchivosXML/telefonoCorreo.xml



*** Test Cases ***


Autenticar credenciales
    [Documentation]    Se automatizan las pruebas para autenticar el inicio de sesión en ARI CC
    Given Abrir Navegador
    Iniciar Grabacion    Autenticar credenciales   
    [Tags]    Test Login
    When Iniciar sesion
    [Teardown]    Detener Grabacion



Creacion de sujeto pasivo

    
    [Documentation]       Creación de sujeto pasivo natural
    Go to     https://almacc.tustributos.com/frames.aspx  
    Iniciar Grabacion    Creación de sujeto pasivo
    [Tags]    Sujeto pasivo
    Given Registrar datos del trámite de sujeto pasivo
    
    And Crear y aceptar el trámite
    And Aprobar el trámite
    Then Verificar trámite
   
    [Teardown]       Run Keywords    
    ...        Detener Grabacion     
    ...        Close All Browsers        

   
    Close All Browsers



