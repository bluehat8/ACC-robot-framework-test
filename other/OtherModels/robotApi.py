from robot.api import ExecutionResult
from robot.api import ResultWriter

# # Cargar el archivo de resultados
result =  ExecutionResult('results/output.xml')
result.configure(stat_config={'suite_stat_level': 2, 'tag_stat_combine': 'tagANDanother'})

# # # # Iterar sobre todas las keywords
for test in result.suite.tests:
    for keyword in test.body:
        name = keyword.name
        status = keyword.status
        start_time = keyword.starttime
        end_time = keyword.endtime
        elapsed_time = keyword.elapsedtime
        log = keyword.messages
        if status == 'FAIL':
            error_message = keyword.messages[-1]
            print(f'Keyword: {name}, Status: {status}, Error Message: {error_message}, Elapsed Time: {elapsed_time}, Start Time: {start_time}, End Time: {end_time}, Log: {log}')
        if status == 'PASS':
            print(f'Keyword: {name}, Status: {status}, Elapsed Time: {elapsed_time}, Start Time: {start_time}, End Time: {end_time}, Log: {log}')


# stats = result.statistics

# for test in stats.suite.tests:
#     for keyword in test.keywords:
#         if keyword.status == 'FAIL':
#             error_message = keyword.messages[0]['message']
#             print(f"El mensaje de error de la keyword '{keyword.name}' es: {error_message}")