from jnpr.junos import Device
from lxml import etree
from pprint import pprint
host="x.x.x.x"
user="xyz"
password="xyz"

with Device(host=host, user=user, port="22", normalize=False, password=password) as dev:

    data = dev.rpc.get_config(options={'database': 'committed', 'inherit': 'inherit', 'commit-scripts': 'apply'})
print (etree.tostring(data.getparent(), encoding='unicode', pretty_print=True))
