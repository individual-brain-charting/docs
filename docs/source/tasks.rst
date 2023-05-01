Tasks
=====

Apart from the MRI data, IBC is also a great resource for fMRI tasks. We have ran over 80 different tasks - gathered from our fellow researchers in the community - that altogether probe a large variety of cognitive domains in the human brain. The following figure depicts how much of the human brain cortex we have covered with these experiments. 

The codes and stimuli for all these tasks are openly available on the `individual-brain-charting/public_protocols <https://github.com/individual-brain-charting/public_protocols>`__ repository. Most of these were implemented with Python, MATLAB or Octave and are hence readily usable. However, some of them were originally implemented with proprietary softwares, and that was what we also used and have provided on the repo. You would still need to have access to these softwares to run those experiments. 

Below, you can find the paradigm descriptions, conditions, contrasts as well as the sample `stimulation videos <https://www.youtube.com/@individualbraincharting6314/videos>`__ for each of these tasks. To help you look for relevant tasks, we have also tagged each of them with some of the broad :bdg-primary:`cognitive_domains` they intend to probe. These tags are based on the definitions from `Cognitive Atlas <https://www.cognitiveatlas.org/concepts>`__.


ArchiStandard
-------------

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-success:`auditory_sentence_comprehension` :bdg-primary:`visual_arithmetic_processing` :bdg-primary:`vertical_checkerboard` :bdg-success:`auditory_arithmetic_processing` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: In-house custom-made sticks featuring one-top button, each one to be used in each hand

   - Audio device: MRConfon MKII

