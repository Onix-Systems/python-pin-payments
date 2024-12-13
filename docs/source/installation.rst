Installation
============

To install the Python-Pin-Payments library, follow these steps:

1. **Install Poetry**

   Poetry is a tool for dependency management and packaging in Python. If Poetry is not already installed, follow the instructions on the Poetry website.

   .. code-block:: bash

      curl -sSL https://install.python-poetry.org | python3 -

2. **Create and Configure a New Project**

   .. code-block:: bash

      poetry new python-pin-payments-project
      cd python-pin-payments-project

3. **Activate the Virtual Environment**

   .. code-block:: bash

      poetry shell

4. **Add Python-Pin-Payments Library**

   If published on PyPI:

   .. code-block:: bash

      poetry add python-pin-payments

   If installing from source:

   .. code-block:: bash

      poetry add add git+https://github.com/Onix-Systems/python-pin-payments
