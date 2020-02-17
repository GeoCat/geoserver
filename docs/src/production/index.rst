Production
==========

The operations described in the following sections are required to setup GeoServer enterprise in order to be used in a production environment.

Changing the default admin password
------------------------------------

GeoServer has a predefined admin user, which can be used to access GeoServer with full administration priviledges. The default password for the `admin` user must be changed to avoid unauthorized access to your GeoServer instance. To change the password of the `admin` user, follow these steps:

	1. Go to the GeoServer administration web page at `[your GeoServer root url]/web` (for instance: `http://localhost:8080/geoserver/web)

		.. figure:: img/geoserverlandpage.png
			:alt: GeoServer administration web page

	2. Login using the :menuselection: login fields in the upper part of the page.
	
		.. figure:: img/loginfields.png
			:alt: Login fields

		Use :kbd:`admin` as username and :kbd:`geoserver` as password.

	3. Click on the :menuselection:`Groups, users, roles` menu link. 

		.. figure:: img/userslink.png
			:alt: User, groups and roles link

	4. In the page that will appear, move to the :menuselection:`Users/Groups` section.

		.. figure:: img/userstab.png
			:alt: User, groups and roles page

		You will see that following content.

		.. figure:: img/userspage.png
			:alt: Users/Groups content

	4. Click on the `admin` username to edit its properties.

		.. figure:: img/adminuser.png
			:alt: `admin` user configuration link

		The following page will open.

		.. figure:: img/userconfpage.png
			:alt: `admin` user configuration page

	5. Type in the new password to use for the `admin` user.

	6. Click on :menuselection:`Save` to save your changes.


Changing the master password
----------------------------

GeoServer has a root user configured with a master password. Changing that master password is also recommended to avoid security issues.

	1. Go to the GeoServer administration web page at `[your GeoServer root url]/web` (for instance: `http://localhost:8080/geoserver/web)

		.. figure:: img/geoserverlandpage.png
			:alt: GeoServer administration web page

	2. Login using the :menuselection: login fields in the upper part of the page.
	
		.. figure:: img/loginfields.png
			:alt: Login fields

		Use :kbd:`admin` as username and :kbd:`geoserver` as password.

	3. Click on the :menuselection:`Passwords` menu link. 

		.. figure:: img/passwordslink.png
			:alt: Passwords link

	4. In the page that will appear, click on the :menuselection:`Change password` link.

		.. figure:: img/changepasswordlink.png
			:alt: Change password link		

	4. Enter :kbd:`geoserver` in the :guilabel:`Current password` field. Enter your new password in the two remaining fields.

		.. figure:: img/changepassword.png
			:alt: `admin` user configuration link

	5. Click on :menuselection:`Change Password` to set the new master password.


Configure the Marlin renderer
-------------------------------


References:

* :ref:`production`