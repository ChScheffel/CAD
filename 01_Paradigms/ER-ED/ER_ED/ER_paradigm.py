#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on August 12, 2021, at 10:12
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

# import parallel port for triggers
from psychopy import parallel
parallel.setPortAddress('0xEFF8') # needs to be checked !!!


import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import random # for randomization of comparison order
from itertools import compress # for logical indexing
from collections import Counter # for counting occurrences within a list
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
# two separate files for ER paradigm and ER discounting
expName1 = 't2_ER'
expName2 = 't2_1vs1'  
expName3 = 't2_ED'

expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName1)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = 't2_paradigm'
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
# For emotion regulation paradigm
filename1 = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName1)
# for 1 vs 1 comparisons
filename2 = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName2)
# for effort discounting
filename3 = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName3)

# An ExperimentHandler isn't essential but helps with data saving
# For emotion regulation paradigm
thisExp1 = data.ExperimentHandler(name=expName1, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\scheffel\\Scheffel\\Forschung\\A_Projects\\2021_COG-ER-ED\\COG-ER-ED\\01_Paradigms\\ER-ED\\ER_ED\\ER_paradigm.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename1)
# For 1 vs 1 comparisons
thisExp2 = data.ExperimentHandler(name=expName2, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\scheffel\\Scheffel\\Forschung\\A_Projects\\2021_COG-ER-ED\\COG-ER-ED\\01_Paradigms\\ER-ED\\ER_ED\\ER_paradigm.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename2)
# For effort discounting
thisExp3 = data.ExperimentHandler(name=expName3, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\scheffel\\Scheffel\\Forschung\\A_Projects\\2021_COG-ER-ED\\COG-ER-ED\\01_Paradigms\\ER-ED\\ER_ED\\ER_paradigm.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename3)

