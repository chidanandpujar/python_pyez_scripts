l = [{'xpath': '/ntp-associations/association', 'testoperation': 'exists', 'passed': [{'id': {}, 'pre': {'refid': '.INIT.'}, 'post': {'refid': '.INIT.'}, 'actual_node_value': '.INIT.', 'message': 'Test PASSED: <.INIT.>'}, {'id': {}, 'pre': {'refid': '.LOCL.'}, 'post': {'refid': '.LOCL.'}, 'actual_node_value': '.LOCL.', 'message': 'Test PASSED: <.LOCL.>'}], 'failed': [], 'test_name': 'test_ntp_association', 'node_name': 'refid', 'result': True, 'count': {'pass': 2, 'fail': 0}}]

for data in l:
    print(data['xpath'])
    print(data['test_name'])
    #values = dict(data)
    #print(values["test_name"])
    #print(values["result"])
