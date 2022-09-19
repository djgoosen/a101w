# Module 05 - Playbooks

## Create a simple directory structure

1. $ `mkdir -p ~/apache_basic/templates`

1. $ `cd ~/apache_basic`

## First playbook: Verifying Apache

1. $ `vim 01-verify-apache.yml`

1. $ `ansible-playbook -i ../inventory 01-verify-apache.yml`

1. $ `cat ../inventory`

1. $ `ssh <HOST1_IP_ADDRESS> curl localhost`

## Now... can you create a playbook which REMOVES Apache?

(Bonus points if you can stop the service before removing...)

1. $ `vim 02-remove-apache.yml`

## Configuring Apache

1. $ `cd templates`

1. $ `curl -O https://levelupworkshops.s3-us-west-2.amazonaws.com/ansible-workshops/101/03-index.html.j2`

1. $ `cd ../`

1. $ `vim 03-update-index-html.yml`

1. $ `ansible-playbook -i ../inventory 03-update-index-html.yml`

1. $ `cat ../inventory`

1. $ `ssh <HOST1_IP_ADDRESS> curl localhost`

## SIDEBAR: Introducing ansible-lint

`ansible-lint` will save you time and trouble.

1. $ `ansible-lint 03-update-index-html.yml`

## Using Variables, Loops, and Handlers

For expanded discussion of this section: http://ansible.redhatgov.io/standard/core/exercise1.4.html

1. $ `cd ~`

1. $ `mkdir -p ~/apache_basic_playbook/templates`

1. $ `cd apache_basic_playbook`

1. $ `vim 04-site.yml`

1. $ `cd templates`

1. $ `curl -O https://levelupworkshops.s3-us-west-2.amazonaws.com/ansible-workshops/101/04-httpd.conf.j2`

1. $ `curl -O https://levelupworkshops.s3-us-west-2.amazonaws.com/ansible-workshops/101/04-index.html.j2`

1. $ `cd ../`

1. $ `ansible-lint 04-site.yml`

1. $ `ansible-playbook -i ../inventory 04-site.yml`

1. $ `cat ../inventory`

1. $ `ssh <HOST1_IP_ADDRESS> curl localhost`

# Additional resources:

https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html

https://docs.ansible.com/ansible/latest/user_guide/playbooks.html#working-with-playbooks

# [NEXT: Module 06 - Roles](../Module%2006%20-%20Roles)
