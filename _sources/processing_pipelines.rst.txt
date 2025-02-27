fMRI processing pipelines
=========================

fMRI preprocessing
------------------

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

Model specification
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

Model estimation
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