The ARCHI tasks are a battery of localizers comprising a wide range of psychological domains. The ArchiStandard task, described in (`Pinel et al., 2007 <https://doi.org/10.1186/1471-2202-8-91>`__ probes basic functions, such as button presses with the left or right hand, viewing horizontal and vertical checkerboards, reading and listening to short sentences, and mental computations (subtractions). Visual stimuli were displayed in four 250-ms epochs, separated by 100ms intervals (i.e., 1.3s in total). Auditory stimuli were generated from a recorded male voice (i.e., a total of 1.6s for motor instructions, 1.2-1.7s for sentences, and 1.2-1.3s for subtraction). The auditory or visual stimuli were shown to the participants for passive viewing or button response in event related paradigms. Informal inquiries undertaken after the MRI session confirmed that the experimental tasks were understood and followed correctly.

The conditions for this task are described in `this table <condArchiStandard_>`__ and the main contrasts derived from those conditions are described in `this table <contArchiStandard_>`__.

.. dropdown:: Conditions for ArchiStandard
   :name: condArchiStandard

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - video_left_button_press
        - Left-hand three-times button press, indicated by visual instruction
      * - video_right_button_press
        - Right-hand three-times button press, indicated by visual instruction
      * - horizontal_checkerboard
        - Visualization of flashing horizontal checkerboards
      * - vertical_checkerboard
        - Visualization of flashing vertical checkerboards
      * - audio_sentence
        - Listen to narrative sentences
      * - video_sentence
        - Read narrative sentences
      * - audio_computation
        - Mental subtraction, indicated by auditory instruction
      * - video_computation
        - Mental subtraction, indicated by visual instruction

.. dropdown:: Contrasts for ArchiStandard
   :name: contArchiStandard

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - video_left_button_press
        - left hand button presses upon video instructions
      * - video_right_button_press
        - right hand button presses upon video instructions
      * - audio_left_button_press
        - left hand button presses upon audio instructions
      * - audio_right_button_press
        - right hand button presses upon audio instructions
      * - left-right_button_press
        - left vs. right hand button press
      * - right-left_button_press
        - right vs. left hand button press
      * - horizontal_checkerboard
        - watch horizontal checkerboard
      * - vertical_checkerboard
        - watch vertical checkerboard
      * - horizontal-vertical
        - horizontal vs. vertical checkerboard
      * - vertical-horizontal
        - vertical vs. horizontal checkerboard
      * - video_sentence
        - read narrative sentence
      * - audio_sentence
        - listen to narrative sentence
      * - video_computation
        - mental subtraction upon video instruction
      * - audio_computation
        - mental subtraction upon audio instruction
      * - sentences
        - read or listen to sentences
      * - computation
        - mental subtraction
      * - sentences-computation
        - sentence reading vs. mental subtraction 
      * - computation-sentences
        - mental subtraction vs. sentence reading
      * - reading-listening
        - reading sentence vs. listening to sentence
      * - listening-reading
        - listening to sentence vs. reading a sentence
      * - reading-checkerboard
        - read sentence vs. checkerboard
      * - cognitive-motor
        - narrative/computation vs. button presses
      * - motor-cognitive
        - button presses vs. narrative/computation

ArchiSpatial
------------

.. container:: tags

   :bdg-light:`hand_chirality_recognition` :bdg-primary:`visual_body_recognition` :bdg-warning:`saccadic_eye_movement` :bdg-warning:`grasping` :bdg-primary:`visual_tool_recognition` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Audio device: MRConfon MKII

The ARCHI tasks are a battery of localizers comprising a wide range of psychological domains. ArchiSpatial includes the performance of (1) ocular saccade, (2) grasping and (3) orientation judgments on objects (the two different tasks were actually made on the same visual stimuli in order to characterize grasping-specific activity), (4) judging whether a hand photograph was the left or right hand or (5) was displaying the front or back. The same input stimuli were presented twice in order to characterize specific reponse to hand side judgment.

The conditions for this task are described in `this table <condArchiSpatial_>`__ and the main contrasts derived from those conditions are described in `this table <contArchiSpatial_>`__.

.. dropdown:: Conditions for ArchiSpatial
   :name: condArchiSpatial

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - saccades
        - Ocular movements were performed according to the displacement of a fixation cross from the center towards peripheral points in the image displayed
      * - rotation_hand
        - Mental judgment on whether the hand displayed on the image is a left or a right hand
      * - rotation_side
        - Mental judgment on the palmar-dorsal direction of a hand displayed as visual stimulus
      * - object_grasp
        - Mimicry of object grasping with right hand, in which the corresponding object was displayed on the screen
      * - object_orientation
        - Mimic orientation of rhombus, displayed as image background on the screen , using right hand along with fingers

.. dropdown:: Contrasts for ArchiSpatial
   :name: contArchiSpatial

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - saccades
        - saccade vs. fixation
      * - rotation_hand
        - left or right hand
      * - rotation_side
        - hand palm or back vs. fixation
      * - hand-side
        - left or right hand vs. hand palm or back
      * - object_grasp
        - object grasping
      * - object_orientation
        - image orientation reporting
      * - grasp-orientation
        - object grasping vs. orientation reporting

ArchiSocial
-----------

.. container:: tags

   :bdg-success:`sound_perception` :bdg-success:`auditory_sentence_recognition` :bdg-primary:`visual_imagery` :bdg-success:`voice_perception` :bdg-secondary:`narrative_comprehension` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Audio device: MRConfon MKII

The ARCHI tasks are a battery of localizers comprising a wide range of psychological domains. ArchiSocial relies on (1) the interpretation of short stories involving false beliefs or not, (2) observation of moving objects with or without a putative intention, and (3) listening to speech and non-speech sounds.

The conditions for this task are described in `this table <condArchiSocial_>`__ and the main contrasts derived from those conditions are described in `this table <contArchiSocial_>`__.

.. dropdown:: Conditions for ArchiSocial
   :name: condArchiSocial

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - mechanistic_audio
        - Interpret short stories (presented as auditory stimuli) through mental reply (no active response was involved), featuring a cause-consequence plot
      * - mechanistic_video
        - Interpret short stories (presented as visual stimuli) through mental reply (no active response was involved), featuring a cause-consequence plot
      * - triangle_mental
        - Watch short movies of triangles, which exhibit a putative interaction
      * - triangle_random
        - Watch short movies of triangles, which exhibit a random movement
      * - false_belief_audio
        - Interpret short stories (presented as auditory stimuli) through mental reply (no active response was involved), featuring a false-belief plot
      * - false_belief_video
        - Interpret short stories (presented as visual stimuli) through mental reply (no active response was involved), featuring a false-belief plot
      * - speech_sound
        - Listen passively to short samples of human voices
      * - non_speech_sound
        - Listen passively to short samples of natural sounds

.. dropdown:: Contrasts for ArchiSocial
   :name: contArchiSocial

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - triangle_mental
        - mental motion of triangle
      * - triangle_random
        - randomly drifting triangle
      * - triangle_mental-random
        - mental motion vs. random motion
      * - false_belief_video
        - false-belief story 
      * - false_belief_audio
        - false-belief tale 
      * - mechanistic_video
        - reading a mechanistic story
      * - mechanistic_audio
        - listening to a mechanistic tale
      * - false_belief-mechanistic_video
        - false-belief story vs. mechanistic story
      * - false_belief-mechanistic_audio
        - false-belief tale vs. mechanistic tale
      * - false_belief-mechanistic
        - false-belief story or tale vs. mechanistic story or tale
      * - speech_sound
        - listen to voice sound
      * - non_speech_sound
        - listen to natural sound
      * - speech-non_speech
        - listen to voice sound vs. natural sound

ArchiEmotional
--------------

.. container:: tags

   :bdg-danger:`emotional_expression` :bdg-light:`gender_discrimination` :bdg-primary:`visual_pattern_recognition` :bdg-primary:`visual_representation` :bdg-primary:`visual_orientation` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Audio device: MRConfon MKII

The ARCHI tasks are a battery of localizers comprising a wide range of psychological domains. ArchiEmotional includes (1) facial judgments of gender, and (2) trustworthiness plus expression based on complete portraits or photos of eyes' expressions.

The conditions for this task are described in `this table <condArchiEmotional_>`__ and the main contrasts derived from those conditions are described in `this table <contArchiEmotional_>`__.

.. dropdown:: Conditions for ArchiEmotional
   :name: condArchiEmotional

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - face_gender
        - Gender evaluation of the presented human faces
      * - face_control
        - Mental assessment on the slope of a gray-scale grid image (obtained from scrambling a face's image) that may be tilted or not
      * - face_trusty
        - Trustworthy evaluation of the presented human faces
      * - expression_intention
        - Trustworthy evaluation of the presented human eye images
      * - expression_gender
        - Gender evaluation of the presented human eye images
      * - expression_control
        - Mental assessment on the slope of a gray-scale grid image (obtained from scrambling an eyes' image) that may be tilted or not

.. dropdown:: Contrasts for ArchiEmotional
   :name: contArchiEmotional

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - face_gender
        - guess the gender from face image
      * - face_control
        - look at scrambled image
      * - face_gender-control
        - guess the gender from face image
      * - face_trusty
        - assess face trustfulness
      * - face_trusty-control
        - assess face trustfulness vs. view scrambled image
      * - face_trusty-gender
        - assess face trustfulness vs. gender
      * - expression_gender
        - guess gender from eyes image
      * - expression_intention
        - guess intention from eyes image
      * - expression_control
        - look at scrambled eyes image
      * - expression_gender-control
        - guess the gender from eyes image vs. view scrambled image
      * - expression_intention-control
        - guess intention from eyes image vs. view scrambled image
      * - expression_intention-gender
        - guess intention vs. gender from eyes image
      * - trusty_and_intention-control
        - assess face trustfulness or guess expression intention vs. scrambled image
      * - trusty_and_intention-gender
        - assess face trustfulness or guess expression intention vs. guess the gender

HcpEmotion
----------

.. container:: tags

   :bdg-light:`feature_comparison` :bdg-primary:`visual_form_recognition` :bdg-primary:`emotional_face_recognition` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The HCP tasks used herein were reproductions made in a subset of task-fMRI paradigms originally developed for the `Human Connectome Project <http://www.humanconnectome.org/>`__ , (`Barch et al., 2013 <https://doi.org/10.1016/j.neuroimage.2013.05.033>`__), but with minor changes. The main purpose of HcpEmotion task was to capture neural activity arising from fear- or angry-response processes. To elicit stronger effects, affective facial expressions were used as visual stimuli due to their importance in adaptive social behavior (`Hariri et al., 2002 <http://doi.org/10.1006/nimg.2002.1179>`__). The paradigm was thus composed by two categories of blocks: (1) the face block, and (2) the shape block. All blocks consisted of a series of events, in which images with faces or shapes were displayed, respectively. There were always three faces/shapes per image; one face/shape was shown at the top and two faces/shapes were shown at the bottom. The participants were then asked to decide which face/shape at the bottom, i.e. left or right face/shape, matched the one displayed at the top, by pressing respectively the index or middle finger's button of the response box. The task was formed by twelve blocks per run, i.e. six face blocks and six shape blocks. The two block categories were alternately presented for each run. All blocks contained six trials and they were always initiated by a cue of three seconds. In turn, the trials included a visual-stimulus period of two seconds and a fixation-cross period of one second; the total duration of the trial was thus three seconds.

The conditions for this task are described in `this table <condHcpEmotion_>`__ and the main contrasts derived from those conditions are described in `this table <contHcpEmotion_>`__.

.. dropdown:: Conditions for HcpEmotion
   :name: condHcpEmotion

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - shape
        - Images with shapes were displayed
      * - face
        - Images with faces were displayed

.. dropdown:: Contrasts for HcpEmotion
   :name: contHcpEmotion

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - shape
        - shape comparison
      * - face
        - emotional face comparison
      * - face-shape
        - emotional face comparison vs. shape comparison
      * - shape-face
        - shape comparison vs. emotional face comparison

HcpGambling
-----------

.. container:: tags

   :bdg-dark:`reward_processing` :bdg-dark:`punishment_processing` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The HCP tasks used herein were reproductions made in a subset of task-fMRI paradigms originally developed for the `Human Connectome Project <http://www.humanconnectome.org/>`__ , (`Barch et al., 2013 <https://doi.org/10.1016/j.neuroimage.2013.05.033>`__), but with minor changes. HcpGambling task was adapted from the Incentive processing task-fMRI paradigm of the HCP and its aim was to localize brain structures that take part to the reward system, namely the basal ganglia complex. The paradigm included eight blocks and each block was composed by eight events. For every event, the participants were asked to play a game. The goal was to guess whether the next number to be displayed, which ranged from one to nine, would be more or less than five while a question mark was shown on the screen. The answer was given by pressing the index or middle finger's button of the response box, respectively. Feedback on the correct number was provided afterwards. There was an equal amount of blocks in which the participants experienced either reward or loss, for most of the events. Concretely, six out of the eight events within a block pertained to one of these two outcomes; the remaining events corresponded to the antagonist or a neutral outcome, i.e. when the correct number was five. The task was constituted by eight blocks per run, in which each half related to reward and loss experience, respectively. The order of the two block categories were pseudorandomized during a single run, but fixed for all participants. A fixation-cross period of fifteen seconds was displayed between blocks. All blocks contained eight trials. The trials included a question-mark visual stimulus lasting up to 1.5 seconds, a feedback period of one second and a fixation-cross period of one second, as well; the total duration of the trial was then 3.5 seconds, approximately.

The conditions for this task are described in `this table <condHcpGambling_>`__ and the main contrasts derived from those conditions are described in `this table <contHcpGambling_>`__.

.. dropdown:: Conditions for HcpGambling
   :name: condHcpGambling

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - punishment
        - The participant experiences loss
      * - reward
        - The participant experiences reward

.. dropdown:: Contrasts for HcpGambling
   :name: contHcpGambling

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - reward
        - gambling with positive outcome
      * - punishment
        - negative gambling outcome
      * - reward-punishment
        - positive vs. negative gambling outcome
      * - punishment-reward
        - negative vs. positive gambling outcome

HcpMotor
--------

.. container:: tags

   :bdg-warning:`right_hand_response_execution` :bdg-warning:`left_hand_response_execution` :bdg-warning:`tongue_response_execution` :bdg-info:`working_memory` :bdg-warning:`response_execution` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
The HCP tasks used herein were reproductions made in a subset of task-fMRI paradigms originally developed for the `Human Connectome Project <http://www.humanconnectome.org/>`__ , (`Barch et al., 2013 <https://doi.org/10.1016/j.neuroimage.2013.05.033>`__), but with minor changes. HCP Motor task was designed with the intent of extracting maps on gross motor topography, in particular motor skills associated with movements of the foot, hand and tongue. There were thus five categories of blocks with respect to motor tasks involving (1) the left foot, (2) the right foot, (3) the left hand, (4) the right hand, and (5) the tongue, respectively. The blocks always started with visual cues referring to which part of the body should be moved. The cues were then followed by a set of events, which were in turn indicated by flashing arrows on the screen. The events pertained to the corresponding movements performed by the participants. The task was formed by five blocks per category, with a total of twenty blocks per run. The order of the block categories were pseudo-randomized during each run, but fixed for all participants. A fixation-dot period of fifteen seconds was inserted between some blocks. All blocks contained ten trials. Every trial included a cue of one second and a period of performance of twelve seconds. During the period of performance, arrows flashed ten times on the screen, as an indication of the number of movements that should be performed. The total duration of the trial was then thirteen seconds.

The conditions for this task are described in `this table <condHcpMotor_>`__ and the main contrasts derived from those conditions are described in `this table <contHcpMotor_>`__.

.. dropdown:: Conditions for HcpMotor
   :name: condHcpMotor

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - left_hand
        - Visual cue indicating the left hand should be moved
      * - right_hand
        - Visual cue indicating the right hand should be moved
      * - left_foot
        - Visual cue indicating the left foot should be moved
      * - right_foot
        - Visual cue indicating the right foot should be moved
      * - tongue
        - Visual cue indicating the tongue hand should be moved
      * - cue
        - Fixation dot

.. dropdown:: Contrasts for HcpMotor
   :name: contHcpMotor

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - left_hand-avg
        - move left hand vs. right hand	 feet and tongue
      * - right_hand-avg
        - move right hand vs. left hand	 feet and tongue
      * - left_foot-avg
        - move left foot vs. right foot	 hands and tongue
      * - right_foot-avg
        - move right foot vs. left foot	 hands and tongue
      * - tongue-avg
        - move tongue vs. hands and feet
      * - left_hand
        - move left hand
      * - right_hand
        - move right hand 
      * - left_foot
        - move left foot 
      * - right_foot
        - move right foot 
      * - tongue
        - move tongue
      * - cue
        - motion cue of motion

HcpLanguage
-----------

.. container:: tags

   :bdg-success:`auditory_arithmetic_processing` :bdg-success:`auditory_sentence_recognition` :bdg-secondary:`narrative_comprehension` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The HCP tasks used herein were reproductions made in a subset of task-fMRI paradigms originally developed for the `Human Connectome Project <http://www.humanconnectome.org/>`__ , (`Barch et al., 2013 <https://doi.org/10.1016/j.neuroimage.2013.05.033>`__), but with minor changes. HCP Language task was used as a localizer of brain regions involved in semantic processing, with special focus on the anterior temporal lobe (ATL) (`Binder et al., 2011 <https://doi.org/10.1016/j.neuroimage.2010.09.048>`__). The paradigm comprised two categories of blocks: (1) story blocks, and (2) math blocks. The math block served as a control task in this context, since it was likely to adress other brain regions during the attentional demands. Both type of blocks exhibited auditory stimuli in short epochs, which in turn finished with a final question followed by two possible answers. During story blocks, participants were presented with stories, whose question targeted their respective topics. Conversely, math blocks showed arithmetic problems for which the correct solution must be selected. The answer was provided after the two possible options were displayed, through pressing the corresponding button of the response box, i.e. the button for the index or middle finger of the response box for the first or second option, respectively. The difficulty levels of the problems, presented for both categories, were adjusted throughout the experiment, in order to keep the participants engaged in the task and, thus, assure accurate performances (`Binder et al., 2011 <https://doi.org/10.1016/j.neuroimage.2010.09.048>`__). The task was composed by eleven blocks per run. For the first run, six story blocks and five math blocks were interleaved, respectively. The reverse amount and order of blocks were used during the second run. The number of trials per block varied between one and four. Nevertheless, it was assured that both block categories matched their length of presentation at every run. There was a cue of two seconds in the beginning of each block, indicating its category. The duration of the trials within a block varied between ten and thirty seconds. Finally, the presentation of the auditory stimuli was always accompanied by the display of a fixation cross on the screen throughout the entire run.

The conditions for this task are described in `this table <condHcpLanguage_>`__ and the main contrasts derived from those conditions are described in `this table <contHcpLanguage_>`__.

.. dropdown:: Conditions for HcpLanguage
   :name: condHcpLanguage

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - story
        - Listening to tales
      * - math
        - Auditorily-cued mental addition

.. dropdown:: Contrasts for HcpLanguage
   :name: contHcpLanguage

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - story
        - listening to tale
      * - math
        - mental additions
      * - story-math
        - listening to tale vs. mental additions
      * - math-story
        - mental additions vs. listening to tale

HcpRelational
-------------

.. container:: tags

   :bdg-light:`feature_comparison` :bdg-primary:`visual_form_recognition` :bdg-primary:`visual_pattern_recognition` :bdg-light:`relational_comparison` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The HCP tasks used herein were reproductions made in a subset of task-fMRI paradigms originally developed for the `Human Connectome Project <http://www.humanconnectome.org/>`__ , (`Barch et al., 2013 <https://doi.org/10.1016/j.neuroimage.2013.05.033>`__), but with minor changes. HCP Relational task employed a relational matching-to-sample paradigm, featuring a second-order comparison of relations between two pairs of objects. It served primarily as a localizer of the rostrolateral prefrontal cortex, since relational matching mechanisms were shown to elicit activation on this region (`Smith et al., 2007 <https://doi.org/10.1016/j.neuroimage.2007.04.032>`__). Similarly to some previous tasks, two categories of blocks described the paradigm: (1) the relational-processing block, and (2) the control-matching block. All blocks were constituted by a set of events. In the relational-processing block, visual stimuli consisted of images representing two pairs of objects, in which one pair was placed at the top and the other one at the bottom of the image, respectively. Objects within a pair may differ in two dimensions: shape and texture. The participants had to identify whether the pair of objects from the top differed in a specific dimension and, subsequently, they were asked to determine whether the pair from the bottom changed along the same dimension. For the control block, one pair of objects was displayed at the top of the image and a single object at the bottom of the same image. In addition, a cue was shown in the middle of that image referring to one of the two possible dimensions. The participants had thus to indicate whether the object from the bottom was matching either of the two objects from the top, according to the dimension specified as a cue. If there was a match they had to press with the index finger on the corresponding button of the button box; otherwise, they had to press with the middle finger on the corresponding one. This task was formed by twelve blocks per run. Two groups of six blocks referred to the two block categories, respectively. Block categories were, in turn, interleaved for display within a run. A fixation-cross period of sixteen seconds was inserted between some blocks. All blocks contained six trials and they were always initiated by a cue of two seconds. The trials were described by a visual-stimulus plus response period followed by a fixation-cross period, lasting up to ten seconds. The duration of the former differed in agreement with the type of block, i.e. it lasted nine seconds and 7.6 seconds during the relational-processing block and control-matching block, respectively.

The conditions for this task are described in `this table <condHcpRelational_>`__ and the main contrasts derived from those conditions are described in `this table <contHcpRelational_>`__.

.. dropdown:: Conditions for HcpRelational
   :name: condHcpRelational

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - relational
        - Relational processing of visual objects
      * - match
        - Simple visual matching

.. dropdown:: Contrasts for HcpRelational
   :name: contHcpRelational

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - match
        - visual feature matching vs. fixation
      * - relational
        - relational comparison vs. fixation
      * - relational-match
        - relational comparison vs. matching

HcpSocial
---------

.. container:: tags

   :bdg-light:`animacy_perception` :bdg-warning:`motion_detection` :bdg-light:`mentalization` :bdg-dark:`animacy_decision` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The HCP tasks used herein were reproductions made in a subset of task-fMRI paradigms originally developed for the `Human Connectome Project <http://www.humanconnectome.org/>`__ , (`Barch et al., 2013 <https://doi.org/10.1016/j.neuroimage.2013.05.033>`__), but with minor changes. HCP Social task intended to provide evidence for task-specific activation in brain structures presumably implicated in social cognition. The paradigm included two categories of blocks, in which movies were presented during short epochs. The movies consisted in triangle-shape clip art, moving in a predetermined fashion. Putative social interactions could be drawn from movements referring to the block category on the effect-of-interest. In contrast, objects appeared to be randomly moving the other category, i.e. the control-effect block. Participants were to decide whether the movements of the objects appeared to represent a social interaction (by pressing with the index finger in the corresponding button of the response box) or not (by pressing with the ring finger in the corresponding button of the response box; in case of uncertainty, they had to press with the middle finger. The task was constituted by ten blocks per run. Each half of the blocks corresponded to one of the aforementioned block categories, whose order was pseudo-randomized for every run, but fixed for all participants. There was only one trial present per block. It consisted of a twenty-second period of video-clip presentation plus three seconds maximum of a response period, indicated by a momentary instruction on the screen. Thus, the total duration of a block was approximately twenty three seconds. A fixation-cross period of fifteen seconds was always displayed between blocks. 

The conditions for this task are described in `this table <condHcpSocial_>`__ and the main contrasts derived from those conditions are described in `this table <contHcpSocial_>`__.

.. dropdown:: Conditions for HcpSocial
   :name: condHcpSocial

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - mental
        - Watching a movie with mental motion
      * - random
        - Watching a movie with random motion

.. dropdown:: Contrasts for HcpSocial
   :name: contHcpSocial

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - random
        - random motion vs. fixation
      * - mental
        - mental motion vs. fixation
      * - mental-random
        - mental motion vs. random motion

HcpWm
-----

.. container:: tags

   :bdg-light:`tool_maintenance` :bdg-light:`body_maintenance` :bdg-primary:`visual_place_recognition` :bdg-light:`place_maintenance` :bdg-info:`working_memory` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The HCP tasks used herein were reproductions made in a subset of task-fMRI paradigms originally developed for the `Human Connectome Project <http://www.humanconnectome.org/>`__ , (`Barch et al., 2013 <https://doi.org/10.1016/j.neuroimage.2013.05.033>`__), but with minor changes. HCP Working Memory task was adapted from the classical n-back task to serve as functional localizer for evaluation of working-memory (WM) capacity and related processes. The paradigm integrated two categories of blocks: (1) the "0-back" WM-task block, and (2) the "2-back" WM-task block. They were both equally presented within a run. A cue was always displayed at the beginning of each block, indicating its task-related type. Blocks were formed by set of events, during which pictures of faces, places, tools or body parts were shown on the screen. One block was always dedicated to one specific category of pictures and the four categories were always presented at every run. At each event, the participant were to decide whether the image matched with the reference or not, by pressing respectively on the index or middle finger's button of the response box. The task was constituted by sixteen blocks per run, splitted into two block categories. Besides, there were four pairs of blocks per category, referring respectively to the four classes of pictures mentioned above. The order of the blocks, regardless their category and corresponding class of pictures, was pseudo-randomized for every run, but fixed for all participants. A fixation-cross period of fifteen seconds was introduced between some blocks. All blocks contained ten trials and they were always initiated by a cue of 2.5 seconds. Trials included in turn the presentation of a picture for two seconds and a very short fixation-cross period for half of a second; the total duration of one trial was thus 2.5 seconds.

The conditions for this task are described in `this table <condHcpWm_>`__ and the main contrasts derived from those conditions are described in `this table <contHcpWm_>`__.

.. dropdown:: Conditions for HcpWm
   :name: condHcpWm

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - 0back_body
        - 0-back, pictures of body parts were displayed
      * - 2back_body
        - 2-back, pictures of body parts were displayed
      * - 0back_face
        - 0-back, pictures of faces were displayed
      * - 2back_face
        - 2-back, pictures of faces were displayed
      * - 0back_tools
        - 0-back, pictures of tools were displayed
      * - 2back_tools
        - 2-back, pictures of tools were displayed
      * - 0back_place
        - 0-back, pictures of places were displayed
      * - 2back_place
        - 2-back, pictures of places were displayed

.. dropdown:: Contrasts for HcpWm
   :name: contHcpWm

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - 2back-0back
        - 2-back vs. 0-back
      * - body-avg
        - body image versus face	 place	 tool image","['visual_body_recognition','body_maintenance']
      * - face-avg
        - face image versus body	 place	 tool image","['visual_face_recognition','face_maintenance']
      * - place-avg
        - place image versus face	 body	 tool image","['visual_place_recognition','place_maintenance']
      * - tools-avg
        - tool image versus face	 place	 body image","['visual_tool_recognition','tool_maintenance']
      * - 0back-2back
        - 0-back vs. 2-back
      * - 0back_body
        - body image 0-back task vs. fixation
      * - 2back_body
        - body image 2-back task vs. fixation
      * - 0back_face
        - face image 0-back task vs. fixation
      * - 2back_face
        - face image 2-back task vs. fixation
      * - 0back_tools
        - tool image 0-back task vs. fixation
      * - 2back_tools
        - tool image 2-back task vs. fixation
      * - 0back_place
        - place image 0-back task vs. fixation
      * - 2back_place
        - place image 2-back task vs. fixation

RSVPLanguage
------------

.. container:: tags

   :bdg-secondary:`word_maintenance` :bdg-primary:`visual_string_recognition` :bdg-info:`working_memory` :bdg-secondary:`syntactic_parsing` :bdg-light:`recognition` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.7.0 (Python 2.7)
   - Response device: In-house custom-made sticks featuring one-top button, each one to be used in each hand

   - Audio device: MRConfon MKII

The Rapid-Serial-Visual-Presentation (RSVP) Language task was adapted from the study undertaken by (`Humphries et al., 2006 <Humphries et al., 2006>`__) on syntactic and semantic processing during auditory sentence comprehension. Specifically, the task herein described targeted the same syntactic and semantic modules, but in the context of reading. It thus allowed for capturing further associations with regard to e.g. visual (pseudo) word recognition and sublexical route, among other aspects related to active reading. The paradigm consisted in a block-design presentation strategy of the stimuli. One block was defined as an epoch within a trial and epochs corresponded in turn to experimental conditions. Such conditions stood for the consecutive visual presentation of ten constituents composed by letters. All linguistic content elicited from the conditions except "consonant strings", such as grammar rules, lexicon and phonemes, were part of the french language. In order to ensure continuous engagement during task performance, participants were asked, straight afterwards the visualization of every sentence, to ascertain whether the current constituent displayed on the screen, aka "the probe", was part of the previous sentence or not. The corresponding answer was provided immediately after the probe, by pressing the button in the left hand if "yes" or the one in the right hand if "no". Data were collected in six runs during one single session. Every run was composed by sixty trials, in which subsets of ten trials were dedicated to each condition, respectively. The order of the trials was pseudo-randomized within and between runs, such that there were no repeated trials during a full session. Moreover, a different pseudo-randomized order for the presentation of the trials was always employed across participants. One trial comprised several experimental manipulations, other than a block integrating one specific condition. It was sequentially formed by a period of fixation-cross display (two seconds), another short period of a blank screen (0.5 seconds), a block containing the linguistic stimuli (0.4 seconds x 10 = 4 seconds), a jittered blank screen (varying from one to 1.5 seconds), a period of a second fixation-cross display (0.5 seconds), a period for the probe display (0.5 seconds), and, finally, a response period (varying up to two seconds). The total duration of one single trial was thus ten seconds. Three extra seconds of blank screen were added at the beginning of every run, i.e. before the presentation of the first trial. Two opposite phase-encoding directions were respectively applied during acquisition of each half of the total amount of runs.

The conditions for this task are described in `this table <condRSVPLanguage_>`__ and the main contrasts derived from those conditions are described in `this table <contRSVPLanguage_>`__.

.. dropdown:: Conditions for RSVPLanguage
   :name: condRSVPLanguage

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - complex
        - Constituents, i.e. words formed syntactically and semantically congruent sentences with more than one clause grid image that may be tilted or not (high sentence-structure complexity)
      * - simple
        - Constituents, i.e. words formed syntactically and semantically congruent sentences of one single clause (low_sentence-structure_complexity)
      * - read_jabberwocky
        - Syntactically congruent sentences composed by non-lexical vocable constituents
      * - word_list
        - Syntactically non-congruent sentences but with semantic content
      * - pseudoword_list
        - Syntactically and semantically non-congruent sentences composed by non-lexical vocable constituents
      * - consonant_string
        - Syntactically and semantically non-congruent sentences composed by non-vocable constituents
      * - probe
        - Presented word, for which one has to assess whether it was in the previously presented sequence or not

.. dropdown:: Contrasts for RSVPLanguage
   :name: contRSVPLanguage

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - consonant_string
        - read and encode consonant strings vs. fixation
      * - word_list
        - read words vs. fixation
      * - word-consonant_string
        - read words vs. consonant strings
      * - pseudoword_list
        - read pseudowords vs. fixation
      * - pseudo-consonant_string
        - read pseudowords vs. consonant strings
      * - word-pseudo
        - read words vs. pseudowords
      * - simple
        - read sentence with simple syntax vs. fixation
      * - simple-consonant_string
        - read simple sentence vs. consonant strings
      * - complex
        - read sentence with complex syntax vs. fixation
      * - complex-consonant_string
        - read complex sentence vs. consonant strings
      * - complex-simple
        - read sentence with complex vs. simple syntax
      * - sentence-consonant_string
        - read sentence vs. consonant strings
      * - sentence-word
        - read sentence vs. words
      * - sentence-pseudo
        - read sentence vs. pseudowords
      * - jabberwocky
        - read jabberwocky vs. fixation
      * - jabberwocky-consonant_string
        - read jabberwocky vs. consonant strings
      * - jabberwocky-pseudo
        - read jabberwocky vs. pseudowords
      * - sentence-jabberwocky
        - read sentence vs. jabberwocky
      * - probe
        - word probe

MTTWE
-----

.. container:: tags

   :bdg-light:`time_orientation` :bdg-secondary:`semantic_categorization` :bdg-info:`spatial_working_memory` :bdg-light:`past_time` :bdg-light:`future_time` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.7.0 / pygame 1.9.3
   - Response device: In-house custom-made sticks featuring one-top button, each one to be used in each hand

The Mental Time Travel (MTT) task battery was developed following previous studies conducted at the NeuroSpin platform on chronosthesia and mental space navigation (`Gauthier et al., 2016 <https://doi.org/10.1016/j.cognition.2016.05.015>`__, `Gauthier et al., 2016 <https://doi.org/10.1523/JNEUROSCI.1400-16.2016>`__, `Gauthier et al., 2018 <https://doi.org/10.1093/cercor/bhy320>`__). Participants were to judge the ordinality of real historical events in time and space by mentally project oneself, i.e. through egocentric mapping. In contrast, the present task was intended to assess the neural correlates underlying both mental time and space judgment involved in allocentric mapping implemented in narratives. To this end, and in order to remove confounds associated with prior subject-specific mental representations linked to the historical events, fictional scenarios were created with fabricated stories and characters. 
The stimuli of each task referred to a different island plotting different stories and characters. There were two stories per island and they were created based on a two-dimensional mesh of nodes. Each node corresponded to a specific action. The stories of each island evolved both in time and in one single cardinal direction. The cardinal directions, cued in the MTTWE task, were West-East (WE). In addition, the stories of each island evolved spatially in opposite ways. So, the two stories plotted in the West-East island evolved across time from west to east and east to west, respectively. Prior to each session, participants were to learn the story of the corresponding session. To prevent any retrieval of graphical memories referring to the schematic representation of the stories, they were presented as audio narratives. Additionally, the participants were also instructed to learn the stories chronographically, i.e. as they were progressively referred to in the narrative, and to refrain from doing (visual) notes, which could be encoded as mental judgments. 
The task was organized as a block-design paradigm, composed of trials with three conditions of audio stimuli: (1) Reference, statement of an action in the story to serve as reference for the time or space judgment in the same trial; (2) Cue, question concerning the type of mental judgment to be performed in the same trial, i.e. "Before or After?" for the time judgment or "West or East?" for the space judgment; and (3) Event, statement of an action to be judged with respect to the Reference and according to the Cue. Every trial started with an audio presentation of the Reference followed by silence, with a duration of two and four seconds, respectively. The audio presentation of the Cue came next, followed by a silence period; they had respectively a duration of two and four seconds. Afterwards, a series of four Events were presented for two seconds each; all of them were interspersed by a Response condition of three seconds. Every trial ended with a silent period of seven seconds, thus lasting thirty nine seconds in total. A black fixation cross was permanently displayed on the screen across conditions and the participants were instructed to never close their eyes. At the very end of each trial, the cross turned to red during half of a second in order to signal the beginning of the next trial; such cue facilitated the identification of the next audio stimulus as the upcoming Reference to be judged. During the Response period, the participants had to press one of the two possible buttons, placed in their respective left and right hand. If the Cue presented in the given trial hinted at time judgment, the participants were to judge whether the previous Event occurred before the Reference, by pressing the button of the left hand, or after the Reference, by pressing the button of the right hand. If the Cue concerned with space judgment, the participants were to judge, in the same way, whether the Event occurred west or east of the Reference in the first session and south or north of the Reference in the second session. 
One session of data collection comprised three runs; each of them included twenty trials. Half of the trials for a given run were about time navigation and the other half, space navigation. Five different references were shared by both types of navigation and, thus, there were two trials with the same reference for each type of navigation. In turn, these two trials differed in terms of distance in the mesh between the node of the Reference and the node of each Event, i.e. *close* referred to two consecutive nodes whereas *far* referred to two nodes interspersed by another node. Within trials, half of the Events related to past or western actions and the other half to future or eastern actions with respect to the Reference. The order of the trials was shuffled within runs, only to ensure that each run would feature a unique sequence of trials according to type of reference (both in time and space) and cue. No pseudo-randomization criterion was imposed as the trials' characterization was already very rich. Since there were only two types of answers, we also randomized events according to their correct answer within each trial. The same randomized sequence for each run was employed for all participants. The code of this randomization is provided together with the protocol of the task on `Github <https://github.com/hbp-brain-charting/public_protocols/tree/master/mtt/mtt_protocol/randomization>`__. Note that the randomized sequence of trials for all runs is pre-determined and, thus, provided as inputs to the protocol for a specific session.

The conditions for this task are described in `this table <condMTTWE_>`__ and the main contrasts derived from those conditions are described in `this table <contMTTWE_>`__.

.. dropdown:: Conditions for MTTWE
   :name: condMTTWE

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - we_average_reference
        - Action in the story to serve as reference for the time or space judgment in the same trial in the west-east island
      * - we_all_space_cue
        - Cue indicating a question about spatial orientation in the west-east island
      * - we_all_time_cue
        - Cue indicating a question about time orientation in the west-east island
      * - we_westside_event
        - Action to be judged whether it takes place west or east from this reference, that actually takes place west from this reference
      * - we_eastside_event
        - Action to be judged whether it takes place west or east from this reference, that actually takes place east from this reference
      * - we_before_event
        - Action to be judged whether it takes place before or after this reference, that actually takes place before this reference, in the west-east island
      * - we_after_event
        - Action to be judged whether it takes place before or after this reference, that actually takes place before this reference, in the west-east island
      * - we_all_event_response
        - Motor responses performed after every event condition in the west-east island

.. dropdown:: Contrasts for MTTWE
   :name: contMTTWE

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - we_average_reference
        - updating ones position in space and time in west-east island
      * - we_all_space_cue
        - spatial cue of the next event in west-east island
      * - we_all_time_cue
        - time cue of the next event in west-east island
      * - we_all_space-time_cue
        - spatial vs. time cues in west-east island
      * - we_all_time-space_cue
        - time vs. spatial cues in west-east island
      * - we_average_event
        - figuring out the space or time of an event in west-east island
      * - we_space_event
        - figuring out the position of an event in west-east island
      * - we_time_event
        - figuring out the time of an event in west-east island
      * - we_space-time_event
        - event in space vs. event in time in west-east island
      * - we_time-space_event
        - event in time vs. event in space in west-east island
      * - we_westside_event
        - events occuring westside vs. fixation
      * - we_eastside_event
        - events occuring eastside vs. fixation
      * - westside-eastside_event
        - events occuring westside vs. eastside
      * - eastside-westside_event
        - events occuring eastside vs. westside
      * - we_before_event
        - events occuring before vs. fixation in west-east island
      * - we_after_event
        - events occuring after vs. fixation in west-east island
      * - we_before-after_event
        - events occuring before vs. after in west-east island
      * - we_after-before_event
        - events occuring after vs. before in west-east island
      * - we_all_event_response
        - motor responses performed after every event condition in the west-east island

MTTNS
-----

.. container:: tags

   :bdg-light:`time_orientation` :bdg-secondary:`semantic_categorization` :bdg-info:`spatial_working_memory` :bdg-dark:`north_cardinal-direction_judgment` :bdg-light:`past_time` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.7.0 / pygame 1.9.4
   - Response device: In-house custom-made sticks featuring one-top button, each one to be used in each hand

The Mental Time Travel (MTT) task battery was developed following previous studies conducted at the NeuroSpin platform on chronosthesia and mental space navigation (`Gauthier et al., 2016 <https://doi.org/10.1016/j.cognition.2016.05.015>`__, `Gauthier et al., 2016 <https://doi.org/10.1523/JNEUROSCI.1400-16.2016>`__, `Gauthier et al., 2018 <https://doi.org/10.1093/cercor/bhy320>`__). The MTTNS task is exactly the same as `MTTWE`_ task except that the the cardinal directions, cued in the task, were North-South (NS). In addition, the two stories plotted in the South-North island evolved across time from north to south and south to north. The MTTNS task was performed in a separate session from the `MTTWE`_ task.

The conditions for this task are described in `this table <condMTTNS_>`__ and the main contrasts derived from those conditions are described in `this table <contMTTNS_>`__.

.. dropdown:: Conditions for MTTNS
   :name: condMTTNS

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - sn_average_reference
        - Action in the story to serve as reference for the time or space judgment in the same trial in the west-east island
      * - sn_all_space_cue
        - Cue indicating a question about spatial orientation in the south-north island
      * - sn_all_time_cue
        - Cue indicating a question about time orientation in the south-north island
      * - sn_southside_event
        - Action to be judged whether it takes place south or north from this reference, that actually takes place south from this reference
      * - sn_northside_event
        - Action to be judged whether it takes place south or north from this reference, that actually takes place north from this reference
      * - sn_before_event
        - Action to be judged whether it takes place before or after this reference, that actually takes place before this reference, in the south-north island
      * - sn_after_event
        - Action to be judged whether it takes place before or after this reference, that actually takes place before this reference, in the south-north island
      * - sn_all_event_response
        - Motor responses performed after every event condition in the south-north island

.. dropdown:: Contrasts for MTTNS
   :name: contMTTNS

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - sn_average_reference
        - updating ones position in space and time in south-north island
      * - sn_all_space_cue
        - spatial cue of the next event in south-north island
      * - sn_all_time_cue
        - time cue of the next event in south-north island
      * - sn_all_space-time_cue
        - spatial vs. time cues in south-north island
      * - sn_all_time-space_cue
        - time vs. spatial cues in south-north island
      * - sn_average_event
        - figuring out the space or time of an event in south-north island
      * - sn_space_event
        - figuring out the position of an event in south-north island
      * - sn_time_event
        - figuring out the time of an event in south-north island
      * - sn_space-time_event
        - event in space vs. event in time in south-north island
      * - sn_time-space_event
        - event in time vs. event in space in south-north island
      * - sn_southside_event
        - events occuring southside vs. fixation
      * - sn_northside_event
        - events occuring northside vs. fixation
      * - southside-northside_event
        - events occuring southside vs. northside
      * - northside-southside_event
        - events occuring northsife vs. southside
      * - sn_before_event
        - events occuring before vs. fixation in south-north island
      * - sn_after_event
        - events occuring after vs. fixation in south-north island
      * - sn_before-after_event
        - events occuring before vs. after in south-north island
      * - sn_after-before_event
        - events occuring after vs. before in south-north island
      * - sn_all_event_response
        - motor responses performed after all event condition in the south-north island

PreferenceFood
--------------

.. container:: tags

   :bdg-dark:`incentive_salience` :bdg-dark:`reward_valuation` :bdg-dark:`judgment` :bdg-light:`food_cue_reactivity` :bdg-dark:`confidence_judgment` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The Preference task battery was adapted from the Pleasantness Rating task described in (`Lebreton et al., 2015 <https://doi.org/10.1038/nn.4064>`__), in order to capture the neural correlates underlying the decision-making for potentially rewarding outcomes (aka "positive-incentive value") as well as the level of confidence of such type of action. The whole task battery is composed of four tasks, each of them pertaining to the presentation of items of a certain kind. Therefore, PreferenceFood task was dedicated to "food items". The task was organized as a block-design experiment with one condition per trial. Every trial started with a fixation cross, whose duration was jittered between 0.5 seconds and 4.5 seconds, after which a picture of an item was displayed on the screen together with a rating scale and a cursor. Participants were to indicate how pleasant the presented stimulus was, by sliding the cursor along the scale. Index and ring finger's of the response box were to move respectively with low and high speed to the left whereas the middle and little fingers were to move respectively with low and high speed to the right; thumb's button was used to validate the answer. The scale ranged between 1 and 100. The value 1 corresponded to the choices "unpleasant" or "indifferent"; the middle of the scale corresponded to the choice "pleasant"; and the value 100 corresponded to the choice "very pleasant". Therefore, the ratings related only to the estimation of the positive-incentive value of the items displayed. The task was presented twice in two fully dedicated runs. The stimuli were always different between runs of the same task. As a consequence, no stimulus was ever repeated in any trial and, thus, no item was ever assessed more than once by the participants. Although each trial had a variable duration, according to the time spent by the participant in the assessment, no run lasted longer than eight minutes and sixteen seconds. To avoid any selection bias in the sequence of stimuli, the order of their presentation was shuffled across trials and between runs of the same type. This shuffle is embedded in the code of the protocol and, thus, the sequence was determined upon launching it. Consequently, the sequence of stimuli was also random across subjects.

The conditions for this task are described in `this table <condPreferenceFood_>`__ and the main contrasts derived from those conditions are described in `this table <contPreferenceFood_>`__.

.. dropdown:: Conditions for PreferenceFood
   :name: condPreferenceFood

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - food_constant
        - Classify the level of pleasantness of a food item displayed on the screen in terms of willingness to eat it, this condition serves as an occurrence regressor when formulated as visual evaluation of an item vs. fixation
      * - food_linear
        - Classify the level of pleasantness of a food item displayed on the screen in terms of willingness to eat it. this condition captures the linear effect of pleasantness (akin to judgement effects) when formulated as visual preference vs. no preference
      * - food_quadratic
        - Classify the level of pleasantness of a food item displayed on the screen in terms of willingness to eat it. this condition captures the quadratic effect of pleasantness (akin to confidence effects) when formulated as confidence in preference vs. no confidence

.. dropdown:: Contrasts for PreferenceFood
   :name: contPreferenceFood

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - food_constant
        - evaluation of food
      * - food_linear
        - linear effect of food preference
      * - food_quadratic
        - quadratic effect of food preference

PreferencePaintings
-------------------

.. container:: tags

   :bdg-dark:`incentive_salience` :bdg-dark:`reward_valuation` :bdg-dark:`judgment` :bdg-dark:`confidence_judgment` :bdg-primary:`visual_color_discrimination` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The Preference task battery was adapted from the Pleasantness Rating task described in (`Lebreton et al., 2015 <https://doi.org/10.1038/nn.4064>`__), in order to capture the neural correlates underlying the decision-making for potentially rewarding outcomes (aka "positive-incentive value") as well as the level of confidence of such type of action. The whole task battery is composed of four tasks, each of them pertaining to the presentation of items of a certain kind. Therefore, PreferencePaintings task was dedicated to "paintings". The task was organized as a block-design experiment with one condition per trial. Every trial started with a fixation cross, whose duration was jittered between 0.5 seconds and 4.5 seconds, after which a picture of an item was displayed on the screen together with a rating scale and a cursor. Participants were to indicate how pleasant the presented stimulus was, by sliding the cursor along the scale. Index and ring finger's of the response box were to move respectively with low and high speed to the left whereas the middle and little fingers were to move respectively with low and high speed to the right; thumb's button was used to validate the answer. The scale ranged between 1 and 100. The value 1 corresponded to the choices "unpleasant" or "indifferent"; the middle of the scale corresponded to the choice "pleasant"; and the value 100 corresponded to the choice "very pleasant". Therefore, the ratings related only to the estimation of the positive-incentive value of the items displayed. The task was presented twice in two fully dedicated runs. The stimuli were always different between runs of the same task. As a consequence, no stimulus was ever repeated in any trial and, thus, no item was ever assessed more than once by the participants. Although each trial had a variable duration, according to the time spent by the participant in the assessment, no run lasted longer than eight minutes and sixteen seconds. To avoid any selection bias in the sequence of stimuli, the order of their presentation was shuffled across trials and between runs of the same type. This shuffle is embedded in the code of the protocol and, thus, the sequence was determined upon launching it. Consequently, the sequence of stimuli was also random across subjects.

The conditions for this task are described in `this table <condPreferencePaintings_>`__ and the main contrasts derived from those conditions are described in `this table <contPreferencePaintings_>`__.

.. dropdown:: Conditions for PreferencePaintings
   :name: condPreferencePaintings

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - painting_constant
        - Classify the level of pleasantness of a painting displayed on the screen in terms of willingness to possess it, this condition serves as an occurrenceregressor when formulated as visual evaluation of an item vs. fixation
      * - painting_linear
        - Classify the level of pleasantness of a painting displayed on the screen in terms of willingness to possess it. this condition captures the linear effect of pleasantness (akin to judgement effects) when formulated as visual preference vs. no preference
      * - painting_quadratic
        - Classify the level of pleasantness of a painting displayed on the screen in terms of willingness to possess it. this condition captures the quadratic effect of pleasantness (akin to confidence effects) when formulated as confidence in preference vs. no confidence

.. dropdown:: Contrasts for PreferencePaintings
   :name: contPreferencePaintings

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - painting_constant
        - evaluation of paintings
      * - painting_linear
        - linear effect of paintings preference
      * - painting_quadratic
        - quadratic effect of paintings preference

PreferenceFaces
---------------

.. container:: tags

   :bdg-dark:`incentive_salience` :bdg-primary:`facial_attractiveness_recognition` :bdg-dark:`reward_valuation` :bdg-dark:`judgment` :bdg-dark:`confidence_judgment` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The Preference task battery was adapted from the Pleasantness Rating task described in (`Lebreton et al., 2015 <https://doi.org/10.1038/nn.4064>`__), in order to capture the neural correlates underlying the decision-making for potentially rewarding outcomes (aka "positive-incentive value") as well as the level of confidence of such type of action. The whole task battery is composed of four tasks, each of them pertaining to the presentation of items of a certain kind. Therefore, PreferenceFaces task was dedicated to "human faces". All tasks were organized as a block-design experiment with one condition per trial. Every trial started with a fixation cross, whose duration was jittered between 0.5 seconds and 4.5 seconds, after which a picture of an item was displayed on the screen together with a rating scale and a cursor. Participants were to indicate how pleasant the presented stimulus was, by sliding the cursor along the scale. Index and ring finger's of the response box were to move respectively with low and high speed to the left whereas the middle and little fingers were to move respectively with low and high speed to the right; thumb's button was used to validate the answer. The scale ranged between 1 and 100. The value 1 corresponded to the choices "unpleasant" or "indifferent"; the middle of the scale corresponded to the choice "pleasant"; and the value 100 corresponded to the choice "very pleasant". Therefore, the ratings related only to the estimation of the positive-incentive value of the items displayed. The task was presented twice in two fully dedicated runs. The stimuli were always different between runs of the same task. As a consequence, no stimulus was ever repeated in any trial and, thus, no item was ever assessed more than once by the participants. Although each trial had a variable duration, according to the time spent by the participant in the assessment, no run lasted longer than eight minutes and sixteen seconds. To avoid any selection bias in the sequence of stimuli, the order of their presentation was shuffled across trials and between runs of the same type. This shuffle is embedded in the code of the protocol and, thus, the sequence was determined upon launching it. Consequently, the sequence of stimuli was also random across subjects.

The conditions for this task are described in `this table <condPreferenceFaces_>`__ and the main contrasts derived from those conditions are described in `this table <contPreferenceFaces_>`__.

.. dropdown:: Conditions for PreferenceFaces
   :name: condPreferenceFaces

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - face_constant
        - Classify the level of pleasantness of a human face displayed on the screen in terms of willingness to meet the person portrayed, this condition serves as an occurrence regressor when formulated as visual evaluation of an item vs. fixation
      * - face_linear
        - Classify the level of pleasantness of a human face displayed on the screen in terms of willingness to meet the person portrayed. this condition captures the linear effect of pleasantness (akin to judgement effects) when formulated as visual preference vs. no preference
      * - face_quadratic
        - Classify the level of pleasantness of a human face displayed on the screen in terms of willingness to meet the person portrayed. this condition captures the quadratic effect of pleasantness (akin to confidence effects) when formulated as confidence in preference vs. no confidence

.. dropdown:: Contrasts for PreferenceFaces
   :name: contPreferenceFaces

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - face_constant
        - evaluation of faces
      * - face_linear
        - linear effect of face preference
      * - face_quadratic
        - quadratic effect of face preference

PreferenceHouses
----------------

.. container:: tags

   :bdg-dark:`incentive_salience` :bdg-primary:`visual_place_recognition` :bdg-dark:`reward_valuation` :bdg-dark:`judgment` :bdg-dark:`confidence_judgment` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The Preference task battery was adapted from the Pleasantness Rating task described in (`Lebreton et al., 2015 <https://doi.org/10.1038/nn.4064>`__), in order to capture the neural correlates underlying the decision-making for potentially rewarding outcomes (aka "positive-incentive value") as well as the level of confidence of such type of action. The whole task battery is composed of four tasks, each of them pertaining to the presentation of items of a certain kind. Therefore, PreferenceHouses task was dedicated to "houses". All tasks were organized as a block-design experiment with one condition per trial. Every trial started with a fixation cross, whose duration was jittered between 0.5 seconds and 4.5 seconds, after which a picture of an item was displayed on the screen together with a rating scale and a cursor. Participants were to indicate how pleasant the presented stimulus was, by sliding the cursor along the scale. Index and ring finger's of the response box were to move respectively with low and high speed to the left whereas the middle and little fingers were to move respectively with low and high speed to the right; thumb's button was used to validate the answer. The scale ranged between 1 and 100. The value 1 corresponded to the choices "unpleasant" or "indifferent"; the middle of the scale corresponded to the choice "pleasant"; and the value 100 corresponded to the choice "very pleasant". Therefore, the ratings related only to the estimation of the positive-incentive value of the items displayed. The task was presented twice in two fully dedicated runs. The stimuli were always different between runs of the same task. As a consequence, no stimulus was ever repeated in any trial and, thus, no item was ever assessed more than once by the participants. Although each trial had a variable duration, according to the time spent by the participant in the assessment, no run lasted longer than eight minutes and sixteen seconds. To avoid any selection bias in the sequence of stimuli, the order of their presentation was shuffled across trials and between runs of the same type. This shuffle is embedded in the code of the protocol and, thus, the sequence was determined upon launching it. Consequently, the sequence of stimuli was also random across subjects.

The conditions for this task are described in `this table <condPreferenceHouses_>`__ and the main contrasts derived from those conditions are described in `this table <contPreferenceHouses_>`__.

.. dropdown:: Conditions for PreferenceHouses
   :name: condPreferenceHouses

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - house_constant
        - Classify the level of pleasantness of a house displayed on the screen in terms of willingness to live in that house. this condition serves as an occurrenceregressor when formulated as visual evaluation of an item vs. fixation
      * - house_linear
        - Classify the level of pleasantness of a house displayed on the screen in terms of willingness to live in that house. this condition captures the linear effect of pleasantness (akin to judgement effects) when formulated as visual preference vs. no preference
      * - house_quadratic
        - Classify the level of pleasantness of a house displayed on the screen in terms of willingness to live in that house. this condition captures the quadratic effect of pleasantness (akin to confidence effects) when formulated as confidence in preference vs. no confidence

.. dropdown:: Contrasts for PreferenceHouses
   :name: contPreferenceHouses

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - house_constant
        - evaluation of houses
      * - house_linear
        - linear effect of houses preference
      * - house_quadratic
        - quadratic effect of houses preference

TheoryOfMind
------------

.. container:: tags

   :bdg-secondary:`semantic_processing` :bdg-secondary:`narrative_comprehension` :bdg-light:`theory-of-mind` 

.. admonition:: Implementation 
   :class: seealso

   - Software:  Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This battery of tasks was adapted from the original task-fMRI localizers of `Saxe Lab <https://saxelab.mit.edu/localizers>`__, that intended to identify functional regions-of-interest in the Theory-of-Mind network and Pain Matrix regions. Minor changes were employed in the present versions of the tasks herein described. Because the cohort of this dataset is composed solely of native French speakers, the verbal stimuli were thus translated to French. Therefore, the durations of the reading period and the response period within conditions were slightly increased. The TheoryOfMind task was a localizer was intended to identify brain regions involved in theory-of-mind and social cognition, by contrasting activation during two distinct story conditions: belief judgments, reading a false-belief story that portrayed characters with false beliefs about their own reality; and fact judgments, reading a story about a false photograph, map or sign (`Dodell-Feder et al., 2011 <https://doi.org/10.1016/j.neuroimage.2010.12.040>`__). The task was organized as a block-design experiment with one condition per trial. Every trial started with a fixation cross of twelve seconds, followed by the main condition that comprised a reading period of eighteen seconds and a response period of six seconds. During this response period, participants were to judge whether a statement about the story previously displayed is true or false by pressing respectively with the index or middle finger in the corresponding button of the response box. The total duration of the trial amounted to thirty six seconds. There were ten trials in a run, followed by an extraperiod of fixation cross for twelve seconds at the end of the run. Two runs were dedicated to this task in one single session. The designs, i.e. the sequence of conditions across trials, for two possible runs were pre-determined by the authors of the original study and hard-coded in the original protocol. The IBC-adapted protocols contain the exactly same designs. For all subjects, design 1 was employed for the PA-run and design 2 for the AP-run.

The conditions for this task are described in `this table <condTheoryOfMind_>`__ and the main contrasts derived from those conditions are described in `this table <contTheoryOfMind_>`__.

.. dropdown:: Conditions for TheoryOfMind
   :name: condTheoryOfMind

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - belief
        - Read a false-belief story
      * - photo
        - Read a false-photograph story

.. dropdown:: Contrasts for TheoryOfMind
   :name: contTheoryOfMind

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - photo
        - manipulation of fact judgments
      * - belief
        - manipulation of belief judgments
      * - belief-photo
        - belief vs. factual judgments

EmotionalPain
-------------

.. container:: tags

   :bdg-danger:`imagined_physical_pain` :bdg-danger:`empathy` :bdg-danger:`imagined_emotional_pain` :bdg-secondary:`narrative_comprehension` 

.. admonition:: Implementation 
   :class: seealso

   - Software:  Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task also belongs to the battery of tasks was adapted from the original task-fMRI localizers of `Saxe Lab <https://saxelab.mit.edu/localizers>`__, that intended to identify functional regions-of-interest in the Theory-of-Mind network and Pain Matrix regions. The EmotionalPain was an emotional pain localizer that was intended to identify brain regions involved in theory-of-mind and Pain Matrix areas, by contrasting activation during two distinct story conditions: reading a story that portrayed characters suffering from emotional pain and physical pain (`Jacoby et al., 2016 <https://doi.org/10.1016/j.neuroimage.2015.11.02>`__). The experimental design of this task is identical to the one employed for the `TheoryOfMind`_ localizer, except that the reading period lasted twelve seconds instead of eighteen seconds. During the response period, the participant had to the judge the amount of pain experienced by the character(s) portrayed in the previous story. For no pain, they had to press with their thumb on the corresponding button of the response box; for mild pain, they had to press with their index finger; for moderate pain, they had to press with the middle finger; and for a strong pain, they had to press with the ring finger.

The conditions for this task are described in `this table <condEmotionalPain_>`__ and the main contrasts derived from those conditions are described in `this table <contEmotionalPain_>`__.

.. dropdown:: Conditions for EmotionalPain
   :name: condEmotionalPain

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - physical_pain
        - Read story about fictional characters suffering from physical pain
      * - emotional_pain
        - Read story about fictional characters suffering from emotional pain

.. dropdown:: Contrasts for EmotionalPain
   :name: contEmotionalPain

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - physical_pain
        - reading physical pain story
      * - emotional_pain
        - reading emotional pain story
      * - emotional-physical_pain
        - emotional vs. physical pain story

PainMovie
---------

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-danger:`imagined_physical_pain` :bdg-danger:`empathy` :bdg-danger:`imagined_emotional_pain` :bdg-light:`mentalization` 

.. admonition:: Implementation 
   :class: seealso

   - Software:  Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Audio device: MRConfon MKII

This task also belongs to the battery of tasks was adapted from the original task-fMRI localizers of `Saxe Lab <https://saxelab.mit.edu/localizers>`__, that intended to identify functional regions-of-interest in the Theory-of-Mind network and Pain Matrix regions. The PainMovie task was a pain movie localizer and consisted displaying "Partly Cloudy", a 6 minutes movie from Disney Pixar, in order to study the responses implicated in theory-of-mind and Pain Matrix brain regions (`Jacoby et al., 2016 <https://doi.org/10.1016/j.neuroimage.2015.11.025>`__, `Richardson et al., 2018 <https://doi.org/10.1038/s41467-018-03399-2>`__). Two main conditions were thus hand-coded in the movie, according to (`Richardson et al., 2018 <https://doi.org/10.1038/s41467-018-03399-2>`__), as follows: mental movie, in which characters were "mentalizing"; and physical pain movie, in which characters were experiencing physical pain. Such conditions were intended to evoke brain responses from theory-of-mind and pain-matrix networks, respectively. All moments in the movie not focused on the direct interaction of the main characters were considered as a baseline period.

The conditions for this task are described in `this table <condPainMovie_>`__ and the main contrasts derived from those conditions are described in `this table <contPainMovie_>`__.

.. dropdown:: Conditions for PainMovie
   :name: condPainMovie

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - movie_pain
        - Watch movie-scene wherein characters experience physical pain
      * - movie_mental
        - Watch movie-scene wherein characters experience changes in beliefs, desires, and/or emotions

.. dropdown:: Contrasts for PainMovie
   :name: contPainMovie

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - movie_pain
        - movie with physically painful events
      * - movie_mental
        - movie with events about changes in beliefs	 desires and emotions","['visual_attention','empathy','imagined_emotional_pain','mentalization','theory-of-mind']
      * - movie_mental-pain
        - mental events vs. physically painful events

VSTM
----

.. container:: tags

   :bdg-info:`short-term_memory` :bdg-primary:`visual_orientation` :bdg-primary:`visual_form_discrimination` :bdg-primary:`visual_buffer` :bdg-light:`numerosity` 

.. admonition:: Implementation 
   :class: seealso

   - Software:  Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This battery of tasks was adapted from the control experiment described in (`Knops et al., 2014 <https://doi.org/10.1523/JNEUROSCI.2758-13.2014>`__). Minor changes were employed for the IBC implementation of this battery which have been described later in this section. In the Visual Short-Term Memory (`VSTM`_) task, participants were presented with a certain number of bars, varying from one to six. Every trial started with the presentation of a black fixation dot in the center of the screen for 0.5 seconds. While still on the screen, the black fixation dot was then displayed together with a certain number of tilted bars - variable between trials from one to six - for 0.15 seconds. Afterwards, a white fixation dot was shown for 1 second. It was next replaced by the presentation of the test stimulus for 1.7 seconds, displaying identical number of tilted bars in identical positions together with a green fixation dot. The participants were to remember the orientation of the bars from the previous sample and answer with one of the two possible button presses, i.e. respectively with the index or middle finger, depending on whether one of the bars in the current display had changed orientation by 90◦ or not, which was the case in half of the trials. The test display was replaced by another black fixation dot for a fixed duration of 3.8 seconds. Thus, the trial was 7.15 seconds long. There were seventy two trials in a run and four runs in one single session. Pairs of runs were launched consecutively. To avoid selection bias in the sequence of stimuli, the order of the trials was shuffled according to numerosity and change of orientation within runs and across participants. Both the response period and the period of the fixation dot at the end of each trial were made constant.

The conditions for this task are described in `this table <condVSTM_>`__ and the main contrasts derived from those conditions are described in `this table <contVSTM_>`__.

.. dropdown:: Conditions for VSTM
   :name: condVSTM

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - vstm_linear
        - Judge whether any bar changed orientation within two consecutive displays of bar sets on the screen, linear response to numerosity
      * - vstm_constant
        - Judge whether any bar changed orientation within two consecutive displays of bar sets on the screen, response to numerosity vs. fixation
      * - vstm_quadratic
        - Judge whether any bar changed orientation within two consecutive displays of bar sets on the screen, response to quadratic numerosity effect

.. dropdown:: Contrasts for VSTM
   :name: contVSTM

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - vstm_constant
        - visual orientation
      * - vstm_linear
        - linear effect of numerosity in visual orientation
      * - vstm_quadratic
        - quadratic effect of numerosity in visual orientation

Enumeration
-----------

.. container:: tags

   :bdg-light:`numerosity` :bdg-primary:`visual_buffer` :bdg-light:`enumeration` :bdg-info:`visual_working_memory` :bdg-primary:`shape_recognition` 

.. admonition:: Implementation 
   :class: seealso

   - Software:  Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The Enumeration task was also a part of battery of tasks was adapted from the control experiment described in (`Knops et al., 2014 <https://doi.org/10.1523/JNEUROSCI.2758-13.2014>`__). Minor changes were employed for the IBC implementation of this battery which have been described later in this section. In this task, participants were presented with a certain number of tilted dark-gray bars on a light-gray background, varying from one to eight. Every trial started with the presentation of a black fixation dot in the center of the screen for 0.5 seconds. While still on the screen, the black fixation dot was then displayed together with a certain number of tilted bars for 0.15 seconds. It was followed by a response period of 1.7s, in which only a green fixation dot was being displayed on the screen. The participants were to remember the number of the bars that were shown right before and answer accordingly, by pressing the corresponding button: once with the thumb's button for one bar; once with the index finger's button for two bars; once with the middle finger's button for three bars; once with the ring finger's button for four bars; twice with the thumb's button for five bars; twice with the index finger's button for six bars; twice with the middle finger's button for seven bars; twice with the ring finger's button for eight bars. Afterwards, another black fixation dot was displayed for a fixed duration of 7.8 seconds. The trial length was thus 9.95 seconds. There were ninety six trials in a run and two (consecutive) runs in one single session. To avoid selection bias in the sequence of stimuli, the order of the trials was shuffled according to numerosity within runs and across participants. Both the response period and the period of the fixation dot at the end of each trial were made constant. The answers were registered via a button-press response box instead of an audio registration of oral responses as in the original study.

The conditions for this task are described in `this table <condEnumeration_>`__ and the main contrasts derived from those conditions are described in `this table <contEnumeration_>`__.

.. dropdown:: Conditions for Enumeration
   :name: condEnumeration

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - enumeration_linear
        - Capture the linear effect of enumeration response to numerosity
      * - enumeration_constant
        - Occurrence regressor for the enumeration response to constant numerosity when compared against fixation
      * - enumeration_quadratic
        - Capture the quadratic effect of enumeration response to numerosity interaction

.. dropdown:: Contrasts for Enumeration
   :name: contEnumeration

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - enumeration_constant
        - enumeration
      * - enumeration_linear
        - linear effect of numerosity in enumeration
      * - enumeration_quadratic
        - quadratic effect of numerosity in enumeration

Self
----

.. container:: tags

   :bdg-info:`episodic_memory` :bdg-light:`other-reference_effect` :bdg-light:`self-reference_effect` :bdg-light:`memory	reading` :bdg-secondary:`reading` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.7.0 (Python 2.7)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The Self task was adapted from (`Genom et al., 2014 <https://doi.org/10.1016/j.cortex.2013.06.009>`__), originally developed to investigate the Self-Reference Effect in older adults. This effect pertains to the encoding mechanism of information referring to the self, characterized as a memory-advantaged process. Consequently, memory-retrieval performance is also better for information encoded in reference to the self than to other people, objects or concepts. The present task was thus composed of two phases, each of them relying on encoding and recognition procedures. The encoding phase was intended to map brain regions related to the encoding of items in reference to the self, whereas the recognition one was conceived to isolate the memory network specifically involved in the retrieval of those items. The phases were interspersed, so that the recognition phase was always related to the encoding phase presented immediately before. The encoding phase had two blocks. Each block was composed of a set of trials pertaining to the same condition. For both conditions, a different adjective was presented at every trial on the screen. The participants were to judge whether or not the adjective described themselves -- *self-reference encoding* condition-- or another person -- *other-reference encoding* condition-- by pressing with the index finger on the corresponding button of the response box for "yes" and with the middle finger for "no". The other person was a public figure in France around the same age range as the cohort, whose gender matched the gender of every participant. Two public figures were mentioned, one at the time, across all runs; four public figures --two of each gender-- were selected beforehand. By this way, we ensured that all participants were able to successfully characterize the same individuals, holding equal the levels of familiarity and affective attributes with respect to these individuals. In the recognition phase, participants were to remember whether or not the adjectives had also been displayed during the previous encoding phase, by pressing with the index finger on the corresponding button of the response box for "yes" and with the middle finger for "no". This phase was composed of a single block of trials, pertaining to three categories of conditions. *New* adjectives were presented during one half of the trials whereas the other half were in reference to the adjectives displayed in the previous phase. Thus, trials referring to the adjectives from *self-reference encoding* were part of the *self-reference recognition* category and trials referring to the *other-reference encoding* were part of the *other-reference recognition* category. 

There were four runs in one session. The first three ones had three phases; the fourth and last run had four phases. Their total durations were twelve and 15.97 seconds, respectively. Blocks of both phases started with an *instruction* condition of five seconds, containing a visual cue. The cue was related to the judgment that should be performed next, according to the type of condition featured in that block. A set of trials, showing different adjectives, were presented afterwards. Each trial had a duration of five seconds, in which a response was to be provided by the participant. During the trials of the encoding blocks, participants had to press the button with their left or right hand, depending on whether they believed or not the adjective on display described someone (i.e. self or other, respectively for *self-reference encoding* or *other-reference encoding* conditions). During the trials of the recognition block, participants had to answer in the same way, depending on whether they believed or not the adjective had been presented before. A fixation cross was always presented between trials, whose duration was jittered between 0.3 seconds and 0.5 seconds. A rest period was introduced between encoding and recognition phases, whose duration was also jittered between ten and fourteen seconds. Long intervals between these two phases, i.e. longer than ten seconds, ensured the measurement of long-term memory processes during the recognition phase, at the age range of the cohort (`Newell et al., 1972 <https://psycnet.apa.org/record/1973-10478-000>`__, `Ericsson et al., 1995 <https://doi.org/10.1037/0033-295x.102.2.211>`__). Fixation-cross periods of three and fifteen seconds were also introduced in the beginning and end of each run, respectively. Lastly, all adjectives were presented in the lexical form according to the gender of the participant. There were also two sets of adjectives. One set was presented as new adjectives during the recognition phase and the other set for all remaining conditions of both phases. To avoid cognitive bias across the cohort, sets were switched for the other half of the participants. Plus, adjectives never repeated across runs but their sequence was fixed for the same runs and across participants from the same set. Yet, pseudo-randomization of the trials for the recognition phase was pre-determined by the authors of the original study, according to their category (i.e. *self-reference recognition*, *other-reference recognition* or *new*), such that no more than three consecutive trials of the same category were presented within a block.

The conditions for this task are described in `this table <condSelf_>`__ and the main contrasts derived from those conditions are described in `this table <contSelf_>`__.

.. dropdown:: Conditions for Self
   :name: condSelf

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - instructions
        - Presentation of a question related to the succeeding block
      * - self-reference_encoding
        - Judge with overt response whether or not a certain adjective, displayed on the screen, qualifies oneself
      * - other-reference_encoding
        - Judging with overt response whether a certain adjective, displayed on the screen, qualifies someone else
      * - self-reference_recognition
        - Successful recognition with an overt response of an adjective, displayed on the screen, as having been already presented during one “self-reference encoding” trial of the preceding encoding phase
      * - other-reference_recognition
        - Successful recognition with an overt response of an adjective, displayed on the screen, as having been already presented during one “other-reference encoding” trial of the preceding encoding phase
      * - memory
        - Successful identification with an overt response that a new adjective has never been presented before
      * - no_recognition
        - Unsuccessful identification with an overt response that a new adjective has been presented before

.. dropdown:: Contrasts for Self
   :name: contSelf

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - instructions
        - read instruction in form of a question
      * - encode_self
        - encoding of adjectives processed with self-reference
      * - encode_other
        - encoding of adjectives processed with other-reference
      * - encode_self-other
        - self-reference effect
      * - recognition_hit
        - recognition of adjectives previously displayed
      * - recognition_self_hit
        - recognition of adjectives previously displayed with self-reference
      * - recognition_other_hit
        - recognition of adjectives previously displayed with other-reference
      * - recognition_self-other
        - memory retrieval of encoded information with self-reference
      * - correct_rejection
        - identification of a new adjective
      * - recognition_hit-correct_rejection
        - recognition of an adjective previously displayed
      * - false_alarm
        - erroneous response

Bang
----

.. container:: tags

   :bdg-secondary:`language_comprehension` :bdg-secondary:`_language_comprehension` :bdg-light:`social_cognition` :bdg-success:`auditory_scene_analysis` :bdg-light:`action_perception` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.9.0 (Python 2.7)
   - Audio device: MagnaCoil (Magnacoustics)

The Bang task was adapted from the study (`Campbell et al., 2015 <https://doi.org/10.1016/j.neurobiolaging.2015.07.028>`__), dedicated to investigate aging effects on neural responsiveness during naturalistic viewing. The task relies on watching - viewing and listening - of an edited version of the episode "Bang! You're Dead" from the TV series "Alfred Hitchcock Presents". The original black-and-white, 25-minute episode was condensed to seven minutes and fifty five seconds while preserving its narrative. The plot of the final movie includes scenes with characters talking to each other as well as scenes with no verbal communication. This task was performed during a single run in one unique session. Participants were never informed of the title of the movie before the end of the session. Ten seconds of acquisition were added at the end of the run. The total duration of the run was thus eight minutes and five seconds. 
**Note:** We used the MagnaCoil (Magnacoustics) audio device for all subjects except for *subject-08*, for whom we employed MRConfon MKII.

The conditions for this task are described in `this table <condBang_>`__ and the main contrasts derived from those conditions are described in `this table <contBang_>`__.

.. dropdown:: Conditions for Bang
   :name: condBang

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - talk
        - Speech: watch contiguous scenes of speech. No speech: watch contiguous scenes with no speech
      * - no_talk
        - Watch contiguous scenes with no speech

.. dropdown:: Contrasts for Bang
   :name: contBang

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - talk-no_talk
        - speech vs. non-speech sections in movie watching
      * - talk
        - speech sections in movie watching
      * - no_talk
        - non-speech section in movie watching

Clips
-----

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Python 2.7
   - Audio device: MRConfon MKII

The Clips battery stands for an adaptation of (`Nishimoto et al., 2011 <https://doi.org/10.1016/j.cub.2011.08.031>`__), in which participants were to visualize naturalistic scenes edited as video clips of ten and a half minutes each. Each run was always dedicated to the data collection of one video clip at a time. As in the original study, runs were grouped in two tasks pertaining to the acquisition of training data and test data, respectively. Scenes from training-clips (ClipsTrn) task were shown only once. Contrariwise, scenes from the test-clips (ClipsVal) task were composed of approximately one-minute-long excerpts extracted from the clips presented during training. Excerpts were concatenated to construct the sequence of every ClipsVal run; each sequence was predetermined by randomly permuting many excerpts that were repeated ten times each across all runs. The same randomized sequences, employed across ClipsVal runs, were used to collect data from all participants. There were twelve and nine runs dedicated to the collection of the ClipsTrn and ClipsVal tasks, respectively. Data from nine runs of each task were interspersedly acquired in three full sessions; the three remaining runs devoted to train-data collection were acquired in half of one last session, before the `Wedge`_ and `Ring`_ tasks. To assure the same topographic reference of the visual field for all participants, a colored fixation point was always presented at the center of the images. Such point was changing three times per second to ensure that it was visible regardless the color of the movie. Ten and twenty extra seconds of acquisition were respectively added at the beginning and end of every run. The total duration of each run was thus ten minutes and fifty seconds.


Wedge
-----

.. container:: tags

   :bdg-primary:`lower-left_vision` :bdg-primary:`upper-left_vision` :bdg-primary:`lower-right_vision` :bdg-primary:`visual_color_discrimination` :bdg-primary:`upper-right_vision` 

.. admonition:: Implementation 
   :class: seealso

   - Software:  Psychopy (Python 2.7)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The Retinotopy tasks refer to the classic retinotopic paradigms - the Wedge and the Ring tasks - consisting of two kinds of visual stimuli as part of the Wedge task: a slowly rotating clockwise or counterclockwise and semicircular checkerboard stimulus. The phase of the periodic response at the rotation or dilation/contraction frequency measured at each voxel relates to the measurement of the perimetric parameters concerning polar angle and eccentricity, respectively (`Sereno et al., 1995 <https://doi.org/10.1126/science.7754376>`__). Under IBC, four runs were devoted to this task (two runs for each direction). Each of them were five-and-a-half minutes long. They were programmed for the same session following the last three "training-data" runs of the `Clips`_ task. Similarly to the Clips task, a point was displayed at the center of the visual stimulus in order to keep constant the perimetric origin in all participants. Participants were thus to fixate continuously this point whose color flickered between red, green, blue and yellow throughout the entire run. To keep the participants engaged in the task, they were instructed that, after each run (i.e. after MRI acquisition was finished), they would be asked which color had most often been presented. Additionally, ten seconds of a non-flickering, red fixation cross were displayed at the end of every run.

The conditions for this task are described in `this table <condWedge_>`__ and the main contrasts derived from those conditions are described in `this table <contWedge_>`__.

.. dropdown:: Conditions for Wedge
   :name: condWedge

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - lower_meridian
        - Visual representation in the lower half-plane of the visual field delimited by its horizontal meridian
      * - upper_meridian
        - Visual representation in the upper half-plane of the visual field delimited by its horizontal meridian
      * - lower_right
        - Visual representation in the lower-right quadrant of the visual field delimited by its vertical and horizontal meridians
      * - upper_left
        - Visual representation in the upper-left quadrant of the visual field delimited by its vertical and horizontal meridians
      * - right_meridian
        - Visual representation in the right half-plane of the visual field delimited by its vertical meridian
      * - left_meridian
        - Visual representation in the left half-plane of the visual field delimited by its vertical meridian
      * - upper_right
        - Visual representation in the upper-right quadrant of the visual field delimited by its vertical and horizontal meridians
      * - lower_left
        - Visual representation in the lower-left quadrant of the visual field delimited by its vertical and horizontal meridians

.. dropdown:: Contrasts for Wedge
   :name: contWedge

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - lower_meridian
        - visual representation in the lower half-plane of the visual field delimited by its horizontal meridian
      * - upper_meridian
        - visual representation in the upper half-plane of the visual field delimited by its horizontal meridian
      * - lower_right
        - visual representation in the lower-right quadrant of the visual field delimited by its vertical and horizontal meridians
      * - upper_left
        - visual representation in the upper-left quadrant of the visual field delimited by its vertical and horizontal meridians
      * - right_meridian
        - visual representation in the right half-plane of the visual field delimited by its vertical meridian
      * - left_meridian
        - visual representation in the left half-plane of the visual field delimited by its vertical meridian
      * - upper_right
        - visual representation in the upper-right quadrant of the visual field delimited by its vertical and horizontal meridians
      * - lower_left
        - visual representation in the lower-left quadrant of the visual field delimited by its vertical and horizontal meridians

Ring
----

.. container:: tags

   :bdg-primary:`mid-peripheral_vision` :bdg-primary:`visual_color_discrimination` :bdg-primary:`far-peripheral_vision` :bdg-primary:`foveal_vision` 

.. admonition:: Implementation 
   :class: seealso

   - Software:  Psychopy (Python 2.7)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The Retinotopy tasks refer to the classic retinotopic paradigms - the Wedge and the Ring tasks - consisting of two kinds of visual stimuli as part of the Ring task: a thick, dilating or contracting ring. The phase of the periodic response at the rotation or dilation/contraction frequency measured at each voxel relates to the measurement of the perimetric parameters concerning polar angle and eccentricity, respectively (`Sereno et al., 1995 <https://doi.org/10.1126/science.7754376>`__). Under IBC, two runs were devoted to this task (two runs for each direction). Each of them were five-and-a-half minutes long. They were programmed for the same session following the last three "training-data" runs of the `Clips`_ task. Similarly to the Clips task, a point was displayed at the center of the visual stimulus in order to keep constant the perimetric origin in all participants. Participants were thus to fixate continuously this point whose color flickered between red, green, blue and yellow throughout the entire run. To keep the participants engaged in the task, they were instructed that, after each run (i.e. after MRI acquisition was finished), they would be asked which color had most often been presented. Additionally, ten seconds of a non-flickering, red fixation cross were displayed at the end of every run.

The conditions for this task are described in `this table <condRing_>`__ and the main contrasts derived from those conditions are described in `this table <contRing_>`__.

.. dropdown:: Conditions for Ring
   :name: condRing

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - foveal
        - Visual representation in the fovea
      * - middle
        - Visual representation in the mid-periphery of the visual field
      * - peripheral
        - Visual representation in the far-periphery of the visual field

.. dropdown:: Contrasts for Ring
   :name: contRing

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - foveal
        - visual representation in the fovea
      * - middle
        - visual representation in the mid-periphery of the visual field
      * - peripheral
        - visual representation in the far-periphery of the visual field

Raiders
-------

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.9.0 (Python 2.7)
   - Audio device: MRConfon MKII

The Raiders task was adapted from (`Haxby et al., 2011 <http://doi.org/10.1016/j.neuron.2011.08.026>`__), in which the full-length action movie Raiders of the Lost Ark was presented to the participants. The main goal of the original study was the estimation of the hyperalignment parameters that transform voxel space of functional data into feature space of brain responses, linked to the visual characteristics of the movie displayed. Similarly, herein, the movie was shown to the IBC participants in contiguous runs determined according to the chapters of the movie defined in the DVD. This task was completed in two sessions. In order to use the acquired fMRI data in train-test split and cross-validation experiments, we performed three extra-runs at the end of the second session in which the three first chapters of the movie were repeated. To account for stabilization of the BOLD signal, ten seconds of acquisition were added at the end of the run.


Lec2
----

.. container:: tags

   :bdg-secondary:`language_comprehension` :bdg-secondary:`word_maintenance` :bdg-secondary:`reading` :bdg-info:`working_memory` :bdg-light:`inhibition` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
Originally described in (`Perrone-Bertolotti et al., 2012 <https://doi.org/10.1523/JNEUROSCI.2982-12.2012>`__), this task focuses on silent reading. During the task, participants were presented with two intermixed stories, shown word by word at a rapid rate. One of the stories was written in black (on a gray screen) and the other in white. Consecutive words with the same color formed a meaningful and simple short story in French. Participants were instructed to read the black story to report it at the end of the block, while ignoring the white one. Each block comprised 400 words, with 200 black words (attend condition) and 200 white words (ignore condition) for the two stories. The time sequence of colors within the 400 words series was randomized, so that participants could not predict whether the subsequent word was to be attended or not; however, the randomization was constrained to forbid series of more than three consecutive words with the same color. Data was acquired in two runs, and each word was presented for 100 ms, with a jittered inter-stimulus interval centered around 700 ms.

The conditions for this task are described in `this table <condLec2_>`__ and the main contrasts derived from those conditions are described in `this table <contLec2_>`__.

.. dropdown:: Conditions for Lec2
   :name: condLec2

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - unattend
        - A white word is rapidly presented and the participant must ignore it
      * - attend
        - A black word is rapidly presented and the participant must silently read it to form a short story together with the rest of black words

.. dropdown:: Contrasts for Lec2
   :name: contLec2

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - attend
        - response to attended text
      * - unattend
        - response to unattended text
      * - attend-unattend
        - response to attended vs. unattended text

Audi
----

.. container:: tags

   :bdg-secondary:`language_comprehension` :bdg-secondary:`semantic_processing` :bdg-success:`sound_perception` :bdg-success:`voice_perception` :bdg-success:`auditory_sentence_recognition` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Audio device: MagnaCoil (Magnacoustics)

This task was originally described in (`Perrone-Bertolotti et al., 2012 <https://doi.org/10.1523/JNEUROSCI.2982-12.2012>`__) together with the `Lec2`_ localizer. Participants listened to sounds of several categories with the instruction that three of them would be presented again at the end of the task, together with three novel sounds and that they should be able to detect previously played items. There were three speech and speech-like categories, including sentences told by a computerized voice in a language familiar to the participant (French) or unfamiliar (Suomi), and reversed speech, originally in French (the same sentences as the "French" category, played backwards). These categories were compared with nonspeech-like human sounds (coughing and yawning), music, environmental sounds, and animal sounds. Participants were instructed to close their eyes while listening to three sounds of each category, with a duration of 12s each, along with three 12 s intervals with no stimulation, serving as a baseline (Silence). Consecutive sounds were separated by a 3 s silent interval. The sequence was pseudorandom, to ensure that two sounds of the same category did not follow each other.

The conditions for this task are described in `this table <condAudi_>`__ and the main contrasts derived from those conditions are described in `this table <contAudi_>`__.

.. dropdown:: Conditions for Audi
   :name: condAudi

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - tear
        - Concatenated sounds of people crying
      * - suomi
        - Suomi speech stimuli
      * - yawn
        - Concatenated sounds of people yawning
      * - human
        - Other human sounds
      * - silence
        - Silence, used as a baseline
      * - music
        - Real-life complex musical sounds
      * - reverse
        - French speech stimuli played in reverse
      * - speech
        - French speech stimuli
      * - alphabet
        - French voice saying the alphabet
      * - cough
        - Concatenated sounds of people coughing
      * - environment
        - Real-life complex environmental sounds
      * - laugh
        - Concatenated sounds of people laughing
      * - animals
        - Real-life animal sounds

.. dropdown:: Contrasts for Audi
   :name: contAudi

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - tear
        - listen to tears
      * - suomi
        - listen to unknown language
      * - yawn
        - listen to yawning
      * - human
        - listen to human sounds
      * - silence
        - listen to silence
      * - music
        - listen to music
      * - reverse
        - listen to reversed speech
      * - speech
        - listen to speech
      * - alphabet
        - listen to letters
      * - cough
        - listen to coughing
      * - environment
        - listen to environment sounds
      * - laugh
        - listen to laugh
      * - animals
        - listen to animals
      * - tear-silence
        - listen to tears
      * - suomi-silence
        - listen to unknown language
      * - yawn-silence
        - listen to yawning
      * - human-silence
        - listen to human sounds
      * - music-silence
        - listen to music
      * - reverse-silence
        - listen to reversed speech
      * - speech-silence
        - listen to speech
      * - alphabet-silence
        - listen to letters
      * - cough-silence
        - listen to coughing
      * - environment-silence
        - listen to environment sounds
      * - laugh-silence
        - listen to laugh
      * - animals-silence
        - listen to animals

Visu
----

.. container:: tags

   :bdg-secondary:`reading` :bdg-primary:`visual_string_recognition` :bdg-light:`object_recognition` :bdg-primary:`visual_scene_perception` :bdg-primary:`visual_representation` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
This task, described in (`Vidal et al., 2010 <https://doi.org/10.3389/fnhum.2010.00195>`__), is a visual odd-ball paradigm, in which participants were instructed to press a button (index finger) every time they see a fruit. Images of the target category and other non-target categories were rapidly presented in a pre-randomized order. Stimuli were presented for a duration of 200ms every 1000-1200ms in series of 5 pictures interleaved by 3-second pause periods during which patients could freely blink. Each non-target category was presented 50 times during the experiment, and data was acquired in two separated runs.

The conditions for this task are described in `this table <condVisu_>`__ and the main contrasts derived from those conditions are described in `this table <contVisu_>`__.

.. dropdown:: Conditions for Visu
   :name: condVisu

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - scrambled
        - Scrambled image, used as baseline
      * - face
        - Viewing the image of a human face
      * - characters
        - Viewing a string of random characters
      * - scene
        - Viewing the image of a naturalistic scene
      * - house
        - Viewing the image of a house
      * - animal
        - Viewing the image of an animal
      * - pseudoword
        - Viewing a string that conforms a pseudoword
      * - tool
        - Viewing the image of a tool
      * - fruit
        - Viewing the image of a fruit

.. dropdown:: Contrasts for Visu
   :name: contVisu

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - scrambled
        - view a scrambled image
      * - face-scrambled
        - view a face image
      * - characters-scrambled
        - view characters
      * - scene-scrambled
        - view a scene
      * - house-scrambled
        - view a house
      * - animal-scrambled
        - view an animal
      * - pseudoword-scrambled
        - view a pseudoword
      * - tool-scrambled
        - view a tool
      * - scene
        - view a scene
      * - tool
        - view a tool
      * - face
        - view a face image
      * - target_fruit
        - view a target object
      * - house
        - view a house
      * - animal
        - view an animal
      * - characters
        - view characters
      * - pseudoword
        - view a pseudoword

Lec1
----

.. container:: tags

   :bdg-secondary:`semantic_processing` :bdg-secondary:`reading` :bdg-primary:`visual_string_recognition` :bdg-primary:`visual_word_recognition` :bdg-primary:`visual_pseudoword_recognition` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

   - Audio device: MagnaCoil (Magnacoustics)

This task, described in (`Saignavong et al., 2017 <https://doi.org/10.1142/S0129065717500010>`__), was originally used to test whether brain activity can be deteted in single trials with intracerebral EEG-fMRI recordings. During the task, participants were presented with three vertically-arranged lines, indicated by the presence of two "+" symbols at both sides, and empty space between them. For each row, a different type of verbal stimulli was presented, and the participant was instructed to make a decission depending on the type of stimuli. The top row presented words, and the decision was an animacy decision ("Is it a living entity?"). The middle row presented pseudowords, and the decision was whether the pseudoword had one or two syllabes. Finally, the bottom row presented consonant strings, and participants were instructed to answer if the string was all-uppercase or all-lowercase. First option was selected by pressing with the index finger on the response box whereas second option was given with the middle finger. The trials were presented in blocks, and each block contained a sequence of 5 stimuli for each of the three conditions. The order of this conditions inside each block was randomized across blocks, but fixed for all participants. The "+" symbols for the row corresponding to the next condition turned white to indicate which condition was next. There were two runs with 6 blocks each, each block comprising 15 trials, which were presented for 2000 ms, with an inter-stimulus interval of 500 ms.

The conditions for this task are described in `this table <condLec1_>`__ and the main contrasts derived from those conditions are described in `this table <contLec1_>`__.

.. dropdown:: Conditions for Lec1
   :name: condLec1

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - random_string
        - A string of random consonants is presented and the participant has to answer if it is all-uppercase or all-lowercase
      * - word
        - A word is presented and the participant has to decide whether it is a living entity or not
      * - pseudoword
        - A pseudoword in presented and the participant has to answer whether it has one or two syllables

.. dropdown:: Contrasts for Lec1
   :name: contLec1

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - word
        - read a word 
      * - random_string
        - read a random string
      * - pseudoword
        - read a pseudoword
      * - word-random_string
        - read a word vs. a random string
      * - word-pseudoword
        - read a word vs. a pseudoword
      * - pseudoword-random_string
        - read a pseudoword vs. a random string

MVEB
----

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-light:`numerosity` :bdg-info:`visual_working_memory` :bdg-primary:`visual_buffer` :bdg-light:`string_maintenance` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task, described in (`Hamamé et al., 2012 <https://doi.org/10.1016/j.neuroimage.2011.07.087>`__), aims to assess verbal working memory (the name stands for "verbal working memory task"). In this case, the participants were presented with a string of 6 characters, from where two, four or six of them can be letters (the rest are "#" symbols). After the string disappears, a single letter appears in screen. The participant had then to indicate if this single letter was part of the previously presented string. This was indicated by the participant with a 5-button response box, with one button for "yes" (index finger) and another for "no" (middle finger). The cognitive load was manipulated with the number of letters, and one condition was included where all the letters of the initial string would be the same one. Each trial commenced with the presentation of a 1500 ms fixation cross, followed by the array of characters (probe) for 1500 ms. After an intermediate period of 3000 ms, and the cue character was presented for 1500 ms. 36 trials were presented in each run. Data was acquired in two separated runs.

The conditions for this task are described in `this table <condMVEB_>`__ and the main contrasts derived from those conditions are described in `this table <contMVEB_>`__.

.. dropdown:: Conditions for MVEB
   :name: condMVEB

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - letter_occurrence_response
        - Subject's index finger response, indicating whether the letter was part of of the previously presented string
      * - 2_letters_different
        - The subject must remember 2 characters from a presented string of different letters
      * - 4_letters_different
        - The subject must remember 4 characters from a presented string of different letters
      * - 6_letters_different
        - The subject must remember 6 characters from a presented string of different letters
      * - 2_letters_same
        - The subject must remember the presented character from a string of 2 identical letters
      * - 4_letters_same
        - The subject must remember the presented character from a string of 4 identical letters
      * - 6_letters_same
        - The subject must remember the presented character from a string of 6 identical letters

.. dropdown:: Contrasts for MVEB
   :name: contMVEB

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - letter_occurrence_response
        - respond by button pressing whether the letter currently displayed was presented before or not
      * - 2_letters_different
        - maintaining two letters
      * - 4_letters_different
        - maintaining four letters
      * - 6_letters_different
        - maintaining six letters
      * - 2_letters_same
        - maintaining one letter
      * - 4_letters_same
        - maintaining one letter
      * - 6_letters_same
        - maintaining one letter
      * - 2_letters_different-same
        - maintaining two letters vs. one
      * - 4_letters_different-same
        - maintaining four letters vs. one
      * - 6_letters_different-same
        - maintaining six letters vs. one
      * - 6_letters_different-2_letters_different
        - maintaining six letters vs. two

MVIS
----

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-info:`spatial_working_memory` :bdg-light:`numerosity` :bdg-info:`visual_working_memory` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task, described in (`Hamamé et al., 2012 <https://doi.org/10.1016/j.neuroimage.2011.07.087>`__), and whose name stands for "visuo-spatial working memory" task, consists on a series of events in which the participant will be presented with a 4x4 grid in which two, four or six dots will appear at different positions, after that, the grid would become empty and finally a single dot would appear on it. The participant had then to indicate if this single dot was in the same position than any of the previously presented ones. This was indicated by the participant with a 5-button response box, with one button for "yes" (index finger) and another for "no" (middle finger). The cognitive load was manipulated with the number of dots, and one condition was included where one of the dots would be highlighted, signifying that was the only position to retain. Each trial commenced with the presentation of a 1500 ms fixation cross, followed by the array of dots (probe) for 1500 ms. The empty grid was presented for 3000ms, and the cue dot was presented for 1500 ms. 36 trials were presented on each run. The data was acquired in two runs.

The conditions for this task are described in `this table <condMVIS_>`__ and the main contrasts derived from those conditions are described in `this table <contMVIS_>`__.

.. dropdown:: Conditions for MVIS
   :name: condMVIS

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - dot_displacement_response
        - Subject's index finger response, indicating whether the dot was in the same position as any of the previously presented ones
      * - 2_dots
        - 2 positions to remember
      * - 2_dots_control
        - 1 position to remember because of the highlighted dot
      * - 4_dots
        - 4 positions to remember
      * - 4_dots_control
        - 1 position to remember because of the highlighted dot
      * - 6_dots
        - 6 positions to remember
      * - 6_dots_control
        - 1 position to remember because of the highlighted dot

.. dropdown:: Contrasts for MVIS
   :name: contMVIS

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - dot_displacement_response
        - respond by button pressing whether the dot currently displayed share the same location as any of those shown before
      * - dots-control
        - maintain position of two to six dots vs. one
      * - 2_dots-2_dots_control
        - maintain position of two dots vs. one
      * - 4_dots-4_dots_control
        - maintain position of four dots vs. one
      * - 6_dots-6_dots_control
        - maintain position of six dots vs. one
      * - 6_dots-2_dots
        - maintain position of six dots vs. two

Moto
----

.. container:: tags

   :bdg-secondary:`reading` :bdg-warning:`saccadic_eye_movement` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: In-house custom-made sticks featuring one-top button, each one to be used in each hand

This task is a basic motor localizer for several body parts. The participants are presented with three small gray squares over a black background image. At the beginning of each block, a text prompt will appear on screen to indicate the body part that will be moved next. Afterwards, the left and right squares will turn white to indicate movement of the corresponding part. For example, for the hands condition, the participant is required to perform a small movement of the left hand when the left square turns white, and likewise for the right hand. Ten movements were prompted for each block, five for the right body part and five for the left, consecutively for each direction and always in the same order. There were two distinct blocks for each body part. For each trial, the white square was presented during 1000 ms, with 1500 ms between trials, for a total duration of 25 s per block, with a total of 12 blocks. Data was acquired in two separated runs.

The conditions for this task are described in `this table <condMoto_>`__ and the main contrasts derived from those conditions are described in `this table <contMoto_>`__.

.. dropdown:: Conditions for Moto
   :name: condMoto

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - finger_right
        - Movement of the right index finger, indicated by a button-press
      * - finger_left
        - Movement of the left index finger, indicated by a button-press
      * - foot_left
        - Movement of the left foot
      * - foot_right
        - Movement of the right foot
      * - hand_left
        - Movement of the left hand
      * - hand_right
        - Movement of the right hand
      * - saccade_left
        - Movement of the eyes to the left
      * - saccade_right
        - Movement of the eyes to the right
      * - tongue_left
        - Movement of the tongue to the left
      * - tongue_right
        - Movement of the tongue to the right
      * - fixation
        - Gaze fixation on the central square

.. dropdown:: Contrasts for Moto
   :name: contMoto

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - instructions
        - read instructions
      * - finger_right-fixation
        - right finger tapping vs. any movement
      * - finger_left-fixation
        - left finger tapping vs. any movement
      * - foot_left-fixation
        - move left foot vs. any movement
      * - foot_right-fixation
        - move right foot vs. any movement
      * - hand_left-fixation
        - move left hand vs. any movement
      * - hand_right-fixation
        - move right hand vs. any movement
      * - saccade-fixation
        - saccade vs. any movement
      * - tongue-fixation
        - move tongue vs. any movement

MCSE
----

.. container:: tags

   :bdg-light:`salience` :bdg-primary:`lower-left_vision` :bdg-primary:`upper-left_vision` :bdg-primary:`visual_localization` :bdg-primary:`lower-right_vision` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task described in (`Ossandón et al., 2012 <https://doi.org/10.1523/JNEUROSCI.6048-11.2012>`__) was originally used to study whether visual search processes of a salient target can be thought as a purely bottom-up process, or if it requires action from top-down attentional processess. The task consisted in the presentation of an array of 35 "L" letters, rotated at different angles, together with a target "T" letter (total 36 stimuli in each trial). Subjects were instructed to search for the target and indicate whether it was on the left or right side of the grid, by pressing respectively with the index or middle finger on a 5-button response box. There were two conditions: high-salience (the target is gray while the other stimuli is black) and low-salience (all stimuli are gray). The two conditions were presented alternatively in blocks, with 6 blocks of 10 trials each. Each trial was presented for 3 s with an inter-stimulus interval of 1 s. There was also a 20 s fixation cross between blocks. Data was acquired in two separated runs.

The conditions for this task are described in `this table <condMCSE_>`__ and the main contrasts derived from those conditions are described in `this table <contMCSE_>`__.

.. dropdown:: Conditions for MCSE
   :name: condMCSE

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - high_salience_left
        - Looking for a salient letter in the left visual field
      * - high_salience_right
        - Looking for a salient letter in the right visual field
      * - low_salience_left
        - Looking for a non-salient letter in the left visual field
      * - low_salience_right
        - Looking for a non-salient letter in the right visual field

.. dropdown:: Contrasts for MCSE
   :name: contMCSE

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - high_salience_left
        - looking for a salient symbol in left visual field
      * - high_salience_right
        - looking for a salient symbol in right visual field
      * - low_salience_left
        - looking for a low-salient symbol in left visual field
      * - low_salience_right
        - looking for a low-salient symbol in right visual field
      * - salience_left-right
        - looking for a symbol in left vs. right visual field
      * - salience_right-left
        - looking for a symbol in right vs. left visual field
      * - low+high_salience
        - looking for a symbol
      * - low-high_salience
        - looking for a low-salient symbol
      * - high-low_salience
        - looking for a high-salient symbol

Audio
-----

.. container:: tags

   :bdg-success:`sound_perception` :bdg-success:`voice_perception` :bdg-success:`listening` :bdg-success:`speech_perception` :bdg-success:`auditory_attention` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.9.0 (Python 3.6)
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

   - Audio device: MagnaCoil (Magnacoustics)

This task, originally described in (`Santoro et al., 2017 <https://doi.org/10.1073/pnas.1617622114>`__), is an auditory localizer. During each run, the participants were presented with sounds from different categories, and were instructed to press a button with the index finger whenever two consecutive sounds were identical. From a group of 288 sounds, divided into 6 different categories, 4 sets were created. Each set contained 72 sounds of each of the categories, and each one was present only in one of the sets. Furthermore, each set was pre-randomized in 3 different orders, and the same sequences were used for all participants. On top of the 72 sounds, each run also included 5 silences and 5 repeated sounds from the original 72. In total, each run consisted of 82 trials of 2 seconds each. It is important to note that the data for this task was acquired using an interrupted acquisition sequence, to minimize the effect that scanner noise can have in the auditory processing targeted by the experiment. To this end, the inter-stimulus interval was programmed in a sequence of 4, 4, and 6 seconds, meaning that the interval between stimuli would be 4s for the first trial, 4s for the second, 6s for the third, and then the sequence repeats until the end of the run. The variability of the ISI and the silence trials avoided stimulus' presentation to be predictable in time. 
**Note:** We used the MagnaCoil (Magnacoustics) audio device for all subjects except for *subject-08*, for whom we employed Optoacoustics.

The conditions for this task are described in `this table <condAudio_>`__ and the main contrasts derived from those conditions are described in `this table <contAudio_>`__.

.. dropdown:: Conditions for Audio
   :name: condAudio

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - animal
        - Sound of animal noises
      * - music
        - Musical sound
      * - nature
        - Naturalistic sound
      * - speech
        - Human speech sound
      * - tool
        - Sound of tool usage
      * - voice
        - Non-speech human sound
      * - catch
        - Repetition of the previous sound
      * - silence
        - No sound

.. dropdown:: Contrasts for Audio
   :name: contAudio

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - animal
        - listen to animals
      * - music
        - listen to music
      * - nature
        - listen to nature
      * - speech
        - listen to speech
      * - tool
        - listen to tool
      * - voice
        - listen to voice
      * - animal-others
        - listen to animals vs. other sounds
      * - music-others
        - listen to music vs. other sounds
      * - nature-others
        - listen to nature vs. other sounds
      * - speech-others
        - listen to speech vs. other sounds
      * - tool-others
        - listen to tool vs. other sounds
      * - voice-others
        - listen to voice vs. other sounds 
      * - mean-silence
        - listening to sounds vs. silence
      * - animal-silence
        - listen to animals vs. silence
      * - music-silence
        - listen to music vs. silence
      * - nature-silence
        - listen to nature vs. silence
      * - speech-silence
        - listen to speech vs. silence
      * - voice-silence
        - listen to voice vs. silence 
      * - tool-silence
        - listen to tool vs. silence 

Attention
---------

.. container:: tags

   :bdg-warning:`saccadic_eye_movement` :bdg-light:`selective_attention` :bdg-light:`spatial_attention` :bdg-light:`attentional_focusing` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `experiment factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. The Attention is a version of the classical flanker task (`Eriksen and Eriksen, 1974 <https://doi.org/10.3758/BF03203267>`__), where the participant has to judge the direction the target flanker (an arrow) is pointing to (left/right). The target flanker is surrounded by other 4 flankers that can be congruent or incongruent with the target one, thus capturing selective attention and inhibitory processes. Two different buttons (index and middle fingers' button, respectively) were assigned to left/right responses, and the participant had to indicate the direction of the central arrow from an horizontal group of 5 arrows. In each trial, one or two positional cues were presented above and below the center of the screen. When one cue was given, the flankers would appear centered around it, whereas when two cues where presented, the flankers would appear centered around one of them. The four flankers surrounding the target would always point to the same direction, and can be congruent or incongruent with the direction the target flanker is facing. The task was acquired in two runs, within the same session as other tasks from the battery and using different phase-encoding directions. 
For the original version of this task, the authors provide a `simulator <https://expfactory.github.io/v1/attention_network_task.html>`__, which contains the original design.

The conditions for this task are described in `this table <condAttention_>`__ and the main contrasts derived from those conditions are described in `this table <contAttention_>`__.

.. dropdown:: Conditions for Attention
   :name: condAttention

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - spatial
        - The stimulus is spatially cued, so the subject knows where the arrows will be shown (only one star appears).
      * - double_cue
        - The stimulus is not spatially cued, so the subject doesn't know where the arrows will be shown (both stars appear).
      * - congruent
        - The stimulus is congruent (same direction) with the rest of the arrows shown.
      * - incongruent
        - The stimulus is not congruent (opposite direction) with the rest of the arrows shown.

.. dropdown:: Contrasts for Attention
   :name: contAttention

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - spatial_cue-double_cue
        - cued vs. uncued probe
      * - spatial_cue
        - cued probe
      * - incongruent-congruent
        - ignore distractors vs. no distractors
      * - double_incongruent-double_congruent
        - ignore distractors vs. no distractors without spatial cue
      * - double_congruent
        - no spatial cue + no distractors in the probe
      * - double_incongruent
        - no spatial cue + distractors in the probe
      * - double_cue
        - cues appear in both possible location of the probe at the same time
      * - spatial_incongruent-spatial_congruent
        - ignore distractors vs. no distractors with spatial cue
      * - spatial_incongruent
        - cued probe with distractors in the probe
      * - spatial_congruent
        - cued  probe	 no distractors","['spatial_attention','attentional_focusing','saccadic_eye_mocement','response_selection','response_execution']

StopSignal
----------

.. container:: tags

   :bdg-primary:`shape_perception` :bdg-light:`proactive_control` :bdg-primary:`shape_recognition` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `experiment factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. StopSignal task was originally used to localize activation relative to inhibition of a prominent motor response (`Bissett and Logan, 2011 <https://doi.org/10.1037/a0021800>`__). Four different polygonal shapes composed the set from which one of them was presented in each trial. Two of them were assigned to the button corresponding to the index finger, and two of them to the button corresponding to the middle finger. The participants were instructed to press the correct button as fast as possible, except if a red-colored star appeared on top of the target stimulus. There were 12 practice trials followed by 123 test trials divided in 3 blocks of 41 trials each, with a resting period of 9 seconds in between blocks. During practice, feedback was provided to indicate correct and incorrect responses, as well as to indicate if the responses were too slow. No stop trials (red star) were present during practice, although the instructions pertaining the red star were presented before practice. This was to build a predominant motor response in order to better capture inhibitory processes. There was a jittered delay between the stop signal and the target stimulus in stop trials that ranged from 400 to 1000 ms. The duration of the stop signal was fixed to 500 ms, the duration of the target stimulus was 850 ms and there was a fixation cross between trials centered around 2250 ms. The task was acquired in two runs, within the same session as other tasks from the battery and using different phase-encoding directions. 
For the original version of this task, the authors provide a `simulator <https://expfactory.github.io/v1/stop_signal.html>`__ which contains the original design.

The conditions for this task are described in `this table <condStopSignal_>`__ and the main contrasts derived from those conditions are described in `this table <contStopSignal_>`__.

.. dropdown:: Conditions for StopSignal
   :name: condStopSignal

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - go
        - Answer to the stim
      * - stop
        - Hold motor response

.. dropdown:: Contrasts for StopSignal
   :name: contStopSignal

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - go
        - shape recognition
      * - stop
        - shape recognition	 stopped response","['shape_recognition','proactive_control','response_inhibition','response_selection','response_execution']
      * - stop-go
        - response inhibition

TwoByTwo
--------

.. container:: tags

   :bdg-light:`cue_switch` :bdg-primary:`visual_perception` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `Experiment Factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. TwoByTwo protocol aimed to study the responses to task-switching and cue-switching in every trial, with the aim to asses the activity elicted by switching either or both task and cue, and how switching one affects the response to the other. It consisted of presenting colored single-digit numbers from 1 to 9, preceded by a cue string indicating which task must be performed. For each trail, the task could either be to judge if the number is greater or less than 5; or to judge whether the digit shown is colored in blue or orange. For each of the two tasks, two different strings could be used as cue: for the first, the cue could display either 'Magnitude' or 'High/Low', both strings indicating the participant must judge the quantity; for the second task, the subject could read either 'Color' or 'Orange/Blue' as cues, both strings indicating the task is to judge the color. Two different buttons (index/middle finger) were assigned to the orange/high and blue/low options, respectively. The task is composed by 16 practice trials, followed by 240 trials divided in 3 blocks of 80 trials each. The order of cue and task switching was randomized. The task was acquired in two runs, within the same session as other tasks from the battery and using different phase-encoding directions. 
For the original version of this task, the authors provide a `simulator <https://expfactory.github.io/v1/threebytwo.html>`__, it contains a slightly different version of the task in which they switch between three different tasks instead of two. 

The conditions for this task are described in `this table <condTwoByTwo_>`__ and the main contrasts derived from those conditions are described in `this table <contTwoByTwo_>`__.

.. dropdown:: Conditions for TwoByTwo
   :name: condTwoByTwo

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - cue_taskstay_cuestay
        - Appearance of the cue on screen when both the task and the cue are the same with respect to the previous trial
      * - cue_taskstay_cueswitch
        - Appearance of the cue on screen when only the cue switches with respect of the previous trial, for example the color task is repeated but the cue changes from 'Color’ to 'Orange/Blue’
      * - cue_taskswitch_cuestay
        - Appearance of the cue on screen when the task switches but the cue stays the same it was the previous trial for that task. For example, the task switches from color to number and the presented cue is the same as the previous number trial
      * - cue_taskswitch_cueswitch
        - Appearance of the cue on screen when both the task and the cue switch, for example the task goes from color to number and the cue changes from 'Magnitude’ to 'High/Low' compared to the previous number trial
      * - stim_taskstay_cuestay
        - Appearance of the stimulus on screen when both the task and the cue are the same with respect to the previous trial
      * - stim_taskstay_cueswitch
        - Appearance of the stimulus on screen when only the cue switches with respect of the previous trial, for example the color task is repeated but the cue changes from 'Color’ to 'Orange/Blue'
      * - stim_taskswitch_cuestay
        - Appearance of the stimulus on screen when the task switches but the cue stays the same it was the previous trial for that task. For example, the task switches from color to number and the presented cue is the same as the previous number trial
      * - stim_taskswitch_cueswitch
        - Appearance of the stimulus on screen when both the task and the cue switch, for example the task goes from color to number and the cue changes from 'Magnitude’ to 'High/Low' compared to the previous number trial

.. dropdown:: Contrasts for TwoByTwo
   :name: contTwoByTwo

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - cue_taskstay_cuestay
        - both task and cue repeats
      * - cue_taskswitch_cueswitch
        - both task and cue switch
      * - cue_taskswitch_cuestay
        - both task and cue switch
      * - cue_taskstay_cueswitch
        - task repeats	 cue switch","['visual_perception','response_selection','response_execution','cue_switch']
      * - stim_taskstay_cuestay
        - both task and cue repeats
      * - stim_taskswitch_cueswitch
        - both task and cue switch
      * - stim_taskswitch_cuestay
        - both task and cue switch
      * - stim_taskstay_cueswitch
        - task repeats	 cue switch","['visual_perception','response_selection','response_execution','cue_switch']
      * - task_switch-stay
        - effect of task switch
      * - cue_switch-stay
        - effect of cur switch

Discount
--------

.. container:: tags

   :bdg-dark:`incentive_salience` :bdg-light:`selective_control` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `experiment factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. Discount is a a decision-making task, where the participant has to decide whether to take a figurative amount of 20 dollars today or a bigger amount in a set number of days. The task is composed by 1 practice trial, followed by 120 test trials divided in 2 blocks of 60 trials each. The amount of money and the number of days is different for each trial. Each trial lasts for 4 seconds. The task was acquired in two runs, within the same session as other tasks from the battery and using different phase-encoding directions. 
For the original version of this task, the authors provide a `simulator <https://expfactory.github.io/v1/discount_titrate.html>`__, it contains a slightly different version of the task in which they ask participants to choose between two different amounts on different periods, instead of the set 20-dollars-today set-up.

The conditions for this task are described in `this table <condDiscount_>`__ and the main contrasts derived from those conditions are described in `this table <contDiscount_>`__.

.. dropdown:: Conditions for Discount
   :name: condDiscount

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - delay
        - Effect of reward delay
      * - amount
        - Effect of reward gain

.. dropdown:: Contrasts for Discount
   :name: contDiscount

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - delay
        - effect of delay on reward 
      * - amount
        - effect of reward gain

SelectiveStopSignal
-------------------

.. container:: tags

   :bdg-primary:`shape_perception` :bdg-light:`proactive_control` :bdg-primary:`shape_recognition` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `experiment factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. Similar to the `StopSignal`_ task, SelectiveStopSignal task required participants to refrain from responding if a red star appears after the target stimulus is presented. In this task, however, the red star only indicates the need to inhibit the motor response in one of the two sides (critical side), while it should be ignored for the other (noncritical side). Motor response is to be given by pressing with the index finger on the corresponding button of the response box. The task is composed by 12 practice trials, followed by 250 test trials divided in 5 blocks of 50 trials each. The task was acquired in two runs, within the same session as other tasks from the battery and using different phase-encoding directions. 
For the original version of this task, the authors provide a `simulator <https://expfactory.github.io/v1/stim_selective_stop_signal.html>`__ which contains the original design.

The conditions for this task are described in `this table <condSelectiveStopSignal_>`__ and the main contrasts derived from those conditions are described in `this table <contSelectiveStopSignal_>`__.

.. dropdown:: Conditions for SelectiveStopSignal
   :name: condSelectiveStopSignal

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - go_critical
        - Answer to the visual stimulus (critical side)
      * - go_noncritical
        - Answer to the visual stimulus (noncritical side)
      * - stop
        - Hold motor response
      * - ignore
        - Answer regardless of the stop signal

.. dropdown:: Contrasts for SelectiveStopSignal
   :name: contSelectiveStopSignal

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - go_critical
        - respond with the correct finger depending on the image displayed (side instructed to stop if the stop signal appears)
      * - go_noncritical
        - respond with the correct finger depending on the image displayed (side instructed to ignore the stop signal)
      * - stop
        - stop the response if the stop signal appears
      * - ignore
        - respond anyway even if the stop signal appears
      * - go_critical-stop
        - inhibit the motor response
      * - go_noncritical-ignore
        - ignore stop signal vs. simply respond
      * - ignore-stop
        - ignore stop signal vs. inhibit motor response
      * - stop-ignore
        - inhibit motor response vs. ignore stop signal

Stroop
------

.. container:: tags

   :bdg-light:`conflict_detection` :bdg-light:`proactive_control` :bdg-primary:`visual_perception` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `experiment factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. In this adaptation of the classic Stroop task (`Stroop, 1935 <https://doi.org/10.1037/h0054651>`__), the participants must press one of three buttons depending on the color of the presented word. In contrast to the classic pen and paper version of the task, the congruent and incongruent trials are intermixed. The three words/colors presented were red, green and blue, whose button presses corresponded on the response box respectively to the index, middle and ring fingers. The amount of money and the number of days is different for each trial. For the original version of this task, the authors provide a `simulator <https://expfactory.github.io/v1/stroop.html>`__ which contains the original design.

The conditions for this task are described in `this table <condStroop_>`__ and the main contrasts derived from those conditions are described in `this table <contStroop_>`__.

.. dropdown:: Conditions for Stroop
   :name: condStroop

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - congruent
        - Color and word are the same
      * - incongruent
        - Color and word are different

.. dropdown:: Contrasts for Stroop
   :name: contStroop

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - congruent
        - word and word color are the same
      * - incongruent
        - word and color are not the same
      * - incongruent-congruent
        - conflict between automatic and instructed response

ColumbiaCards
-------------

.. container:: tags

   :bdg-dark:`risk_processing` :bdg-dark:`reward_processing` :bdg-dark:`risk_aversion` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `experiment factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. The ColumbiaCards task is a gambling task in where the participants are presented with a set of cards facing down. In each trial, a different number of cards appear and the participant is informed of the amount gained per good card uncovered, the amount loss when uncovering the bad card, and the number of bad cards in the set. The participant can uncover as many cards as they want, by pressing the index finger's button on the response box, before pressing the middle finger's button to end the trial and start the next one. Uncovering a bad card automatically ends the trial. In each trial, the number of total cards, the number of bad cards, the amount gained per card uncovered and the amount lost if a bad card was uncovered changed. The order in which the cards is pre-determined for each trial, but the participant does not know it. The task is composed by 88 trials divided in 4 blocks of 22 trials each and was acquired in two runs, within the same session as other tasks from the battery and using different phase-encoding directions. 
For the original version of this task, the authors provide a `simulator <https://expfactory.github.io/v1/columbia_card_task_hot.html>`__ which contains the original design.

The conditions for this task are described in `this table <condColumbiaCards_>`__ and the main contrasts derived from those conditions are described in `this table <contColumbiaCards_>`__.

.. dropdown:: Conditions for ColumbiaCards
   :name: condColumbiaCards

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - num_loss_cards
        - Probability of losing in gambling
      * - loss
        - Expected loss in gambling
      * - gain
        - Expected gain in gambling

.. dropdown:: Contrasts for ColumbiaCards
   :name: contColumbiaCards

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - num_loss_cards
        - probability of losing
      * - loss
        - expected loss
      * - gain
        - expected gain

DotPatterns
-----------

.. container:: tags

   :bdg-light:`proactive_control` :bdg-primary:`shape_recognition` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `experiment factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. DotPatterns task presents the participant with pairs of stimuli, separated by a fixation cross. The participant has to press a button (index finger) as fast as possible after the presentation of the probe, and only one specific combination of cue-probe is instructed to be responded to differently. This task was designed to capture activation relative to the expectancy of the probe elicited by the correct cue. The task is composed by 160 trials divided in 4 blocks of 40 trials each. Each cue and probe lasted for 500ms, with a fixation cross that separates both lasting for 2000ms. It was acquired in two runs, within the same session as other tasks from the battery and using different phase-encoding directions.

The conditions for this task are described in `this table <condDotPatterns_>`__ and the main contrasts derived from those conditions are described in `this table <contDotPatterns_>`__.

.. dropdown:: Conditions for DotPatterns
   :name: condDotPatterns

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - cue
        - Look at the stimulus to provide a description of the cue
      * - correct_cue_correct_probe
        - Target pair, captures expectancy after correct cue
      * - correct_cue_incorrect_probe
        - Nontarget pair that also captures expectancy after correct cue
      * - incorrect_cue_correct_probe
        - Incorrect pair. The probe is correct but the cue is not
      * - incorrect_cue_incorrect_probe
        - Incorrect pair, both are incorrect

.. dropdown:: Contrasts for DotPatterns
   :name: contDotPatterns

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - cue
        - attend to cue
      * - correct_cue_correct_probe
        - both cue and probe are correct (AX)
      * - correct_cue_incorrect_probe
        - the cue is correct	 but the probe is not (AY)","['shape_recognition','proactive_control','response_selection','response_execution']
      * - incorrect_cue_correct_probe
        - cue is incorrect but probe is correct (BX)
      * - incorrect_cue_incorrect_probe
        - both cue and probe are incorrect (BY)
      * - correct_cue_incorrect_probe-correct_cue_correct_probe
        - incorrect vs. correct probe with correct cue
      * - incorrect_cue_incorrect_probe-incorrect_cue_correct_probe
        - shape recognition
      * - correct_cue_incorrect_probe-incorrect_cue_correct_probe
        - effect of cognitive control
      * - incorrect_cue_incorrect_probe-correct_cue_incorrect_probe
        - effect of cognitive control
      * - correct_cue-incorrect_cue
        - effect of cognitive control
      * - incorrect_probe-correct_probe
        - shape recognition

WardAndAllport
--------------

.. container:: tags

   :bdg-info:`working_memory` :bdg-light:`goal_hierarchy` :bdg-light:`search_depth` :bdg-light:`planning` :bdg-primary:`visual_perception` 

.. admonition:: Implementation 
   :class: seealso

   - Software: JavaScript, Python 2.7
   - Response device:  Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This task is a part of a battery of several tasks coming from the `experiment factory <https://github.com/expfactory/expfactory-experiments>`__ published in (`Eisenberg et al., 2017 <https://doi.org/10.1016/j.brat.2017.09.014>`__) and presented using `expfactory-python <https://github.com/expfactory/expfactory-python>`__ package. The battery was used to capture several aspects of self-regulation, including behavioral inhibition, decision making and planning abilities, among others. The adjustments concerned the translation to all written stimuli and instructions into french, as well as fixing a total time limit for experimentsthat allowed the participants their own pace for responding. All these modifications were done with extreme care of not altering the psychological state that the original tasks were designed to capture during scanning. WardAndAllport task is a digital version of the WATT3 task (`Ward, Allport, 1997 <https://doi.org/10.1080/713755681>`__, `Shallice, 1982 <https://doi.org/10.1098/rstb.1982.0082>`__), and its main purpose is to capture activation related to planning abilities. For this, the task uses a factorial manipulation of 2 task parameters: search depth and goal hierarchy. Search depth involves mentally constructing the steps necessary to reach the goal state, and the interdependecy between steps in order to do so. This is expressed by the presence or absence of intermediate movements necessary for an optimal solution of each problem. Goal hierarchy refers to whether the order in which the three balls have to be put in their goal positions can be completely extracted from looking at the goal state or if it requires the participant to integrate information between goal and starting states (which result in unambiguous or partially ambiguous goal states, respectively). Detailed explanations and examples of each one of the four categories can be found in `Kaller et al., 2011 <https://doi.org/10.1093/cercor/bhq096>`__. The task was divided in 4 practice trials, followed by 48 test trials divided in 3 blocks of 14 trials each, separated by 10 seconds of resting period. Data was only acquired during the test trials, although the practice trials were also performed inside the scanner with its corresponding equipment. In each trial, the participant would see two configurations of the towers: the test towers on the left, and the target towers on the right. The towers of the right showed the final configuration of balls required to complete the trial. Three buttons were assigned to the left (index finger' button), middle (middle finger's button) and right (ring finger's button) columns respectively, and each button press would either take the upper ball of the selected column or drop the ball in hand at the top of the selected column. On the upper left corner, a gray square with the text "Ball in hand" would show the ball currently in hand. All trials could be solved in 3 movements, considering taking a ball and putting it elsewhere as a single movement. The time between the end of one trial and the beginning of the next one was 1000 ms.

The conditions for this task are described in `this table <condWardAndAllport_>`__ and the main contrasts derived from those conditions are described in `this table <contWardAndAllport_>`__.

.. dropdown:: Conditions for WardAndAllport
   :name: condWardAndAllport

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - planning_ambiguous_intermediate
        - Partially ambiguous goal state with intermediate movement
      * - planning_unambiguous_direct
        - Unambiguous goal state without intermediate movement
      * - planning_ambiguous_direct
        - Partially ambiguous goal state without intermediate movement
      * - planning_unambiguous_intermediate
        - Unambiguous goal state with intermediate movement

.. dropdown:: Contrasts for WardAndAllport
   :name: contWardAndAllport

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - planning_ambiguous_intermediate
        - complex goal hierarchy + complex search depth
      * - planning_unambiguous_direct
        - simple goal hierarchy + simple search depth
      * - planning_ambiguous_direct
        - complex goal hierarchy + simple search depth
      * - planning_unambiguous_intermediate
        - simple goal hierarchy + complex search depth
      * - intermediate-direct
        - effect of search depth
      * - ambiguous-unambiguous
        - effect of goal hierarchy
      * - move_ambiguous_intermediate
        - complex goal hierarchy + complex search depth
      * - move_unambiguous_direct
        - simple goal hierarchy + simple search depth
      * - move_ambiguous_direct
        - complex goal hierarchy + simple search depth
      * - move_unambiguous_intermediate
        - simple goal hierarchy + complex search depth

BiologicalMotion1
-----------------

.. container:: tags

   :bdg-light:`vertical_flip` :bdg-warning:`global_motion_coherence` :bdg-warning:`local_motion_coherence` :bdg-warning:`motion_detection` :bdg-light:`BiologicalMotion` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The phenomenon known as "biological motion" was first introduced in (`Johansson, 1973 <https://doi.org/10.3758/BF03212378>`__), and consisted in point-light displays arranged and moving in a way that resembled a person moving. The task that we used was originally developed by (`Chang et al., 2018 <https://doi.org/10.1016/j.neuroimage.2018.03.013>`__). During the task, the participants were shown a point-light "walker", and they had to decide if the walker's orientation was to the left or to the right, by pressing on the response box respectively on the index finger's button or the middle finger's button. The data was acquired in 4 runs. The stimuli was divided in 6 different categories: three types of walkers, as well as their reversed versions. The division of the categories focuses on three types of information that the participant can get from the walker: global information, local information and orientation. Global information refers to the general structure of the body and the spatial relationships between its parts. Local information refers to kinematics, speed of the points and mirror-symmetric motion. Please see `Chang et al., 2018 <https://doi.org/10.1016/j.neuroimage.2018.03.013>`__ for more details about the stimuli. Each run comprises 12 blocks with 8 trials per block. The stimulus duration was 500ms and the inter-stimulus interval 1500ms (total 16s per block). Each of the blocks was followed by a fixation block, that also lasted 16s. Each run contained 4 of the six conditions, repeated 3 times each. Run type 1 contained both global types (natural and inverted) and both local naturals.

The conditions for this task are described in `this table <condBiologicalMotion1_>`__ and the main contrasts derived from those conditions are described in `this table <contBiologicalMotion1_>`__.

.. dropdown:: Conditions for BiologicalMotion1
   :name: condBiologicalMotion1

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - global_upright
        - Structural information is preserved, but individual local trajectories are mirror-symmetric. Global-only in the original paper
      * - global_inverted
        - Global walker, inverted upside-down
      * - natural_upright
        - Local information is preserved, but the points are randomly shuffled along the X-axis, rendering global cues uninformative. "Local-natural" in the original experiment
      * - natural_inverted
        - Local natural walker, inverted along the horizontal axis

.. dropdown:: Contrasts for BiologicalMotion1
   :name: contBiologicalMotion1

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - global_upright
        - global biological motion vs. fixation
      * - global_inverted
        - global reversed biological motion vs. fixation
      * - natural_upright
        - local biological motion vs. fixation
      * - natural_inverted
        - local reversed biological motion vs. fixation
      * - global_upright - natural_upright
        - effect of global information on motion perception
      * - global_upright - global_inverted
        - effect of orientation on motion perception
      * - natural_upright - natural_inverted
        - effect of orientation on motion perception
      * - global-natural
        - effect of global information on motion perception
      * - natural-global
        - Negative effect of global information on motion perception
      * - inverted-upright
        - effect of orientation on motion perception

BiologicalMotion2
-----------------

.. container:: tags

   :bdg-light:`vertical_flip` :bdg-warning:`scrambled_motion` :bdg-warning:`local_motion_coherence` :bdg-warning:`motion_detection` :bdg-light:`BiologicalMotion` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychophysics Toolbox Version 3 (PTB-3), aka Psychtoolbox-3, for GNU Octave
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

The phenomenon known as "biological motion" was first introduced in (`Johansson, 1973 <https://doi.org/10.3758/BF03212378>`__), and consisted in point-light displays arranged and moving in a way that resembled a person moving. The task that we used was originally developed by (`Chang et al., 2018 <https://doi.org/10.1016/j.neuroimage.2018.03.013>`__). During the task, the participants were shown a point-light "walker", and they had to decide if the walker's orientation was to the left or to the right, by pressing on the response box respectively on the index finger's button or the middle finger's button. The data was acquired in 4 runs. The stimuli was divided in 6 different categories: three types of walkers, as well as their reversed versions. The division of the categories focuses on three types of information that the participant can get from the walker: global information, local information and orientation. Global information refers to the general structure of the body and the spatial relationships between its parts. Local information refers to kinematics, speed of the points and mirror-symmetric motion. Please see `Chang et al., 2018 <https://doi.org/10.1016/j.neuroimage.2018.03.013>`__ for more details about the stimuli. Each run comprises 12 blocks with 8 trials per block. The stimulus duration was 500ms and the inter-stimulus interval 1500ms (total 16s per block). Each of the blocks was followed by a fixation block, that also lasted 16s. Each run contained 4 of the six conditions, repeated 3 times each. Run type 2 contained both local naturals and both local modified.

The conditions for this task are described in `this table <condBiologicalMotion2_>`__ and the main contrasts derived from those conditions are described in `this table <contBiologicalMotion2_>`__.

.. dropdown:: Conditions for BiologicalMotion2
   :name: condBiologicalMotion2

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - modified_upright
        - Neither structural or local information is carried out by this type of walker, it uses both types of modifications used for the previous two categories. "Local modified" in the original study
      * - modified_inverted
        - Local modified walker, inverted along the horizontal axis
      * - natural_upright
        - Local information is preserved, but the points are randomly shuffled along the X-axis, rendering global cues uninformative. "Local-natural" in the original experiment
      * - natural_inverted
        - Local natural walker, inverted along the horizontal axis

.. dropdown:: Contrasts for BiologicalMotion2
   :name: contBiologicalMotion2

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - modified_upright
        - scrambled motion information vs. fixation
      * - modified_inverted
        - no motion information reversed vs. fixation
      * - natural_upright
        - local biological motion vs. fixation
      * - natural_inverted
        - local reversed biological motion vs. fixation
      * - natural_upright - modified_upright
        - effect of local information on motion perception
      * - modified_upright - modified_inverted
        - effect of orientation on motion perception
      * - natural_upright - natural_inverted
        - effect of orientation on motion perception
      * - modified-natural
        - Negative effect of local information on motion perception
      * - natural-modified
        - effect of local information on motion perception
      * - inverted-upright
        - effect of orientation on motion perception

LePetitPrince
-------------

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.9.0 (Python 3.6)
   - Audio device: OptoACTIVE (Optoacoustics)

This experiment is a natural language comprehension protocol, originally implemented by (`Bhattasali et al., 2019 <https://doi.org/10.1080/23273798.2018.1518533>`__, `Hale et al., 2022 <https://doi.org/10.1146/annurev-linguistics-051421-020803>`__). The use of complex naturalistic language stimuli has been used to study other processes, like semantic maps (`Huth et al., 2016 <https://doi.org/10.1038/nature17637>`__). The data was acquired in two different sessions, each one comprising five and four runs, respectively. Each run comprised three chapters of the "Le Petit Prince" story in french. During each run, the participant was presented with the audio of the story. In between runs, the experimenters would ask some multiple choice questions, as well as two or three open ended questions about the contents of the previous run, in order to keep the participants engaged. The length of the runs varied between nine and thirteen minutes. There was also a six-minutes localizer at the end of the second acquisition, in order to accurately map language areas for each participant. 
**Note:** We used the OptoACTIVE (Optoacoustics) audio device for all subjects except for *subject-08*, for whom we employed MRConfon MKII.


MathLanguage
------------

.. container:: tags

   :bdg-success:`auditory_sentence_comprehension` :bdg-primary:`visual_arithmetic_processing` :bdg-success:`auditory_geometric_processing` :bdg-success:`auditory_arithmetic_processing` :bdg-success:`auditory_sentence_recognition` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.9.0 (Python 3.6)
   - Response device: In-house custom-made sticks featuring one-top button, each one to be used in each hand

   - Audio device: OptoACTIVE (Optoacoustics)

The MathLanguage protocol was taken from (`Amalric et al., 2016 <https://doi.org/10.1073/pnas.1603205113>`__). This task aims to comprehensively capture the activation related with several types of mathematical and other types of facts, presented as sentences. During the task, the participants are presented a series of sentences, each one in either of two modalities: auditory or visual. Some of the categories include theory of mind statements, arithmetic facts and geometry facts. After each sentence, the participant has to indicate whether they believe the presented fact to be true or false, by respectively pressing the button in the left or right hand. For each participant, the data was divided in four runs, with an equal number of trials of each category in each run. As previously stated, each stimulus is presented either in auditory or visual form, which was pre-randomized and equal for every participant. A second version of each run (runs "B") was generated reverting the modality for each trial, so those being visual in the original runs (runs "A"), would be auditory in their corresponding B version, and vice-versa. 
**Note:** We used the OptoACTIVE (Optoacoustics) audio device for all subjects except for *subject-05* and *subject-08*, who completed the session using MRConfon MKII.

The conditions for this task are described in `this table <condMathLanguage_>`__ and the main contrasts derived from those conditions are described in `this table <contMathLanguage_>`__.

.. dropdown:: Conditions for MathLanguage
   :name: condMathLanguage

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - arithmetic_fact_auditory
        - Listen to arithmetic fact
      * - arithmetic_fact_visual
        - Read arithmetic fact
      * - arithmetic_principle_auditory
        - Listen to arithmetic principle
      * - arithmetic_principle_visual
        - Read arithmetic principle
      * - colorlessg_auditory
        - Jabberwocky sentence presented as auditory stimulus
      * - colorlessg_visual
        - Jabberwocky sentence presented as visual stimulus
      * - context_auditory
        - Beep sound indicating that the following stimuli will be audio
      * - context_visual
        - Red cross indicating that the following stimuli will be visual
      * - general_auditory
        - Listen to sentence
      * - general_visual
        - Read sentence
      * - geometry_fact_auditory
        - Listen to geometric fact
      * - geometry_fact_visual
        - Read geometric fact
      * - theory_of_mind_auditory
        - Listen to false-belief tale
      * - theory_of_mind_visual
        - Read false-belief tale
      * - wordlist_auditory
        - Listen to word list
      * - wordlist_visual
        - Read word list

.. dropdown:: Contrasts for MathLanguage
   :name: contMathLanguage

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - colorlessg_auditory
        - auditory jabberwocky sentence parsing
      * - colorlessg_visual
        - visual jabberwocky sentence parsing
      * - wordlist_auditory
        - listen to word list
      * - wordlist_visual
        - read word list
      * - arithmetic_fact_auditory
        - listen to arithmetic fact
      * - arithmetic_fact_visual
        - read arithmetic fact
      * - arithmetic_principle_auditory
        - listen to arithmetic principle
      * - arithmetic_principle_visual
        - read to arithmetic principle
      * - theory_of_mind_auditory
        - auditory false-belief tale
      * - theory_of_mind_visual
        - read false-belief tale
      * - geometry_fact_auditory
        - listen to geometric fact
      * - geometry_fact_visual
        - read geometric fact
      * - general_auditory
        - listen to sentence
      * - general_visual
        - read sentence
      * - context_auditory
        - audio cue
      * - context_visual
        - visual cue
      * - visual-auditory
        - read vs to listen to instruction
      * - auditory-visual
        - list to vs read instruction
      * - colorlessg-wordlist
        - jabberwocky vs word list
      * - general-colorlessg
        - listen to sentence vs jabberwocky
      * - math-nonmath
        - math vs others
      * - nonmath-math
        - others vs math
      * - geometry-othermath
        - geometry vs other maths
      * - arithmetic_principle-othermath
        - arithmetic principle vs other maths
      * - arithmetic_fact-othermath
        - arithmetic fact vs other maths
      * - theory_of_mind-general
        - false belief vs general statement
      * - context-general
        - cue vs language statement
      * - theory_of_mind-context
        - false belief vs cue
      * - context-theory_of_mind
        - cue vs false belief
      * - theory_of_mind_and_context-general
        - false belief and cue vs general statement

SpatialNavigation
-----------------

.. container:: tags

   :bdg-info:`spatial_working_memory` :bdg-light:`navigation` :bdg-primary:`visual_search` :bdg-info:`spatial_memory` :bdg-light:`spatial_localization` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Vizard 6
   - Response device: Five-button ergonomic pad (current designs, package 932 with pyka hhsc-1x5-n4)

This protocol, an adaptation from the one used in (`Diersch et al., 2021 <https://doi.org/10.1523/JNEUROSCI.0528-20.2021>`__), was originally designed to capture the effects of spatial encoding and orientation learning in different age groups. The task demands subjects to navigate and orientate themselves in a complex virtual environment. There are three parts of this task: familiarisation (outside of the scanner), encoding (in scanner) and retrieval (in scanner). Before entering the scanner, the participants would do a familiarisation phase where they would be able to freely move through the virtual environment and the objective is to collect eight red balls that can be found in different streets of the virtual city. During this time, the participants can familiarize with the different buildings and their particular features, as well as learning the location of the two key buildings that are indicated at the beginning (Town Hall and Church). After they collect all the red balls, a short training of the main task is performed to ensure the correct understanding of the instructions. The task is comprised by eight runs, from which seven of them (all except the first) starts with an encoding phase. During this period, the participant has to passively watch the camera move from one key building to the other, in such a way that every street of the virtual environment is passed through in every direction possible. Then, after the encoding phase, the retrieval phase is performed. During this part of the experiment, the task is divided in 8 experimental trials and 4 control trials per run. For every trial, the participant appears near an intersection of the virtual environment, which is now covered in a thick fog that prevents them from seeing far ahead. Then, the camera automatically approaches the intersection and stands in the center of it. The task for the participant is to point in the direction of the key building (showed in a miniature picture at the bottom of the screen). Index and middle finger's button of the response box move respectively to the left and right whereas thumb's button validates the answer. Control trials are identical to experimental ones, but the participant must point to one of the buildings of the intersection that has been colored in blue.

The conditions for this task are described in `this table <condSpatialNavigation_>`__ and the main contrasts derived from those conditions are described in `this table <contSpatialNavigation_>`__.

.. dropdown:: Conditions for SpatialNavigation
   :name: condSpatialNavigation

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - encoding_phase
        - Encode location of key building
      * - intersection
        - Camera approaches intersection during encoding phase
      * - control
        - Camera approaches intersection in an control trial
      * - pointing_control
        - Participant rotates camera to point to blue building in control trial
      * - experimental
        - Camera approaches intersection in an experimental trial
      * - pointing_experimental
        - Participant rotates camera to point to key building in experimental trial
      * - navigation
        - Camera navigates through the streets during encoding phase

.. dropdown:: Contrasts for SpatialNavigation
   :name: contSpatialNavigation

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - experimental-intersection
        - spatial navigation
      * - experimental-control
        - spatial navigation
      * - intersection
        - spatial localization
      * - experimental
        - spatial navigation
      * - retrieval
        - retrieving a landmark
      * - pointing_experimental
        - pointing a landmark
      * - control
        - spatial navigation
      * - navigation
        - spatial navigation
      * - pointing_control
        - pointing a landmark

GoodBadUgly
-----------

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.9.0 (Python 2.7)
GoodBadUgly task was adapted from the study (`Mantini et al., 2012 <https://doi.org/10.1038/nmeth.1868>`__), dedicated to investigate correspondence between monkey and human brains using naturalistic stimuli. The task relies on watching - viewing and listening - of the whole movie "The Good, the Bad and the Ugly" by Sergio Leone. The original, 177-minute movie was cut into 10-minute segments (except the first two and the last ones) to adjust to the segment length of the original study, which presented only three 10-min segments of the middle of the movie. This resulted in a total of 18 segments. For IBC, the French-dubbed version "Le Bon, la Brute et le Truand" was presented. This task was performed during three acquisition sessions with seven segments each, one segment per run. The first three segments were repeated during the last acquisition after the movie was completed. The total duration of the run ten minutes for the majority of segments, around eight minutes for the first two runs, and four minutes and a half for the last run.


EmoMem
------

.. container:: tags

   :bdg-light:`imagination` :bdg-primary:`visual_cue` :bdg-danger:`negative_emotion` :bdg-danger:`positive_emotion` :bdg-primary:`visual_perception` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Octave 4.4 + Psychtoolbox 3.0
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task is a part of the CamCAN (`Cambridge Centre for Ageing and Neuroscience <https://www.cam-can.org/>`__) battery, designed to understand how individuals can best retain cognitive abilities into old age. The adjustments concerned the translation of all stimuli and instructions into french, replacing Matlab functions with Octave functions as needed, and eliminating the use of a custom Matlab toolbox `mrisync <https://github.com/MRC-CBU/mrisync>`__ that was used to interface with the MRI Scanner (3T Siemens Prisma) over a National Instruments card. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The EmoMem task was designed to provide an assessment of implicit and explicit memory, and how it is affected by emotional valence. At the IBC we only conducted the encoding part of the task the Study phase as mentioned in (`Shafto et al., 2014 <https://doi.org/10.1186/s12883-014-0204-1>`__) but not the Test phase that happened outside the scanner in the original study. On each trial of this task, participants see a background picture for 2 seconds, after which a foreground picture of an object is superimposed. Participants are instructed to imagine a "story" linking the background and foreground picture, and after an 8 second presentation, the next trial begins. The emotional valence manipulation affects only the background image, which is negative, neutral, or positive. In all, 120 trials were presented over 2 runs.

The conditions for this task are described in `this table <condEmoMem_>`__ and the main contrasts derived from those conditions are described in `this table <contEmoMem_>`__.

.. dropdown:: Conditions for EmoMem
   :name: condEmoMem

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - neutral_image
        - Neutral background image
      * - negative_image
        - Negative background image
      * - positive_image
        - Positive background image
      * - object
        - Neutral object

.. dropdown:: Contrasts for EmoMem
   :name: contEmoMem

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - neutral_image
        - viewing a neutral image
      * - positive-neutral_image
        - positive vs neutral image
      * - negative_image
        - viewing a negative image
      * - negative-neutral_image
        - negative vs neutral image
      * - positive_image
        - viewing a positive image
      * - object
        - foreground object and imagination task

EmoReco
-------

.. container:: tags

   :bdg-primary:`face_perception` :bdg-danger:`emotional_expression` :bdg-danger:`negative_emotion` :bdg-light:`gender_perception` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software:  E-Prime 2.0
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task is a part of the CamCAN (`Cambridge Centre for Ageing and Neuroscience <https://www.cam-can.org/>`__) battery, designed to understand how individuals can best retain cognitive abilities into old age. The adjustments concerned the translation of all stimuli and instructions into french, replacing Matlab functions with Octave functions as needed, and eliminating the use of a custom Matlab toolbox `mrisync <https://github.com/MRC-CBU/mrisync>`__ that was used to interface with the MRI Scanner (3T Siemens Prisma) over a National Instruments card. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The EmoReco task compares brain activity when observing angry versus neutral expressions, and assesses how individuals differ in how they regulate responses to negative emotional expressions (`Shafto et al., 2014 <https://doi.org/10.1186/s12883-014-0204-1>`__). The expressions were presented on female and male faces (15 each), and each face had an angry and a neutral expression version. On each trial, participants reported the gender of the face. Emotions were presented in blocks of angry and neutral, with equal numbers of female and male faces in each block. There were 12 blocks of each emotion and each block consisted of 5 trials. In all, 60 trials were presented in each of the 2 runs.

The conditions for this task are described in `this table <condEmoReco_>`__ and the main contrasts derived from those conditions are described in `this table <contEmoReco_>`__.

.. dropdown:: Conditions for EmoReco
   :name: condEmoReco

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - neutral_female
        - Neutral emotion on female face
      * - neutral_male
        - Neutral emotion on male face
      * - angry_female
        - Angry emotion on female face
      * - angry_male
        - Angry emotion on male face

.. dropdown:: Contrasts for EmoReco
   :name: contEmoReco

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - neutral_male
        - neutral male face perception
      * - neutral
        - neutral face perception
      * - female-male
        - female vs male face perception
      * - angry_male
        - angry male face perception
      * - angry
        - angry face perception
      * - neutral_female
        - neutral female face perception
      * - angry-neutral
        - angry vs neutral face perception
      * - angry_female
        - angry female face perception
      * - neutral-angry
        - neutral vs angry face perception
      * - male-female
        - male vs female face

StopNogo
--------

.. container:: tags

   :bdg-primary:`shape_perception` :bdg-light:`proactive_control` :bdg-primary:`shape_recognition` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task is a part of the CamCAN (`Cambridge Centre for Ageing and Neuroscience <https://www.cam-can.org/>`__) battery, designed to understand how individuals can best retain cognitive abilities into old age. The adjustments concerned the translation of all stimuli and instructions into french, replacing Matlab functions with Octave functions as needed, and eliminating the use of a custom Matlab toolbox `mrisync <https://github.com/MRC-CBU/mrisync>`__ that was used to interface with the MRI Scanner (3T Siemens Prisma) over a National Instruments card. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The StopNogo task assesses systems involved in action restraint and action cancellation by randomly interleaving "Go", "Stop" and "No-Go" trials. On Go trials, participants viewed a black arrow pointing left or right for 1000 ms, and indicated the direction of the arrow by pressing left/right buttons with their right hand. On Stop trials, the black arrow changed colour (from black to red), after a short variable stop-signal delay. Participants were instructed that to not respond to the red arrow, so stop signal trials required cancelling the initial response to the black arrow. The Stop-Signal delay varied trial-to-trial in steps of 50 ms, and a staircase procedure was used to maintain a performance level of 66% successful inhibition. Finally, in No-Go trials, the arrow was red in colour (stop-signal delay of 0) and participants were required to make no response.

The conditions for this task are described in `this table <condStopNogo_>`__ and the main contrasts derived from those conditions are described in `this table <contStopNogo_>`__.

.. dropdown:: Conditions for StopNogo
   :name: condStopNogo

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - go
        - Arrow stays black; press button corresponding to arrow direction
      * - nogo
        - Arrow starts out red so do not press button
      * - successful_stop
        - Arrow starts out black but turns red; motor response inhibited
      * - unsuccessful_stop
        - Arrow starts out black but turns red; motor response not inhibited

.. dropdown:: Contrasts for StopNogo
   :name: contStopNogo

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - go
        - shape recognition
      * - nogo-go
        - response inhibition
      * - successful+nogo-unsuccessful
        - failed to inhibit response
      * - nogo
        - no response
      * - unsuccessful-successful_stop
        - effect of failed inhibition
      * - successful_stop
        - shape recognition	 stopped response","['shape_recognition','proactive_control','response_inhibition','response_selection','response_execution']
      * - unsuccessful_stop
        - shape recognition	 failed stopped response","['shape_recognition','proactive_control','response_selection','response_execution']

Catell
------

.. container:: tags

   :bdg-light:`oddball_detection` :bdg-primary:`visual_form_discrimination` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Octave 4.4 + Psychtoolbox 3.0
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task is a part of the CamCAN (`Cambridge Centre for Ageing and Neuroscience <https://www.cam-can.org/>`__) battery, designed to understand how individuals can best retain cognitive abilities into old age. The adjustments concerned the translation of all stimuli and instructions into french, replacing Matlab functions with Octave functions as needed, and eliminating the use of a custom Matlab toolbox `mrisync <https://github.com/MRC-CBU/mrisync>`__ that was used to interface with the MRI Scanner (3T Siemens Prisma) over a National Instruments card. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The Catell task was used to provide a measure of neural activity underpinning fluid intelligence (`Shafto et al., 2014 <https://doi.org/10.1186/s12883-014-0204-1>`__). On each trial, participants were presented with 4 images and had to identify the "odd one out". Some trials were easy with easily identifiable differences between the oddball and other images, while others were difficult and participants had to detect abstract patterns to identify the oddball image. The task employs a block design, where participants solve alternating blocks of easy and difficult trials, lasting 30 seconds each. In all, participants completed four blocks of easy and four blocks of difficult problems. On each trial a stimulus appears and remains on the screen until the participant responds, with the block automatically ending after 30 seconds and the next block beginning immediately. Participants were encouraged take as long as necessary, only responding when they are confident of the correct answer. This design means that the number of trials in a block varies across individuals, but the time spent on each type of problem (easy and difficult) is held constant.


.. dropdown:: Contrasts for Catell
   :name: contCatell

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - easy
        - easy oddball task
      * - hard
        - hard oddball task
      * - hard-easy
        - easy vs hard oddball task

FingerTapping
-------------

.. container:: tags

   :bdg-warning:`motor_planning` :bdg-warning:`motor_control` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Octave 4.4 + Psychtoolbox 3.0
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task is a part of the CamCAN (`Cambridge Centre for Ageing and Neuroscience <https://www.cam-can.org/>`__) battery, designed to understand how individuals can best retain cognitive abilities into old age. The adjustments concerned the translation of all stimuli and instructions into french, replacing Matlab functions with Octave functions as needed, and eliminating the use of a custom Matlab toolbox `mrisync <https://github.com/MRC-CBU/mrisync>`__ that was used to interface with the MRI Scanner (3T Siemens Prisma) over a National Instruments card. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The FingerTapping task was used to study executive control and action decisions in ageing and neurodegenerative disease (`Shafto et al., 2014 <https://doi.org/10.1186/s12883-014-0204-1>`__). Participants were presented with an image of a right hand and were instructed to press a button with one of their four right hand fingers in response to a cue. The cue was either a "specified" cue in which a single opaque circle indicates which finger to press, or a "chosen" cue in which 3 circles appeared opaque indicating participants must choose on of the 3 opaque fingers to press. The task includes 40 specified trials (10 for each finger) and 40 chosen trials, interspersed with 40 blank trials in which no cue is presented. Cues were presented for 1 second with a stimulus onset asynchrony of 2.5 seconds, and were pseudorandomly ordered so that participants did not see four or more responses of the same condition (action selection, specified or null) in a row.

The conditions for this task are described in `this table <condFingerTapping_>`__ and the main contrasts derived from those conditions are described in `this table <contFingerTapping_>`__.

.. dropdown:: Conditions for FingerTapping
   :name: condFingerTapping

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - specified
        - Finger to tap is highlighted
      * - chosen
        - Participant chooses 1 out of 3 highlighted fingers to tap
      * - null
        - No finger tap

.. dropdown:: Contrasts for FingerTapping
   :name: contFingerTapping

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - specified
        - cued finger tapping
      * - chosen-specified
        - uncued vs cued finfer tapping
      * - chosen
        - uncued finger tapping
      * - specified-null
        - cued vs inhibited finger tapping
      * - null
        - inhibited finger tapping
      * - chosen-null
        - uncued vs inhibited finger tapping
      * - fingertap-rest
        - button press vs rest

VSTMC
-----

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-info:`spatial_working_memory` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Octave 4.4 + Psychtoolbox 3.0
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task is a part of the CamCAN (`Cambridge Centre for Ageing and Neuroscience <https://www.cam-can.org/>`__) battery, designed to understand how individuals can best retain cognitive abilities into old age. The adjustments concerned the translation of all stimuli and instructions into french, replacing Matlab functions with Octave functions as needed, and eliminating the use of a custom Matlab toolbox `mrisync <https://github.com/MRC-CBU/mrisync>`__ that was used to interface with the MRI Scanner (3T Siemens Prisma) over a National Instruments card. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. On each trial of the VSTMC (or the Visual short-term memory) task, participants saw three arrays of coloured dots, one red, one yellow, and one blue. The dot displays were presented in quick succession: a 250 ms fixation was followed by a 500 ms dot display. As a manipulation of set size, one, two, or three of the dot displays moved in a single direction, which had to be remembered. The other displays rotated around a central axis, and these rotating distractor displays had be ignored. After the third display, there was an 8 s delay, during which the direction(s) of motion of non-rotating dots had to be remember. This was followed by the probe display, which had a coloured circle to indicate which dot display to recall (red, yellow, or blue). The circle contained a pointer that had to be adjusted to indicate which direction the target dot display had been moving. Participants were given 5 seconds to adjust the pointer to match the direction of the to-be-remembered dot display. On 90% of trials the probed movements were in one of three directions (7, 127, or 247 degrees).

The conditions for this task are described in `this table <condVSTMC_>`__ and the main contrasts derived from those conditions are described in `this table <contVSTMC_>`__.

.. dropdown:: Conditions for VSTMC
   :name: condVSTMC

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - stim_load1
        - Dots in only one colour move coherently in a given direction
      * - stim_load2
        - Dots in two colours move coherently in two different directions
      * - stim_load3
        - Dots in all three colours move coherently in 3 different directions
      * - resp_load1
        - Response period of stim_load1 trials
      * - resp_load2
        - Response period of stim_load2 trials
      * - resp_load3
        - Response period of stim_load3 trials

.. dropdown:: Contrasts for VSTMC
   :name: contVSTMC

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - stim_load1
        - attending to one set of points
      * - resp_load1
        - response to motion direction of one set of points
      * - stim
        - attending to sets of points
      * - resp_load3-load1
        - difference in response to one vs three sets of points
      * - stim_load2
        - attending to two sets of points
      * - resp_load2
        - response to motion direction of two sets of points
      * - resp
        - response to motion
      * - stim_load3
        - attending to three set of points
      * - resp_load3
        - response to motion direction of three sets of points
      * - stim_load3-load1
        - difference in attending to motion of one vs three sets of points

RewProc
-------

.. container:: tags

   :bdg-primary:`visual_cue` :bdg-dark:`reward_processing` :bdg-dark:`loss_aversion` :bdg-dark:`reward_valuation` :bdg-light:`cue_switch` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychopy 2021.1.3 (Python 3.8.5)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from `O'Doherty et al., 2001 <https://doi.org/10.1038/82959>`__ and `O'Doherty et al., 2003 <https://doi.org/10.1523/JNEUROSCI.23-21-07931.2003>`__, which aimed at discerning the role of the orbitofrontal cortex (OFC) using a similar emotion-related visual reversal-learning task in which choice of the correct stimulus led to a probabistically determined "monetary" reward and choice of the incorrect stimulus led to a monetary loss. In each trial of a run of this protocol, two unfamiliar and easily discriminable fractal patterns were displayed on a gray background, positioned to the left and right of a central fixation cross. At the beginning of the task, one of these two patterns was arbitrarily designated as "correct" and the other as "incorrect". Then, the subject's task was to to select one of these two patterns. Selection of the correct pattern led to a monetary gain with a probability of 70% and a monetary loss with a probability of 30%. On the other hand, selection of the incorrect pattern led to a monetary gain with a probability of 30% and a monetary loss with a probability of 70% (reversed gain-loss probability contingencies). On selecting either pattern, a black box appeared around it followed by a feedback on whether and how much of the symbolic money (either 20 or 10 units) was gained or lost in the particular trial. There was an equal probability whether this amount of money would be 10 or 20. Further, if the subject selected the correct pattern consecutively for a given criterion i.e. 5 times here, a reversal of the gain-loss probability contingencies occurred after a Poisson process, such that there was a probability of 25% that a reversal took place on any given post-criterion trial. The data was acquired in 2 runs during one scanning session. Each run comprised 85 trials. The trial event timings used in the IBC implementaton of the task were different from those used in either of the two aforementioned studies. This was done upon discussion with the original authors who insisted that these timing were more optimal in the sense that events are separated enough to reduce temporal correlations, but short enough to have a reasonable total trial length. The pre-fixation cross was displayed for 500-1500 ms. The stimuli remained on screen for selection for less than 3000 ms and the outcome feedback was displayed after a delay of 1750 ms, for 1750 ms.

The conditions for this task are described in `this table <condRewProc_>`__ and the main contrasts derived from those conditions are described in `this table <contRewProc_>`__.

.. dropdown:: Conditions for RewProc
   :name: condRewProc

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - green
        - Subject selected the green pattern
      * - purple
        - Subject selected the purple pattern
      * - left
        - Selected pattern was in the left side of the screen
      * - right
        - Selected pattern was in the right side of the screen
      * - switch
        - Selected pattern was different from the one selected in previous trial
      * - stay
        - Selected pattern was the same as the one selected in previous trial
      * - plus_20
        - Gained 20 units of reward as a result of the selection
      * - minus_20
        - Lost 20 units of reward as a result of the selection
      * - plus_10
        - Gained 10 units of reward as a result of the selection
      * - minus_10
        - Lost 10 units of reward as a result of the selection

.. dropdown:: Contrasts for RewProc
   :name: contRewProc

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - stim
        - appearance of the cue images
      * - minus_20
        - lost 20 units of reward
      * - plus_20
        - gained 20 units of reward
      * - minus_10
        - lost 10 units of reward
      * - plus_10
        - gained 10 units of reward
      * - green-purple
        - green vs purple pattern selected
      * - purple-green
        - purple vs green pattern selected
      * - left-right
        - selected pattern on the left vs right side
      * - right-left
        - selected pattern on the right vs left side
      * - switch
        - selected a different pattern than previous trial
      * - stay
        - selected the same pattern than previous trial
      * - switch-stay
        - selected a different vs same pattern
      * - stay-switch
        - selected the same vs different pattern
      * - gain
        - gained 20 or 10 units of reward 
      * - loss
        - lost 20 or 10 units of reward
      * - gain-loss
        - gained vs lost 20 or 10 units of reward 
      * - loss-gain
        - lost vs gained 20 or 10 units of reward

NARPS
-----

.. container:: tags

   :bdg-dark:`loss_aversion` :bdg-dark:`reward_processing` :bdg-dark:`reward_valuation` :bdg-dark:`reward_anticipation` :bdg-dark:`risk_aversion` 

.. admonition:: Implementation 
   :class: seealso

   - Software:  Psychtoolbox-3 (Octave 5.2.0)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol is more commonly know as the mixed gambles task and was adapted from the Neuroimaging Analysis Replication and Prediction Study (NARPS) (`Botvinik-Nezer et al., 2019 <https://doi.org/10.1038/s41597-019-0113-7>`__) study, that aimed to estimate the variability of neuroscientific results across analysis teams. The mixed gambles task though, is originally from (`Tom et al., 2007 <https://doi.org/10.1126/science.1134239>`__) that studied the neural basis of loss aversion. Loss aversion is the phenomenon that suggests that people tend to be more sensitive to losses as compared to equal-sized gains. The study therefore, investigated whether potential losses elicit negative emotions, which then drive loss aversion, or rather the same neural systems, encoding subjective value, asymmetrically respond to losses compared to gains.  In each trial of this protocol, the subjects were presented with a mixed gamble where they had a 50% chance of either gaining one amount of symbolic money or losing another amount. The possible gains and losses both ranged between 5-20 units (equal range condition), in increments of 1 unit and all 256 possible combinations of gains and losses were presented to each subject in the same sequence. The subjects were then asked to decide whether or not they would like to accept the gambles presented to them, with four possible responses for each gamble: strongly accept, weakly accept, weakly reject or strongly reject. The stimulus consisted of a circle presented on a grey screen and divided into two halves: on one side the gain amount was presented in green with a plus (+) sign before the number, and on the other side the loss amount was presented in red with a minus (-) sign before the number. The data was acquired in four runs during one scanning session. Each run comprised 64 trials. The gamble was presented on the screen until the participant responded or four seconds have passed, followed by a grey screen until the onset of the next trial. In the aforementioned NARPS study, the same amount of data was also acquired for an equal indifference condition where the possible gains ranged between 10-40 units while losses ranged between 5-20 units. This was not done for the IBC implementation, as no significant differences were observed between the two task designs in the NARPS study.    

The conditions for this task are described in `this table <condNARPS_>`__ and the main contrasts derived from those conditions are described in `this table <contNARPS_>`__.

.. dropdown:: Conditions for NARPS
   :name: condNARPS

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - strongly_accept
        - Subject accepted the gamble with high confidence
      * - weakly_accept
        - Subject accepted the gamble with low confidence
      * - weakly_reject
        - Subject rejected the gamble with low confidence
      * - strongly_reject
        - Subject rejected the gamble with high confidence
      * - stim
        - Mixed gamble stimulus with given units of potential gain and loss (amounts could vary between 5-20)
      * - gain
        - Significant parametric increase in BOLD signal to increasing potential gains
      * - loss
        - Significant parametric decrease in BOLD signal to increasing potential losses
      * - reject-accept
        - Gambles rejected vs. gambles accepted

.. dropdown:: Contrasts for NARPS
   :name: contNARPS

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - gain
        - potential gains during stim events
      * - loss
        - potential losses during stim events
      * - weakly_accept
        - accept the gamble with low confidence
      * - weakly_reject
        - reject the gamble with low confidence
      * - strongly_accept
        - accept the gamble with high confidence
      * - strongly_reject
        - reject the gamble with high confidence
      * - reject-accept
        - gambles rejected vs gambles accepted
      * - accept-reject
        - gambles accepted vs gambles rejected

FaceBody
--------

.. container:: tags

   :bdg-light:`body_maintenance` :bdg-primary:`visual_place_recognition` :bdg-primary:`visual_number_recognition` :bdg-light:`place_maintenance` :bdg-info:`working_memory` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychtoolbox-3 (Octave 5.2.0)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from `Stigliani A 2015 <https://doi.org/10.1523/JNEUROSCI.4822-14.2015>`__), where it was used to define category-selective cortical regions that respond preferentially to faces (e.g., fusiform face area), places (e.g., parahippocampal place area), bodies (e.g., extrastriate body area), or printed characters (e.g., visual word form area). A detailed description and code for the original protocol is available `here <https://github.com/VPNL/fLoc>`__. Each of the five aforementioned stimulus categories were associated with two related subcategories with 144 images per subcategory. The protocol used a mini-block design in which 12 stimuli of the same subcategory were presented in each block. The sequence of the blocks was randomized over the ten subcategories and a blank baseline condition, and each subject was presented with the same sequence. To ensure that the subjects remain alert throughout the experiment, they were asked to press a button when an image repeated as a mirrored image (flipped 1-back task). The data were acquired in four runs during one scanning session. Each run comprised of 76 blocks each associated with the conditions given in `this table <condFaceBody_>`__ that were equally represented. Each block consisted of 12 images and was 6 seconds long (500 ms/image).

The conditions for this task are described in `this table <condFaceBody_>`__ and the main contrasts derived from those conditions are described in `this table <contFaceBody_>`__.

.. dropdown:: Conditions for FaceBody
   :name: condFaceBody

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - bodies_body
        - Images of body parts (category) with full bodies without faces (subcategory)
      * - bodies_limb
        - Images of body parts (category) with just limbs (subcategory)
      * - characters_number
        - Images of printed characters (category) with just numbers (subcategory)
      * - characters_word
        - Images of printed characters (category) with just words (subcategory)
      * - faces_adult
        - Images of faces (category) of adults (subcategory)
      * - faces_child
        - Images of faces (category) of children (subcategory)
      * - objects_car
        - Images of objects (category) with just cars (subcategory)
      * - objects_instrument
        - Images of objects (category) with just musical instruments (subcategory)
      * - places_corridor
        - Images of places (category) with just corridors (subcategory)
      * - places_house
        - Images of places (category) with just houses (subcategory)

.. dropdown:: Contrasts for FaceBody
   :name: contFaceBody

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - bodies_body
        - body image 1-back task vs. fixation
      * - objects_instrument
        - object image 1-back task vs. fixation
      * - characters_number
        - character images 1-back vs fixation
      * - places_house
        - place image 1-back task vs. fixation
      * - faces_adult
        - face image 1-back task vs. fixation
      * - characters-others
        - character images 1-back vs. rest of categories
      * - faces-others
        - face image 1-back task vs. rest of categories
      * - objects_car
        - object image 0-back task vs. fixation
      * - places-others
        - place image 1-back task vs. rest of categories
      * - places_corridor
        - place image 1-back task vs. fixation
      * - bodies-others
        - body image 1-back task vs. rest of categories
      * - objects-others
        - object image 0-back task vs. rest of categories
      * - faces_child
        - face image 1-back task vs. fixation
      * - bodies_limb
        - body image 1-back task vs. fixation
      * - characters_word
        - words images 1-back vs fixation

Scene
-----

.. container:: tags

   :bdg-light:`oddball_detection` :bdg-light:`salience` :bdg-primary:`lower-left_vision` :bdg-primary:`upper-left_vision` :bdg-primary:`visual_scene_perception` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from `Douglas et al., 2017 <https://doi.org/10.1002/hipo.22673>`__ and was designed to identify how the brain combines spatial elements to form a coherent percept. To this end, participants judged whether Escher-like scenes were possible or impossible. 56 scenes were designed for the original study `Douglas et al., 2017 <https://doi.org/10.1002/hipo.22673>`__ that appeared spatially incoherent when viewed from a particular angle, and these were termed "impossible scenes". Possible counterparts were created to each impossible scene, and these were termed "possible scenes". For comparison, baseline non-scene images were created by scrambling the scenes and matched for low-level visual properties. A partially transparent circle was overlaid at a pseudo-random location on each of the scrambled scenes, such that half of these dots were found on the left and half on the right of the baseline scrambled images. These trials were called the "dot trials", and there were easy and hard versions that depended on the transparency of the overlaid circle. The data were acquired in four runs during one scanning session. Each run was comprised of 56 trials, 14 for "impossible scene" and "possible scene" conditions, and 7 for "dot easy left" and "dot easy right", "dot hard left" and "dot hard right".

The conditions for this task are described in `this table <condScene_>`__ and the main contrasts derived from those conditions are described in `this table <contScene_>`__.

.. dropdown:: Conditions for Scene
   :name: condScene

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - scene_impossible_correct
        - Impossible scene trial that the subject identified correctly
      * - scene_impossible_incorrect
        - Impossible scene trial that the subject identified incorrectly
      * - scene_possible_correct
        - Possible scene trial that the subject identified correctly
      * - scene_possible_incorrect
        - Possible scene trial that the subject identified incorrectly
      * - dot_easy_left
        - More opaque dot on left
      * - dot_easy_right
        - More opaque dot on right
      * - dot_hard_left
        - More transparent dot on left
      * - dot_hard_right
        - More transparent dot on right

.. dropdown:: Contrasts for Scene
   :name: contScene

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - dot_easy_left
        - looking for a salience dot in left visual field
      * - dot_easy_right
        - looking for a salience dot in right visual field
      * - dot_hard_left
        - looking for a low-salience dot in left visual field
      * - dot_hard_right
        - looking for a low-salience dot in right visual field
      * - scene_impossible_correct
        - successful identification of an impossible scene
      * - scene_impossible_incorrect
        - failed  identification an impossible scene
      * - scene_possible_correct
        - successful identification of an possible scene
      * - scene_possible_correct-scene_impossible_correct
        - successful identification of an possible vs impossible scene
      * - scene_correct-dot_correct
        - assessing scenes vs detecting a dot
      * - dot_left-right
        - looking for a dot in left vs right visual field
      * - dot_hard-easy
        - looking for low-salience vs high-salience dot

BreathHolding
-------------

.. container:: tags

   :bdg-light:`self_monitoring` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task was a part of the FBIRN (Function Biomedical Informatics Research Network) (`Keator et al., 2016 <https://doi.org/10.1016/j.neuroimage.2015.09.003>`__) battery of protocols designed to, amongst other goals, assess the major sources of variation in fMRI studies conducted across scanners, including instrumentation, acquisition protocols, challenge tasks, and analysis methods. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The BreathHolding task was designed to measure vascular response. In a block design, the participant alternated between breathing normally for 20 s and holding their breath for 16 s. They were given a warning 2 s before the hold breath signal was given, so they could prepare to hold their breath. This cycle was repeated 10 times. No response was required in this task.

The conditions for this task are described in `this table <condBreathHolding_>`__ and the main contrasts derived from those conditions are described in `this table <contBreathHolding_>`__.

.. dropdown:: Conditions for BreathHolding
   :name: condBreathHolding

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - breathe
        - Breathe normally
      * - get_ready
        - Prepare to hold breath
      * - hold_breath
        - Hold breath

.. dropdown:: Contrasts for BreathHolding
   :name: contBreathHolding

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - breathe
        - breathe normally
      * - hold_breath
        - hold breath
      * - hold-breathe
        - hold breath vs breathe normally
      * - breathe-hold
        - breathe normally vs hold breath

Checkerboard
------------

.. container:: tags

   

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task was a part of the FBIRN (Function Biomedical Informatics Research Network) (`Keator et al., 2016 <https://doi.org/10.1016/j.neuroimage.2015.09.003>`__) battery of protocols designed to, amongst other goals, assess the major sources of variation in fMRI studies conducted across scanners, including instrumentation, acquisition protocols, challenge tasks, and analysis methods. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The Checkerboard task is a block design sensorimotor task with alternating 16s long blocks of rest and visual stimulation with a checkerboard stimulus. In the checkerboard block, a checkerboard filling the visual field was presented for a period of 200 ms at random intervals (avg. ISI=762 ms, range: 500-1000 ms), and the subject pressed a button each time the checkerboard appeared on screen. The run starts and ends with fixation blocks, and 11 blocks of checkerboard stimulation are presented.

The conditions for this task are described in `this table <condCheckerboard_>`__ and the main contrasts derived from those conditions are described in `this table <contCheckerboard_>`__.

.. dropdown:: Conditions for Checkerboard
   :name: condCheckerboard

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - checkerboard
        - Checkerboard block
      * - fixation
        - Fixation block

.. dropdown:: Contrasts for Checkerboard
   :name: contCheckerboard

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - checkerboard-fixation
        - checkerboard

FingerTap
---------

.. container:: tags

   

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task was a part of the FBIRN (Function Biomedical Informatics Research Network) (`Keator et al., 2016 <https://doi.org/10.1016/j.neuroimage.2015.09.003>`__) battery of protocols designed to, amongst other goals, assess the major sources of variation in fMRI studies conducted across scanners, including instrumentation, acquisition protocols, challenge tasks, and analysis methods. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The FingerTap task is a block design reaction time task in which subjects press one of the four keypad buttons when they see a corresponding visual cue ('1' for button1, '2' for button2 and so on). The stimuli appear at 1 s intervals and subjects get 2 s to make their response. The run starts and ends with task blocks, with 4 task blocks per run and 64 trials per task block. The task blocks are interleaved with rest blocks lasting 15 s.

The conditions for this task are described in `this table <condFingerTap_>`__.

.. dropdown:: Conditions for FingerTap
   :name: condFingerTap

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - fingertap
        - Press button corresponding to visual stimulus
      * - rest
        - Rest block

ItemRecognition
---------------

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-info:`spatial_working_memory` :bdg-light:`spatial_working_memorytask_difficulty` :bdg-light:`numerosity` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: E-Prime 2.0 Professional (Psychological Software Tools, Inc.)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This task was a part of the FBIRN (Function Biomedical Informatics Research Network) (`Keator et al., 2016 <https://doi.org/10.1016/j.neuroimage.2015.09.003>`__) battery of protocols designed to, amongst other goals, assess the major sources of variation in fMRI studies conducted across scanners, including instrumentation, acquisition protocols, challenge tasks, and analysis methods. All modifications were done taking care to not alter the psychological state that the original tasks were designed to capture. The ItemRecognition task is a working memory (WM) task with load 1, 3 and 5. Subjects memorize a set of targets (digits) that appear in red. They are then presented with probes (also digits) in green and respond by indicating whether the probe is a target or not. This is also a block design task with 2 blocks each with the 3 WM load conditions and 2 blocks in which subjects identify the direction of arrows on the screen (Left or Right).

The conditions for this task are described in `this table <condItemRecognition_>`__ and the main contrasts derived from those conditions are described in `this table <contItemRecognition_>`__.

.. dropdown:: Conditions for ItemRecognition
   :name: condItemRecognition

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - load1_instr
        - Instruction signaling start of load 1 blocks
      * - encode1
        - Encode digit of load 1 blocks
      * - probe1_mem
        - Probe digit that was encoded at the start of load 1 blocks
      * - probe1_new
        - Probe digit that is new for load 1 blocks
      * - load3_instr
        - Instruction signaling start of load 3 blocks
      * - encode3
        - Encode digit of load 3 blocks
      * - probe3_mem
        - Probe digit that was encoded at the start of load 3 blocks
      * - probe3_new
        - Probe digit that is new for load 3 blocks
      * - load5_instr
        - Instruction signaling start of load 5 blocks
      * - encode5
        - Encode digit of load 5 blocks
      * - probe5_mem
        - Probe digit that was encoded at the start of load 5 blocks
      * - probe5_new
        - Probe digit that is new for load 5 blocks
      * - arrow_right
        - Rightward pointing arrow
      * - arrow_left
        - Leftward pointing arrow

.. dropdown:: Contrasts for ItemRecognition
   :name: contItemRecognition

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - encode5-encode1
        - encoding 5 vs 1 item
      * - probe5_mem-probe1_mem
        - probing an encoded digit in a load of 5 vs 1
      * - probe5_new-probe1_new
        - probing a new digit in a load 5 vs 1
      * - prob-arrow
        - probing digits vs trials of pointing arrows
      * - encode
        - encoding 1	 3 and 5 items","['visual_attention','spatial_working_memory']
      * - arrow_left-arrow_right
        - identifying a left vs right pointing arrow

VisualSearch
------------

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-info:`working_memory_maintenance` :bdg-primary:`visual_pattern_recognition` :bdg-primary:`visual_form_discrimination` :bdg-primary:`visual_search` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.10.0 (Python 3.8.5)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from `Kuo BC et al., 2016 <https://doi.org/10.1162/jocn_a_00352>`__, that aimed to elaborate the neurophysiological mechanism underlying the spatially specific activation of sensory codes while searching for a visual or remembered target. A set of eight stimuli items were selected from a set of 100 novel and difficult to verbalize closed shape contours previously developed by `Endo N et al. 2003 <https://pubmed.ncbi.nlm.nih.gov/14708480/>`__ in the original as well as in the IBC implementation of the study. Each run of the protocol involved two kinds of trials - visual search and working memory search. In visual search trials, the participants were first shown an abstract item (sample item) and then they had to search for that item in a set of two or four items (search array). In the working memory search trials, the participants were first shown a set of two or four items (memory array) and then they had to tell whether a subsequently shown item (probe item) was present in the previously shown set of items. Thus, in addition to the type of search (visual or working memory) and search response (target present or absent), the array load (two or four items) was also varied in each trial. The data was acquired in four runs during one scanning session. Each run comprised forty-eight trials. In the original study, the participants also performed a separate session for a visual localizer task, where they viewed the stimuli passively without making any responses. This session was excluded from the IBC implementation of the protocol. Further, the response period was also increased from 1000 msec to 2000 msec and the stimuli size from 1.72 to 1.80 degrees of visual angle, following the feedback from the pilot sessions. Apart from these changes, the rest of the task design was similar to that of the original study.

The conditions for this task are described in `this table <condVisualSearch_>`__ and the main contrasts derived from those conditions are described in `this table <contVisualSearch_>`__.

.. dropdown:: Conditions for VisualSearch
   :name: condVisualSearch

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - memory_array_two
        - Array of two items, with or without the item to search for (probe item) - in working memory trials
      * - memory_array_four
        - Array of four items, with or without the item to search for (probe item) - in working memory trials
      * - delay_wm
        - Delay period between memory array and probe item in working memory trials
      * - probe_item_two_absent
        - Item to search for but was absent in memory array of two items - in working memory trials
      * - probe_item_four_absent
        - Item to search for but was absent in memory array of four items - in working memory trials
      * - probe_item_two_present
        - Item to search for and was present in memory array of two items - in working memory trials
      * - probe_item_four_present
        - Item to search for and was present in memory array of four items - in working memory trials
      * - sample_item
        - Item to search for in an array of two or four items (search array) - in visual search trials
      * - delay_vis
        - Delay period between sample item and search array in visual search trials
      * - search_array_two_absent
        - Array of two items, without sample item - in visual search trials
      * - search_array_two_present
        - Array of two items, with sample item - in visual search trials
      * - search_array_four_absent
        - Array of four items, without sample item - in visual search trials
      * - search_array_four_present
        - Array of four items, with sample item - in visual search trials
      * - response_hit
        - Subject responded correctly
      * - response_miss
        - Subject responded incorrectly

.. dropdown:: Contrasts for VisualSearch
   :name: contVisualSearch

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - memory_array_four
        - array of four items with or without the item to search for
      * - memory_array_two
        - array of two items with or without the item to search for
      * - sample_item
        - item to search for in an array of two or four items
      * - delay_vis
        - delay period on visual search
      * - probe_item_four_absent
        - probing an absent item from array of four
      * - probe_item_two_absent
        - probing an absent item from array of four
      * - probe_item_four_present
        - probing a present item from array of four
      * - probe_item_two_present
        - probing a present item from array of four
      * - response_hit
        - subject's correct response
      * - response_miss
        - subject's incorrect response
      * - delay_wm
        - delay period on working memory
      * - search_array_four_absent
        - array of four items without sample item
      * - search_array_four_present
        - array of four items with sample item
      * - search_array_two_absent
        - array of two items without the sample item
      * - search_array_two_present
        - array of two items with the sample item
      * - probe_item
        - probing an item	 absent or present","['visual_search','visual_pattern_recognition','visual_form_discrimination']
      * - search_array
        - array of items	 four or two","['visual_pattern_recognition','visual_attention','visual_working_memory','visual_form_discrimination']
      * - probe_item_absent'probe_item_present
        - probing an absent vs present item
      * - search_array_absent'search_array_present 
        - array of items without vs with sample item
      * - probe_item_four'probe_item_two
        - probing an item from an array of four vs two
      * - search_array_four'search_array_two
        - array of four vs two items
      * - delay_vis'delay_wm
        - delay period on visual search vs on working memory

MonkeyKingdom
-------------

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.9.0 (Python 2.7)
   - Audio device: MRConfon MKII

The movie Monkey Kingdom (in french Au royaume des singes) task was adapted from a study done in the lab of Wim Vanduffel at Leuven University dedicated to investigate correspondence between monkey and human brains using naturalistic stimuli. The task relies on watching –viewing and listening– of the whole Disney movie “Monkey Kingdom”. The original, 81-minute movie was cut into 15-minute segments that corresponded to the segments in the original study. This resulted in a total of 5 segments. This acquisition was conducted in one session.


Color
-----

.. container:: tags

   :bdg-info:`working_memory` :bdg-light:`color_perception` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychopy 2021.1.3 (Python 3.8.5)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from `McKeefry et al., 1997 <https://doi.org/10.1093/brain/120.12.2229>`__, that aimed at exploring the position and variability of the colour centre in the human brain. The protocol used a mini-block design, in which 12 stimuli of the same type (either chromatic or achromatic) were presented consecutively. These stimuli were Mondrian patterns - abstract images with no recognizable objects - each composed of 20 cicular blobs of different isoluminant colors. Each run consisted of two kinds of blocks - chromatic and achromatic. During chromatic blocks, colored Mondrian patterns were presented while during achromatic blocks, grayscaled or achromatic versions of those patterns were presented. Both the conditions were equally represented in each run and the same randomized sequence of these conditions alternating with a baseline fixation cross was presented to each subject. To ensure that the subjects remained alert throughout the experiment, they were asked to press a button when an image repeated (1-back task). The data was acquired in four runs during one scanning session. Each run comprised of 36 blocks. Each block consisted of 12 images, was 7.2 seconds long (500 ms/image + 100 ms delay after each image) and was followed by a inter-block fixation cross that stayed on screen for 5 seconds. The images presented were 16 x 16 degrees of visual angle.

The conditions for this task are described in `this table <condColor_>`__ and the main contrasts derived from those conditions are described in `this table <contColor_>`__.

.. dropdown:: Conditions for Color
   :name: condColor

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - chromatic
        - Chromatic Mondrian patterns
      * - achromatic
        - Achromatic Mondrian patterns
      * - response
        - Subject's response to 1-back task i.e. when the same color pattern was presented twice consecutively

.. dropdown:: Contrasts for Color
   :name: contColor

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - chromatic
        - attending to chromatic mondrian patterns
      * - achromatic
        - attending to achromatic mondrian patterns
      * - chromatic-achromatic
        - chromatic vs achromatic mondrian patterns
      * - response
        - response to repeated mondrian patterns

Motion
------

.. container:: tags

   :bdg-primary:`lower-left_vision` :bdg-primary:`upper-left_vision` :bdg-light:`color_perception` :bdg-primary:`visual_awareness` :bdg-light:`motion detection` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychopy 2021.1.3. (Python 3.8.5)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from `Helfrich et al., 2013 <https://doi.org/10.1007/s10548-012-0226-1>`__, that aimed at delineating areas of the visual cortex that responded to coherent visual motion under conditions of controlled attention and fixation.  In this protocol, the stimulus was composed of a rectangular random dot pattern with white dots on a dark background. Each run consisted of trials with three different conditions, namely: stationary, coherent and incoherent motion. In coherent motion condition, the motion direction was same for all dots, while in incoherent motion condition, the dots moved independently in all possible directions. For both these motion conditions, the motion direction was changed every 2 seconds in steps of 60 degrees. Due to this, the coherent motion condition was further divided into types - one where the motion direction changed clockwise and the other where it changed anti-clockwise. During the stationary condition, which was the baseline, the random dot pattern was presented with a limited dot lifetime of 1000 ms as in the motion conditions. In addition to the motion conditions, the field of presentation of the stimuli was also varied during the experiment. This means that some of the stimuli in a run were presented only on the right, others on the left hand side and the rest on the full screen. During all the runs the subjects were asked to maintain a fixation on the central fixation point. This fixation point changed colors at a rate of 2 Hz selected randomly out of six colors (red, yellow, blue, green, magenta, white). To ensure that the subjects remained alert throughout the experiment, they were asked to press a button when this fixation point turned blue. The conditions were counterbalanced and were presented in the same randomized sequence to each subject. The randomized sequence of the changing colors of the fixation point was also the same for each subject. The data was acquired in four runs during one scanning session. Each run comprised of 32 trials. Each trial was 12 seconds long with changes in motion direction (only in the motion conditions) after every 2 seconds in steps of 60 degrees. Each trial was followed by an inter-trial fixation cross that stayed on the screen for 2 seconds. The fixation point remained on the screen throughout each trial and changed colors randomly at a rate of 2 Hz (i.e. after every 500 ms). The stimuli were extended to 40 degrees in the horizontal and 20 degrees in the vertical direction. The central visual area of 3 x 3 degrees was not stimulated. Each dot (including the fixation dot) had a diameter of 8.6 arc min and moved at 6 degrees/sec. All the dots had a limited lifetime of 1000 ms and dot density was 6 dots/degree^2 throughout all trials.

The conditions for this task are described in `this table <condMotion_>`__ and the main contrasts derived from those conditions are described in `this table <contMotion_>`__.

.. dropdown:: Conditions for Motion
   :name: condMotion

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - incoherent
        - Motion condition when dots were moving incoherently in random directions
      * - coherent
        - Motion condition when dots were moving coherently in the same direction
      * - stationary
        - Motion condition when dots stayed stationary but each dot was respawned in a different location after 1 sec
      * - clock
        - Trials with direction of coherent motion changing in the clockwise direction
      * - anti
        - Trials with direction of coherent motion changing in the anti-clockwise direction
      * - left
        - Trials where dot pattern was presented only in the left visual field
      * - right
        - Trials where dot pattern was presented only in the right visual field

.. dropdown:: Contrasts for Motion
   :name: contMotion

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - incoherent
        - dots moving incoherently
      * - coherent
        - dots moving coherently
      * - stationary
        - stationary dots appearing in different locations
      * - clock
        - motion in clockwise direction
      * - anti
        - anti-clockwise motion
      * - response
        - fixation point turning blue
      * - coherent-incoherent
        - dots moving coherently vs coherently
      * - coherent-stationary
        - dots moving coherently vs staying stationary
      * - incoherent-stationary
        - dots moving incoherently vs staying stationary
      * - clock-anti
        - clockwise vs anti-clockwise motion
      * - left-right
        - dot pattern in left vs right visual field

OptimismBias
------------

.. container:: tags

   :bdg-light:`self-reference_effect` :bdg-light:`past_time` :bdg-light:`future_time` :bdg-light:`episodic_future_thinking` :bdg-info:`emotional_memory` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychopy 2021.1.3. (Python 3.8.5)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from `Sharot et al. 2007 <https://doi.org/10.1038/nature06280>`__, that aimed at examining the neurobiological basis of optimism. The subjects were presented with a series of events as text that described a life episode alongwith the word "past" or "future" to indicate that the subjects had to think of the given event such that it occurred in the past or might occur in the future. They were instructed to press a button once the memory or projection of that event was beginning to form in their mind. Following that, they had to rate the memory or projection for whether the event was (very, a little or not at all) emotionally arousing and also its valence (whether it was negative or positive). Each event was displayed for 14 seconds on the screen and they had 2 seconds for each rating (emotional arousal and valence) task. In the original study, 80 unique events were presented over 4 runs (20 events in each run). For IBC, we added a fifth run where the events were picked randomly out of the given 80 and the past and future contingencies were reversed. Each run was 10 minutes and 2 seconds long. Each trial was labeled with one of the conditions given in `this table <condOptimismBias_>`__ based on the rating received for emotional arousal and valence from the subjects. Trials were labeled negative when they received high ("very") or medium ("a little") arousal rating and negative valence. Similarly, they were labeled positive when they received high ("very") or medium ("a little") arousal rating and positive valence. In case of all other combinations of responses, trials were labeled neutral and in absence of either or both responses they were labeled inconclusive. Past and future part of the label of course depended upon whether the presented event was that of past or future. 

The conditions for this task are described in `this table <condOptimismBias_>`__ and the main contrasts derived from those conditions are described in `this table <contOptimismBias_>`__.

.. dropdown:: Conditions for OptimismBias
   :name: condOptimismBias

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - past_positive
        - Past, positive valence and very or a little arousing event
      * - past_negative
        - Past, negative valence and very or a little arousing event
      * - future_positive
        - Future, positive valence and very or a little arousing event
      * - future_negative
        - Future, negative valence and very or a little arousing event
      * - past_neutral
        - Past, negative or positive valence and not at all arousing event
      * - future_neutral
        - Future, negative or positive valence and not at all arousing event
      * - inconclusive
        - Absence of either or both responses

.. dropdown:: Contrasts for OptimismBias
   :name: contOptimismBias

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - all_events
        - all events
      * - optimism_bias
        - future negative vs other events
      * - future_vs_past
        - future  vs past events
      * - positive_vs_negative
        - positive vs negative events
      * - future_positive_vs_negative
        - future positive vs negative
      * - past_positive_vs_negative
        - past positive vs negative
      * - interaction
        - interaction of (future vs past) and (positive vs negative)

MovieAomic
----------

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Expyriment 0.9.0 (Python 2.7)
   - Audio device: MRConfon MKII

This was a passive movie watching task. The movie clip presented was about 11 minutes long and consisted of continuous compilation of 22 natural scenes taken from the movie Koyaanisqatsi (`Reggio G. Koyaanisqatsi, 1982 <https://www.koyaanisqatsi.org/films/koyaanisqatsi.php>`__) with music composed by Philip Glass. As mentioned in (`Snoek et al., 2021 <https://doi.org/10.1038/s41597-021-00870-6>`__): "the scenes were selected because they broadly sample a set of visual parameters (textures and objects with different sizes and different rates of movement). Importantly, the focus on variation of visual parameters means, in this case, that the movie lacks a narrative and thus may be inappropriate to investigate semantic or other high-level processes". The resolution was adjusted to subtend a 16 degrees of visual angle (as in the orginal study) for the IBC setup.


HarririAomic
------------

.. container:: tags

   :bdg-danger:`emotional_expression` :bdg-primary:`visual_orientation` :bdg-primary:`emotional_face_recognition` :bdg-primary:`face_perception` :bdg-primary:`shape_recognition` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol is a part of the AOMIC (`Amsterdam Open MRI Collection <https://nilab-uva.github.io/AOMIC.github.io>`__) battery and is published in `Snoek et al., 2021 <https://doi.org/10.1038/s41597-021-00870-6>`__. HarririAomic explores the processes related to (facial) emotion processing. The subjects were shown three images each trial positioned in the form of a triangle - one on the top and two on the bottom. Their task was to say that which one of the two bottom images matched with the top one and respond accordingly. During a shape condition trial, they had to match the shape of the images i.e. whether the oval shape was vertically or horizontally oriented. While during a emotion condition trial, they had to match the emotion/facial expression (either fear or anger) in the images. The stimulus disappeared after 4.8 seconds or as soon as the subject responded and new trial always appeared 5 seconds after the onset of each trial. This task was done for 2 runs and the trials were presented in a block-design with alternating *shape* and *emotion* blocks consisting of six stimuli of 5 seconds each. There were four blocks for each condition, making each run 270 seconds long.

The conditions for this task are described in `this table <condHarririAomic_>`__ and the main contrasts derived from those conditions are described in `this table <contHarririAomic_>`__.

.. dropdown:: Conditions for HarririAomic
   :name: condHarririAomic

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - shape
        - Viewing a shape
      * - emotion
        - When the presented trial was that with emotions
      * - index_response
        - When subject responded with index finger, meaning the image on left matched with image on top
      * - middle_response
        - When subject responded with middle finger, meaning the image on right matched with image on top

.. dropdown:: Contrasts for HarririAomic
   :name: contHarririAomic

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - emotion
        - match the facial expression
      * - shape
        - match the shape of images
      * - index_response
        - matching left image to top cue
      * - middle_response
        - matching right image to top cue
      * - emotion-shape
        - match facial expression vs the shape of image

FacesAomic
----------

.. container:: tags

   :bdg-danger:`negative_emotion` :bdg-light:`feature_integration` :bdg-primary:`facial_expression` :bdg-danger:`emotional_expression` :bdg-light:`gender_perception` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol is a part of the AOMIC (`Amsterdam Open MRI Collection <https://nilab-uva.github.io/AOMIC.github.io>`__) battery and is published in `Snoek et al., 2021 <https://doi.org/10.1038/s41597-021-00870-6>`__. FacesAomic explores the processes related to (emotional) facial perception. The stimuli here are videos of people's facial expressions, male or female, northern european or mediterranean, where they were expressing certain emotion (pride, contempt, anger, joy or no expression). For IBC, this protocol was implemented slightly differently from what is mentioned in `Snoek et al., 2021 <https://doi.org/10.1038/s41597-021-00870-6>`__. The run duration was extended from about 4 minutes to 6 minutes and an additional run of 6 minutes was done by adding a few more of the said video stimuli from the `Amsterdam Dynamic Facial Expression Set (ADFES) <https://aice.uva.nl/research-tools/adfes-stimulus-set/adfes-stimulus-set.html?cb>`__ (`Schalk et al., 2011 <https://doi.org/10.1037/a0023853>`__). More specifically, in addition to the female models, we also used the videos with male models and added a post-acquisition task to control for attention after each run, instead of just passive viewing as in the original study. The subjects were instructed to try and remember the faces as well as expressions they had seen during the acquisition run and then say post-acquisition whether a given video was presented before. Each video was 4 seconds long, with 5 seconds of inter-trial interval and 8 videos in each run. Each video was associated with three conditions - *emotions*, *sex* and *ethnicity* which were counterbalanced in each and across runs.

The conditions for this task are described in `this table <condFacesAomic_>`__ and the main contrasts derived from those conditions are described in `this table <contFacesAomic_>`__.

.. dropdown:: Conditions for FacesAomic
   :name: condFacesAomic

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - anger
        - Video of a face expressing anger
      * - contempt
        - Video of a face expressing contempt
      * - joy
        - Video of a face expressing joy
      * - pride
        - Video of a face expressing pride
      * - neutral
        - Baseline, when no emotion was expressed
      * - male
        - Video with male face expressing some emotion
      * - female
        - Video with female face expressing some emotion
      * - mediterranean
        - Video with a mediterranean ethnicity model expressing some emotion
      * - european
        - Video with an european ethnicity model expressing some emotion

.. dropdown:: Contrasts for FacesAomic
   :name: contFacesAomic

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - anger
        - attending to face expressing anger
      * - contempt
        - attending to face expressing contempt
      * - joy
        - attending to face expressing joy
      * - neutral
        - attending to neutral face
      * - pride
        - attending to face expressing pride
      * - all-neutral
        - attending to expressive vs neutral faces
      * - anger-neutral
        - attending to angry vs neutral face
      * - contempt-neutral
        - attending to contempt vs neutral face
      * - joy-neutral
        - attending to joyful vs neutral face
      * - pride-neutral
        - attending to pride vs neutral face
      * - male-female
        - attending to male vs female face
      * - female-male
        - attending to female vs male face
      * - mediterranean-european
        - attending to mediterranean vs european ethnicity face
      * - european-mediterranean
        - attending to european vs mediterranean ethnicity face

StroopAomic
-----------

.. container:: tags

   :bdg-light:`conflict_detection` :bdg-primary:`visual_word_recognition` :bdg-light:`gender_perception` :bdg-primary:`face_perception` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol is a part of the AOMIC (`Amsterdam Open MRI Collection <https://nilab-uva.github.io/AOMIC.github.io>`__) battery and is published in `Snoek et al., 2021 <https://doi.org/10.1038/s41597-021-00870-6>`__. StroopAomic explores the processes related to cognitive conflict and control. The subjects were presented with images of faces of male and female models in greyscale with certain words associated with each sex in red overlayed on top of these images. The words used were French ones for "man", "sir", "woman", and "lady" in either lower or upper case. Their task was to say whether the image was that of a male or a female model while ignoring the word overlayed on top of the image. Everything was implemented the same way for IBC as in the original study except for the images of faces which were not available. The images were hence taken from `another stimulus set <https://osf.io/g27wf/>`__ used in `Morrison2017 <https://doi.org/10.1371/journal.pone.0185093>`__. In addition, two runs were done instead of just one as in the original study. Each face-word composite stimulus was presented for 0.5 seconds in an event-related design, and was either *congruent* (same sex of face and word) or *incongruent* (different sex of face and word). Total 96 such stimuli were presented making each run 270 seconds long and there were 2 runs. The *congruent* and *incongruent* conditions were counterbalanced in each run. The response condition was inserted for each trial post-run based on subject responses to make the contrasting easier.

The conditions for this task are described in `this table <condStroopAomic_>`__ and the main contrasts derived from those conditions are described in `this table <contStroopAomic_>`__.

.. dropdown:: Conditions for StroopAomic
   :name: condStroopAomic

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - congruent
        - The presented word matches the face shown
      * - incongruent
        - The presented word did not match the face shown
      * - face_male
        - Male face shown
      * - face_female
        - Female face shown
      * - word_male
        - The presented word corresponds to a male
      * - word_female
        - The presented word corresponds to a female

.. dropdown:: Contrasts for StroopAomic
   :name: contStroopAomic

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - incongruent_word_male_face_female
        - attending to female face while reading 'male'
      * - congruent_word_female_face_female
        - attending to female face while reading 'female'
      * - congruent_word_male_face_male
        - attending to male face while reading 'male'
      * - incongruent_word_female_face_male
        - attending to male face while reading 'female'
      * - index_response
        - identifying a male face
      * - middle_response
        - identifying a female face
      * - congruent-incongruent
        - word and face matched vs did not match
      * - incongruent-congruent
        - word and face did not match vs matched
      * - face_male-face_female
        - male vs female face
      * - word_male-word_female
        - word 'male' vs 'female'
      * - index-middle
        - indicate the face is of male vs of female
      * - middle-index
        - indicate the face is of female vs of male

WorkingMemoryAomic
------------------

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-primary:`visual_orientation` :bdg-info:`visual_working_memory` 

.. admonition:: Implemented using proprietary software
   :class: seealso

   - Software: Presentation (Version 20.1, Neurobehavioral Systems, Inc., Berkeley, CA)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol is a part of the AOMIC (`Amsterdam Open MRI Collection <https://nilab-uva.github.io/AOMIC.github.io>`__) battery and is published in `Snoek et al., 2021 <https://doi.org/10.1038/s41597-021-00870-6>`__. WorkingMemoryAomic explores the processes related to visual working memory. The trials were presented in a fixed event-related in a design and each consisted of six phases: an alert phase (1 second), an encoding phase (1 second), a retention phase (2 seconds), a test phase (1 second), a response phase (1 second) and an inter-stimulus interval (0-4 seconds). In the retention phase, the subjects were shown a set of six white bars arranged in a circle around a fixation cross. Each of these bars had a random orientation (either 0, 45, 90, or 135 degrees). Then in the test phase, one of these six blocks appeared again - either with same orientation or a different one. The subject's task was to say whether or not the bar had the same orientation during response phase and respond accordingly. Each trial was associated with one of three conditions: *active_change*, *active_no_change* or *passive*. In total, there were 8 *passive* trials, 16 *active_change* and *active_no_change* trials, in addition to 20 *null* trials of 6 seconds (which are equivalent to an additional inter-stimulus interval of 6 seconds). Each run was 324 seconds long and there were two runs of this task.

The conditions for this task are described in `this table <condWorkingMemoryAomic_>`__ and the main contrasts derived from those conditions are described in `this table <contWorkingMemoryAomic_>`__.

.. dropdown:: Conditions for WorkingMemoryAomic
   :name: condWorkingMemoryAomic

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - active_change
        - The probe had a different orientation than it had on the array
      * - active_no_change
        - The probe had the same orientation than it had on the array
      * - passive
        - Passive trials, the bars were not displayed

.. dropdown:: Contrasts for WorkingMemoryAomic
   :name: contWorkingMemoryAomic

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - active_change
        - probe did not match previous orientation
      * - active_no_change
        - probe matched previous orientation
      * - passive
        - null event
      * - active-passive
        - assess probe orientation vs null event
      * - active_change-active_no_change
        - probe did not match vs matched orientation

AbstractionLocalizer
--------------------

.. container:: tags

   :bdg-primary:`visual_attention` :bdg-primary:`visual_place_recognition` :bdg-primary:`vertical_checkerboard` :bdg-primary:`visual_number_recognition` :bdg-primary:`horizontal_checkerboard` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychtoolbox-3 (MATLAB 2021b)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from an ongoing study from our colleagues at Neurospin, CEA Saclay, France. The goal of the study is to understand the neural representations of  real-world things from different semantic categories at various levels of abstraction/rendering, and with that aim, they encountered the need to have a special run to localize areas or regions specific to different categories before presenting them on different levels of abstraction. The localizer was different from the four runs in that the images were from eight different categories - faces, human body, words, non-sense words, numbers, places, objects and checkerboards. Each category in the localizer was presented in a block of 6 seconds with each image being displayed for 100 ms followed by a 200 ms inter-stimuli interval.

The conditions for this task are described in `this table <condAbstractionLocalizer_>`__ and the main contrasts derived from those conditions are described in `this table <contAbstractionLocalizer_>`__.

.. dropdown:: Conditions for AbstractionLocalizer
   :name: condAbstractionLocalizer

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - localizer_faces
        - Face images
      * - localizer_humanbody
        - Body images
      * - localizer_words
        - Words images
      * - localizer_nonsensewords
        - Non-sense words images
      * - localizer_numbers
        - Number images
      * - localizer_places
        - Place images
      * - localizer_objects
        - Object Images
      * - localizer_checkerboards
        - Checkerboards images
      * - response
        - Subject's button press when they saw a star

.. dropdown:: Contrasts for AbstractionLocalizer
   :name: contAbstractionLocalizer

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - localizer_faces
        - localizer for human faces
      * - localizer_humanbody
        - localizer for human bodies
      * - localizer_words
        - localizer for words
      * - localizer_nonsensewords
        - localizer for nonsense words
      * - localizer_numbers
        - localizer for numbers
      * - localizer_places
        - localizer for places
      * - localizer_objects
        - localizer for objects
      * - localizer_checkerboards
        - localizer for checkerboards
      * - localizer_faces-other
        - human faces vs other categories
      * - localizer_humanbody-other
        - human bodies vs other categories
      * - localizer_words-other
        - words vs other categories
      * - localizer_nonsensewords-other
        - nonsense words vs other categories
      * - localizer_numbers-other
        - numbers vs other categories
      * - localizer_places-other
        - places vs other categories
      * - localizer_objects-other
        - objects vs other categories
      * - localizer_checkerboards-other
        - checkerboards vs other categories
      * - response
        - response to star image as control

Abstraction
-----------

.. container:: tags

   :bdg-primary:`visual_form_recognition` :bdg-primary:`visual_place_recognition` :bdg-secondary:`semantic_categorization` :bdg-light:`mental_representation` :bdg-primary:`visual_body_recognition` 

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychtoolbox-3 (MATLAB 2021b)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from an ongoing study from our colleagues at Neurospin, CEA Saclay, France. The goal of the study is to understand the neural representations of  real-world things from different semantic categories at various levels of abstraction/rendering. So to achieve that, the subjects were presented with images belonging to six different semantic categories - human body, animals, faces, flora, objects and places, all rendered at three different levels of detail namely - geometry, edges and photos (in an ascending order of detail). To control for the attention there were five images of a star and the subjects were required to press a button when they saw them. There were four different examples from each category making a total of (6 categories x 4 examples x 3 renderings = 72 + 5 star probes =) 77 images. Each image was presented twice, for 300 ms with a variable inter-stimulus durations of 4, 6 or 8 seconds. There were 8 such runs and a localizer. The localizer was different from the four runs in that the images were from eight different categories - faces, human body, words, non-sense words, numbers, places, objects and checkerboards. Each category in the localizer was presented in a block of 6 seconds with each image being displayed for 100 ms followed by a 200 ms inter-stimuli interval. Each category block was presented 5 times (8 categories x 5 = 40 blocks) and the inter-block intervals were jittered for 4, 6 and 8 seconds (mean = 6 seconds).

The conditions for this task are described in `this table <condAbstraction_>`__ and the main contrasts derived from those conditions are described in `this table <contAbstraction_>`__.

.. dropdown:: Conditions for Abstraction
   :name: condAbstraction

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - humanbody_standing_geometry
        - Geometry rendering of standing human
      * - humanbody_walking_geometry
        - Geometry rendering of walking human
      * - humanbody_hand_geometry
        - Geometry rendering of hands
      * - humanbody_legs_geometry
        - Geometry rendering of legs
      * - humanbody_standing_edge
        - Edge rendering of standing human
      * - humanbody_walking_edge
        - Edge rendering of walking human
      * - humanbody_hand_edge
        - Edge rendering of hands
      * - humanbody_legs_edge
        - Edge rendering of legs
      * - humanbody_standing_photo
        - Photo rendering of standing human
      * - humanbody_walking_photo
        - Photo rendering of walking human
      * - humanbody_hand_photo
        - Photo rendering of hands
      * - humanbody_legs_photo
        - Photo rendering of legs
      * - animals_bird_geometry
        - Images of a bird presented with the geometry render
      * - animals_fish_geometry
        - Images of a fish presented with the geometry render
      * - animals_giraffe_geometry
        - Images of a giraffe presented with the geometry render
      * - animals_butterfly_geometry
        - Images of a butterfly presented with the geometry render
      * - animals_bird_edge
        - Images of a bird presented with the edge render
      * - animals_fish_edge
        - Images of a fish presented with the edge render
      * - animals_giraffe_edge
        - Images of a giraffe presented with the edge render
      * - animals_butterfly_edge
        - Images of a butterfly presented with the edge render
      * - animals_bird_photo
        - Images of a bird presented with the photo render
      * - animals_fish_photo
        - Images of a fish presented with the photo render
      * - animals_giraffe_photo
        - Images of a giraffe presented with the photo render
      * - animals_butterfly_photo
        - Images of a butterfly presented with the photo render
      * - faces_face_geometry
        - Image of a face presented with the geometry render
      * - faces_face2_geometry
        - Image of a different face presented with the geometry render
      * - faces_eyes_geometry
        - Image of eyes presented with the geometry render
      * - faces_cat_geometry
        - Image of a cat face presented with the geometry render
      * - faces_face_edge
        - Image of a face presented with the edge render
      * - faces_face2_edge
        - Image of a different face presented with the edge render
      * - faces_eyes_edge
        - Image of eyes presented with the edge render
      * - faces_cat_edge
        - Image of a cat face presented with the edge render
      * - faces_face_photo
        - Image of a face presented with the photo render
      * - faces_face2_photo
        - Image of a different face presented with the photo render
      * - faces_eyes_photo
        - Image of eyes presented with the photo render
      * - faces_cat_photo
        - Image of a cat face presented with the photo render
      * - flora_tree_geometry
        - Image of a tree presented with the photo render
      * - flora_flower_geometry
        - Image of a flower presented with the photo render
      * - flora_cherry_geometry
        - Image of a cherry presented with the photo render
      * - flora_carrot_geometry
        - Image of a carrot presented with the photo render
      * - flora_tree_edge
        - Image of a tree presented with the photo render
      * - flora_flower_edge
        - Image of a flower presented with the photo render
      * - flora_cherry_edge
        - Image of a cherry presented with the photo render
      * - flora_carrot_edge
        - Image of a carrot presented with the photo render
      * - flora_tree_photo
        - Image of a tree presented with the photo render
      * - flora_flower_photo
        - Image of a flower presented with the photo render
      * - flora_cherry_photo
        - Image of a cherry presented with the photo render
      * - flora_carrot_photo
        - Image of a carrot presented with the photo render
      * - objects_truck_geometry
        - Image of a truck presented with the photo render
      * - objects_key_geometry
        - Image of a key presented with the photo render
      * - objects_camera_geometry
        - Image of a camara presented with the photo render
      * - objects_watch_geometry
        - Image of a watch presented with the photo render
      * - objects_truck_edge
        - Image of a truck presented with the photo render
      * - objects_key_edge
        - Image of a key presented with the photo render
      * - objects_camera_edge
        - Image of a camara presented with the photo render
      * - objects_watch_edge
        - Image of a watch presented with the photo render
      * - objects_truck_photo
        - Image of a truck presented with the photo render
      * - objects_key_photo
        - Image of a key presented with the photo render
      * - objects_camera_photo
        - Image of a camara presented with the photo render
      * - objects_watch_photo
        - Image of a watch presented with the photo render
      * - places_house_geometry
        - Image of a house presented with the photo render
      * - places_mountain_geometry
        - Image of a mountain presented with the photo render
      * - places_road_geometry
        - Image of a road presented with the photo render
      * - places_windmill_geometry
        - Image of a windmill presented with the photo render
      * - places_house_edge
        - Image of a house presented with the photo render
      * - places_mountain_edge
        - Image of a mountain presented with the photo render
      * - places_road_edge
        - Image of a road presented with the photo render
      * - places_windmill_edge
        - Image of a windmill presented with the photo render
      * - places_house_photo
        - Image of a house presented with the photo render
      * - places_mountain_photo
        - Image of a mountain presented with the photo render
      * - places_road_photo
        - Image of a road presented with the photo render
      * - places_windmill_photo
        - Image of a windmill presented with the photo render
      * - response
        - Subject's button press when they saw a star

.. dropdown:: Contrasts for Abstraction
   :name: contAbstraction

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - humanbody_geometry
        - geometry renders of human bodies
      * - humanbody_edge
        - edges renders of human bodies
      * - humanbody_photo
        - photos of human bodies
      * - animals_geometry
        - geometry renders of animals
      * - animals_edge
        - edge renders of an animals
      * - animals_photo
        - photo of an animal
      * - faces_geometry
        - geometry renders of human faces
      * - faces_edge
        - edge renders of human faces
      * - faces_photo
        - photos of human faces
      * - flora_geometry
        - geometry renders of flora
      * - flora_edge
        - edge renders of flora
      * - flora_photo
        - photos of flora
      * - objects_geometry
        - geometry renders of objects
      * - objects_edge
        - edge renders of objects
      * - objects_photo
        - photos of objects
      * - places_geometry
        - geometry renders of places
      * - places_edge
        - edge renders of places
      * - places_photo
        - photos of places
      * - humanbody-other
        - renders of human bodies vs of rest of categories
      * - animals-other
        - renders of animals vs of rest of categories
      * - faces-other
        - renders of faces vs of rest of categories
      * - flora-other
        - renders of flora vs of rest of categories
      * - objects-other
        - renders of objects vs of rest of categories
      * - places-other
        - renders of places vs of rest of categories
      * - geometry-other
        - geometry vs edge and photo render
      * - edge-other
        - edge vs geometry and photo render
      * - photo-other
        - photo vs geometry and edge render
      * - humanbody_geometry-humanbody_other
        - geometry vs edge and photo render of human bodies
      * - humanbody_edge-humanbody_other
        - edge vs geometry and photo render of human bodies
      * - humanbody_photo-humanbody_other
        - photo vs geometry and edge render of human bodies
      * - animals_geometry-animals_other
        - geometry vs edge and photo render of animals
      * - animals_edge-animals_other
        - edge vs geometry and photo render of animals
      * - animals_photo-animals_other
        - photo vs geometry and edge render of animals
      * - faces_geometry-faces_other
        - geometry vs edge and photo render of faces
      * - faces_edge-faces_other
        - edge vs geometry and photo render of faces
      * - faces_photo-faces_other
        - photo vs geometry and edge render of faces
      * - flora_geometry-flora_other
        - geometry vs edge and photo render of flora
      * - flora_edge-flora_other
        - edge vs geometry and photo render of flora
      * - flora_photo-flora_other
        - photo vs geometry and edge render of flora
      * - objects_geometry-objects_other
        - geometry vs edge and photo render of objects
      * - objects_edge-objects_other
        - edge vs geometry and photo render of objects
      * - objects_photo-objects_other
        - photo vs geometry and edge render of objects
      * - places_geometry-places_other
        - geometry vs edge and photo render of places
      * - places_edge-places_other
        - edge vs geometry and photo render of places
      * - places_photo-places_other
        - photo vs geometry and edge render of places
      * - response
        - button press to star

MDTB
----

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychopy 2021.1.3. (Python 3.8.5)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This protocol was adapted from a study conducted by `King et al., 2019 <https://doi.org/10.1038/s41593-019-0436-x>`__, where they aimed to investigate the functional organization of the cerebellum cortex by running a fMRI study with a collection of more than 20 tasks. The authors made the paradigm's code and parameters openly available for 9 of those tasks at the time `here <https://github.com/DiedrichsenLab/mdtb_reduced>`__, which allowed us to integrate them in the IBC project. The implementation was different than usual; here we presented all 9 tasks in one run, instead of dedicating a separated run for each task. The protocol consisted of a short training session outside the scanner and 4 runs inside the scanner. In every run each task was performed twice in blocks of 35 seconds. In every run each task was performed twice in blocks of 35 seconds. At the beginning of each block, the instructions were displayed for 5 seconds so that subjects remember the instructions and expected actions. Immediately after, the task was performed continuously for 30 seconds, therefore each run lasted around 10 minutes and 30 seconds. If the task involved response from the subjects, they received feedback on their performance, which was given in form of a green check mark or a red cross, for correct or incorrect answers. At the end of each run, the success rates for each task were displayed followed by a video of a knot being tied as a part of an attention control task during the action observation task (described below). Following are detailed descriptions for each task, and table 146 lists the main contrasts for the MDTB task: 

**1) Visual search:** Several 'L' shaped characters rotated at different angles were shown on each trial and subjects were asked to search for the standard (correct) orientation and press with their index finger if it was present, or with their middle finger if it was not. On each run, this task was performed twice, and for each time there were 12 trials, half of them being True (the correct 'L' shape was present). The order of True and False trials was randomized for each block on each run. 

**2) Action observation:** Videos of knots being tied were displayed along with their name tags, and subjects were asked to remember the knot and its name. Two different knots were presented per run, and at the end of each run, another video of a knot was shown, this time without the name tag. We then asked subjects if this particular knot was displayed during the run, and if so, say the name. Only for run 3 the knot displayed at end was presented during the run. 

**3) Flexion - extension:** Alternating cues with the words 'Extension' and 'Flexion' were presented, to indicate the participants to do so with their toes. 

