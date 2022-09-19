# Module 03 - How Ansible Works

## Module Overview

To paraphase Alan Kay...

### Ansible makes simple things simple, and complex things possible.

By default and by design, Ansible:
* Passes your own credentials to authenticate.
* Uses SSH to connect to hosts.
* Requires zero additional software to be installed on hosts.

## Three Important Rules Upfront

### Rule 1: Nothing happens without an inventory!

Hosts are basically the nouns of Ansible.

Let's update an inventory file to define the IP addresses we gave you at the beginning of today's workshop:

$ ```vim /home/ec2-user/inventory```

Ansible has a default search path for inventory files.
But you can also specify your own:

$ `ansible -i inventory all -m ping`

### Rule 2: Almost everything you do with Ansible uses a module

Modules are kinda the verbs of Ansible.

(The above example uses the ping module.)

Every task we create today will use modules. Many modules take arguments. Learn to look for these arguments.

### Rule 3: Ansible is declarative, which means idempotency, which means it doesn't do work that doesn't need to be done.

Understanding "ok" vs. "changed"

# Additional resources:

https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#inventory-aliases

https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html#action-run-your-first-ansible-commands

# [NEXT: Module 04 - Ad-Hoc Commands](../Module%2004%20-%20Ad-Hoc%20Commands)
