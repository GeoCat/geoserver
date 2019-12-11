Installation
============

Java Runtime Environment
------------------------

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is very enthusiastic about this change, and we are pleased to see OpenJDK supported by a number of different distributions.

GeoServer Enterprise required a Java 8 runtime Environment.

* Linux Environment. Recommend use OpenJDK 8 provided by your Linux distribution.
* Windows and MacOS environment: Prebuilt OpenJDK binaries are available from `AdoptOpenJDK <https://adoptopenjdk.net>`__

.. tip: Oracle customers are welcome to continue using `Oracle JDK <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__ (keeping in mind that license terms have changed and this is no longer available free of chrage).

.. only:: premium
   
   .. note:: GeoServer Enterprise Premium customers may also make use of Java 11 at this time.

Apache Tomcat
-------------

`Apache Tomcat <https://tomcat.apache.org>`__ is the leading open source application server.

GeoServer Enterprise supports Apache Tomcat 8.5.x or 9.0.x.

#. Follow the installation instructions for your environment.

#. GeoServer Enterprise java virtual machine runtime parameters.
   
   * Linux and macOS :download:`setenv.sh <files/setenv.sh>`:
   
     .. literalinclude:: files/setenv.sh
        :language: shell
   
   * Windows :download:`setup.bat <files/setenv.bat>`:
     
     .. literalinclude:: files/setenv.bat
        :language: batch
      
.. only:: premium

   .. note:: GeoServer Enterprise Premium customers may also make use of their own application server.
  
      When making use of your own application server please pay special attention to the JVM options required for the GeoServer application.

Writing Guide
=============

Lists
-----

There are two types of lists, bulleted lists and numbered lists. A bulleted list looks like this:

* An item
* Another item
* Yet another item

This is accomplished with the following code:

.. code-block:: rst

   * An item
   * Another item
   * Yet another item

A numbered list looks like this:

#. First item
#. Second item
#. Third item

This is accomplished with the following code:

.. code-block:: rst

   #. First item
   #. Second item
   #. Third item

.. hint:: Note that numbers are automatically generated, making it easy to add/remove items.


List-tables
-----------

Bulleted lists can sometimes be cumbersome and hard to follow.  When dealing with a long list of items, use list-tables.  For example, to talk about a list of options, create a table that looks like this:

.. list-table::
   :widths: 20 80
   :header-rows: 1
   
   * - Shapes
     - Description
   * - Square
     - Four sides of equal length, 90 degree angles
   * - Rectangle
     - Four sides, 90 degree angles
    
This is done with the following code::

   .. list-table::
      :widths: 20 80
      :header-rows: 1
      
      * - Shapes
        - Description
      * - Square
        - Four sides of equal length, 90 degree angles
      * - Rectangle
        - Four sides, 90 degree angles

Notes and warnings
------------------

.. Attention:: Directives at large.

.. Caution:: Don't take any wooden nickels.

.. DANGER:: Mad scientist at work!

.. Error:: Does not compute.

.. Hint:: It's bigger than a bread box.

.. Important::
   - Wash behind your ears.
   - Clean up your room.

     - Including the closet.
     - The bathroom too.

       - Take the trash out of the bathroom.
       - Clean the sink.
   - Call your mother.
   - Back up your data.

.. Note:: This is a note.
   Equations within a note:
   :math:`G_{\mu\nu} = 8 \pi G (T_{\mu\nu}  + \rho_\Lambda g_{\mu\nu})`.

.. Tip:: 15% if the service is good.

    +---------+
    | Example |
    +=========+
    | Thing1  |
    +---------+
    | Thing2  |
    +---------+
    | Thing3  |
    +---------+

.. WARNING:: Strong prose may provoke extreme mental exertion.
   Reader discretion is strongly advised.

Images & Figures
----------------

Images
^^^^^^

An image example:

.. image:: img/example.jpg

Figures
^^^^^^^

.. figure:: img/example.jpg
   :alt: reStructuredText, the markup syntax

   A figure is an image with a caption and/or a legend:

Blocks
======

Literal Blocks
--------------