**4) Finger sequence:** A sequence of 6 digits from 1 to 4 were displayed and subjects were asked to press the keys corresponding to the numbers in the shown sequence. The mapping went from index being 1 to pinky being 4. Each block consisted of 8 trials and two blocks were presented during each run. The trials could be either simple or complex: the simple trials involving one or two consecutive fingers, and the complex involving three or four fingers, not necessarily consecutive. As the subject pressed the buttons, the digits became green if the correct key was pressed or red if not. At the end of each trial, if all the digits on the sequence were accurately followed, a green check appeared as feedback, if one or more was incorrect, a red cross appeared. Each trial lasted for 3.5 seconds, if the subject didn't complete the sequence before the end of the trial, it was counted as incorrect and the red cross appeared. 

**5) Theory of mind:** The subject was presented with a short paragraph narrating a story, followed by a related statement. Subjects must decide whether the statement is true based on the initial paragraph by pressing with their index finger, or false by pressing with their middle finger. Four trials in total were performed per run, half of them being true. If the subject answered correctly, a green check appeared, and on the contrary, a red cross appeared. Each trial lasted 14 seconds, if the subject did not reply during that period, the trial was counted as a mistake and the negative feedback appeared. 

**6) 2-back:** Several images were presented, one after another. For each presented image, participants had to press with their index finger if it is the same that was presented 2 images before or with their middle finger if it was not. The trials were divided into easy and hard. The easy trials were the ones where the current image presented was not displayed two images before, and the hard trials were those where it was. There were 12 trials per block, 7 of the easy type and 5 of the hard type. As the rest of tasks, this was performed twice, leading to 24 trials in total per run. Each image was displayed for 2 seconds, followed by the feedback which was once again a green check or a red cross. 

