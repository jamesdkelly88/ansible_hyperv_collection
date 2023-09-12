# Ansible Collection: jamesdkelly88.win_hyperv

The `jamesdkelly88.win_hyperv` collection includes the powershell scripts that I use to manage Hyper-V hosts and guests (VMs).

## Ansible version compatibility

This collection has been tested against following Ansible versions: **2.10.8**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.

## Collection Documentation

TODO: [setup docsite](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_documenting.html)

## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the `ansible-galaxy` CLI:

    ansible-galaxy collection install git+https://github.com/jamesdkelly88/ansible_hyperv_collection.git

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:

- src: https://github.com/jamesdkelly88/ansible_hyperv_collection.git
  version: 1.0.0
  name: jamesdkelly88.win_hyperv
```

### Using the Collection

The modules in the collection must be run on the Hyper-V host directly. This requires the ansible controller to be able to connect to the Windows host either with WinRM or OpenSSH. If `win_ping` works and Hyper-V is enabled, you should be fine!

## License

BSD Zero Clause License

See [COPYING](COPYING) to see the full text.