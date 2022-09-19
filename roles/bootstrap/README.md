bootstrap
=========

This role bootstraps an AWS EC2-based Ansible 101 workshop environment.

Requirements
------------

No pre-requisites beyond the obvious. Start with the 101/README.md  

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

---
- hosts: student
  name: This bootstraps the Ansible 101 workshop environment in EC2
  gather_facts: false
  become: true

  roles:
    - bootstrap


Author Information
------------------

arc@levelupla.io
