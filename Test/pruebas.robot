*** Settings ***
Documentation     Prueba de Robot Framework que guarda un mensaje si pasó o no el test en el archivo XML.
Library    Selenium2Library
Library    ScreenCapLibrary


*** Variables ***
${mensaje}=    aprobado

*** Keywords ***

LogError
    Fail

Abrir navegador
    Open Browser    https://almacc.tustributos.com    chrome
    Maximize Browser Window
    Sleep    2s
    #Log       Navegador abierto correctamente
    #BuiltIn.Set Test Message     navegador abierto

Iniciar sesion
    Input Text      name=txtUserName    gamayatx
    # Wait Until Element Is Visible    name=usuerioprueba
    #Run Keyword If Test Failed    LogError    
    Input Text    name=txtUserPasswor    Agas1234
    #Run Keyword If Test Failed    Log    error    console=yes
    Log    Usuario:gamayatx    console=yes
    Sleep    2s
    #BuiltIn.Set Test Message     Usuario:gamayatx

Aplicar roles básicos
    Log     ${rolbasico}    console=yes
   # "BuiltIn.Set Test Message     usuario:gamayatx | usuario básico  


*** Variables ***
${rolbasico}    usuario basico


*** Test Cases ***
Test Guardar Mensaje
    [Documentation]    Guarda el mensaje de Pass o Fail en un archivo xml
    [Tags]    Prueba
    ##${resultado}=    Run Keyword And Return Status    Abrir navegador  
    #Log    ${resultado}
    Abrir navegador
    # ${result}    Run Keyword And Return Status      Iniciar sesion
    Given Iniciar sesion
    #Log    user:gamayatx
    # Run Keyword If    '${result}'=='False'    Log     Falló
    Then Aplicar roles básicos
    # Log   ${rolbasico}

    #${resultadoLogin}=    Run Keyword And Return Status    Iniciar sesion
    #Log    Usuario:gamayatx contraseña:Agas1234   

    # Run Keyword If    '${resultado}'=='PASS'    Set Variable    ${mensaje}    Mensaje de Prueba Pasó
    # ...    ELSE    Set Variable    ${mensaje}    Mensaje de Prueba No Pasó

    #Log    ${mensaje}
# Test Cobro general
#     [Documentation]     Le cobra a los contribuyentes
#     [Tags]    Prueba de cobro general
#     Abrir navegador
#     Given Iniciar sesion
#     Log     user:gamatyatx
#     Then Aplicar roles básicos
#     Log   ${rolbasico}

