#!/usr/bin/python
# -*- coding: utf-8 -*-

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
- TODO: add example of how to enable with ansible
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