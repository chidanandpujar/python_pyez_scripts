from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='xx.xx.xx.xx', user='xyz', password='xyz', gather_facts=False)
dev.open()

cu = Config(dev)
data = 'deactivate system scripts'
try:
    cu.load(data, format='set')
    cu.pdiff()
    if cu.commit_check():
       cu.commit()
    else:
       cu.rollback()
except Exception as err:
    print("Exception occured ",err)