# save a log file for detail verbose info
logFile = logging.LogFile(filename1 +'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Randomize negative picture sets across negative Blocks
# create a list of 4 negative blocks
Stimuli_Order = list(range(1,6))
# randomize order
shuffle(Stimuli_Order)

# Create lists with all the different variable names
EDstratcompList = ['Ablenken', 'Distanzieren',
'Ablenken', 'Unterdrücken',
'Distanzieren', 'Unterdrücken'] # these are all the comparison pairs that will be done
EDstratList = [1, 2,
1, 3,
2, 3]

# The steps in which the monetary values will be adapted in the ED part
EDsteps = [1.00,0.50,0.25,0.13,0.06,0.03,0.02]
# The constant monetary value that will be assigned to the option that was not chosen in the 1€ vs 1€ comparison
EDfix = [2.00]
# Create array corresponding to rounds of effort discounting aka the list elements
EDrounds = list(range(3))
# Create array corresponding to every second element in the list of comparisons, which will be randomized for every participant
EDcomps = [0,2,4]
random.shuffle(EDcomps)

# Function to send triggers
def sendTrigger(triggerCode):
        if isinstance(triggerCode, np.integer):
            triggerCode = triggerCode.item()
        parallel.setData(triggerCode)
        core.wait(0.005) #wait 5 ms
        parallel.setData(0) # set Trigger Channel back to 0

# define trigger for events
trigger_ExpStart = 100
trigger_ExpEnd = 200

trigger_instr = 15

trigger_Fix = 10

trigger_choice = 26

# define trigger for specific buttons
trigger_space = 4
trigger_1 = 1
trigger_2 = 2
trigger_3 = 3

# 1 vs 1 comparisons:
# define 9 comparisons, with randomized left-right-assignment
leftright = [0,1]
VS1stratcompList = []
VS1stratList = []

for i in [0,1,2]: # each pair will be presented three times
    for j in [0,1,2]: # referring to elements in ED comp
        random.shuffle(leftright)
        VS1stratcompList.append(EDstratcompList[EDcomps[j] + leftright[0]])
        VS1stratcompList.append(EDstratcompList[EDcomps[j] + leftright[1]])
        VS1stratList.append(EDstratList[EDcomps[j] + leftright[0]])
        VS1stratList.append(EDstratList[EDcomps[j] + leftright[1]])

# create array corresponding to rounds of 1 vs 1 comparisons
VS1rounds = list(range(9))
# Create array corresponding to every second element in the list of comparisons, which will be randomized for every participant
VS1comps = [0,2,4,6,8,10,12,14,16]
random.shuffle(VS1comps)
         
############################
# INITIALIZE ALL COMPONENTS
############################

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Willkommen!\n\nDas Experiment besteht aus zwei Teilen.\nIm ersten Teil werden Sie Bilder betrachten und mittels verschiedener Strategien Ihre Emotionen regulieren.\n\nIm zweiten Teil werden Sie die verschiedenen Emotionsregulationsstrategien miteinander vergleichen.\n\nZum Fortfahren drücken Sie bitte die Leertaste.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WelcomeResponse = keyboard.Keyboard()



# Initialize components for Routine "Instruction_View"
Instruction_ViewClock = core.Clock()
text_ActiveViewing = visual.TextStim(win=win, name='text_ActiveViewing',
    text='ANSCHAUEN\n\nIn diesem Block werden Sie eine Reihe von Bildern sehen.\nDiese sollen Sie aufmerksam ansehen. Bitte reagieren\nSie natürlich auf die Bildinhalte, ohne aufkommende \nEmotionen zu verändern!\n\nZum Starten des Blocks drücken Sie bitte die Leertaste.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_view_resp = keyboard.Keyboard()

# Initialize components for Routine "Pics_View"
Pics_ViewClock = core.Clock()
image_view = visual.ImageStim(
    win=win,
    name='image_view', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fixcross"
fixcrossClock = core.Clock()
text_fixcross = visual.TextStim(win=win, name='text_fixcross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "Instruction_Reg"
Instruction_RegClock = core.Clock()
text_Instruction = visual.TextStim(win=win, name='text_Instruction',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_reg_resp = keyboard.Keyboard()

# Initialize components for Routine "Pics_Reg"
Pics_RegClock = core.Clock()
image_reg = visual.ImageStim(
    win=win,
    name='image_reg', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1,0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)


# Initialize components for Routine "Slider_Arousal"
Slider_ArousalClock = core.Clock()
text_slider_arousal = visual.TextStim(win=win, name='text_slider_arousal',
    text='Wie hoch schätzen Sie Ihre durchschnittliche emotionale Aufregung beim Betrachten der Bilder ein?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_arousal = visual.Slider(win=win, name='slider_arousal',
    size=[1.0,0.1], pos=(0, -0.2), units=None,
    labels=("sehr gering", "sehr hoch"), ticks=(0,400), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='black', fillColor='black', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "Slider_Effort"
Slider_EffortClock = core.Clock()
text_slider_effort = visual.TextStim(win=win, name='text_slider_effort',
    text='Wie hoch schätzen Sie Ihre geistige Anstrengung während des Anwendens der Strategie ein?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_effort = visual.Slider(win=win, name='slider_effort',
    size=(1.0,0.1), pos=(0, -0.2), units=None,
    labels=("sehr gering","sehr hoch"), ticks=(0,400), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='black', fillColor='black', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize buffer screen between ratings
RATINGbufferscreenClock = core.Clock()
RATINGbufferscreen = visual.TextStim(win=win, name='RATINGbufferscreen',
    text='',
    font='Open Sans',
    pos=[0,0.1], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bufferscreenkey = keyboard.Keyboard()
RATINGstorebutton = []

# ------------------------------
# 1 vs 1 components
# ------------------------------

# Initialize components for 1 vs 1 instruction routine
Instruction1vs1Clock = core.Clock()
VS1text = visual.TextStim(win=win, name='VS1text',
    text='Nun beginnt der nächste Teil.\n\nDie unterschiedlichen Strategien, die Sie gerade absolviert haben, werden nun nacheinander gegenübergestellt.\n'\
        'Auf dem Bildschirm erscheint die Frage "Welche Bezahlung würden Sie eher für welche Strategie annehmen?". Darunter befinden sich zwei Textfelder, '\
        'zum Beispiel "1,00€ für Ablenken" und "1,00€ für Distanzieren". Sie können die Frage beantworten, indem Sie mit der Maus '\
        '(mit einem einfachen Klick) auf eins der beiden Felder klicken. Dabei geht es nicht um Schnelligkeit! Nachdem Sie geklickt haben, '\
        'werden sich die Strategien verändern und Sie können sich erneut entscheiden. Auf diese Weise werden alle Strategien mehrmals miteinander verglichen.\n'\
        '\n\n'\
        'Drücken Sie die Leertaste, um zu beginnen.',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize 1vs1 question routine
VS1roundClock = core.Clock()
question = visual.TextStim(win=win, name='question',
    text='Welche Bezahlung würden Sie eher für welche Strategie annehmen?',
    font='Open Sans',
    pos=[0,0.1], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize 1vs1 mouse click routine
VS1click = event.Mouse(win=win)
x, y = [None, None]
VS1click.mouseClock = core.Clock()

# Initialize 1vs1 left button
VS1leftbutton = visual.ButtonStim(win, 
    text= '', font='Open Sans',
    pos=[-0.3,-0.15],units='height',
    letterHeight=0.03,
    size=[0.5,0.1], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=0.03,
    anchor='center',
    name='VS1leftbutton')
VS1leftbutton.buttonClock = core.Clock()

# Initialize 1vs1 right button
VS1rightbutton = visual.ButtonStim(win, 
   text= '', font='Open Sans',
   pos=[0.3,-0.15],units='height',
   letterHeight=0.03,
   size=[0.5,0.1], borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='black', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=0.03,
   anchor='center',
   name='VS1rightbutton')
VS1rightbutton.buttonClock = core.Clock()

# ------------------------------
# Effort Discounting components
# ------------------------------

# Initialize components for ED instruction routine
InstructionEDClock = core.Clock()
text_EDinstruction = visual.TextStim(win=win, name='text_EDinstruction',
    text='Nun ändert sich der Ablauf.\n\nEs verändern sich jetzt nicht mehr vorrangig die Strategien, sondern die Geldbeträge, die Ihnen geboten werden.\n'\
        'Bitte entscheiden Sie sich wieder für eine der Optionen, es geht dabei nicht um Schnelligkeit! \n'\
        'Die Geldbeträge werden Ihnen NICHT zusätzlich zu Ihrer Teilnahme-Vergütung ausgezahlt. Es handelt sich um fiktive Beträge.'\
        'Versuchen Sie deshalb bitte nicht, die Beträge künstlich in die Höhe zu treiben, sondern entscheiden Sie sich so, '\
        'dass Sie mit dem Verhältnis der Optionen wirklich zufrieden sind.\n'\
        '\n\n'\
        'Drücken Sie die Leertaste, um zu beginnen.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard() 

# Initialize ED question routine
EDroundClock = core.Clock()
question = visual.TextStim(win=win, name='question',
    text='Welche Bezahlung würden Sie eher für welche Strategie annehmen?',
    font='Open Sans',
    pos=[0,0.1], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize ED mouse click routine
EDclick = event.Mouse(win=win)
x, y = [None, None]
EDclick.mouseClock = core.Clock()

# Initialize ED left button
EDleftbutton = visual.ButtonStim(win, 
    text= '', font='Open Sans',
    pos=[-0.3,-0.15],units='height',
    letterHeight=0.03,
    size=[0.55,0.1], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=0.03,
    anchor='center',
    name='EDleftbutton')
EDleftbutton.buttonClock = core.Clock()

# Initialize ED right button
EDrightbutton = visual.ButtonStim(win, 
   text= '', font='Open Sans',
   pos=[0.3,-0.15],units='height',
   letterHeight=0.03,
   size=[0.55,0.1], borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='black', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=0.03,
   anchor='center',
   name='EDrightbutton')
EDrightbutton.buttonClock = core.Clock()

# Initialize ED buffer screen for between button clicks
EDbufferscreenClock = core.Clock()
EDbufferscreen = visual.TextStim(win=win, name='EDbufferscreen',
    text='Welche Bezahlung würden Sie eher für welche Strategie annehmen?',
    font='Open Sans',
    pos=[0,0.1], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bufferscreenkey = keyboard.Keyboard()
EDstorebutton = []
VS1storebutton = []

# Initialize components for Routine "Choice_reapply"
Choice_reapplyClock = core.Clock()
text_choice = visual.TextStim(win=win, name='text_choice',
    text='Nun werden Sie zum letzten Mal eine Reihe von Bildern sehen. Diese sollen Sie aufmerksam ansehen und dabei eine der vorherigen Strategien anwenden. Sie können sich nun entscheiden, welche der drei Strategien Sie einsetzen möchten.\n\nEntscheiden Sie sich bitte nun für eine der drei Strategien.\n\nDrücken Sie bitte die Taste\n1    für Ablenken\n2    für Distanzieren\n3    für Unterdrücken',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_choice = keyboard.Keyboard()

# Initialize components for Routine "Instruction_Choice"
Instruction_ChoiceClock = core.Clock()
text_instr_choice = visual.TextStim(win=win, name='text_instr_choice',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Pics_Choice"
Pics_ChoiceClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.0, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Stimuli_Choice = 'StimuliNegative_{}.xlsx'.format(Stimuli_Order[4])



# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Das Experiment ist nun beendet. Vielen Dank für die Teilnahme!\n\nBitte wenden Sie sich an die Versuchsleitung.\n\nZum Beenden bitte Leertaste drücken.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#########################
# START EXPERIMENT
#########################

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
WelcomeResponse.keys = []
WelcomeResponse.rt = []
_WelcomeResponse_allKeys = []
# hide mouse cursor
win.mouseVisible = False
# keep track of which components have finished
WelcomeScreenComponents = [WelcomeText, WelcomeResponse]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if WelcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.tStart = t  # local t and not account for scr refresh
        WelcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sendTrigger, trigger_ExpStart) 
        WelcomeText.setAutoDraw(True)
    
    # *WelcomeResponse* updates
    waitOnFlip = False
    if WelcomeResponse.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        WelcomeResponse.frameNStart = frameN  # exact frame index
        WelcomeResponse.tStart = t  # local t and not account for scr refresh
        WelcomeResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeResponse, 'tStartRefresh')  # time at next scr refresh
        WelcomeResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(WelcomeResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(WelcomeResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if WelcomeResponse.status == STARTED and not waitOnFlip:
        theseKeys = WelcomeResponse.getKeys(keyList=['space'], waitRelease=False)
        _WelcomeResponse_allKeys.extend(theseKeys)
        if len(_WelcomeResponse_allKeys):
            WelcomeResponse.keys = _WelcomeResponse_allKeys[-1].name  # just the last key pressed
            WelcomeResponse.rt = _WelcomeResponse_allKeys[-1].rt
            sendTrigger(trigger_space)
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if WelcomeResponse.keys in ['', [], None]:  # No response was made
    WelcomeResponse.keys = None
thisExp1.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks_view = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks_view.xlsx'),
    seed=None, name='blocks_view')
thisExp1.addLoop(blocks_view)  # add the loop to the experiment
thisBlocks_view = blocks_view.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_view.rgb)
if thisBlocks_view != None:
    for paramName in thisBlocks_view:
        exec('{} = thisBlocks_view[paramName]'.format(paramName))

for thisBlocks_view in blocks_view:
    currentLoop = blocks_view
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_view.rgb)
    if thisBlocks_view != None:
        for paramName in thisBlocks_view:
            exec('{} = thisBlocks_view[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instruction_View"-------
    continueRoutine = True
    # update component parameters for each repeat
    instr_view_resp.keys = []
    instr_view_resp.rt = []
    _instr_view_resp_allKeys = []
    # hide mouse cursor
    win.mouseVisible = False
    if blocks_view.thisN  == 1: # only second block
        conds_view_File = 'StimuliNegative_{}.xlsx'.format(Stimuli_Order[0])
    
    # keep track of which components have finished
    Instruction_ViewComponents = [text_ActiveViewing, instr_view_resp]
    for thisComponent in Instruction_ViewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instruction_ViewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instruction_View"-------
    while continueRoutine:
        # get current time
        t = Instruction_ViewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instruction_ViewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_ActiveViewing* updates
        if text_ActiveViewing.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_ActiveViewing.frameNStart = frameN  # exact frame index
            text_ActiveViewing.tStart = t  # local t and not account for scr refresh
            text_ActiveViewing.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_ActiveViewing, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(sendTrigger, trigger_instr) # send trigger for instruction
            text_ActiveViewing.setAutoDraw(True)
        
        # *instr_view_resp* updates
        waitOnFlip = False
        if instr_view_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            instr_view_resp.frameNStart = frameN  # exact frame index
            instr_view_resp.tStart = t  # local t and not account for scr refresh
            instr_view_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_view_resp, 'tStartRefresh')  # time at next scr refresh
            instr_view_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_view_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_view_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_view_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_view_resp.getKeys(keyList=['space'], waitRelease=False)
            _instr_view_resp_allKeys.extend(theseKeys)
            if len(_instr_view_resp_allKeys):
                instr_view_resp.keys = _instr_view_resp_allKeys[-1].name  # just the last key pressed
                instr_view_resp.rt = _instr_view_resp_allKeys[-1].rt
                sendTrigger(trigger_space) # send trigger for press for space bar
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction_ViewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruction_View"-------
    for thisComponent in Instruction_ViewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if instr_view_resp.keys in ['', [], None]:  # No response was made
        instr_view_resp.keys = None
    # the Routine "Instruction_View" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_view = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conds_view_File),
        seed=None, name='trials_view')
    thisExp1.addLoop(trials_view)  # add the loop to the experiment
    thisTrials_view = trials_view.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_view.rgb)
    if thisTrials_view != None:
        for paramName in thisTrials_view:
            exec('{} = thisTrials_view[paramName]'.format(paramName))
    
    for thisTrials_view in trials_view:
        currentLoop = trials_view
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_view.rgb)
        if thisTrials_view != None:
            for paramName in thisTrials_view:
                exec('{} = thisTrials_view[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixcross"-------
        continueRoutine = True
        # update component parameters for each repeat
        
        # random jitter between 3 and 5 seconds
        jitter = random.uniform(3,5)
        jitter = round(jitter, 1)
        # add jitter to log file
        thisExp1.addData('Fix_jitter', jitter)
        
        # hide mouse cursor
        win.mouseVisible = False
        
        # keep track of which components have finished
        fixcrossComponents = [text_fixcross]
        for thisComponent in fixcrossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixcrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixcross"-------
        while continueRoutine:
            # get current time
            t = fixcrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixcrossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fixcross* updates
            if text_fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fixcross.frameNStart = frameN  # exact frame index
                text_fixcross.tStart = t  # local t and not account for scr refresh
                text_fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fixcross, 'tStartRefresh')  # time at next scr refresh
                win.callOnFlip(sendTrigger, trigger_Fix) # send trigger for fix cross
                text_fixcross.setAutoDraw(True)
            if text_fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fixcross.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fixcross.tStop = t  # not accounting for scr refresh
                    text_fixcross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_fixcross, 'tStopRefresh')  # time at next scr refresh
                    text_fixcross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixcrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixcross"-------
        for thisComponent in fixcrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "Pics_View"-------
        continueRoutine = True
        #routineTimer.add(6.000000)
        # update component parameters for each repeat
        image_view.setImage(ImageFile)

        # hide mouse cursor
        win.mouseVisible = False

        # keep track of which components have finished
        Pics_ViewComponents = [image_view]
        for thisComponent in Pics_ViewComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Pics_ViewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Pics_View"-------
        while continueRoutine:# and routineTimer.getTime() > 0:
            # get current time
            t = Pics_ViewClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Pics_ViewClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_view* updates
            if image_view.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_view.frameNStart = frameN  # exact frame index
                image_view.tStart = t  # local t and not account for scr refresh
                image_view.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_view, 'tStartRefresh')  # time at next scr refresh
                win.callOnFlip(sendTrigger, TriggerBlockView) # send trigger for each picture -> same trigger for whole block
                image_view.setAutoDraw(True)
            if image_view.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_view.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_view.tStop = t  # not accounting for scr refresh
                    image_view.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_view, 'tStopRefresh')  # time at next scr refresh
                    image_view.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pics_ViewComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Pics_View"-------
        for thisComponent in Pics_ViewComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_view.addData('image_view.started', image_view.tStartRefresh)
        trials_view.addData('image_view.lasted', image_view.tStop)
        trials_view.addData('image_view.stopped', image_view.tStopRefresh)
        
        thisExp1.nextEntry()
    # completed 1.0 repeats of 'trials_view'
    
    # ------Prepare to start Routine "Slider_Arousal"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_arousal.reset()
    # show mouse cursor
    win.mouseVisible = True
    # keep track of which components have finished
    Slider_ArousalComponents = [text_slider_arousal, slider_arousal]
    for thisComponent in Slider_ArousalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Slider_ArousalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Slider_Arousal"-------
    while continueRoutine:
        # get current time
        t = Slider_ArousalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Slider_ArousalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_slider_arousal* updates
        if text_slider_arousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_slider_arousal.frameNStart = frameN  # exact frame index
            text_slider_arousal.tStart = t  # local t and not account for scr refresh
            text_slider_arousal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_slider_arousal, 'tStartRefresh')  # time at next scr refresh
            text_slider_arousal.setAutoDraw(True)
        
        # *slider_arousal* updates
        if slider_arousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_arousal.frameNStart = frameN  # exact frame index
            slider_arousal.tStart = t  # local t and not account for scr refresh
            slider_arousal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_arousal, 'tStartRefresh')  # time at next scr refresh
            slider_arousal.setAutoDraw(True)
        
        # Check slider_arousal for response to end routine
        if slider_arousal.getRating() is not None and slider_arousal.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Slider_ArousalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Slider_Arousal"-------
    for thisComponent in Slider_ArousalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks_view.addData('slider_arousal.response', slider_arousal.getRating())
    blocks_view.addData('slider_arousal.rt', slider_arousal.getRT())
    # the Routine "Slider_Arousal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "bufferscreen"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    bufferscreenkey.keys = []
    bufferscreenkey.rt = []
    _bufferscreenkey_allKeys = []
    # keep track of which components have finished
    RATINGbufferscreenComponents = [RATINGbufferscreen, bufferscreenkey]
    for thisComponent in RATINGbufferscreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RATINGbufferscreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "bufferscreen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = RATINGbufferscreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RATINGbufferscreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *bufferscreen* updates
        if RATINGbufferscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RATINGbufferscreen.frameNStart = frameN  # exact frame index
            RATINGbufferscreen.tStart = t  # local t and not account for scr refresh
            RATINGbufferscreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RATINGbufferscreen, 'tStartRefresh')  # time at next scr refresh
            RATINGbufferscreen.setAutoDraw(True)
        if RATINGbufferscreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RATINGbufferscreen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                RATINGbufferscreen.tStop = t  # not accounting for scr refresh
                RATINGbufferscreen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RATINGbufferscreen, 'tStopRefresh')  # time at next scr refresh
                RATINGbufferscreen.setAutoDraw(False)

        # *bufferscreenkey* updates
        waitOnFlip = False
        if bufferscreenkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bufferscreenkey.frameNStart = frameN  # exact frame index
            bufferscreenkey.tStart = t  # local t and not account for scr refresh
            bufferscreenkey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bufferscreenkey, 'tStartRefresh')  # time at next scr refresh
            bufferscreenkey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(bufferscreenkey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(bufferscreenkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if bufferscreenkey.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bufferscreenkey.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                bufferscreenkey.tStop = t  # not accounting for scr refresh
                bufferscreenkey.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bufferscreenkey, 'tStopRefresh')  # time at next scr refresh
                bufferscreenkey.status = FINISHED
        if bufferscreenkey.status == STARTED and not waitOnFlip:
            theseKeys = bufferscreenkey.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _bufferscreenkey_allKeys.extend(theseKeys)
            if len(_bufferscreenkey_allKeys):
                bufferscreenkey.keys = _bufferscreenkey_allKeys[-1].name  # just the last key pressed
                bufferscreenkey.rt = _bufferscreenkey_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RATINGbufferscreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Bufferscreen"-------
    for thisComponent in RATINGbufferscreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if bufferscreenkey.keys in ['', [], None]:  # No response was made
        bufferscreenkey.keys = None

    # ------Prepare to start Routine "Slider_Effort"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_effort.reset()
    # show mouse cursor
    win.mouseVisible = True
    # keep track of which components have finished
    Slider_EffortComponents = [text_slider_effort, slider_effort]
    for thisComponent in Slider_EffortComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Slider_EffortClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Slider_Effort"-------
    while continueRoutine:
        # get current time
        t = Slider_EffortClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Slider_EffortClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_slider_effort* updates
        if text_slider_effort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_slider_effort.frameNStart = frameN  # exact frame index
            text_slider_effort.tStart = t  # local t and not account for scr refresh
            text_slider_effort.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_slider_effort, 'tStartRefresh')  # time at next scr refresh
            text_slider_effort.setAutoDraw(True)
        
        # *slider_effort* updates
        if slider_effort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_effort.frameNStart = frameN  # exact frame index
            slider_effort.tStart = t  # local t and not account for scr refresh
            slider_effort.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_effort, 'tStartRefresh')  # time at next scr refresh
            slider_effort.setAutoDraw(True)
        
        # Check slider_effort for response to end routine
        if slider_effort.getRating() is not None and slider_effort.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Slider_EffortComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Slider_Effort"-------
    for thisComponent in Slider_EffortComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks_view.addData('slider_effort.response', slider_effort.getRating())
    blocks_view.addData('slider_effort.rt', slider_effort.getRT())
    # the Routine "Slider_Effort" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    thisExp1.nextEntry()
