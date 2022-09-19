# Module 02 - Installing Ansible

## Module Overview

Today’s workshop is being run on Amazon EC2.
Each student will be assigned a number (e.g. student01, student02), as well as:

* An SSH key pair
* The IP addresses of each of your EC2 instances

### Your Workshop EC2 Instances

Each student’s personal EC2 lab is composed of the following:

1. Control node (to run Ansible plays).
1. Host nodes (to target).

### Pre-Steps

#### Pre-steps on your laptop (Linux/Mac)

1. $ `mv ~/Downloads/ansible-workshop2.pem ~/.ssh/.`

1. $ `chmod 600 ~/.ssh/ansible-workshop2.pem`

1. $ `ssh-add ~/.ssh/ansible-workshop2.pem`

1. $ `ssh-add -l | grep ansible`


#### Pre-steps on your laptop (Windows)

https://www.ssh.com/ssh/putty/putty-manuals/0.68/Chapter8.html

### Testing Your Workshop Environment

* Launch a terminal or terminal emulator (like PuTTY).

* ssh to each of your EC2 instances.

* EXAMPLE: `ssh -A ec2-user@54.68.121.204`

Be sure you can ssh into to all 3 of your ec2 instances. If you can’t ssh into any of them, please let your instructor know immediately!


### Installing Ansible via `virtualenv` on the Control Node

Using a virtual environment is a common way of installing Ansible.

$ `cat ~/setup.sh`

$ `source ~/setup.sh`

### Only If You Run Into Problems With Your SSH Key Forwarding:

$ `source ./ffwd.sh`

### Want to follow along today, but without all the typing?

No judgments! In that case, we've pre-loaded a bash history [file](../roles/bootstrap/files/bash_history) on your Control node. To run each corresponding command by its line number, type `!1`, `!2`, ... `!80`. 

(You'll still have to transcribe or copy+paste the YAML file code, but this will save you some keystrokes for sure.)
 

### A Note on `vim` and Other Text Editors

In this workshop, we edit text files on the command line.

All of this workshop's file examples use vim, but your instances also come with nano.

For a quick tutorial on vim:

$ `vimtutor`

### Module Conclusion

That's it! (BTW, notice how we aren't installing anything on the host nodes?)

# Additional resources:

https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

# [NEXT: Module 03 - How Ansible Works](../Module%2003%20-%20How%20Ansible%20Works)
