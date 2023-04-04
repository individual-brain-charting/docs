MRI-data organization
=====================

The tree structure of the IBC dataset follows BIDS Specification
(`http://bids.neuroimaging.io/ <http://bids.neuroimaging.io/>`__.), as in the `figure below <bids_>`__.

-  The identifiers of the 13 participants are "sub-01", "sub-02",
   "sub-04", ..., "sub-15".

-  The acquisitions are organized in sessions ("ses-00", "ses-01", ..., "ses-20", etc.).

-  Within each session, data is divided according to modality: "anat", "dwi", "fmap", "func".

-  For each modality, files are stored in .nii.gz format, with a name that recapitulates subject, session and modality together with meta-information stored in .tsv and .json files.

.. _bids:

.. figure:: ibc_bids.png
   :alt: **Imaging modalities employed in each session.**

   **Imaging modalities employed in each session.**
