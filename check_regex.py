import re
pattern = "rpd"
msg = """rpd daemon running with PID 100
          rpd daemon running with PID 101
          rpd daemon running with PID 102 
"""
ret = re.match(pattern,msg)
print(ret)

ret = re.search(pattern, msg,0)
print(ret)

for match in re.findall(pattern, msg):
    print("found", match)

ret = re.sub("rpd","routed", msg)
print(ret)