**7) Semantic prediction**: Words from a sentence were shown, one at a time. Subjects must decide whether the last word fits into the sentence or not, by pressing with their index or middle finger, respectively. There were 4 trials per block, leading to 8 trials per run. Each block consisted of 2 'True' and 2 'False' trials, and the order of appearance was randomized. Each trial could be either hard or easy to perform, depending on the ambiguity of the sentence and there were 2 easy and 2 hard trials per block. The subjects received feedback after their response, a green check or a red cross, consistent with the tasks described above. 

**8) Romance movie watching:** A 30 second clip from the 2009 Disney Pixar movie 'Up' was presented without any sound. Subjects were instructed to watch passively. Two such clips were presented on each run, and no clip was repeated across or within the runs. 

**9) Rest:** Short resting-state period, a fixation cross was displayed and subjects were asked to fixate on it and not move.

The conditions for this task are described in `this table <condMDTB_>`__ and the main contrasts derived from those conditions are described in `this table <contMDTB_>`__.

.. dropdown:: Conditions for MDTB
   :name: condMDTB

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - search_easy
        - It is easy to judge whether there is a right-oriented 'L' shape present on the array
      * - search_hard
        - It is hard to judge whether there is a right-oriented 'L' shape present on the array
      * - action_action
        - Watching a pair of hands make a specific knot
      * - action_control
        - The resulting knot is shown from different angles
      * - flexion_extension
        - Continuous flexion and extension of toes
      * - finger_complex
        - Sequence of button presses that is hard to complete (with no consecutive or repeated fingers)
      * - finger_simple
        - Sequence of button presses that is easy to complete (using consecutive or repeated fingers)
      * - tom_belief
        - The statement presented relates to thoughts or believes the characters from the paragraph might have
      * - tom_photo
        - The statement presented relates to facts described on the paragraph
      * - 2back_easy
        - Easy 2-back trial, it is easy to remember whether the image was shown 2 images ago.
      * - 2back_hard
        - Hard 2-back trial, it is hard to remember whether the image was shown 2 images ago.
      * - semantic easy
        - Easy to decide whether the last word fits in the sentence, natural sequence
      * - semantic hard
        - Hard to decide whether the last word fits in the sentence, ambiguous sequence

