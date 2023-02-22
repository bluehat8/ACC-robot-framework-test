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


Iniciar sesion
    Input Text      name=txtUserName    gamayatx
    Input Text    name=txtUserPasswor    Agas1234
    Log    Usuario:gamayatx    console=yes
    Sleep    2s

Aplicar roles básicos
    Log     ${rolbasico}    console=yes
   BuiltIn.Set Test Message     usuario:gamayatx | usuario básico  


*** Variables ***
${rolbasico}    usuario basico


*** Test Cases ***
Test Login
    [Documentation]    Guarda el mensaje de Pass o Fail en un archivo xml
    [Tags]    Prueba

    Abrir navegador
    Given Iniciar sesion
    Then Aplicar roles básicos

