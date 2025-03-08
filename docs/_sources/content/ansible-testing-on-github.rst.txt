Ansible Testing on Github
#########################

..	include:: /header.inc

|GH| provides an easy way to run tests against a project every time you push
changes to their server. *Github Workflows* define the testing process. These
are placed in a **.github/workflows** directory in your project. IN this note we
will examine the workflow |JG| put together for his **mac-dev-playbook**

A *workflow* is a simple *YAML* script stored in the **workflows** subdirectory.
Jeff created two such files: **ci.yml** and **stale.yml**. 

Continuous Integration
======================

The **ci.yml** file 