# completed 1.0 repeats of 'blocks_view'


# set up handler to look after randomisation of conditions etc
blocks_reg = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks_reg.xlsx'),
    seed=None, name='blocks_reg')
thisExp1.addLoop(blocks_reg)  # add the loop to the experiment
thisBlocks_reg = blocks_reg.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_reg.rgb)
if thisBlocks_reg != None:
    for paramName in thisBlocks_reg:
        exec('{} = thisBlocks_reg[paramName]'.format(paramName))

for thisBlocks_reg in blocks_reg:
    currentLoop = blocks_reg
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_reg.rgb)
    if thisBlocks_reg != None:
        for paramName in thisBlocks_reg:
            exec('{} = thisBlocks_reg[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instruction_Reg"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_Instruction.setText(instr_1 + '\n\n' + 'In diesem Block werden Sie eine Reihe von Bildern sehen. Diese sollen Sie aufmerksam ansehen.' + '\n' + instr_2 + '\n\n' + 'Bitte konzentrieren Sie Ihre Regulationsbemühungen nur auf das Bild, nicht aber auf die Zeiträume zwischen den Bildern.' + '\n\n' + 'Zum Starten des Blocks Leertaste drücken'
)
    instr_reg_resp.keys = []
    instr_reg_resp.rt = []
    _instr_reg_resp_allKeys = []
    # hide mouse cursor
    win.mouseVisible = False

    if blocks_reg.thisN  == 0: # first regulation block
        conds_reg_File = 'StimuliNegative_{}.xlsx'.format(Stimuli_Order[1])
        
    elif blocks_reg.thisN  == 1: # second block
        conds_reg_File = 'StimuliNegative_{}.xlsx'.format(Stimuli_Order[2])
    
    elif blocks_reg.thisN  == 2: # third block
        conds_reg_File = 'StimuliNegative_{}.xlsx'.format(Stimuli_Order[3])
    # keep track of which components have finished
    Instruction_RegComponents = [text_Instruction, instr_reg_resp]
    for thisComponent in Instruction_RegComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instruction_RegClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instruction_Reg"-------
    while continueRoutine:
        # get current time
        t = Instruction_RegClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instruction_RegClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Instruction* updates
        if text_Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Instruction.frameNStart = frameN  # exact frame index
            text_Instruction.tStart = t  # local t and not account for scr refresh
            text_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Instruction, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(sendTrigger, trigger_instr) # send trigger for instructions
            text_Instruction.setAutoDraw(True)
        
        # *instr_reg_resp* updates
        waitOnFlip = False
        if instr_reg_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            instr_reg_resp.frameNStart = frameN  # exact frame index
            instr_reg_resp.tStart = t  # local t and not account for scr refresh
            instr_reg_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_reg_resp, 'tStartRefresh')  # time at next scr refresh
            instr_reg_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_reg_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_reg_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_reg_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_reg_resp.getKeys(keyList=['space'], waitRelease=False)
            _instr_reg_resp_allKeys.extend(theseKeys)
            if len(_instr_reg_resp_allKeys):
                instr_reg_resp.keys = _instr_reg_resp_allKeys[-1].name  # just the last key pressed
                instr_reg_resp.rt = _instr_reg_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction_RegComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruction_Reg"-------
    for thisComponent in Instruction_RegComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if instr_reg_resp.keys in ['', [], None]:  # No response was made
        instr_reg_resp.keys = None
  
    # the Routine "Instruction_Reg" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_reg = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conds_reg_File),
        seed=None, name='trials_reg')
    thisExp1.addLoop(trials_reg)  # add the loop to the experiment
    thisTrials_reg = trials_reg.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_reg.rgb)
    if thisTrials_reg != None:
        for paramName in thisTrials_reg:
            exec('{} = thisTrials_reg[paramName]'.format(paramName))
    
    for thisTrials_reg in trials_reg:
        currentLoop = trials_reg
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_reg.rgb)
        if thisTrials_reg != None:
            for paramName in thisTrials_reg:
                exec('{} = thisTrials_reg[paramName]'.format(paramName))
        
         # ------Prepare to start Routine "fixcross"-------
        continueRoutine = True
        # update component parameters for each repeat
        # random jitter between 3 and 5 seconds
        jitter = random.uniform(3,5)
        jitter = round(jitter, 1)
        # add jitter to log file
        thisExp1.addData('Fix_jitter', jitter)

        # hide mouse cursor
        win.mouseVisible = False

        # keep track of which components have finished
        fixcrossComponents = [text_fixcross]
        for thisComponent in fixcrossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixcrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixcross"-------
        while continueRoutine:
            # get current time
            t = fixcrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixcrossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fixcross* updates
            if text_fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fixcross.frameNStart = frameN  # exact frame index
                text_fixcross.tStart = t  # local t and not account for scr refresh
                text_fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fixcross, 'tStartRefresh')  # time at next scr refresh
                win.callOnFlip(sendTrigger, trigger_Fix) # send trigger for fix cross
                text_fixcross.setAutoDraw(True)
            if text_fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_fixcross.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    text_fixcross.tStop = t  # not accounting for scr refresh
                    text_fixcross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_fixcross, 'tStopRefresh')  # time at next scr refresh
                    text_fixcross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixcrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixcross"-------
        for thisComponent in fixcrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "Pics_Reg"-------
        continueRoutine = True
        #routineTimer.add(6.000000)
        # update component parameters for each repeat
        image_reg.setImage(ImageFile)

        # hide mouse cursor
        win.mouseVisible = False

        # keep track of which components have finished
        Pics_RegComponents = [image_reg]
        for thisComponent in Pics_RegComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Pics_RegClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Pics_Reg"-------
        while continueRoutine: # and routineTimer.getTime() > 0:
            # get current time
            t = Pics_RegClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Pics_RegClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_reg* updates
            if image_reg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_reg.frameNStart = frameN  # exact frame index
                image_reg.tStart = t  # local t and not account for scr refresh
                image_reg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_reg, 'tStartRefresh')  # time at next scr refresh
                win.callOnFlip(sendTrigger, TriggerBlockReg) # send trigger for each picture 
                image_reg.setAutoDraw(True)
            if image_reg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_reg.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_reg.tStop = t  # not accounting for scr refresh
                    image_reg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_reg, 'tStopRefresh')  # time at next scr refresh
                    image_reg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pics_RegComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Pics_Reg"-------
        for thisComponent in Pics_RegComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_reg.addData('image_reg.started', image_reg.tStartRefresh)
        trials_reg.addData('image_reg.lasted', image_reg.tStop)
        trials_reg.addData('image_reg.stopped', image_reg.tStopRefresh)
        
        thisExp1.nextEntry()
    # completed 1.0 repeats of 'trials_reg'
    
    # ------Prepare to start Routine "Slider_Arousal"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_arousal.reset()
    # show mouse cursor
    win.mouseVisible = True
    # keep track of which components have finished
    Slider_ArousalComponents = [text_slider_arousal, slider_arousal]
    for thisComponent in Slider_ArousalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Slider_ArousalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Slider_Arousal"-------
    while continueRoutine:
        # get current time
        t = Slider_ArousalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Slider_ArousalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_slider_arousal* updates
        if text_slider_arousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_slider_arousal.frameNStart = frameN  # exact frame index
            text_slider_arousal.tStart = t  # local t and not account for scr refresh
            text_slider_arousal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_slider_arousal, 'tStartRefresh')  # time at next scr refresh
            text_slider_arousal.setAutoDraw(True)
        
        # *slider_arousal* updates
        if slider_arousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_arousal.frameNStart = frameN  # exact frame index
            slider_arousal.tStart = t  # local t and not account for scr refresh
            slider_arousal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_arousal, 'tStartRefresh')  # time at next scr refresh
            slider_arousal.setAutoDraw(True)
        
        # Check slider_arousal for response to end routine
        if slider_arousal.getRating() is not None and slider_arousal.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Slider_ArousalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Slider_Arousal"-------
    for thisComponent in Slider_ArousalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks_reg.addData('slider_arousal.response', slider_arousal.getRating())
    blocks_reg.addData('slider_arousal.rt', slider_arousal.getRT())
    # the Routine "Slider_Arousal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "bufferscreen"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    bufferscreenkey.keys = []
    bufferscreenkey.rt = []
    _bufferscreenkey_allKeys = []
    # keep track of which components have finished
    RATINGbufferscreenComponents = [RATINGbufferscreen, bufferscreenkey]
    for thisComponent in RATINGbufferscreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RATINGbufferscreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "bufferscreen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = RATINGbufferscreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RATINGbufferscreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *bufferscreen* updates
        if RATINGbufferscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RATINGbufferscreen.frameNStart = frameN  # exact frame index
            RATINGbufferscreen.tStart = t  # local t and not account for scr refresh
            RATINGbufferscreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RATINGbufferscreen, 'tStartRefresh')  # time at next scr refresh
            RATINGbufferscreen.setAutoDraw(True)
        if RATINGbufferscreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RATINGbufferscreen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                RATINGbufferscreen.tStop = t  # not accounting for scr refresh
                RATINGbufferscreen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RATINGbufferscreen, 'tStopRefresh')  # time at next scr refresh
                RATINGbufferscreen.setAutoDraw(False)

        # *bufferscreenkey* updates
        waitOnFlip = False
        if bufferscreenkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bufferscreenkey.frameNStart = frameN  # exact frame index
            bufferscreenkey.tStart = t  # local t and not account for scr refresh
            bufferscreenkey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bufferscreenkey, 'tStartRefresh')  # time at next scr refresh
            bufferscreenkey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(bufferscreenkey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(bufferscreenkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if bufferscreenkey.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bufferscreenkey.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                bufferscreenkey.tStop = t  # not accounting for scr refresh
                bufferscreenkey.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bufferscreenkey, 'tStopRefresh')  # time at next scr refresh
                bufferscreenkey.status = FINISHED
        if bufferscreenkey.status == STARTED and not waitOnFlip:
            theseKeys = bufferscreenkey.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _bufferscreenkey_allKeys.extend(theseKeys)
            if len(_bufferscreenkey_allKeys):
                bufferscreenkey.keys = _bufferscreenkey_allKeys[-1].name  # just the last key pressed
                bufferscreenkey.rt = _bufferscreenkey_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RATINGbufferscreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Bufferscreen"-------
    for thisComponent in RATINGbufferscreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if bufferscreenkey.keys in ['', [], None]:  # No response was made
        bufferscreenkey.keys = None    
    
    # ------Prepare to start Routine "Slider_Effort"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_effort.reset()
    # show mouse cursor
    win.mouseVisible = True
    # keep track of which components have finished
    Slider_EffortComponents = [text_slider_effort, slider_effort]
    for thisComponent in Slider_EffortComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Slider_EffortClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Slider_Effort"-------
    while continueRoutine:
        # get current time
        t = Slider_EffortClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Slider_EffortClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_slider_effort* updates
        if text_slider_effort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_slider_effort.frameNStart = frameN  # exact frame index
            text_slider_effort.tStart = t  # local t and not account for scr refresh
            text_slider_effort.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_slider_effort, 'tStartRefresh')  # time at next scr refresh
            text_slider_effort.setAutoDraw(True)
        
        # *slider_effort* updates
        if slider_effort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_effort.frameNStart = frameN  # exact frame index
            slider_effort.tStart = t  # local t and not account for scr refresh
            slider_effort.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_effort, 'tStartRefresh')  # time at next scr refresh
            slider_effort.setAutoDraw(True)
        
        # Check slider_effort for response to end routine
        if slider_effort.getRating() is not None and slider_effort.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Slider_EffortComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Slider_Effort"-------
    for thisComponent in Slider_EffortComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks_reg.addData('slider_effort.response', slider_effort.getRating())
    blocks_reg.addData('slider_effort.rt', slider_effort.getRT())
    # the Routine "Slider_Effort" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    thisExp1.nextEntry()
