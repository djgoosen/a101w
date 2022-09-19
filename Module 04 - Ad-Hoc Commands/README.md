# Module 04: Ad-Hoc Commands


## Formally introducing Ansible ad-hoc commands

1. $ `ansible -i inventory web -m ping`

1. $ `ansible -i inventory all -a "/bin/echo hello"`

1. $ `ansible -i inventory web -m command -a "uptime" -o`

### Gathering facts

1. $ `ansible -i inventory web -m setup`

### Managing files & directories

1. $ `echo hello at $(date) > timestamp.txt`

1. $ `ansible -i inventory all -m copy -a "src=timestamp.txt dest=/tmp/timestamp.txt"`

1. $ `ansible -i inventory host1 -m file -a "dest=/tmp/timestamp.txt mode=600"`

1. (RUN THAT AGAIN)

1. $ `ansible -i inventory host1 -m file -a "dest=/tmp/mydir mode=755 owner=ec2-user group=ec2-user state=directory"`

1. $ `ansible -i inventory host1 -m file -a "dest=/tmp/mydir state=absent"`

### Managing packages & services

(NOTE THAT WE NEED `-b` OR `--become` HERE!)

1. $ `ansible -i inventory host1 -m yum -a "name=httpd state=present" -b`

1. (RUN THAT AGAIN)

1. $ `ansible -i inventory host1 -m service -a "name=httpd state=started" -b`

1. $ `ansible -i inventory host1 -m command -a "service httpd status" -b`

1. $ `ansible -i inventory host1 -m service -a "name=httpd state=restarted" -b`

1. $ `ansible -i inventory host1 -m service -a "name=httpd state=stopped" -b`

1. $ `ansible -i inventory host1 -m yum -a "name=httpd state=absent" -b`


# Additional resources

https://docs.ansible.com/ansible/latest/user_guide/intro_adhoc.html#intro-adhoc

https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html#all-modules

# [NEXT: Module 05 - Playbooks](../Module%2005%20-%20Playbooks)
