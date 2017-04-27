#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""vsphere_testing. Entrypoint used to test the vSphere class. Has examples of API usage.

Usage:
    vsphere_testing.py [-v] [options]
    vsphere_testing.py --version
    vsphere_testing.py (-h | --help)

Options:
    -h, --help          Shows this help
    --version           Prints current version
    --no-color          Do not color terminal output
    -v, --verbose       Emit debugging logs to terminal
    -f, --file FILE     Name of JSON file with server connection information

"""

import logging

from docopt import docopt
from pyVmomi import vim

from adles.vsphere.vsphere_class import Vsphere
from adles.utils import script_setup
from adles.vsphere import vm_utils

args = docopt(__doc__, version=Vsphere.__version__, help=True)
server = script_setup('vsphere_testing.log', args, (__file__, Vsphere.__version__))

test = server.find_by_inv_path("vm/cgoes_testing/script_testing/monkeys/test-vm")
if test is not None:
    vm_utils.get_vm_info(test)
else:
    print("GOT EM")

vm = server.get_vm("dummy")
vm.get_info()

test2 = server.get_folder("vm/cgoes_testing/script_testing/monkeys")
if test2 is not None:
    print(test2)
else:
    print("DRAT")

folder = server.get_folder("monkeys")
folder.create("HAHAHAHhaHAHhaHA (hi)")
print(folder.enumerate())

# from adles.vsphere.vm import VM
# from adles.vsphere.hosts import Host
# folder = server.get_folder("monkeys")
# vm = server.get_vm("test-vm")
# service = VM(vm=vm)
# service = VM(name="test-vm", folder=folder, resource_pool=server.get_pool(),
#              datastore=server.get_datastore(), host=server.get_host())
# template = server.get_vm("dummy")
# service.create(template=template)
# service.change_state("on")
# print(service.screenshot())
# service.change_state("off")
# service.set_note("testing 1... 2... 3...")
# print(str(service))
# print(hash(service))
# print(service.get_info(True, True, True, True))
# service.upgrade(12)
# service.convert_template()
# service.destroy()

# host = Host(server.get_host())
# print(str(host))
# print(hash(host))

# from adles.vsphere.network_utils import create_vswitch
# host = server.get_host()
# create_vswitch("competition_vswitch", host)

# bios_uuid = "42053029-1098-6ef1-da79-5e2c4103f600"
# instance_uuid = "50056cfe-aaa0-c28d-a702-d72e68e50f3a"
# vm = server.find_by_uuid(uuid=instance_uuid)
# vm = server.find_by_ds_path(path="[Datastore] (MASTER) apache/(MASTER) apache.vmx")
# logging.info("%s", vm_utils.get_info(vm, uuids=True))

# pool = server.get_item(vim.ResourcePool)
# vm_spec = vm_utils.gen_vm_spec(name="test_vm", datastore_name="Datastore",
#                                annotation="testing 1...")
# vm_utils.create_vm(folder, vm_spec, pool)
# attach_iso(vm, "ISO-Images/vyos-1.1.7-amd64.iso", server.get_datastore("Datastore"))

# vm = server.get_vm("real-vm")
# logging.info(vm_utils.get_info(vm, detailed=True, uuids=True, snapshot=True, vnics=True))

# vms = server.get_all_vms()
# for vm in vms:
#     logging.info(vm_utils.get_info(vm))

# net = server.get_network("ARP-LAN")
# logging.info(str(net))

# host = server.get_host()
# logging.info(host)

# logging.info(str(server))
# logging.info(repr(server))

# from adles.vsphere.folder_utils import traverse_path
# folder = server.get_folder("script_testing")
# vm = traverse_path(folder, "/Templates/Routers/VyOS 1.1.7 (64-bit)")
# logging.info(get_info(vm))

# datastore = server.get_datastore("Datastore")
# logging.info(get_datastore_info(datastore))

# portgroup = server.get_item(vim.Network, "test_network")
# logging.info("Portgroup: %s", str(portgroup))
# vm_utils.add_nic(vm, portgroup, "test_summary")
# vm_utils.edit_nic(vm, 2, summary="lol")
# vm_utils.remove_nic(vm, 1)

# create_portgroup("test_portgroup", server.get_host(), "test_vswitch")
# delete_portgroup("test_portgroup", server.get_host())