Literal blocks are indicated with a double-colon ("::") at the end of
the preceding paragraph (over there ``-->``).  They can be indented::

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None

Or they can be quoted without indentation::

>> Great idea!
>
> Why didn't I think of that?

Line Blocks
-----------

You can use line blocks, but block quotes are easier.

| This is a line block. It ends with a blank line.
|     Each new line begins with a vertical bar ("|").
|     Line breaks and initial indents are preserved.
| Continuation lines are wrapped portions of long lines;
  they begin with a space in place of the vertical bar.
|     The left edge of a continuation line need not be aligned with
  the left edge of the text above it.

| This is a second line block.
|
| Blank lines are permitted internally, but they must begin with a "|".

Take it away, Eric the Orchestra Leader!

    | A one, two, a one two three four
    |
    | Half a bee, philosophically,
    |     must, *ipso facto*, half not be.
    | But half the bee has got to be,
    |     *vis a vis* its entity.  D'you see?
    |
    | But can a bee be said to be
    |     or not to be an entire bee,
    |         when half the bee is not a bee,
    |             due to some ancient injury?
    |
    | Singing...

Block Quotes
------------

Block quotes consist of indented body elements:

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

Doctest Blocks
--------------

>>> print 'Python-specific usage examples; begun with ">>>"'
Python-specific usage examples; begun with ">>>"
>>> print '(cut and pasted from interactive Python sessions)'
(cut and pasted from interactive Python sessions)

Code Blocks
-----------

.. parsed-literal::

    # parsed-literal test
    curl -O http://someurl/release-|version|.tar-gz


.. code-block:: json
    :caption: Code Blocks can have captions.

    {
    "windows": [
        {
        "panes": [
            {
            "shell_command": [
                "echo 'did you know'",
                "echo 'you can inline'"
            ]
            },
            {
            "shell_command": "echo 'single commands'"
            },
            "echo 'for panes'"
        ],
        "window_name": "long form"
        }
    ],
    "session_name": "shorthands"
    }

Emphasized lines with line numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   :linenos:
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

References
==========

Footnotes
---------

.. [1] A footnote contains body elements, consistently indented by at
   least 3 spaces.

   This is the footnote's second paragraph.

.. [#label] Footnotes may be numbered, either manually (as in [1]_) or
   automatically using a "#"-prefixed label.  This footnote has a
   label so it can be referred to from multiple places, both as a
   footnote reference ([#label]_) and as a hyperlink reference
   (label_).

.. [#] This footnote is numbered automatically and anonymously using a
   label of "#" only.

.. [*] Footnotes may also use symbols, specified with a "*" label.
   Here's a reference to the next footnote: [*]_.

.. [*] This footnote shows the next symbol in the sequence.

.. [4] Here's an unreferenced footnote, with a reference to a
   nonexistent footnote: [5]_.

Citations
---------

.. [11] This is the citation I made, let's make this extremely long so that we can tell that it doesn't follow the normal responsive table stuff.

.. [12] This citation has some ``code blocks`` in it, maybe some **bold** and
       *italics* too. Heck, lets put a link to a meta citation [13]_ too.

.. [13] This citation will have two backlinks.


Here's a reference to the above, [12]_, and a [nonexistent]_ citation.

Here is another type of citation: `citation`

Glossary
--------

This is a glossary with definition terms for thing like :term:`Writing`:

.. glossary::
  
   Documentation
      Provides users with the knowledge they need to use something.

   Reading
      The process of taking information into ones mind through the use of eyes.

   Writing
      The process of putting thoughts into a medium for other people to :term:`read <Reading>`.

Targets
-------

.. _example:

This paragraph is pointed to by the explicit "example" target.
A reference can be found under `Inline Markup`_, above. `Inline
hyperlink targets`_ are also possible.

Section headers are implicit targets, referred to by name. See
Targets_, which is a subsection of `Body Elements`_.

Explicit external targets are interpolated into references such as "Python_".

.. _Python: http://www.python.org/

Targets may be indirect and anonymous.  Thus `this phrase`__ may also
refer to the Targets_ section.

__ Targets_

Here's a `hyperlink reference without a target`_, which generates an error.
