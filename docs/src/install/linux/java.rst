.. _Manual Linux Java Install:


Manual Linux Java Install
-------------------------

To manually install OpenJDK 8, follow these steps:

#. Navigate to the `AdoptOpenJDK download page <https://adoptopenjdk.net/releases.html>`_

#. Select :guilabel:`OpenJDK 8 (LTS)` as the version to download.

   .. figure:: img/openjdk8.png

#. Select :guilabel:`Linux` as your Operating System.

   .. figure:: img/openjdklinux.png

#. Select the corresponding architecture for your system in the :guilabel:`Architecture` field.

   .. figure:: img/openjdkarchitecturelinux.png

#. Click on the available JRE archive file download link for the above selected options, to download the OpenJDK prebuilt binary.

   .. figure:: img/openjdkdownloadlinklinux.png

#. In your system, create a folder called :file:`java` and :command:`cd` into it.

   .. todo: what is the "correct" location for this

#. Expand the downloaded file using the following command (adapt the filename according to the name of your downloaded file):

   .. code-block:: console

      $ tar -xf OpenJDK8U-jre_x64_linux_hotspot_8u242b08.tar.gz

#. Add Java to your PATH:

   .. code-block:: console

      $ export PATH=$PWD/jdk8u242-b08-jre/bin:$PATH

#. To ensure that Java is now correctly installed, open a console and type `java -version`. The output should look something like this:

   .. code-block:: console

      $ java -version
      openjdk version "1.8.0_242"
      OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_242-b08)
      OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.242-b08, mixed mode)

.. tip: Oracle customers are welcome to continue using `Oracle JDK <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__ (keeping in mind that license terms have changed and this is no longer available free of chrage).

.. only:: premium

   .. note:: GeoServer Enterprise Premium customers may also make use of Java 11 at this time.
