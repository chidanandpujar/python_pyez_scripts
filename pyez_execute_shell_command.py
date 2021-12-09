from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
from pprint import pprint

with Device(host="xx.xx.xx.xx", user="xyz", passwd="xyz") as dev:
  with StartShell(dev) as shell:
    result = shell.run('cli -c "show version | no-more"') 
    pprint(result)