.. dropdown:: Contrasts for MDTB
   :name: contMDTB

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Contrast
        - Description
      * - action_action 
        - watching hands make a specific knot
      * - action_control
        - resulting knot shown from different angles
      * - finger_simple
        - easy sequence of button presses
      * - finger_complex
        - hard sequence of button presses
      * - semantic_hard
        - hard to decide whether the last word fits in a sentence
      * - semantic_easy
        - easy to decide whether the last word fits in a sentence
      * - 2back_easy
        - easy 2-back
      * - 2back_hard
        - hard 2-back
      * - tom_photo
        - statement relates to facts from paragraph
      * - tom_belief
        - statement relates to character's believes
      * - search_easy
        - easy to look for the right-oriented shape
      * - search_hard
        - hard to look for the right-oriented shape
      * - flexion_extension
        - continuous toes flexion-extension
      * - action_action-control
        - hands making specific knot vs resulting knot
      * - finger_complex-simple
        - hard vs easy button sequence
      * - semantic_hard-easy
        - ambiguous vs natural sequence
      * - 2back_hard-easy
        - hard vs easy 2-back
      * - tom_belief-photo
        - statement relates to believes vs facts
      * - search_hard-easy
        - hard vs easy to look for the correct shape

Emotion
-------

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychtoolbox-3 (MATLAB 2021b)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

