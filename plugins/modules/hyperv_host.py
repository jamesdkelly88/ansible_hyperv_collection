#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Trond Hindenes <trond@hindenes.com>, and others
# Copyright: (c) 2017, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
---
module: hyperv_host
short_description: Get or set Hyper-V settings
description:
- This module collects all the Hyper-V settings for the host, and if parameters are included then ensures the values match. It does not install/enable Hyper-V if it is missing.
options:
  virtual_machine_path:
    description:
    - If supplied, update the default location to store VMs on the host.
    type: str
    required: no
notes:
- Requires Hyper-V to be enabled on the host.
- "TODO: add example of how to enable with ansible"
author:
- James Kelly (jamesdkelly88)
'''

EXAMPLES = r'''
- name: get current hyper-v settings
  jamesdkelly88.win_hyperv.hyperv_host:
  register: hyperv

- debug:
    var: hyperv
'''

RETURN = r'''
computer_name:
  description: Host name of Hyper-V server
  returned: always
  type: str
  sample: "WIN-ABC123"

domain_name:
  description: Fully qualified domain name / workgroup name of Hyper-V server
  returned: always
  type: str
  sample: WORKGROUP

logical_processor_count:
  description: Virtual CPU count for Hyper-V server
  returned: always
  type: int
  sample: 4

max_storage_migrations:
  description: How many storage migrations can be performed simultaneously on the Hyper-V server
  returned: always
  type: int
  sample: 2

max_vm_migrations:
  description: How many virtual machine migrations can be performed simultaneously on the Hyper-V server
  returned: always
  type: int
  sample: 2

memory_capacity:
  description: Memory capacity (in bytes) of the Hyper-V server
  returned: always
  type: int
  sample: 34239225856

network:
  description: available network adapters on the Hyper-V server
  returned: always
  type: complex
  sample: { "external_adapters": null, "internal_adapters": "Default" }

supported_vm_versions:
  description: supported Hyper-V versions for guest virtual machines (e.g. 5.0 == Windows Server 2012 R2)
  returned: always
  type: list
  sample: ["8.0","8.1","8.2"]

virtual_hard_disk_path:
  description: default location for new virtual hard drives to be created
  returned: always
  type: str
  sample: C:\\VMs

virtual_machine_path:
  description: default location for new virtual machines to be created
  returned: always
  type: str
  sample: C:\\VMs

vm_migration_enabled:
  description: whether VM migrations are enabled on the Hyper-V server
  returned: always
  type: bool
  sample: false
'''
