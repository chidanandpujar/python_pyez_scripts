results = dict()
results = {
        "test_results": {
            "show chassis alarms": [
                {
                    "count": {
                        "fail": 0,
                        "pass": 1
                    },
                    "failed": [],
                    "node_name": "alarm-summary/active-alarm-count",
                    "passed": [
                        {
                            "POST": {},
                            "PRE": {},
                            "id": {
                                "alarm-summary/active-alarm-count": "null"
                            },
                            "message": "Test Succeeded!! no chassis alarm"
                        }
                    ],
                    "result": "true",
                    "test_name": "test_chassis_alarm_check",
                    "testoperation": "not-exists",
                    "xpath": "//alarm-information"
                },
                {
                    "result":  "null"
                }
            ],
            "show ospf neighbor instance all": [
                {
                    "count": {
                        "fail": 0,
                        "pass": 0
                    },
                    "expected_node_value": [
                        "2-Way",
                        "Full"
                    ],
                    "failed": [],
                    "node_name": "ospf-neighbor-state",
                    "passed": [],
                    "result": "null",
                    "test_name": "test_ospf_neighbor",
                    "testoperation": "is-in",
                    "xpath": "/ospf-neighbor-information-all/ospf-instance-neighbor/ospf-neighbor"
                }
            ],
            "show system core-dumps": [
                {
                    "result": "null"
                }
            ],
            "show system memory": [
                {
                    "count": {
                        "fail": 1,
                        "pass": 0
                    },
                    "expected_node_value": [
                        70.0,
                        99.0
                    ],
                    "failed": [
                        {
                            "actual_node_value": "null",
                            "id": {},
                            "post": {},
                            "pre": {},
                            "xpath_error": "true"
                        }
                    ],
                    "node_name": "system-memory-information/system-memory-summary-information/system-memory-free-percent",
                    "passed": [],
                    "result": "false",
                    "test_name": "check_system_memory_usage",
                    "testoperation": "in-range",
                    "xpath": "multi-routing-engine-item"
                }
            ]
        } 
        }
#print(results)

for res in results["test_results"]:
    #print(results["test_results"][res])
    for data in results["test_results"][res]:
        #print(data)
        for key, value in data.items():
            #print(key, value)
            if 'test_name' in key:
                if data['result'] == 'false':
                    print(data['test_name']) 
                    print(data['result'])