# completed 1.0 repeats of 'blocks_reg'

# ------Prepare to start Routine "Instruction 1vs 1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# make mouse cursor visible
win.mouseVisible = True
# keep track of which components have finished
Instruction1vs1Components = [VS1text, key_resp]
for thisComponent in Instruction1vs1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction1vs1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction 1vs 1"-------
while continueRoutine:
    # get current time
    t = Instruction1vs1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction1vs1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if VS1text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VS1text.frameNStart = frameN  # exact frame index
        VS1text.tStart = t  # local t and not account for scr refresh
        VS1text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VS1text, 'tStartRefresh')  # time at next scr refresh
        VS1text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction1vs1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction 1 vs 1"-------
for thisComponent in Instruction1vs1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp2.nextEntry()
# the Routine "Instruction1 vs 1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Some variables to grow within the loop
leftbutton_1vs1_strat = [] # a variable to store the strategies of the left button
rightbutton_1vs1_strat = [] # a variable to store the strategies of the right button
leftbutton_1vs1_clicked = [] # whether it was clicked or not
rightbutton_1vs1_clicked = [] # whether it was clicked or not

# -----------------------------
# Loop for the 9 comparisons
# -----------------------------

# set up handler to look after randomisation of conditions etc
VS1round = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('VS1_Rounds.xlsx'),
    seed=None, name='EDround')
