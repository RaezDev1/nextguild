Roles
=====


This section provides an overview of the role-related methods available in the NextGuild library. The following methods are used to interact with roles:


add_role
--------

.. code-block:: python

    add_role(serverid, userid, roleid)

Adds a role to a member in the specified server.

+-----------+------+--------------------------------------------------+
| Parameter | Type | Description                                      |
+===========+======+==================================================+
| serverid  | str  | The ID of the server where the member is located |
+-----------+------+--------------------------------------------------+
| userid    | str  | The ID of the member to add the role to          |
+-----------+------+--------------------------------------------------+
| roleid    | int  | The ID of the role to add                        |
+-----------+------+--------------------------------------------------+

remove_role
-----------

.. code-block:: python

    remove_role(serverid, userid, roleid)

Removes a role from a member in the specified server.

+-----------+------+--------------------------------------------------+
| Parameter | Type | Description                                      |
+===========+======+==================================================+
| serverid  | str  | The ID of the server where the member is located |
+-----------+------+--------------------------------------------------+
| userid    | str  | The ID of the member to remove the role from     |
+-----------+------+--------------------------------------------------+
| roleid    | int  | The ID of the role to remove                     |
+-----------+------+--------------------------------------------------+

member_has_role
-----------

.. code-block:: python

    member_has_role(serverid, userid, roleid)

Returns True if the specified member has the specified role.

+-----------+------+----------------------------------------------+
| Parameter | Type | Description                                  |
+===========+======+==============================================+
| serverid  | str  | The ID of the server                         |
+-----------+------+----------------------------------------------+
| userid    | str  | The ID of the member                         |
+-----------+------+----------------------------------------------+
| roleid    | int  | The ID of the role                           |
+-----------+------+----------------------------------------------+


get_member_roles
----------------

.. code-block:: python

    get_member_roles(serverid, userid)

Gets the roles of a member in the specified server.

+-----------+------+---------------------------------------------------+
| Parameter | Type | Description                                       |
+===========+======+===================================================+
| serverid  | str  | The ID of the server where the member is located  |
+-----------+------+---------------------------------------------------+
| userid    | str  | The ID of the member whose roles to fetch         |
+-----------+------+---------------------------------------------------+