This tasks was inspired from `Favre et al., 2021 <https://doi.org/10.1016/j.neuroimage.2021.118132>`__. This protocol aimed to examine emotional processing and the regions engaged on it. The subjects were presented with a series of pictures divided in two categories: neutral and negative images. The scenes depicted were mainly in a social context, for instance people chatting or eating during the neutral block; and people suffering or fighting during the negative block. The task consisted of two runs and a short training session before the acquisition. Each run consisted of 12 blocks of 10 images, alternating between neutral and negative blocks. Every picture was displayed for 2 seconds, and the subjects were instructed to press with their index finger if the scene occurred indoors, either inside a building or a car. The inter-block interval lasted 2 seconds, in which a fixation cross was shown. In the middle and in the end of the run the subjects were presented with two questions: *How do you feel?* and *How nervous do you feel?*, along with a scale for them to answer, going from *not well* to *extremelly well* for the former question and *not nervous* to *extremely nervous* for the latter. The subjects used their index and middle fingers to slide through the scale and had 7 seconds to give their answer. The images used for stimuli were extracted from different databases: the International Affective Picture system (IAPS) (`Lang et al., 2008 <https://doi.org/10.1007/978-3-319-28099-8_42-1>`__), the Geneva Affective Picture Database (GAPED) ,(`Dan-Glauser and Scherer, 2011 <http://doi.org/10.3758/s13428-011-0064-1>`__), the Socio-Moral Image Databade (SMID) (`Crone et al., 2018 <https://doi.org/10.1371/journal.pone.0190954>`__), the Complex Affective Scene Set (COMPASS) (`Weierich et al., 2019 <https://doi.org/10.1525/collabra.256>`__), the Besançon Affective Picture Set-Adolescents (BAPS-Ado) (`Szymanska et al., 2015 <https://doi.org/10.1016/j.psychres.2015.04.055>`__) and the EmoMadrid database (`Carretié et al., 2019 <https://doi.org/10.1007/s11031-019-09780-y>`__). The training session was performed inside the scanner before running the experiment, in order to get the subject familiar with the task and the slider used to answer. The training consisted of 3 blocks: neutral, negative and neutral images, followed by the two questions. We therefore had three main conditions for the task: *neutral*, *negative* and *assesment*.