thisExp2.addLoop(VS1round)  # add the loop to the experiment
thisVS1round = VS1round.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisVS1round != None:
    for paramName in thisVS1round:
        exec('{} = thisVS1round[paramName]'.format(paramName))

for thisVS1round in VS1round:
    currentLoop = VS1round
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisVS1round != None:
        for paramName in thisVS1round:
            exec('{} = thisVS1round[paramName]'.format(paramName))

    # ------Prepare to start Routine "bufferscreen"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    bufferscreenkey.keys = []
    bufferscreenkey.rt = []
    _bufferscreenkey_allKeys = []
    # make mouse cursor visible
    win.mouseVisible = True
    # keep track of which components have finished
    VS1bufferscreenComponents = [EDbufferscreen, bufferscreenkey]
    for thisComponent in VS1bufferscreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EDbufferscreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "bufferscreen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EDbufferscreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EDbufferscreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *bufferscreen* updates
        if EDbufferscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EDbufferscreen.frameNStart = frameN  # exact frame index
            EDbufferscreen.tStart = t  # local t and not account for scr refresh
            EDbufferscreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EDbufferscreen, 'tStartRefresh')  # time at next scr refresh
            EDbufferscreen.setAutoDraw(True)
        if EDbufferscreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EDbufferscreen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                EDbufferscreen.tStop = t  # not accounting for scr refresh
                EDbufferscreen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(EDbufferscreen, 'tStopRefresh')  # time at next scr refresh
                EDbufferscreen.setAutoDraw(False)

        # *bufferscreenkey* updates
        waitOnFlip = False
        if bufferscreenkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bufferscreenkey.frameNStart = frameN  # exact frame index
            bufferscreenkey.tStart = t  # local t and not account for scr refresh
            bufferscreenkey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bufferscreenkey, 'tStartRefresh')  # time at next scr refresh
            bufferscreenkey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(bufferscreenkey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(bufferscreenkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if bufferscreenkey.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bufferscreenkey.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                bufferscreenkey.tStop = t  # not accounting for scr refresh
                bufferscreenkey.frameNStop = frameN  # exact frame index
                win.timeOnFlip(bufferscreenkey, 'tStopRefresh')  # time at next scr refresh
                bufferscreenkey.status = FINISHED
        if bufferscreenkey.status == STARTED and not waitOnFlip:
            theseKeys = bufferscreenkey.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _bufferscreenkey_allKeys.extend(theseKeys)
            if len(_bufferscreenkey_allKeys):
                bufferscreenkey.keys = _bufferscreenkey_allKeys[-1].name  # just the last key pressed
                bufferscreenkey.rt = _bufferscreenkey_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VS1bufferscreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Bufferscreen"-------
    for thisComponent in VS1bufferscreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # hide mouse cursor
    win.mouseVisible = False
    # check responses
    if bufferscreenkey.keys in ['', [], None]:  # No response was made
        bufferscreenkey.keys = None
        
    # ------Prepare to start Routine -------
    continueRoutine = True
    # update component parameters for each repeat
    # update component parameters for each repeat
    LB = '1 € für Strategie ' + str(VS1stratcompList[VS1comps[vsx]])
    RB = '1 € für Strategie ' + str(VS1stratcompList[VS1comps[vsx]+1])
    
    VS1leftbutton.setText(LB)
    VS1rightbutton.setText(RB)
    # setup some python lists for storing info about the response click
    VS1click.clicked_name = []
    gotValidClick = False  # until a click is received
    # make mouse cursor visible
    win.mouseVisible = True
    # keep track of which components have finished
    VS1roundComponents = [question, VS1click, VS1leftbutton, VS1rightbutton]
    for thisComponent in VS1roundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    VS1roundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
        
    # -------Run Routine -------
    while continueRoutine:
        # get current time
        t = VS1roundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=VS1roundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
            
        # *question* updates
        if question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question.frameNStart = frameN  # exact frame index
            question.tStart = t  # local t and not account for scr refresh
            question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
            question.setAutoDraw(True)
        # *response click* updates
        if VS1click.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            VS1click.frameNStart = frameN  # exact frame index
            VS1click.tStart = t  # local t and not account for scr refresh
            VS1click.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(VS1click, 'tStartRefresh')  # time at next scr refresh
            VS1click.status = STARTED
            VS1click.mouseClock.reset()
            VS1click.clickReset()
            prevButtonState = VS1click.getPressed()  # if button is down already this ISN'T a new click
        if VS1click.status == STARTED:  # only update if started and not finished!
            buttons = VS1click.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [VS1leftbutton,VS1rightbutton]:
                        if obj.contains(VS1click):
                            gotValidClick = True
                            VS1click.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
            
        # *LeftButton* updates
        if VS1leftbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            VS1leftbutton.frameNStart = frameN  # exact frame index
            VS1leftbutton.tStart = t  # local t and not account for scr refresh
            VS1leftbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(VS1leftbutton, 'tStartRefresh')  # time at next scr refresh
            VS1leftbutton.setAutoDraw(True)            
        if VS1leftbutton.status == STARTED:
            # check whether LeftButton has been pressed
            if VS1leftbutton.isClicked:
                if not VS1leftbutton.wasClicked:
                    VS1leftbutton.timesOn.append(VS1leftbutton.buttonClock.getTime()) # store time of first click
                    VS1leftbutton.timesOff.append(VS1leftbutton.buttonClock.getTime()) # store time clicked until
                else:
                    VS1leftbutton.timesOff[-1] = VS1leftbutton.buttonClock.getTime() # update time clicked until
                if not VS1leftbutton.wasClicked:
                    continueRoutine = False  # end routine when LeftButton is clicked
                    None
                VS1leftbutton.wasClicked = True  # if LeftButton is still clicked next frame, it is not a new click
            else:
                VS1leftbutton.wasClicked = False  # if LeftButton is clicked next frame, it is a new click
        else:
            VS1leftbutton.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
            VS1leftbutton.wasClicked = False  # if LeftButton is clicked next frame, it is a new click
        
        # *RightButton* updates
        if VS1rightbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            VS1rightbutton.frameNStart = frameN  # exact frame index
            VS1rightbutton.tStart = t  # local t and not account for scr refresh
            VS1rightbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(VS1rightbutton, 'tStartRefresh')  # time at next scr refresh
            VS1rightbutton.setAutoDraw(True)
        if VS1rightbutton.status == STARTED:
            # check whether RightButton has been pressed
            if VS1rightbutton.isClicked:
                if not VS1rightbutton.wasClicked:
                    VS1rightbutton.timesOn.append(VS1rightbutton.buttonClock.getTime()) # store time of first click
                    VS1rightbutton.timesOff.append(VS1rightbutton.buttonClock.getTime()) # store time clicked until
                else:
                    VS1rightbutton.timesOff[-1] = VS1rightbutton.buttonClock.getTime() # update time clicked until
                if not VS1rightbutton.wasClicked:
                    continueRoutine = False  # end routine when RightButton is clicked
                    None
                VS1rightbutton.wasClicked = True  # if RightButton is still clicked next frame, it is not a new click
            else:
                VS1rightbutton.wasClicked = False  # if RightButton is clicked next frame, it is a new click
        else:
            VS1rightbutton.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
            VS1rightbutton.wasClicked = False  # if RightButton is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VS1roundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        
    # -------Ending Routine-------
    for thisComponent in VS1roundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    VS1round.addData('question.started', question.tStartRefresh)
    # store data for rounds (TrialHandler)
    x, y = VS1click.getPos()
    buttons = VS1click.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [VS1leftbutton,VS1rightbutton]:
            if obj.contains(VS1click):
                gotValidClick = True
                VS1click.clicked_name.append(obj.name)
    if len(VS1click.clicked_name):
        VS1round.addData('VS1click.clicked_name', VS1click.clicked_name[0])
    # which button was clicked (1 = yes, 0 = no)
    if VS1click.clicked_name[0] == 'VS1leftbutton':
        VS1round.addData('VS1leftbutton.wasclicked', 1)
        leftbutton_1vs1_clicked.append(True)
        VS1round.addData('VS1rightbutton.wasclicked', 0)
        rightbutton_1vs1_clicked.append(False)
    else:
        VS1round.addData('VS1leftbutton.wasclicked', 0)
        leftbutton_1vs1_clicked.append(False)
        VS1round.addData('VS1rightbutton.wasclicked', 1)
        rightbutton_1vs1_clicked.append(True)
    # what strategy each button was
    VS1round.addData('VS1leftbutton.strat', VS1stratList[VS1comps[vsx]])
    VS1round.addData('VS1rightbutton.strat', VS1stratList[VS1comps[vsx]+1])
    leftbutton_1vs1_strat.append(VS1stratList[VS1comps[vsx]])
    rightbutton_1vs1_strat.append(VS1stratList[VS1comps[vsx]+1])
    # store the necessary variables to be able to use it in the iteration process and for the random pick of the last n-back
    VS1storebutton.append(VS1click.clicked_name[0])
        
    # open up the next row for more data
    thisExp2.nextEntry()
    
    # the Routine was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

# ------- Calculate which strategies are fixed and which are flexible in each pair ------------

# create empty variables to store the information of fixed and flexible
choices12 = []
choices13 = []
choices23 = []


for i in VS1rounds:
    # create variables containing the strategies on and choices of both buttons
    currentbuttons = [leftbutton_1vs1_strat[i], rightbutton_1vs1_strat[i]]
    currentchoices = [leftbutton_1vs1_clicked[i], rightbutton_1vs1_clicked[i]]
    # now check for levels to put them in the respective 'choices' variable
    if all(x in currentbuttons for x in [1,2]):
        # this command retains only the level that was chosen
        currentclick = list(compress(currentbuttons, currentchoices))
        # append chosen level to the variable
        choices12.append(currentclick[0])
    elif all(x in currentbuttons for x in [1,3]):
        currentclick = list(compress(currentbuttons, currentchoices))
        choices13.append(currentclick[0])
    elif all(x in currentbuttons for x in [2,3]):
        currentclick = list(compress(currentbuttons, currentchoices))
        choices23.append(currentclick[0])

# now reduce all 'choices' variables to the level that was chosen at least 2 out of 3 times
flexible12 = most_frequent(choices12)
flexible13 = most_frequent(choices13)
flexible23 = most_frequent(choices23)

# put the information of fixed and flexible in the same format as the other ED variables
EDfixflexList = []
if flexible12 == 1:
    EDfixflexList.append('flexible')
    EDfixflexList.append('fixed')
else:
    EDfixflexList.append('fixed')
    EDfixflexList.append('flexible')
if flexible23 == 2:
    EDfixflexList.append('flexible')
    EDfixflexList.append('fixed')
else:
    EDfixflexList.append('fixed')
    EDfixflexList.append('flexible')
if flexible13 == 1:
    EDfixflexList.append('flexible')
    EDfixflexList.append('fixed')
else:
    EDfixflexList.append('fixed')
    EDfixflexList.append('flexible')

# ------Prepare to start Routine "InstructionED"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# show mouse cursor
win.mouseVisible = True
# keep track of which components have finished
InstructionEDComponents = [text_EDinstruction, key_resp]
for thisComponent in InstructionEDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionEDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionED"-------
while continueRoutine:
    # get current time
    t = InstructionEDClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionEDClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_EDinstruction* updates
    if text_EDinstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_EDinstruction.frameNStart = frameN  # exact frame index
        text_EDinstruction.tStart = t  # local t and not account for scr refresh
        text_EDinstruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_EDinstruction, 'tStartRefresh')  # time at next scr refresh
        text_EDinstruction.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionEDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionED"-------
for thisComponent in InstructionEDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp2.nextEntry()
# the Routine "InstructionED" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Some variables to grow within the loop
finals_leftbutton_strat = [] # a variable to store the strategy of the left button
finals_rightbutton_strat = [] # a variable to store the strategy of the right button
finals_leftbutton_value = [] # the last value displayed on the left button
finals_rightbutton_value = [] # the last value displayed on the right button

# -----------------------------
# Loop for the 3 comparisons
# -----------------------------

for edx in EDrounds:

    # set up handler to look after randomisation of conditions etc
    EDround = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Moneyvalues.xlsx'),
        seed=None, name='EDround')
    thisExp3.addLoop(EDround)  # add the loop to the experiment
    thisEDround = EDround.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisEDround != None:
        for paramName in thisEDround:
            exec('{} = thisEDround[paramName]'.format(paramName))

    EDstorebutton = [] # a variable to store responses in (for adapting the button values correctly)

    for thisEDround in EDround:
        currentLoop = EDround
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisEDround != None:
            for paramName in thisEDround:
                exec('{} = thisEDround[paramName]'.format(paramName))

        # ------Prepare to start Routine "bufferscreen"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        bufferscreenkey.keys = []
        bufferscreenkey.rt = []
        _bufferscreenkey_allKeys = []
        # keep track of which components have finished
        EDbufferscreenComponents = [EDbufferscreen, bufferscreenkey]
        for thisComponent in EDbufferscreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EDbufferscreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
    
        # -------Run Routine "bufferscreen"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = EDbufferscreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EDbufferscreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
    
            # *bufferscreen* updates
            if EDbufferscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EDbufferscreen.frameNStart = frameN  # exact frame index
                EDbufferscreen.tStart = t  # local t and not account for scr refresh
                EDbufferscreen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EDbufferscreen, 'tStartRefresh')  # time at next scr refresh
                EDbufferscreen.setAutoDraw(True)
            if EDbufferscreen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EDbufferscreen.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    EDbufferscreen.tStop = t  # not accounting for scr refresh
                    EDbufferscreen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(EDbufferscreen, 'tStopRefresh')  # time at next scr refresh
                    EDbufferscreen.setAutoDraw(False)
    
            # *bufferscreenkey* updates
            waitOnFlip = False
            if bufferscreenkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bufferscreenkey.frameNStart = frameN  # exact frame index
                bufferscreenkey.tStart = t  # local t and not account for scr refresh
                bufferscreenkey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bufferscreenkey, 'tStartRefresh')  # time at next scr refresh
                bufferscreenkey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(bufferscreenkey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(bufferscreenkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if bufferscreenkey.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > bufferscreenkey.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    bufferscreenkey.tStop = t  # not accounting for scr refresh
                    bufferscreenkey.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(bufferscreenkey, 'tStopRefresh')  # time at next scr refresh
                    bufferscreenkey.status = FINISHED
            if bufferscreenkey.status == STARTED and not waitOnFlip:
                theseKeys = bufferscreenkey.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
                _bufferscreenkey_allKeys.extend(theseKeys)
                if len(_bufferscreenkey_allKeys):
                    bufferscreenkey.keys = _bufferscreenkey_allKeys[-1].name  # just the last key pressed
                    bufferscreenkey.rt = _bufferscreenkey_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
    
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EDbufferscreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
    
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "Bufferscreen"-------
        for thisComponent in EDbufferscreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if bufferscreenkey.keys in ['', [], None]:  # No response was made
            bufferscreenkey.keys = None
        
        # ------Prepare to start Routine -------
        continueRoutine = True
        # update component parameters for each repeat
        if EDfixflexList[EDcomps[edx]] == 'flexible':
            #right button is set to display 2 EUR
            RB = str(format(EDfix[0],'.2f')) + '€ für Strategie ' +str(EDstratcompList[EDcomps[edx]+1])
            # display flexible value on left button
            if Currentstep == 0:
                # for the first 1-vs-2 comparison, no reference to last buttonclick is necessary
                LB = str(format(EDsteps[0], '.2f')) + '€ für Strategie ' +str(EDstratcompList[EDcomps[edx]])
                # set 'old' value of the flexible button to 1€ 
                oldvalue = EDsteps[0]
            else:
                # value on left button is changed according to previous choice
                if EDstorebutton[Currentstep-1] == 'EDleftbutton':
                    newvalue = oldvalue - EDsteps[Currentstep]
                # if the pricier option was chosen, raise the other options' value by the current EDsteps value
                else:
                    newvalue = oldvalue + EDsteps[Currentstep]
                LB = str(format(newvalue,'.2f')) + '€ für Strategie ' + str(EDstratcompList[EDcomps[edx]])
                oldvalue = newvalue
        
        else:
            # set left button to display 2€
            LB = str(format(EDfix[0],'.2f')) + '€ für Strategie ' + str(EDstratcompList[EDcomps[edx]])
            # display flexible value on right button
            if Currentstep == 0:
                # for the first 1-vs-2 comparison, no reference to last buttonclick is necessary
                RB = str(format(EDsteps[0], '.2f')) + '€ für Strategie ' +str(EDstratcompList[EDcomps[edx]+1])
                # set 'old' value of the flexible button to 1€ 
                oldvalue = EDsteps[0]
            else:
                # value on right button is changed according to previous choice
                if EDstorebutton[Currentstep-1] == 'EDrightbutton':
                    newvalue = oldvalue - EDsteps[Currentstep]
                # if the pricier option was chosen, raise the other options' value by the current EDsteps value
                else:
                    newvalue = oldvalue + EDsteps[Currentstep]
                RB = str(format(newvalue,'.2f')) + '€ für Strategie ' + str(EDstratcompList[EDcomps[edx]+1])
                oldvalue = newvalue
        
        EDleftbutton.setText(LB)
        EDrightbutton.setText(RB)
        # setup some python lists for storing info about the response click
        EDclick.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        EDroundComponents = [question, EDclick, EDleftbutton, EDrightbutton]
        for thisComponent in EDroundComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        EDroundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine -------
        while continueRoutine:
            # get current time
            t = EDroundClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=EDroundClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question* updates
            if question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question.frameNStart = frameN  # exact frame index
                question.tStart = t  # local t and not account for scr refresh
                question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
                question.setAutoDraw(True)
            # *response click* updates
            if EDclick.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EDclick.frameNStart = frameN  # exact frame index
                EDclick.tStart = t  # local t and not account for scr refresh
                EDclick.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EDclick, 'tStartRefresh')  # time at next scr refresh
                EDclick.status = STARTED
                EDclick.mouseClock.reset()
                EDclick.clickReset()
                prevButtonState = EDclick.getPressed()  # if button is down already this ISN'T a new click
            if EDclick.status == STARTED:  # only update if started and not finished!
                buttons = EDclick.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [EDleftbutton,EDrightbutton]:
                            if obj.contains(EDclick):
                                gotValidClick = True
                                EDclick.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *LeftButton* updates
            if EDleftbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EDleftbutton.frameNStart = frameN  # exact frame index
                EDleftbutton.tStart = t  # local t and not account for scr refresh
                EDleftbutton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EDleftbutton, 'tStartRefresh')  # time at next scr refresh
                EDleftbutton.setAutoDraw(True)
            if EDleftbutton.status == STARTED:
                # check whether LeftButton has been pressed
                if EDleftbutton.isClicked:
                    if not EDleftbutton.wasClicked:
                        EDleftbutton.timesOn.append(EDleftbutton.buttonClock.getTime()) # store time of first click
                        EDleftbutton.timesOff.append(EDleftbutton.buttonClock.getTime()) # store time clicked until
                    else:
                        EDleftbutton.timesOff[-1] = EDleftbutton.buttonClock.getTime() # update time clicked until
                    if not EDleftbutton.wasClicked:
                        continueRoutine = False  # end routine when LeftButton is clicked
                        None
                    EDleftbutton.wasClicked = True  # if LeftButton is still clicked next frame, it is not a new click
                else:
                    EDleftbutton.wasClicked = False  # if LeftButton is clicked next frame, it is a new click
            else:
                EDleftbutton.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
                EDleftbutton.wasClicked = False  # if LeftButton is clicked next frame, it is a new click
            
            # *RightButton* updates
            if EDrightbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EDrightbutton.frameNStart = frameN  # exact frame index
                EDrightbutton.tStart = t  # local t and not account for scr refresh
                EDrightbutton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EDrightbutton, 'tStartRefresh')  # time at next scr refresh
                EDrightbutton.setAutoDraw(True)
            if EDrightbutton.status == STARTED:
                # check whether RightButton has been pressed
                if EDrightbutton.isClicked:
                    if not EDrightbutton.wasClicked:
                        EDrightbutton.timesOn.append(EDrightbutton.buttonClock.getTime()) # store time of first click
                        EDrightbutton.timesOff.append(EDrightbutton.buttonClock.getTime()) # store time clicked until
                    else:
                        EDrightbutton.timesOff[-1] = EDrightbutton.buttonClock.getTime() # update time clicked until
                    if not EDrightbutton.wasClicked:
                        continueRoutine = False  # end routine when RightButton is clicked
                        None
                    EDrightbutton.wasClicked = True  # if RightButton is still clicked next frame, it is not a new click
                else:
                    EDrightbutton.wasClicked = False  # if RightButton is clicked next frame, it is a new click
            else:
                EDrightbutton.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
                EDrightbutton.wasClicked = False  # if RightButton is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EDroundComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine-------
        for thisComponent in EDroundComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        EDround.addData('question.started', question.tStartRefresh)
        # store data for rounds (TrialHandler)
        x, y = EDclick.getPos()
        buttons = EDclick.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [EDleftbutton,EDrightbutton]:
                if obj.contains(EDclick):
                    gotValidClick = True
                    EDclick.clicked_name.append(obj.name)
        if len(EDclick.clicked_name):
            EDround.addData('EDclick.clicked_name', EDclick.clicked_name[0])
        # which button was clicked (1 = yes, 0 = no)
        if EDclick.clicked_name[0] == 'EDleftbutton':
            EDround.addData('EDleftbutton.wasclicked', 1)
            EDround.addData('EDrightbutton.wasclicked', 0)
        else:
            EDround.addData('EDleftbutton.wasclicked', 0)
            EDround.addData('EDrightbutton.wasclicked', 1)
        # what value was depicted on each button
        EDround.addData('EDleftbutton.value', LB[0:4])
        EDround.addData('EDrightbutton.value', RB[0:4])
        # what strategy each button had
        EDround.addData('EDleftbutton.strat', EDstratList[EDcomps[edx]])
        EDround.addData('EDrightbutton.strat', EDstratList[EDcomps[edx]+1])
                # store the necessary variables to be able to use it in the iteration process and for the random pick of the last n-back
        EDstorebutton.append(EDclick.clicked_name[0])
        if Currentstep == 0:
            finals_leftbutton_strat.append(EDstratList[EDcomps[edx]])
            finals_rightbutton_strat.append(EDstratList[EDcomps[edx]+1])
        elif Currentstep == 6:
            finals_leftbutton_value.append(LB[0:4])
            finals_rightbutton_value.append(RB[0:4])
        
        # open up the next row for more data
        thisExp3.nextEntry()
        
        # the Routine was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    
   
