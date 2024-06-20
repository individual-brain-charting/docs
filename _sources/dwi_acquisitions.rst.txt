Diffusion-weighted Imaging
==========================

Acquisition parameters
~~~~~~~~~~~~~~~~~~~~~~

Three types of diffusion sequences were employed in three different
sessions, respectively:

-  High-resolution (1.3mm isotropic, 60 directions) acquisitions with
   :math:`B=1500` or :math:`B=3000`.

.. _higresdiff:

.. table:: Acquisition parameters for high-resolution diffusion imaging.

   ========================= ===========================
   Parameter                 Value
   ========================= ===========================
   *Sequence*                diff_dw60_TE76
   *TR*                      7000 ms
   *TE*                      76 ms
   *Flip angle*              90 deg
   *Refocusing flip angle*   180 deg
   *FOV*                     240 mm
   *Slice thickness*         1.30 mm
   *Number of slices*        112 slices
   *GRAPPA iPAT*             2
   *Multiband accel. factor* 2
   *Echo spacing*            0.71 ms
   *BW*                      1598 Hz/Px
   *Phase partial Fourier*   6/8
   *b-values*                [1500, 3000] s/mm\ :sup:`2`
   ========================= ===========================

-  Multi-shell (1.3mm isotropic, 20 directions) acquisitions for
   multiple B-values ranging from 300 to 3000 in steps of 300.

.. _multishelldiff:

.. table:: Acquisition parameters for multi-shell diffusion imaging.

   ========================= ============================================
   Parameter                 Value
   ========================= ============================================
   *Sequence*                diff_dw26_TE76
   *TR*                      7000 ms
   *TE*                      76 ms
   *Flip angle*              90 deg
   *Refocusing flip angle*   180 deg
   *FOV*                     240 x 240 mm
   *Matrix*                  128 x 128
   *Slice thickness*         1.30 mm, 112 slices, 1.30 mm isotropic
   *Multiband accel. factor* 2
   *Echo spacing*            0.71 ms
   *BW*                      1598 Hz/Px
   *Phase partial Fourier*   6/8
   *b-values*                [0, 300, 600, 900, 1200, 1500,
   \                         1800, 2100, 1400, 2700, 3000] s/mm\ :sup:`2`
   ========================= ============================================

-  Two low-resolution acquisitions (2mm, 20 directions) used for screening.

.. _screeningdiff:

.. table:: Acquisition parameters for screening.

   ========================= =========================
   Parameter                 Value
   ========================= =========================
   *Sequence*                diff_screening_2mmiso
   *TR*                      9000 ms
   *TE*                      66,00 ms
   *Flip angle*              90 deg
   *Refocusing flip angle*   180 deg
   *FOV*                     240 x 240 mm
   *Matrix*                  128 x 128
   *Slice thickness*         2 mm isotropic, 70 slices
   *Multiband accel. factor* 1
   *Echo spacing*            0,54 ms
   *BW*                      2192 Hz/Px
   *Phase partial Fourier*   6/8
   *b-values*                0, 1500 s/mm\ :sup:`2`
   ========================= =========================

.. table::

   ========================= ===========================
   Parameter                 Value
   ========================= ===========================
   *Sequence*                diff_dw20_MB
   *TR*                      5700 ms
   *TE*                      79,40 ms
   *Flip angle*              90 deg
   *Refocusing flip angle*   180 deg
   *FOV*                     240 x 240 mm
   *Matrix*                  160 x 160
   *Slice thickness*         1,5 mm isotropic, 94 slices
   *Multiband accel. factor* 2
   *Echo spacing*            0,65 ms
   *BW*                      1838 Hz/Px
   *Phase partial Fourier*   6/8
   *b-values*                0, 1500 s/mm\ :sup:`2`
   ========================= ===========================