The conditions for this task are described in `this table <condEmotion_>`__.

.. dropdown:: Conditions for Emotion
   :name: condEmotion

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - neutral_image
        - Block of neutral images
      * - negative_image
        - Block of negative images
      * - echelle_valence
        - Subject’s rating of emotional state

MultiModal
----------

.. container:: tags

   

.. admonition:: Implementation 
   :class: seealso

   - Software: Psychopy 2021.1.3. (Python 3.8.5)
   - Response device: Five-button ergonomic pad (Current Designs, Package 932 with Pyka HHSC-1x5-N4)

   - Audio device: MRConfon MKII

   - Hardware: LabJack-U3, custom-made computer-controlled pneumatic system

This protocol was derived from work by colleagues at `Laboratory for Neuro- and Psychophysiology <https://gbiomed.kuleuven.be/english/research/50000666/50000669/50488669>`__ from the KU Leuven Medical School, who aimed to compare evoked responses to the same sensory stimulation across two different cohorts of human and non-human primates. Three categories of stimuli were used: visual, tactile and auditory. Visual stimuli consisted of grey-scale pictures of ten classes: monkey and human faces, monkey and human bodies (without the head), four-legged mammals, birds, man-made objects that looked either like a human or a monkey's body (e.g. guitar or kettle), fruits/vegetables and body-like sculptures. We presented 10 pictures per class, giving a total of 100 images, which were presented superimposed onto a pink noise background that filled the entire display. Tactile stimuli consisted of compressed air puffs delivered on both left and right side of the subjects' face on three different locations: above the upper lip, around the cheek area or middle lip and beneath the lower lip. The air puffs were delivered using 6 plastic pipes, one to each target location, with an intensity of 0.5 bars, at a distance of aproximately 5 mm to the face, without touching it. The plastic pipes were connected to a custom-made computer controlled pneumatic system in the console room. Auditory stimuli consisted of 1-second clips of different natural sounds from six classes: human speech, human no-speech (e.g. baby crying, cough), monkey calls, animal sounds (e.g. horse), tool sounds and musical instruments (e.g. scissors, piano), and sounds from nature (e.g. rain, thunder). There were 10 different sounds per class, thus 60 different sound-clips in total. MR-compatible headphones were used. To be congruent with the study from our colleagues, the auditory stimuli needed to be presented during silent periods, meaning no scanner noise, to ensure they were clearly audible and distinguishable (`Erb et al., 2018 <https://doi.org/10.1093/cercor/bhy243>`__). To achieve that, the repetion time (TR) for this protocol was modified to 2.6 seconds, during which we had a silence period (no data acquired, no scanner noise) of 1.2 seconds for stimuli presentation and 1.4 seconds of acquisition 120 time (TA). To ensure uniformity across the experiment, all three types of stimuli were presented during the silent period. Due to the change on TR and TA, some parameters were also updated to maintain a good enough spatial-resolution. :ref:`This table <multimodalparam>` contains the final set of acquisition parameters used for this protocol.

