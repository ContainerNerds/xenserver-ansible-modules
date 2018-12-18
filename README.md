# Citrix Xenserver Ansible Modules
This repository provides [Ansible](http://ansible.com) modules for configuring, provisioning, and managing your Xenserver workload. It uses Ansible command wrappers to the host remote system. This module has been tested against **XenServer 7.6+**.

The code here should be considered alpha quality and may be broken at times due to experiments and refactoring. Tagged releases should be stable. 

## Documentation
Documentation is hosted at (coming soon)

Currently the following modules are implemented

- xen_vm_list - List Virtual Machines
- xen_vm_install - Provision a Virtual Machine
- xen_vm_start - Start a Virtual Machine
- xen_vm_shutdown - Shutdown a Virtual Machine
- xen_vm_disk_list - List disks associated with Virtual Machines

## Pre-requisites
- Ansible 2.4+
- Python 2.7 or 3.x
- Requires build tools (make)

## Build & Install
```
make
make install
# It installs under /usr/share/ansible/xenserver
```
Edit /etc/ansible/ansible.cfg and add the following lines:
```
library = /usr/share/ansible/modules
module_utils = /usr/share/ansible/module_utils
```

### Uninstall
```
make uninstall
```

## Example play using the module
```
---
- hosts: xenserver01
  remote_user: root
  tasks:
    - name: "List xen guests"
      xen_vm_list:
        params: all
        
    - name: "install vm"
      xen_vm_install:
        template: <template uuid>
        name_label: test-from-ansible
      register: vm_uuid

    - name: "start vm"
      xen_vm_start:
        uuid: "{{ vm_uuid.uuid }}"

    - name: "get ipv4 address"
      xen_vm_param:
        uuid: "{{ vm_uuid.uuid }}"
        param: networks
      register: vm_ip
...
```

## LICENSE
**GPL V3**
See [LICENSE](./LICENSE) 

## COPYRIGHT
**COPYRIGHT 2018 ContainerNerds**

## Contribute:
Pull requests and issues are welcome. Compatability testing for XenServer is needed.