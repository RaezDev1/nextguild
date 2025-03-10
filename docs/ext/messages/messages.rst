Messages
========

This section provides an overview of the message-related methods available in the NextGuild library. The following methods are used to interact with channels and messages:

send_message
------------

.. code-block:: python

    send_message(channel_id, content, embed, isPrivate)

Send a message to the specified channel. Optionally, provide content and/or an embed.

+-------------+---------------+--------------------------------------------+
| Parameter   | Type          | Description                                |
+=============+===============+============================================+
| channel_id  | str           | The ID of the channel to send the message. |
+-------------+---------------+--------------------------------------------+
| content     | str, optional | The content of the message.                |
+-------------+---------------+--------------------------------------------+
| embed       | object,       | An embed object to be sent with the        |
|             | optional      | message.                                   |
+-------------+---------------+--------------------------------------------+
| isPrivate   | bool          | If the message should be private or not.   |
+-------------+---------------+--------------------------------------------+

send_reply
----------

.. code-block:: python

    send_reply(channel_id, content, replyids, embed, isPrivate)

Send a reply to a message in the specified channel.

+-------------+---------+-----------------------------------------+
| Parameter   | Type    | Description                             |
+=============+=========+=========================================+
| channel_id  | str     | The ID of the channel to send the reply.|
+-------------+---------+-----------------------------------------+
| content     | str     | The content of the reply.               |
+-------------+---------+-----------------------------------------+
| replyids    | list    | A list of message IDs to reply to.      |
+-------------+---------+-----------------------------------------+
| embed       | list    | An embed object to be sent with the     |
|             |         |    message                              |
+-------------+---------+-----------------------------------------+
| isPrivate   | bool    | If the message should be private or not.|
+-------------+---------+-----------------------------------------+

edit_message
------------

.. code-block:: python

    edit_message(channel_id, message_id, content, embed, isPrivate)

Edit an existing message in the specified channel.

+-------------+---------+-----------------------------------------+
| Parameter   | Type    | Description                             |
+=============+=========+=========================================+
| channel_id  | str     | The ID of the channel where the message |
|             |         | is.                                     |
+-------------+---------+-----------------------------------------+
| message_id  | str     | The ID of the message to edit.          |
+-------------+---------+-----------------------------------------+
| content     |optional,|     The updated content of the message. |
|             | str     |                                         |
+-------------+---------+-----------------------------------------+
| embed       |object,  | An embed object to be sent with         |
|             |optional |  the message                            |
+-------------+---------+-----------------------------------------+
| isPrivate   | bool    | If the message should be private or not.|
+-------------+---------------+-----------------------------------+

delete_message
--------------

.. code-block:: python

    delete_message(channel_id, message_id)

Delete a message in the specified channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channel_id  | str     | The ID of the channel where the message  |
|             |         | is.                                      |
+-------------+---------+------------------------------------------+
| message_id  | str     | The ID of the message to delete.         |
+-------------+---------+------------------------------------------+

get_message
-----------

.. code-block:: python

    get_message(channel_id, message_id)

Retrieve a specific message from a channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channel_id  | str     | The ID of the channel where the message  |
|             |         | is.                                      |
+-------------+---------+------------------------------------------+
| message_id  | str     | The ID of the message to retrieve.       |
+-------------+---------+------------------------------------------+

get_channel_messages
--------------------

.. code-block:: python

    get_channel_messages(channel_id, limit, before, after, includePrivate)

Retrieves a list of messages from a channel.

+----------------+----------------+-----------------------------------------------------------------+
| Parameter      | Type           | Description                                                     |
+================+================+=================================================================+
| channel_id     | str            | The ID of the channel to get messages from.                     |
+----------------+----------------+-----------------------------------------------------------------+
| limit          | int, optional  | The maximum number of messages to retrieve.                     |
+----------------+----------------+-----------------------------------------------------------------+
| before         | str, optional  | The message ID to start retrieving messages before.             |
+----------------+----------------+-----------------------------------------------------------------+
| after          | str, optional  | The message ID to start retrieving messages after.              |
+----------------+----------------+-----------------------------------------------------------------+
| includePrivate | bool, optional | Whether to include private messages in the retrieved messages.  |
+----------------+----------------+-----------------------------------------------------------------+

purge
-----

.. code-block:: python

    purge(channel_id, amount)

Purge a specified number of messages from a channel.

+-------------+---------+------------------------------------------+
| Parameter   | Type    | Description                              |
+=============+=========+==========================================+
| channel_id  | str     | The ID of the channel to purge messages  |
|             |         | from.                                    |
+-------------+---------+------------------------------------------+
| amount      | int     | The number of messages to purge.         |
+-------------+---------+------------------------------------------+