# Effort Discounting is complete

# ------Prepare to start Routine "Choice_reapply"-------
continueRoutine = True
# update component parameters for each repeat
resp_choice.keys = []
resp_choice.rt = []
_resp_choice_allKeys = []
# hide mouse cursor
win.mouseVisible = False
# keep track of which components have finished
Choice_reapplyComponents = [text_choice, resp_choice]
for thisComponent in Choice_reapplyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Choice_reapplyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Choice_reapply"-------
while continueRoutine:
    # get current time
    t = Choice_reapplyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Choice_reapplyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_choice* updates
    if text_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_choice.frameNStart = frameN  # exact frame index
        text_choice.tStart = t  # local t and not account for scr refresh
        text_choice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_choice, 'tStartRefresh')  # time at next scr refresh
        text_choice.setAutoDraw(True)
    
    # *resp_choice* updates
    waitOnFlip = False
    if resp_choice.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        resp_choice.frameNStart = frameN  # exact frame index
        resp_choice.tStart = t  # local t and not account for scr refresh
        resp_choice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_choice, 'tStartRefresh')  # time at next scr refresh
        resp_choice.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_choice.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_choice.status == STARTED and not waitOnFlip:
        theseKeys = resp_choice.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        _resp_choice_allKeys.extend(theseKeys)
        if len(_resp_choice_allKeys):
            resp_choice.keys = _resp_choice_allKeys[-1].name  # just the last key pressed
            resp_choice.rt = _resp_choice_allKeys[-1].rt
            
            # send trigger according to button press
            if resp_choice.keys == '1':
                sendTrigger(trigger_1)
            elif resp_choice.keys == '2':
                sendTrigger(trigger_2)
            elif resp_choice.keys == '3':
                sendTrigger(trigger_3)

            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Choice_reapplyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Choice_reapply"-------
