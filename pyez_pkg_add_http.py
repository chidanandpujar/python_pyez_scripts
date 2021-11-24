from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

dev = Device(host='xx.xx.xx.xx', user='xyz', password='xyz', gather_facts=False)
dev.open()

def myprogress(dev, report):
        print("host: {}, report: {}".format( dev.hostname, report))

pkg = 'http://1.1.1.2//images/xyz.tgz'

sw = SW(dev)
ok, msg = sw.install(package=pkg, validate=True, no_copy=False, remote_path='/var/tmp', progress=myprogress)
if ok:
   sw.reboot()
