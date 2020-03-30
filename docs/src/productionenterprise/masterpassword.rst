Changing the master password
----------------------------

GeoServer has a root user configured with a master password. Changing that master password is recommended to avoid security issues.

It is also recommened to change setup the master password before you edit any other of the security setting in yous Geoserver instance.

To change the master password, follow these steps:

1. Go to the GeoServer administration web page at `[your GeoServer root url]/web` (for instance: `http://localhost:8080/geoserver/web`)

	.. figure:: img/geoserverlandpage.png
		:alt: GeoServer administration web page

2. Login using the :guilabel: login fields in the upper part of the page.

	.. figure:: img/loginfields.png
		:alt: Login fields

	Use :kbd:`admin` as username and :kbd:`geoserver` as password.

3. Click on the :guilabel:`Passwords` link. 

	.. figure:: img/passwordslink.png
		:alt: Passwords link

4. In the page that will appear, click on the :guilabel:`Change password` link.

	.. figure:: img/changepasswordlink.png
		:alt: Change password link		

4. Enter :kbd:`geoserver` in the :guilabel:`Current password` field. Enter your new password in the two remaining fields.

	.. figure:: img/changepassword.png
		:alt: `admin` user configuration link

5. Click on :guilabel:`Change Password` to set the new master password.