for thisComponent in Choice_reapplyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if resp_choice.keys in ['', [], None]:  # No response was made
    resp_choice.keys = None
thisExp1.addData('resp_choice.keys',resp_choice.keys)
if resp_choice.keys != None:  # we had a response
    thisExp1.addData('resp_choice.rt', resp_choice.rt)

thisExp1.nextEntry()
# the Routine "Choice_reapply" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instruction_Choice"-------
continueRoutine = True
# update component parameters for each repeat
if resp_choice.keys == '1':
    instr_choice_1 = 'ABLENKEN'
    instr_choice_2 = 'Denken Sie während des Betrachtens der Bilder an etwas Neutrales, das mit dem Bild nichts zu tun hat. Das könnten geometrische Figuren, Alltagstätigkeiten oder bekannte Orte sein.'
elif resp_choice.keys == '2':
    instr_choice_1 = 'DISTANZIEREN'
    instr_choice_2 = 'Nehmen Sie die Position eines uninvolvierten Beobachters ein. Denken Sie über das Bild in einer neutralen Weise nach.'
elif resp_choice.keys == '3':
    instr_choice_1 = 'UNTERDRÜCKEN'
    instr_choice_2 = 'Unterdrücken Sie alle aufkommenden emotionalen Ausdrücke. Wenn Sie also die Bilder ansehen, verhalten Sie sich so, dass eine außenstehende Person nicht sehen kann, welche Emotionen Sie gerade empfinden.'
