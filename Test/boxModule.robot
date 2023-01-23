*** Settings ***
Library     Collections
Library     JIRALibrary


*** Variables ***
${URL}      https://jira.com
${USER}     amayasoza
${PASS}     contraseñajuanito


*** Test Cases ***
Connect To JIRA
    ${session}    Connect To Jira    ${URL}    ${USER}    ${PASS}
    ${projects}    Projects    ${session}

Connect To JIRA And Skip SSL Check
    Evaluate    urllib3.disable_warnings()
    ${session}    Connect To Jira    ${URL}    ${USER}    ${PASS}    verify_ssl=${False}
    ${projects}    Projects    ${session}

Add Comment to Issue
    ${session}    Connect To Jira    ${URL}    ${USER}    ${PASS}
    Issue Add Comment    ${session}    JIRAID-1234    My long comment !