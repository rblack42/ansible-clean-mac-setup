Unpacking the Standard Homebrew Install Script
##############################################

..	literalinclude::	../../refs/install.sh
    :linenos:
    :lines: 1-6

This code may be used in the **homebrew** development environment. The comments
are ignored when actually in use by a user.

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 7

This line tells the shell to treat undefined variables as an error

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 9-11

This is a general purpose abort function that displays a message as it aborts
the installation.

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 14-40

Check the environment variables to make sure we are running properly. This code
is not needed in the *ansible* code.

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 42-77

All of the above code is designed to enhance the outputs of the script. This
code has nothing to do with the actual installation.

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 79-130

This block of code checks to see how the script is being run. It ends by setting
**USER** to the system account name of the user who runs the script. That user
should have **sudo** privileges, and the script will ask for the password when
it is needed.

At this point the real work of the installer begins. The first thing done is to
check to see if the installer is running on Mac or Linux. You can install on
Intel or Arm64 Mac systems, and Intel systems for Linux.

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 132-142

For Mac installs, the script checks to see if the machine is a new, Apple
Silicon machine. If so, it is based on **arm64** and not Intel **x86-64**. This
determines where *Homebrew* will be installed.

The key variable set here is **HOMEBREW_PREFIX**, which we will need to set as a
variable in the *Ansible role. Note that the Homebrew repository, which we will
have to clone from *GitHub*, is located in the **HOMEBREW_REPOSITORY**
directory.

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 144-161

This block sets up the location of the installation, defined by
**HOMEBREW_PREFIX**.

This next block sets up shortcuts used to set owner and group for files
installed later. 

This same block is repeated in case the installation is on a Linux machine:

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 163-187

Next, we set the locations of the Homebrew repositories:

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 188-189

With these definitions in place, the locations of the repositories are set as
environment variables:

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 191-203

Homebrew currently is supported for versions 13.0 through 16.0:

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 213-214

Apparently, analytics are collected in development. They are turned off during
user installs:

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 217-218

Since sudo access is required for the instalation, the next block sets up a
function that make sure this capability is available:

..  literalinclude::    ../../refs/install.sh
    :linenos:
    :lines: 220-254







