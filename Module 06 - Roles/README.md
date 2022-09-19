# Module 06 - Roles

## Module Overview

Roles are ways of automatically loading certain vars_files, tasks, and handlers based on a known file structure.

Grouping content by roles also allows easy sharing of roles with other users.

Ansible Galaxy helps us build role directory/file structures quickly.

Ansible Galaxy is also where the community shares roles with each other.

For expanded discussion of this section: http://ansible.redhatgov.io/standard/core/exercise1.6.html

### Key Concepts:

* Code Reuse
* Using Roles
* Role Directory Structure
* Ansible Galaxy

# First role: decomposing the original site.yml playbook

1. $ `cd ~/apache_basic_playbook`

1. $ `cp templates/04-index.html.j2 templates/index.html.j2`

1. $ `cp templates/04-httpd.conf.j2 templates/httpd.conf.j2`

1. $ `mkdir roles`

1. $ `cd roles`

1. $ `ansible-galaxy init apache-simple`

1. $ `cd ~/apache_basic_playbook/roles/apache-simple/`

1. $ `rm -rf tests files`

1. $ `tree`

1. $ `cd ~/apache_basic_playbook/`

1. $ `vim site.yml`

1. $ `vim roles/apache-simple/defaults/main.yml`

1. $ `vim roles/apache-simple/handlers/main.yml`

1. $ `vim roles/apache-simple/tasks/main.yml`

1. $ `vim roles/apache-simple/vars/main.yml`

1. $ `ansible-playbook -i ../inventory site.yml`

1. $ `cat ../inventory`

1. $ `ssh <HOST1_IP_ADDRESS> curl localhost`

# Additional resources:

https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html

https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#finding-roles-on-galaxy

# [NEXT: Module 07 - Ansible Best Practices](../Module%2007%20-%20Ansible%20Best%20Practices)
