# Module 07 - Ansible Best Practices

# Module Overview

There are many best practices for working with Ansible in the real world. Here are three of them.

## Best Practice #1: Keep your secrets with `ansible-vault`

Encrypting version-controlled passwords is important.

BTW, you should know that increasing verbosity (e.g., `-vvvv`) risks your secrets leaking into log files, etc.

While most use cases involve targeting remote hosts, we also want to show an example of running an Ansible playbook against the localhost. 

1. $ `cd ~`

1. $ `vim creds.yml`

1. $ `echo Pad1ock > ~/.vpass.txt`

1. $ `ansible-vault encrypt creds.yml`

1. $ `cat creds.yml`

1. $ `vim encryptiondemo.yml`

1. $ `id <USERNAME>`

1. $ `ansible-playbook -v -i localhost -c local encryptiondemo.yml --vault-password-file ~/.vpass.txt`

1. $ `id <USERNAME>`

1. $ `su <USERNAME>`

1. $ `whoami`

1. $ `exit`

A related demo video: https://levelupla.io/video-integrate-ansible-and-jira/

## Best Practice #2: Look before you leap with `--check` and `--diff`

Check Mode (aka “Dry Run”)

1. $ `cd ~`

1. $ `ansible-playbook -i inventory apache_basic/02-remove-apache.yml --check --diff --limit host1`

1. $ `ssh <HOST1> curl localhost`

Ansible docs: https://docs.ansible.com/ansible/latest/user_guide/playbooks_checkmode.html

## Best Practice #3: Rolling updates: Go fast without breaking everything at the same time

1. `cd ~/apache_basic_playbook`
1. $ `ansible-playbook -i ../inventory 04-site.yml`
1. Note that Ansible playbook run outputs groups by TASK by default.
1. Uncomment `serial: 1` in 04-site.yml
1. $ `ansible-playbook -i ../inventory 04-site.yml`
1. Note that your latest Ansible playbook is grouping all tasks by HOST now.

## Also worth mentioning:

* Live up to your team's code standards using customized `ansible-lint` rules
* `ansible-pull`: for those who want to invert Ansible's push-based design
* Molecule; or Test Kitchen for Ansible: for those who want to be test-driven


# Additional resources:

https://docs.ansible.com/ansible/latest/user_guide/playbooks_special_topics.html (Advanced Playbooks Features)

https://docs.ansible.com/ansible/latest/user_guide/playbooks_strategies.html

https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html

A related `ansible-lint`demo video: https://levelupla.io/video-iac-standards-w-ansible-lint-becoming-cloud-native-automation/