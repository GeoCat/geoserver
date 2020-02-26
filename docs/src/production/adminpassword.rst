Changing the default admin password
------------------------------------

GeoServer has a predefined admin user, which can be used to access GeoServer with full administration priviledges. The default password for the `admin` user must be changed to avoid unauthorized access to your GeoServer instance. To change the password of the `admin` user, follow these steps:

1. Go to the GeoServer administration web page at `[your GeoServer root url]/web` (for instance: `http://localhost:8080/geoserver/web`)

	.. figure:: img/geoserverlandpage.png
		:alt: GeoServer administration web page

2. Login using the login fields in the upper part of the page.

	.. figure:: img/loginfields.png
		:alt: Login fields

	Use :kbd:`admin` as username and :kbd:`geoserver` as password.

3. Click on the :guilabel:`Groups, users, roles` menu link. 

	.. figure:: img/userslink.png
		:alt: User, groups and roles link

4. In the page that will appear, move to the :guilabel:`Users/Groups` section.

	.. figure:: img/userstab.png
		:alt: User, groups and roles page

	You will see the following content.

	.. figure:: img/userspage.png
		:alt: Users/Groups content

4. Click on the :guilabel:`admin` username to edit its properties. The following page will open.

	.. figure:: img/userconfpage.png
		:alt: `admin` user configuration page

5. Type in the new password to use for the `admin` user.

6. Click on :guilabel:`Save` to save your changes.