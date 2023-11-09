

Installing NGINX Plus
=====================

Introduction
------------

NGINX Plus is supported on Amazon Linux, CentOS, Debian, FreeBSD, Oracle
Linux, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server
(SLES), and Ubuntu.

For sizing guidance on Deploying NGINX Plus, see `Sizing Guide for
Deploying NGINX Plus on Bare Metal
Servers <https://www.nginx.com/resources/datasheets/nginx-plus-sizing-guide/>`__

Prerequisites
-------------

Before being able to use NGINX Plus you will need the following:

- An NGINX Plus subscription
- A supported operating system 
- Your credentials to the NGINX Plus Customer Portal
- Your NGINX Plus certificate and public key

.. note:: The prerequisites have been completed for you in this lab

.. seealso:: Official installing NGINX documentation:
   `Installing NGINX Plus 
   <https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-plus/>`_

   Official NGINX App Protect documentation:
   `App Protect Module
   <https://docs.nginx.com/nginx-app-protect-waf/admin-guide/install/#ubuntu-1804--ubuntu-2004--ubuntu-2204-installation/>`_
   
   Official NGINX GeoIP2 documentation:
   `GeoIP2 Module 
   <https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-plus/>`_

Learning Objectives
-------------------

By the end of the lab you will be able to:

-  Install NGINX Plus
-  Install a NGINX Plus Dynamic Module
-  Verify Installation
-  Invoke NGINX and common options from from the command line

Exercise 1: Install NGINX Plus
------------------------------

#. In the **WORKSPACE** folder found on the desktop, open the
   **NGINX-PLUS-3** workspace by double clicking the NGINX-PLUS-3 file.  This will start an instance of Visual Studio Code.

   **Select Workspace**

   .. image:: ./images/2020-06-29_20-56.png

   If you are prompted **Are you sure you want to continue?** Select
   **continue**

   .. image:: ./images/2020-06-29_20-57.png

#. In VSCode, open a terminal window by selecting **View > Terminal.** 
   You will now be able to both run NGINX commands and edit NGINX Plus
   configuration files via the VSCode Console and terminal.

   .. image:: ./images/2020-06-29_21-01.png

   .. note:: Terminal will appear on the bottom portion of the VSCode window.
   
   .. image:: ./images/vscode.png
      :width: 1000 px

#. In the terminal run the following commands to install NGINX Plus

   a. Confirm you are root
 
      .. code:: bash

         whoami
   
   b. Move to the /root directory and check that the nginx-repo.crt and 
      nginx-repo.key files are present.

      .. code:: bash

         cd /root 
         ls

   c. Run installation commands
      

      Update Packages

      .. code:: bash

         apt-get update
      
      Create NGINX directory

      .. code:: bash

         mkdir -p /etc/ssl/nginx
         cp nginx-repo.* /etc/ssl/nginx

      Install Signing Prerequisites

      .. code:: bash

         wget https://cs.nginx.com/static/keys/nginx_signing.key && sudo apt-key add nginx_signing.key
         wget https://cs.nginx.com/static/keys/app-protect-security-updates.key && sudo apt-key add app-protect-security-updates.key
         apt-get install -y apt-transport-https lsb-release ca-certificates wget gnupg2 ubuntu-keyring

      Download and add NGINX signing key and App Protect security updates signing key

      .. code:: bash

         wget -qO - https://cs.nginx.com/static/keys/nginx_signing.key | gpg --dearmor | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
         wget -qO - https://cs.nginx.com/static/keys/app-protect-security-updates.key | gpg --dearmor | sudo tee /usr/share/keyrings/app-protect-security-updates.gpg >/dev/null

      Add the NGINX Plus and App Protect repository

      .. code:: bash

         printf "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] https://pkgs.nginx.com/plus/ubuntu `lsb_release -cs` nginx-plus\n" | sudo tee /etc/apt/sources.list.d/nginx-plus.list
         printf "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] https://pkgs.nginx.com/app-protect/ubuntu `lsb_release -cs` nginx-plus\n" | sudo tee /etc/apt/sources.list.d/nginx-app-protect.list
         printf "deb [signed-by=/usr/share/keyrings/app-protect-security-updates.gpg] https://pkgs.nginx.com/app-protect-security-updates/ubuntu `lsb_release -cs` nginx-plus\n" | sudo tee /etc/apt/sources.list.d/app-protect-security-updates.list

      Download the apt configuration

      .. code:: bash

         wget -P /etc/apt/apt.conf.d https://cs.nginx.com/static/files/90pkgs-nginx
      
      Update Packages

      .. code:: bash

         apt-get update
      
      Install NGINX Plus

      .. code:: bash

         apt-get install -y nginx-plus

#. Verify the version of NGINX Plus that was installed:

   .. code:: bash

      nginx -v

