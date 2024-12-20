Files API
=========

The `Files` API provides methods for uploading, retrieving, and deleting files, such as dispute evidence.


To initialize the `Files` class, use the following:

.. code-block:: python

    from files import Files
    from config import get_api_key

    files_api = Files(api_key=get_api_key(), mode='test')

Upload a File
-------------

Uploads a new file for a specified purpose.

**Usage Example**

.. code-block:: python

    response = files_api.upload_file(file_path="path/to/file.pdf", purpose="dispute_evidence")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "file_token_1",
            "purpose": "dispute_evidence",
            "created_at": "2023-10-01T10:00:00Z"
        },
        "status": 200
    }


Retrieve File Details
---------------------

Retrieves details of an uploaded file by its token.

**Usage Example**

.. code-block:: python

    response = files_api.get_file_details(file_token="file_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "response": {
            "token": "file_token_1",
            "purpose": "dispute_evidence",
            "file_name": "evidence.pdf",
            "created_at": "2023-10-01T10:00:00Z"
        },
        "status": 200
    }


Delete a File
-------------

Deletes a file by its token.

**Usage Example**

.. code-block:: python

    response = files_api.delete_file(file_token="file_token_1")
    print(response)

**Response Example**

.. code-block:: json

    {
        "status": 204
    }

.. tip:: Learn More

    To learn more about files functionality, refer to: :mod:`pin_payments.files`