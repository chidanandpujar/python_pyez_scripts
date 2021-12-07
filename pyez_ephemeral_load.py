from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='xx.xx.xx.xx', user='xyz', password='xyz', gather_facts=False)
dev.open()
dev.timeout=300

with Config(dev, mode='ephemeral', ephemeral_instance='test1') as cu:
    try:
       cu.load(path="test.xml", format='xml')
    except Exception as err:
        print(err)
