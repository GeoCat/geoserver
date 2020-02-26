Configure disk quota for tile storage
-------------------------------------

By default, Geoserver can use as much space as needed to store cached tiles. This can cause issues, and it's recommended to set a limit to the amount of disk space that tiles can use.

Follow these steps to set a disk quota:

1. From the main page of the Geoserver web interface, click on the :guilabel:`Disk Quota` link.

	.. figure:: img/diskquota.png

2. Check the :guilabel:`Enable disk quota` check box.

	.. figure:: img/enablediskquota.png

3. The default space allocated for cached tiles is 500 MiB. If you want to set a different size, enter it in the :guilable:`Maximum tile cache size` box.

4. Click the :guilabel:`Submit` button to save your changes.