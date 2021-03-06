#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
'''xen_vm_shutdown: wrapper around xe vm-shutdown command
   TODO:
    * check state before and after
    * return proper 'changed' status
'''

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: xen_vm_shutdown
author:
    - Anthony Loukinas (@anthonyloukinas)
version_added: "2.7"
short_description: Shutdown Xenserver Virtual Machine
requirements: [ xe ]
description:
    - Manage xenserver guests using xe commands
options:
    uuid:
        description:
            - uuid of the vm to shutdown
        required: true

'''

EXAMPLES = '''
- xen_vm_shutdown:
    uuid: <vm uuid>
'''

import os
import socket
import traceback

from ansible.module_utils.basic import (
    AnsibleModule,
    get_distribution,
    get_distribution_version,
    get_platform,
    load_platform_subclass,
)
from ansible.module_utils._text import to_native
from ansible.module_utils.xenserver_common import XeBase

class XeVmStart(XeBase):
    """
    This is a xe vm_list command wrapper class
    """

    def vm_shutdown(self, uuid=None):
        """vm_shutdown(str) -> dict
        Args:
            uuid (str): uuid of vm to shutdown
        Returns:
            dict
        """
        self.cmd.append('vm-shutdown')
        self.cmd.append('uuid=%s' % uuid)
        rc, out, err = self.module.run_command(self.cmd)
        if rc != 0:
            self.module.fail_json(
                msg="Command failed rc=%d, out=%s, err=%s" % (rc, out, err)
            )
        return to_native(out).strip()

def main():
    module = AnsibleModule(
        argument_spec=dict(
            uuid=dict(required=True),
        ),
        supports_check_mode=True,
    )

    vm_shutdown_cmd = XeVmStart(module)
    vm_uuid = module.params['uuid']

    out = vm_shutdown_cmd.vm_shutdown(uuid=vm_uuid)
    
    out_formated = out.strip().split()[1::2]
    kw = dict(changed=True, vm_shutdown=out,
              ansible_facts=dict(
                    ansible_fqdn=socket.getfqdn(),
                    ansible_domain='.'.join(socket.getfqdn().split('.')[1:])
                    )
              )

    #if changed:
    #    kw['diff'] = {'after': '\n',
    #                  'before': '\n'}

    module.exit_json(**kw)

if __name__ == '__main__':
    main()