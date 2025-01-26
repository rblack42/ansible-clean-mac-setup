Ansible Mac Clean Setup
#######################

:Author: Roie R. Black
:Email: roie.black@gmail.com
:Repo: https://github.com/rblack42/ansible-clean-mac-setup.git
:Docs: https://rblack42.github.io/ansible-clean-mac-setup

This project details the development of an *Ansible* playbook that I use to
initialize a Mac after a clean setup. I used this procedure to zero out my
teaching Macs after each term so I could start with a fresh known state for my
development system before starting teaching in a new term.

Most of the code here is based on the work of Jeff Geerling (geerlingguy) who
actually inspired me to include *Ansible* in my teaching.

Why Not Just Use Jeff's Playbooks?
==================================

I am an educator. Because of that, most of what I write is aimed at teaching the
reader how things work, not just getting a job done. Ultimately, I want my
students to write documentation for their projects that explains why their
project came into being, how it was designed, and how it works. All of this is
hugely useful to those who will use and maintain their projects long after the
original creators have left the project. My intent, here, is to provide a
step-by-step guide that will perform the desired system setup in a way that you
will fully understand.  Furthermore, you will see exactly where you might need
to make changes to my code to tune the system to your particular needs.

Starting Point
==============

This project assumes that you have a brand new Mac system, or an old one on
which you have performed a *clean install* of the version of MacOS you will  be
using.  (You may be limited in the OS version you can install if your system is
too old for current versions.) Your system must have a version of *Python3*
installed. All work will be done directly on your new machine. For that reason,
we will not be cloning this project code directly onto the target machine.
(Note that **git** is probably not installed yet.)

Project Documentation
=====================

The documentation for this project is available at
https://rblack42.github.io/ansible-clean-mac-setup. I use *Python Sphinx* as my
primary documentation system.

Issues
======

If you try this project out on your own system and run into any problems, please
use the **issue** tool on *GitHub* to let me know. I will try to fix any
problems discovered as soon as I can. 

Contributions
=============

If you would like to help with this project, please follow the **CONTRIBUTIONS**
note in this repository to get started. All such contributions will be noted in
the project documentation.