The conditions for this task are described in `this table <condMultiModal_>`__.

.. dropdown:: Conditions for MultiModal
   :name: condMultiModal

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Condition
        - Description
      * - audio_monkey
        - Monkey sounds used as audio stimulus
      * - audio_animal
        - Animal sounds different from monkeys used as audio stimulus
      * - audio_nature
        - Nature sounds (i.e. rain) used as audio stimulus
      * - audio_silence
        - Control condition for both audio and visual stimuli, no sound played and no image displayed
      * - audio_speech
        - Speech sounds used as audio stimulus
      * - audio_tools
        - Tools sounds used as audio stimulus
      * - audio_voice
        - Human sounds (i.e. laugh, cough) used as audio stimulus
      * - tactile_bottom
        - Air puffs delivered beneath the lower lips as tactile stimulus
      * - tactile_middle
        - Air puffs delivered by the middle lips as tactile stimulus
      * - tactile_top
        - Air puffs delivered above the upper lips as tactile stimulus
      * - tactile_novalve
        - Control condition for tactile stimulus, air is sent to the pair of pipes placed outside the coil, so it doesn't touch the subject
      * - image_animals
        - Image of an animal different from monkeys and birds used as visual stimulus
      * - image_birds
        - Image of a bird used as visual stimulus
      * - image_fruits
        - Image of fruits used as visual stimulus
      * - image_human_body
        - Image of a human body (without the head) used as visual stimulus
      * - image_human_face
        - Image of a human face used as visual stimulus
      * - image_human_object
        - Image of an object used by humans (i.e. guitar) used as visual stimulus
      * - image_monkey_body
        - Image of a monkey body (without the head) used as visual stimulus
      * - image_monkey_face
        - Image of a monkey face used as visual stimulus
      * - image_monkey_object
        - Image of an object used by monkeys (i.e. drinker) used as visual stimulus
      * - image_sculpture
        - Image of a sculpture used as visual stimulus

