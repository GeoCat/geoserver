Master password
---------------

GeoServer uses a master password used to safely store security certificates. This password can optionally be used to login as the `root` user.

Recommendations:

* When upgrading you may receive a warning to change the master password from a historical default.

* When integrating with an external security system such as a LDAP it is recommended to enable `root` user login using the master password.

* When setting up GeoServer for the first time removing the generated :file:`masterpw.info` file is recommended to avoid security issues.

Remove master password has not been changed from the default warning
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#. When upgrading an early `GEOSERVER_DATA_DIRECTORY` setup you will be asked replace the default master password.
   
     The master password for this server has not been changed from the default. It is highly recommended that you change it now.

   Click :guilabel:`Change it` link to open the :guilabel:`Change Master Password` page.

   .. figure:: img/histroical_warning.png
      :width: 60%
      
      Change master password warning

#. Change the master password using:

   .. list-table::
      :widths: 30 70
      :width: 100%
      :stub-columns: 1
      
      * - Current password
        - :kbd:`geoserver`
      * - New Password
        - New password definition. Master password policy requires at least eight characters.
      * - Confirmation
        - Retype your new password

   .. figure:: img/change.png
      :alt: `admin` user configuration link
      
      Change master password

#. Press :guilabel:`Change Password` to set the new master password.  

Remove masterpw.info warning
''''''''''''''''''''''''''''

When the `GEOSERVER_DATA_DIR/security` folder is created a :file:`masterpw.info` is created for your referemce.

To remove the :file:`masterpw.info` file:

#. The :menuselection:`Welcome` page displays the following warning to administrators:
   
     Please read the file security/masterpw.info and remove it afterwards. This file is a *security risk*.
   
   .. figure:: img/masterpw_warning.png
      :width: 60%
      
      masterpw.info warning
   
#. Navigate to :menuselection:`Tools` page, and open :guilabel:`Resource browser`.
   
   .. figure:: img/tools.png
      
      Tools page

#. Select :file:`security/master.pw.info` and :guilabel:`Edit` to view the contents of the file.
   
   Make a note of this password for your records.

   The contents are generated when the :file:`security` folder is created, so your password will be different from the one shown below.
   
   .. figure:: img/masterpw.png
      :width: 70%
      
      Edit master.pw.info file
      
#. Select :file:`security/master.pw.info` and :guilabel:`Delete` to remove the file and address the warning on the welcome screen.
   
   .. figure:: img/masterpw_delete.png
      
      Delete master.pw.info file

Recover master password
'''''''''''''''''''''''

The master password can be written out to the filesystem:

#. Navigate to :menuselection:`Security > Passwords` page.

#. Click :guilabel:`Master password forgotten` link to open the *Dump master password* page.

  
   .. figure:: img/password_page.png
      
      Password page

#. Use the :guilabel:`Dump master password page` to define a file location to export the master password:
   
   .. list-table::
      :widths: 30 70
      :width: 100%
      :stub-columns: 1

      * - Filename:
        - :file:`/usr/local/geoserver-live/data/master.txt`
   
   .. figure:: img/filename.png
      
      Location to export master password

#. Press :guilabel:`Dump to file` to write the file out.

   .. figure:: img/review.png
      
      Master passport export

#. Use the :menuselection:`Tools > Resource browser` to select the :file:`master.txt` created above:
   
   * Use :guilabel:`Edit` to review the contents of the file and make a note of the master password.
   * Use :guilabel:`Delete` to remove this file when finished
   
   .. figure:: img/master.png
      
      Review and delete exported file

Change master password
''''''''''''''''''''''

To change the master password, follow these steps:

#. Navigate to :menuselection:`Security > Passwords` page.

#. Click the :guilabel:`Change password` link.
  
   .. figure:: img/password_page.png
      
      Password page

#. Change the master password using:

   .. list-table::
      :widths: 30 70
      :width: 100%
      :stub-columns: 1

      * - Current password
        - Current master password recorded from :file:`master.pw.info` or recovered to an exported file. 
      * - New Password
        - New password definition. Master password policy requires at least eight characters.
      * - Confirmation
        - Retype your new password

   .. figure:: img/change.png
      :alt: `admin` user configuration link
      
      Change master password

#. Press :guilabel:`Change Password` to set the new master password.

Enable root user login
''''''''''''''''''''''

To enable root user login:

#. Navigate to :menuselection:`Security > Passwords` page.

#. Locate the :guilabel:`Master Password Providers` table and select :guilabel:`default` from the list.

   .. figure:: img/password_provider.png
      
      Master password providers
      
#. Update the settings:

   .. list-table::
      :widths: 30 70
      :width: 100%
      :stub-columns: 1

      * - Allow "root" user to login as Admin
        - Selected

   .. figure:: img/default_settings.png
      
      Master password settings

#. Press :guilabel:`Save`

#. Press :guilabel:`Logout` button at the top of the screen, and use your paster password to login as `root`.

   .. list-table::
      :widths: 30 70
      :width: 100%
      :stub-columns: 1

      * - User name
        - root
      * - Password
        - Current master password recorded from :file:`master.pw.info` or recovered to an exported file. 

   .. figure:: img/root_login.png
      
      Login as root user