from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

dev = Device(host='xx.xx.xx.xx', user='xyz', password='xyz', gather_facts=False)
dev.open()

try:
   sw = SW(dev)
   result = sw.safe_copy(
            package="xyx.vmdk",
            remote_path="/var/tmp",
            progress=True,
            cleanfs=True,
            force_copy=False,
            checksum ="11212121212abd",
            checksum_algorithm="sha256",
   )
except Exception as err:
    print("Copy failure caused by Error:", err)