text_instr_choice.setText(instr_choice_1 + '\n\n' + 'In diesem Block werden Sie eine Reihe von Bildern sehen. Diese sollen Sie aufmerksam ansehen.' + '\n' + instr_choice_2 + '\n\n' + 'Bitte konzentrieren Sie Ihre Regulationsbemühungen nur auf das Bild, nicht aber auf die Zeiträume zwischen den Bildern.' + '\n\n' + 'Zum Starten des Blocks Leertaste drücken')
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# hide mouse cursor
win.mouseVisible = False
# keep track of which components have finished
Instruction_ChoiceComponents = [text_instr_choice, key_resp]
for thisComponent in Instruction_ChoiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction_ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction_Choice"-------
while continueRoutine:
    # get current time
    t = Instruction_ChoiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction_ChoiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr_choice* updates
    if text_instr_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instr_choice.frameNStart = frameN  # exact frame index
        text_instr_choice.tStart = t  # local t and not account for scr refresh
        text_instr_choice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instr_choice, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sendTrigger,trigger_instr) # send trigger for 
        text_instr_choice.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            sendTrigger(trigger_space) # send trigger for button press
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_ChoiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction_Choice"-------
for thisComponent in Instruction_ChoiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp1.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp1.addData('key_resp.rt', key_resp.rt)

thisExp1.nextEntry()
# the Routine "Instruction_Choice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_choice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(Stimuli_Choice),
    seed=None, name='trials_choice')
thisExp1.addLoop(trials_choice)  # add the loop to the experiment
thisTrials_choice = trials_choice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_choice.rgb)
if thisTrials_choice != None:
    for paramName in thisTrials_choice:
        exec('{} = thisTrials_choice[paramName]'.format(paramName))

for thisTrials_choice in trials_choice:
    currentLoop = trials_choice
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_choice.rgb)
    if thisTrials_choice != None:
        for paramName in thisTrials_choice:
            exec('{} = thisTrials_choice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixcross"-------
    continueRoutine = True
    # update component parameters for each repeat
    # random jitter between 3 and 5 seconds
    jitter = random.uniform(3,5)
    jitter = round(jitter, 1)
    # add jitter to log file
    thisExp1.addData('Fix_jitter', jitter)

    # hide mouse cursor
    win.mouseVisible = False

    # keep track of which components have finished
    fixcrossComponents = [text_fixcross]
    for thisComponent in fixcrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixcrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixcross"-------
    while continueRoutine:
        # get current time
        t = fixcrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixcrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_fixcross* updates
        if text_fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_fixcross.frameNStart = frameN  # exact frame index
            text_fixcross.tStart = t  # local t and not account for scr refresh
            text_fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_fixcross, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(sendTrigger, trigger_Fix)
            text_fixcross.setAutoDraw(True)
        if text_fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_fixcross.tStartRefresh + jitter-frameTolerance:
                # keep track of stop time/frame for later
                text_fixcross.tStop = t  # not accounting for scr refresh
                text_fixcross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_fixcross, 'tStopRefresh')  # time at next scr refresh
                text_fixcross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixcrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixcross"-------
    for thisComponent in fixcrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Pics_Choice"-------
    continueRoutine = True
    #routineTimer.add(6.000000)
    # update component parameters for each repeat
    image.setImage(ImageFile)

    # hide mouse cursor
    win.mouseVisible = False
    
    # keep track of which components have finished
    Pics_ChoiceComponents = [image]
    for thisComponent in Pics_ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pics_ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pics_Choice"-------
    while continueRoutine: #and routineTimer.getTime() > 0:
        # get current time
        t = Pics_ChoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pics_ChoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(sendTrigger, trigger_choice)
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pics_ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pics_Choice"-------
    for thisComponent in Pics_ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_choice.addData('image.started', image.tStartRefresh)
    trials_choice.addData('image.lased', image.tStop)
    trials_choice.addData('image.stopped', image.tStopRefresh)
    
    thisExp1.nextEntry()
# completed 1.0 repeats of 'trials_choice'


# ------Prepare to start Routine "Slider_Arousal"-------
continueRoutine = True
# update component parameters for each repeat
slider_arousal.reset()
# show mouse cursor
win.mouseVisible = True
# keep track of which components have finished
Slider_ArousalComponents = [text_slider_arousal, slider_arousal]
for thisComponent in Slider_ArousalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Slider_ArousalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Slider_Arousal"-------
while continueRoutine:
    # get current time
    t = Slider_ArousalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Slider_ArousalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_slider_arousal* updates
    if text_slider_arousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_slider_arousal.frameNStart = frameN  # exact frame index
        text_slider_arousal.tStart = t  # local t and not account for scr refresh
        text_slider_arousal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_slider_arousal, 'tStartRefresh')  # time at next scr refresh
        text_slider_arousal.setAutoDraw(True)
    
    # *slider_arousal* updates
    if slider_arousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_arousal.frameNStart = frameN  # exact frame index
        slider_arousal.tStart = t  # local t and not account for scr refresh
        slider_arousal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_arousal, 'tStartRefresh')  # time at next scr refresh
        slider_arousal.setAutoDraw(True)
    
    # Check slider_arousal for response to end routine
    if slider_arousal.getRating() is not None and slider_arousal.status == STARTED:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Slider_ArousalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Slider_Arousal"-------
for thisComponent in Slider_ArousalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp1.addData('slider_arousal.response', slider_arousal.getRating())
thisExp1.addData('slider_arousal.rt', slider_arousal.getRT())

# the Routine "Slider_Arousal" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
    
# ------Prepare to start Routine "bufferscreen"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
bufferscreenkey.keys = []
bufferscreenkey.rt = []
_bufferscreenkey_allKeys = []
# keep track of which components have finished
RATINGbufferscreenComponents = [RATINGbufferscreen, bufferscreenkey]
for thisComponent in RATINGbufferscreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RATINGbufferscreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bufferscreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = RATINGbufferscreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RATINGbufferscreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *bufferscreen* updates
    if RATINGbufferscreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RATINGbufferscreen.frameNStart = frameN  # exact frame index
        RATINGbufferscreen.tStart = t  # local t and not account for scr refresh
        RATINGbufferscreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RATINGbufferscreen, 'tStartRefresh')  # time at next scr refresh
        RATINGbufferscreen.setAutoDraw(True)
    if RATINGbufferscreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > RATINGbufferscreen.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            RATINGbufferscreen.tStop = t  # not accounting for scr refresh
            RATINGbufferscreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(RATINGbufferscreen, 'tStopRefresh')  # time at next scr refresh
            RATINGbufferscreen.setAutoDraw(False)

    # *bufferscreenkey* updates
    waitOnFlip = False
    if bufferscreenkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bufferscreenkey.frameNStart = frameN  # exact frame index
        bufferscreenkey.tStart = t  # local t and not account for scr refresh
        bufferscreenkey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bufferscreenkey, 'tStartRefresh')  # time at next scr refresh
        bufferscreenkey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(bufferscreenkey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(bufferscreenkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if bufferscreenkey.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bufferscreenkey.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            bufferscreenkey.tStop = t  # not accounting for scr refresh
            bufferscreenkey.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bufferscreenkey, 'tStopRefresh')  # time at next scr refresh
            bufferscreenkey.status = FINISHED
    if bufferscreenkey.status == STARTED and not waitOnFlip:
        theseKeys = bufferscreenkey.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
        _bufferscreenkey_allKeys.extend(theseKeys)
        if len(_bufferscreenkey_allKeys):
            bufferscreenkey.keys = _bufferscreenkey_allKeys[-1].name  # just the last key pressed
            bufferscreenkey.rt = _bufferscreenkey_allKeys[-1].rt
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RATINGbufferscreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Bufferscreen"-------
for thisComponent in RATINGbufferscreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if bufferscreenkey.keys in ['', [], None]:  # No response was made
    bufferscreenkey.keys = None

# ------Prepare to start Routine "Slider_Effort"-------
continueRoutine = True
# update component parameters for each repeat
slider_effort.reset()
# show mouse cursor
win.mouseVisible = True
# keep track of which components have finished
Slider_EffortComponents = [text_slider_effort, slider_effort]
for thisComponent in Slider_EffortComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Slider_EffortClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Slider_Effort"-------
while continueRoutine:
    # get current time
    t = Slider_EffortClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Slider_EffortClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_slider_effort* updates
    if text_slider_effort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_slider_effort.frameNStart = frameN  # exact frame index
        text_slider_effort.tStart = t  # local t and not account for scr refresh
        text_slider_effort.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_slider_effort, 'tStartRefresh')  # time at next scr refresh
        text_slider_effort.setAutoDraw(True)
    
    # *slider_effort* updates
    if slider_effort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_effort.frameNStart = frameN  # exact frame index
        slider_effort.tStart = t  # local t and not account for scr refresh
        slider_effort.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_effort, 'tStartRefresh')  # time at next scr refresh
        slider_effort.setAutoDraw(True)
    
    # Check slider_effort for response to end routine
    if slider_effort.getRating() is not None and slider_effort.status == STARTED:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Slider_EffortComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Slider_Effort"-------
for thisComponent in Slider_EffortComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp1.addData('slider_effort.response', slider_effort.getRating())
thisExp1.addData('slider_effort.rt', slider_effort.getRT())

# the Routine "Slider_Effort" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# hide mouse cursor
win.mouseVisible = False

# keep track of which components have finished
EndScreenComponents = [text_end, key_resp_2]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Trigger End Experiment
sendTrigger(trigger_ExpEnd)

# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp1.nextEntry()
# the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp1.saveAsWideText(filename1+'.csv', delim='auto')
thisExp1.saveAsPickle(filename1)
thisExp2.saveAsWideText(filename2+'.csv', delim='auto')
thisExp2.saveAsPickle(filename2)
logging.flush()
# make sure everything is closed down
thisExp1.abort()  # or data files will save again on exit
thisExp2.abort()
win.close()
core.quit()
