DWI Preprocessing Pipeline
==========================

DWI Preprocessing 
-----------------

The DWI data were preprocessed using *MRtrix3* (`Tournier et al., 2019 <https://doi.org/10.1016/j.neuroimage.2019.116137>`__)
and *FSL* (`Smith et al., 2004 <http://doi.org/10.1016/j.neuroimage.2004.07.051>`__). The images were first denoised using the
Marchenko-Pastur PCA method (`Veraart et al., 2016 <https://doi.org/10.1016/j.neuroimage.2016.08.016>`__, `Cordero-Grande et
al. 2019 <https://doi.org/10.1016/j.neuroimage.2019.06.039>`__) implemented with the MRtrix :code:`dwidenoise` function. Then, to
correct the distortions due to inhomogeneities of the magnetic field,
FSL’s *topup* (`Andersson, Skare, and Ashburner 2003 <http://doi.org/10.1016/S1053-8119(03)00336-7>`__) and *eddy*
(`Andersson and Sotiropoulos 2016 <https://doi.org/10.1016/j.neuroimage.2015.10.019>`__) correction were used. The *topup*
method estimates the susceptibility-induced distortions of the subject's
head from the pairs of images with opposite distortion patterns (because
of acquisition with opposite phase-encoding directions -
anterior-to-posterior and posterior-to-anterior). This was followed by
*eddy* correction that corrects for eddy current-induced distortions,
which are a consequence of rapid switching of the diffusion gradients.
No bias field correction was done.

.. _subsubsec:fodtract:

Fiber Orientation Density Estimation and Tractography
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From this preprocessed data, the response functions (required for fiber
orientation density estimation) for each of white matter, grey matter,
and cerebro-spinal fluid tissue types were estimated using :code:`dwi2response
dhollander` the MRtrix implementation of the Dhollander algorithm
(`Dhollander et al., 2019 <https://archive.ismrm.org/2019/0555.html>`__). These derived response functions were then
used to estimate the amount of diffusion in three orthogonal directions
(known as fiber orientation density estimation) using multi-shell
multi-tissue constrained deconvolution method implemented under
:code:`dwi2fod` in MRtrix.

Then to seed the streamlines from the grey matter-white matter interface
in the next step, a mask of this grey matter-white matter boundary was
first generated using the high-resolution segmented T1 image with the
:code:`5tt2gmwmi` function in MRtrix. Finally, using this grey matter-white
matter boundary mask and the estimated white-matter fiber orientation
density, the second-order integration over fiber orientation
distributions (iFOD2) method (`Tournier et al., 2010 <https://archive.ismrm.org/2010/1670.html>`__) was used to estimate
the streamline tracts. For this, the MRtrix function :code:`tckgen`, was used
to generate :math:`10^{7}` streamlines with a maximum length of 250 mm
and the fiber orientation density amplitude cut-off set at 0.6.

.. _subsubsec:strucconn:

Structural Connectivity Estimation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These streamlines were then warped into the MNI152 space using *ANTs*
(`Avants et al., 2009 <https://psychiatry.ucsd.edu/research/programs-centers/snl/_files/ants2.pdf>`__) image registration described
`here <https://community.mrtrix.org/t/registration-using-transformations-generated-from-other-packages/2259>`__.
The structural connectivity matrix was then calculated for the warped
streamlines in MNI space for 400 parcels of the Schaefer atlas (`Schaefer et al., 2018 <https://doi.org/10.1093/cercor/bhx179>`__) using :code:`tck2connectome` from MRtrix. Each value in this
connectivity matrix was the sum of the contribution (SIFT2 weights
(`Smith et al., 2015 <https://doi.org/10.1016/j.neuroimage.2015.06.092>`__) calculated using :code: `tcksift2`) of each streamline
(between any two given parcels) to the overall fiber orientation density
and was normalized by the volume of the two parcels (using parameter
:code:`-scale_invnondevol` with :code:`tck2connectome`).