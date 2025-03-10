Document Comments
===============

This section provides an overview of the document comment-related methods available in the NextGuild library. The following methods are used to interact with document comments:

create_doc_comment
------------------

.. code-block:: python

    create_doc_comment(channelid, docid, content=None, embed=None)

Creates a comment on a document.

+-------------+--------+----------------------------------------+
| Parameter   | Type   | Description                            |
+=============+========+========================================+
| channelid   |str     | The ID of the channel the doc is in.   |
+-------------+--------+----------------------------------------+
| docid       |int     | The ID of the document to comment on.  |
+-------------+--------+----------------------------------------+
| content     |str,    | The content of the comment.            |
|             |optional|                                        |
+-------------+--------+----------------------------------------+
| embed       |Embed,  | The embed of the comment.              |
|             |optional|                                        |
+-------------+--------+----------------------------------------+

update_doc_comment
------------------

.. code-block:: python

    update_doc_comment(channelid, docid, commentid, content=None, embed=None)

Updates a document comment.

+-------------+--------+-----------------------------------------+
| Parameter   | Type   | Description                             |
+=============+========+=========================================+
| channelid   |str     | The ID of the channel the doc is in.    |
+-------------+--------+-----------------------------------------+
| docid       |int     |The ID of the document the comment is in.|
+-------------+--------+-----------------------------------------+
| commentid   |int     | The ID of the comment to update.        |
+-------------+--------+-----------------------------------------+
| content     |str,    | The new content of the comment.         |
|             |optional|                                         |
+-------------+--------+-----------------------------------------+
| embed       |Embed,  | The new embed of the comment.           |
|             |optional|                                         |
+-------------+--------+-----------------------------------------+

delete_doc_comment
------------------

.. code-block:: python

    delete_doc_comment(channelid, docid, commentid)

Deletes a document comment.

+-------------+--------+-----------------------------------------+
| Parameter   | Type   | Description                             |
+=============+========+=========================================+
| channelid   |str     | The ID of the channel the doc is in.    |
+-------------+--------+-----------------------------------------+
| docid       |int     |The ID of the document the comment is in.|
+-------------+--------+-----------------------------------------+
| commentid   |int     | The ID of the comment to delete.        |
+-------------+--------+-----------------------------------------+
