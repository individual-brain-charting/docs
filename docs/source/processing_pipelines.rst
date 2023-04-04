Processing pipelines
====================

fMRI Preprocessing Pipeline
---------------------------

Source data were preprocessed using *PyPreprocess*. This library offers
a collection of Python tools to facilitate pipeline runs, reporting and
quality check (https://github.com/neurospin/pypreprocess). It is built
upon the *Nipype* library (`Gorgolewski et al., 2011 <http://doi.org/10.3389/fninf.2011.00013>`__) v0.12.1, that in
turn launched various commands used to process neuroimaging data. These
commands were taken from the *SPM12* software package (Wellcome
Department of Imaging Neuroscience, London, UK) v6685, and the *FSL*
library (Analysis Group, FMRIB, Oxford, UK) v5.0.

All fMRI images, i.e. GE-EPI volumes, were collected twice with reversed
phase-encoding directions, resulting in pairs of images with distortions
going in opposite directions. Susceptibility-induced off-resonance field
was estimated from the two Spin-Echo EPI volumes in reversed
phase-encoding directions. The images were corrected based on the
estimated deformation model, using the *topup* tool (`Andersson, Skare,
and Ashburner 2003 <http://doi.org/10.1016/S1053-8119(03)00336-7>`__) implemented in FSL (`Smith et al., 2004 <http://doi.org/10.1016/j.neuroimage.2004.07.051>`__).

Further, the GE-EPI volumes were aligned to each other within each
participant. A rigid body transformation was employed, in which the
average volume of all images was used as reference (`Friston et al.,
1995 <https://doi.org/10.1006/nimg.1995.1019>`__). The mean EPI volume was also co-registered onto the corresponding
T1-weighted MPRAGE (anatomical) volume for every participant (`Ashburner
and Friston 1997 <https://doi.org/10.1006/nimg.1997.0290>`__). The individual anatomical volumes were then segmented
into tissue types to finally allow for the normalization of both
anatomical and functional data (`Ashburner and Friston 2005 <https://doi.org/10.1016/j.neuroimage.2005.02.018>`__). Concretely,
the segmented volumes were used to compute the deformation field for
normalization to the standard MNI152 space. The deformation field was
then applied to the EPI data. In the end, all volumes were resampled to
their original resolution, i.e. 1 mm isotropic for the
T1-weighted MPRAGE images and 1.5 mm for the EPI images.

.. _subsubsec:modelspec:

Model Specification
~~~~~~~~~~~~~~~~~~~

The fMRI data were analyzed using the *General Linear Model* (GLM).
Regressors of the model were designed to capture variations in BOLD
response strictly following stimulus timing specifications. They were
estimated through the convolution of temporal representations referring
to the task-conditions with the canonical *Hemodynamic Response
Function* (HRF), defined according to (`Friston, Fletcher, et al.,
1998 <http://doi.org/10.1006/nimg.1997.0306>`__) and (`Friston, Josephs, et al., 1998 <https://doi.org/10.1002/mrm.1910390109>`__).

The temporal profile of the conditions was characterized by boxcar
functions. To build such models, paradigm descriptors grouped in
triplets (i.e. onset time, duration and trial type according to BIDS
Specification) were determined from the log files' registries generated
by the stimulus-delivery software.

To account for small fluctuations in the latency of the HRF peak
response, additional regressors were computed based on the convolution
of the same task-conditions profile with the time derivative of the HRF.

Nuisance regressors were also added to the design matrix in order to
minimize the final residual error. To remove signal variance associated
with spurious effects arising from movements, six temporal regressors
were defined for the motion parameters. Further, the first five
principal components of the signal, extracted from voxels showing the 5%
highest variance, were also regressed to capture physiological noise
(`Behzadi et al., 2007 <https://doi.org/10.1016/j.neuroimage.2007.04.042>`__).

In addition, a discrete-cosine transform set was applied for high-pass filtering (cutoff = 128 seconds). Model specification was implemented using *Nistats* library v0.0.1b, a Python module devoted to statistical analysis of fMRI data (https://nistats.github.io), which leverages *Nilearn* (`Abraham et al., 2014 <https://doi.org/10.3389/fninf.2014.00014>`__), a Python library for statistical learning on neuroimaging data (https://nilearn.github.io/).

.. _subsubsec:modelest:

Model Estimation
~~~~~~~~~~~~~~~~

In order to restrict GLM parameters estimation to voxels inside
functional brain regions, a brain mask was extracted from the mean EPI
volume. The procedure implemented in the Nilearn software simply
thresholds the mean fMRI image of each subject in order to separate
brain tissue from background, and performs then a morphological opening
of the resulting image to remove spurious voxels.

Regarding noise modeling, a first-order autoregressive model was used in
the maximum likelihood estimation procedure.

A mass-univariate GLM fit was applied separately to the preprocessed
GE-EPI data of each run with respect to a specific task. Parameter
estimates pertaining to the experimental conditions were thus computed,
along with the respective covariance at every voxel. Various contrasts
(linear combinations of the effects), were then defined, referring only
to differences in evoked responses between either *(i)* two
conditions-of-interest or *(ii)* one condition-of-interest and baseline.
GLM estimation and subsequent statistical analyses were also implemented
using Nistats v0.1. fMRI data analysis was first run on unsmoothed data
and, afterwards, on data smoothed with a 5mm full-width-at-half-maximum
kernel. Such procedure allows for increased *Signal-to-Noise Ratio*
(SNR) and it facilitates between-image comparison.

DWI Preprocessing Pipeline
--------------------------

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