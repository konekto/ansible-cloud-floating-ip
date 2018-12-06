import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/sysconfig/network-scripts/ifcfg-eth0:1')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

    assert f.contains("IPADDR=8.8.8.8")