#. Install the NGINX Plus App Protect

   .. code:: bash

      apt-get install -y app-protect

   .. note:: 
      
      Installing **NGINX App-Protect** installs **NGINX-Plus**. 
      Seperated installation was for lab demonstration purposes only.

   .. note::

      In the output of the previous command view the instructions to enable
      the module via the NGINX config. **We will do this later:**

      ``The App Protect module for NGINX Plus have been installed. 
      To enable these modules, add the following to /etc/nginx/nginx.conf 
      and reload nginx:`` 

         **load_module modules/ngx_http_app_protect_module.so;** 

#. Install the NGINX Plus GeoIP2 Dynamic Module

   .. code:: bash

      apt-get -y install nginx-plus-module-geoip2 

   .. note::

      In the output of the previous command view the instructions to enable
      the module via the NGINX config. **We will do this later:**

      ``The 3rd-party GeoIP2 dynamic modules for NGINX Plus have been installed. 
      To enable these modules, add the following to /etc/nginx/nginx.conf 
      and reload nginx:`` 

         **load_module modules/ngx_http_geoip2_module.so;** 
            
         **load_module modules/ngx_stream_geoip2_module.so;**

      Please refer to the module documentation for further details:

      https://github.com/leev/ngx_http_geoip2_module

#. Start NGINX Plus

   .. code:: bash

      systemctl start nginx 

#. Verify that NGINX Plus has started

   .. code:: bash

      systemctl status nginx 

#. Test the NGINX Plus instance in your browser. Open **Google Chrome** from 
   your Desktop and enter the following URL, http://nginx-plus-3. 
   
   You should see the NGINX default page:

   .. image:: ./images/2020-06-26_12-33.png

Exercise 2: NGINX Plus command line basics
------------------------------------------

In this exercise, we will review and configure NGINX Plus as a basic load
balancer and test/verify configured functionality.

#. If you have closed VSCode, once again, open the **WORKSPACE** folder found on
   the desktop, double click the **NGINX-PLUS-3** workspace shortcut to open Visual Studio
   Code.

   .. image:: ./images/2020-06-29_20-56.png

   .. image:: ./images/vscode.png
      :width: 1000 px

#. In VSCode, open a **terminal window**, using **View > Terminal menu** 
   command. You will now be able to both run NGINX commands and edit NGINX Plus
   configuration files via the VSCode Console and terminal.

#. In the terminal try running the following NGINX commands and inspect
   the output (output won't be listed in below):

   Print help for command-line parameters

   .. code:: bash

      nginx -h 
   
   Test the configuration file: 
   
   NGINX checks the configuration for correct syntax, and then tries to open 
   files referred in the configuration.
      
   .. code:: bash

      nginx -t

   same as -t, but additionally dump configuration files to standard output

   .. code:: bash
      
      nginx -T 
      
      
   print the NGINX version

   .. code:: bash

      nginx -v
      
   print the NGINX version, compiler version, and configure parameters.
      
   .. code:: bash
      
      nginx -V 
 
   send a signal to the master process. The argument signal can be one of:

   - stop — shut down quickly
   - quit — shut down gracefully
   - reload — reload configuration, start the new worker process with a new
     configuration, gracefully shut down old worker processes.
   - reopen — reopen log files
      
   .. code:: bash
      
      nginx -s reload 

Exercise 3: Inspect NGINX Plus modules
--------------------------------------

Now that NGINX Plus is installed, browse to the NGINX configuration root,
**/etc/nginx**

#. **File > Open Folder...**

   .. image:: ./images/2020-06-29_15-47.png

#. Enter **/etc/nginx** in the open folder menu the click **OK**

   .. image:: ./images/2020-06-29_21-07.png
      :width: 1000 px


#. Select the **nginx.conf** file in the VSCode Explorer section.

#. To enable modules for NGINX Plus that have been
   installed, add the following lines to **/etc/nginx/nginx.conf** in the
   **main context** and **reload nginx**:

   .. code:: nginx

      load_module modules/ngx_http_app_protect_module.so;
      load_module modules/ngx_http_geoip2_module.so; 
      load_module modules/ngx_stream_geoip2_module.so;

   
   For example, it may look like this:

   .. image:: ./images/modules.png

   To enabled App Protect, additional updates will need to be made to **/etc/nginx/nginx.conf** 

   
   For example, it may look like this:

   .. image:: ./images/appprotect.png

#. In the terminal window select **File > Save** or use **ctrl+s** to save the
   file.

#. Open the terminal window again by selecting **View > Terminal** and in the 
   terminal window, run the following commands to reload nginx:

   .. code:: bash

      nginx -t && nginx -s reload

   .. image:: ./images/2020-06-29_21-13.png
      :width: 1000 px

#. See which Dynamic modules are installed:

   .. code:: bash

      cd /etc/nginx/modules  
      ls -al
