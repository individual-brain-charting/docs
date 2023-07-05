Initial setup
================

Download the data
-----------------

All the data (raw images, preprocessed files, contrast map, etc.) are hosted online on
3 main platforms.

- **NeuroVault:** Click `here <https://neurovault.org/collections/6618/>`__ to access raw and preprocessed fMRI files.
- **OpenNeuro:** Click `here <https://openneuro.org/datasets/ds002685/versions/1.3.1>`__ to access raw and preprocessed fMRI files, along with task-specific information.
- **EBRAINS:** Click `here <https://search.kg.ebrains.eu/instances/8ddf749f-fb1d-4d16-acc3-fbde91b90e24>`__ to access preprocessed fMRI files, along with statistical contrast maps. Note that you must create an account, see the section below for more details.


API Installation
----------------

To facilitate data fetching with minimal coding, we've integrated powerful tools into
this `API <https://github.com/individual-brain-charting/api>`__.

To install the package containing the API, execute the following command:

.. raw:: html

.. code-block:: python
    :name: quick_install

    pip install git+https://github.com/individual-brain-charting/api.git#egg=ibc_api

This api is under active development, so make sure to update it regularly:

.. code-block:: python
    :name: quick_update

    pip install -U git+https://github.com/individual-brain-charting/api.git#egg=ibc_api

Get access with EBRAINS
-----------------------

The primary hosting platform for IBC data is `EBRAINS <https://search.kg.ebrains.eu/instances/c10859c9-536f-45c0-a1d1-442f79f2a66e>`__.
To access the data, an EBRAINS account is required. You can register for an account by clicking
`here <https://www.ebrains.eu/page/sign-up>`__.



