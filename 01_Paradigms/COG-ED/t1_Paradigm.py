#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    in June 2021
If you publish work using this script the most relevant publication is:
    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y
"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

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
expName1 = 't1_nback'
expName2 = 't1_1vs1'
expName3 = 't1_ED'
expName4 = 't1_randomchoice'
expInfo = {'Participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title='t1_Paradigm')
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = 't1_Paradigm'
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
# For n-back
filename1 = _thisDir + os.sep + u'data/%s_%s' % (expInfo['Participant'], expName1)
# For the 1 vs 1 questions
filename2 = _thisDir + os.sep + u'data/%s_%s' % (expInfo['Participant'], expName2)
# For Effort Discounting
filename3 = _thisDir + os.sep + u'data/%s_%s' % (expInfo['Participant'], expName3)
# For the final n-back level at the end that is randomly chosen
filename4 = _thisDir + os.sep + u'data/%s_%s' % (expInfo['Participant'], expName4)

# An ExperimentHandler isn't essential but helps with data saving
# For n-back
thisExp1 = data.ExperimentHandler(name=expName1, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='t1_Paradigm.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename1)
# For the 1 vs 1 questions
thisExp2 = data.ExperimentHandler(name=expName2, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='t1_Paradigm.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename2)
# For Effort Discounting
thisExp3 = data.ExperimentHandler(name=expName3, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='t1_Paradigm.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename3)
# For the final n-back level at the end that is randomly chosen
thisExp4 = data.ExperimentHandler(name=expName4, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='t1_Paradigm.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename4)

# save a log file for detail verbose info
logFile = logging.LogFile(filename1+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
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


# Create lists with all the different variable names for each n-back level, so the loops can refer to it
levelinwordsList = ['direkt', 'zwei', 'drei', 'vier'] # will be used in the instructions
levelcolorList = ['black', 'darkred', 'darkblue', 'darkgreen'] # will be used to change the colors of the stimuli
levelcolorinwordsList = ['Schwarz', 'Rot', 'Blau', 'Grün'] # will be used in the instructions
stimuliList = ['Stimuli\\1back_run1.xlsx', 'Stimuli\\1back_run2.xlsx',
'Stimuli\\2back_run1.xlsx', 'Stimuli\\2back_run2.xlsx',
'Stimuli\\3back_run1.xlsx', 'Stimuli\\3back_run2.xlsx',
'Stimuli\\4back_run1.xlsx', 'Stimuli\\4back_run2.xlsx'] # will be used to import the excel files with the n-back stimuli
finaln_stimuliList = ['Stimuli\\1back.xlsx', 'Stimuli\\2back.xlsx',
'Stimuli\\3back.xlsx', 'Stimuli\\4back.xlsx'] # for import of the stimuli for the final round after the ED part
EDlevcompList = ['schwarze', 'rote',
'rote', 'blaue',
'blaue', 'grüne',
'schwarze', 'grüne',
'rote', 'grüne',
'schwarze', 'blaue'] # these are all the comparison pairs that will be done
EDlevcolorList = ['black', 'darkred',
'darkred', 'darkblue',
'darkblue', 'darkgreen',
'black', 'darkgreen',
'darkred', 'darkgreen',
'black', 'darkblue'] # the system color names for all the levels
EDlevList = [1, 2,
2, 3,
3, 4,
1, 4,
2, 4,
1, 3] # the n-back level that corresponds to the color (will be fed into the data file to know which button was which level)

# Create array corresponding to levels of n-back aka the list elements
nlevel = list(range(4))
# Consecutive numbers corresponding to the total number of runs per n-back level
nruns = list(range(2))
# Create array to correctly refer to the different runs depending on n-back in the loops
nref = [0,2,4,6]

# The steps in which the monetary values will be adapted in the ED part
EDsteps = [1.00,0.50,0.25,0.13,0.06,0.03,0.02]
# The constant monetary value that will be assigned to the option that was not chosen in the 1€ vs 1€ comparison
EDfix = [2.00]
# Create array corresponding to rounds of effort discounting aka the list elements
EDrounds = list(range(6))
# Create array corresponding to every second element in the list of comparisons, which will be randomized for every participant
EDcomps = [0,2,4,6,8,10]
random.shuffle(EDcomps)

# Create the 18 comparisons of 1 vs 1, with randomized left-right-assignment
leftright = [0,1]
VS1levcompList = []
VS1levcolorList = []
VS1levList = []
for j in [0,1,2]: # three times because each pair will be presented three times
    for i in [0,1,2,3,4,5]: # to refer to the elements of EDcomps
        random.shuffle(leftright)
        VS1levcompList.append(EDlevcompList[EDcomps[i] + leftright[0]])
        VS1levcompList.append(EDlevcompList[EDcomps[i] + leftright[1]])
        VS1levcolorList.append(EDlevcolorList[EDcomps[i] + leftright[0]])
        VS1levcolorList.append(EDlevcolorList[EDcomps[i] + leftright[1]])
        VS1levList.append(EDlevList[EDcomps[i] + leftright[0]])
        VS1levList.append(EDlevList[EDcomps[i] + leftright[1]])

# Create array corresponding to rounds of 1 vs 1 comparisons aka the list elements
VS1rounds = list(range(18))
# Create array corresponding to every second element in the list of comparisons, which will be randomized for every participant
VS1comps = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34]
random.shuffle(VS1comps)

# ------------------------------
# n-back task components
# ------------------------------

# Initialize components for welcome screen
WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Willkommen!\n\nDas Experiment besteht aus zwei Teilen.\nIm ersten Teil werden Sie eine Aufgabe mit verschiedenen Schwierigkeitsstufen durchführen.\n'\
        'Im zweiten Teil werden Sie die verschiedenen Schwierigkeitsstufen des ersten Teils miteinander vergleichen.\n\n'\
        'Drücken Sie die Leertaste, um mit dem ersten Teil zu beginnen und die Instruktion des ersten Levels zu lesen.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WelcomeKey = keyboard.Keyboard()

# Initialize n-back instruction routine
instruction_Clock = core.Clock()
instructiontext = visual.TextStim(win=win, name='instructiontext',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructionkey = keyboard.Keyboard()

# Initialize fixation cross routine
fixcross_Clock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Courier New',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fixcrosskey = keyboard.Keyboard()

# Initialize n-back stimuli presentation
trial_Clock = core.Clock()
nback_trial = visual.TextStim(win=win, name='trial',
    text='',
    font='Courier New',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_resp = keyboard.Keyboard()

# Initialize feedback routine
fb_Clock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
feedback = visual.TextStim(win=win, name='feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fb_key = keyboard.Keyboard()


# ------------------------------
# 1 vs 1 components
# ------------------------------

# Initialize components for 1 vs 1 instruction routine
Instruction1vs1Clock = core.Clock()
VS1text = visual.TextStim(win=win, name='VS1text',
    text='Nun beginnt der zweite Teil.\n\nDie unterschiedlichen Level, die Sie gerade absolviert haben, werden nun nacheinander gegenübergestellt.\n'\
        'Auf dem Bildschirm erscheint die Frage "Welche Bezahlung würden Sie eher für welches Level annehmen?". Darunter befinden sich zwei Textfelder, '\
        'zum Beispiel "1,00€ für das rote Level" und "1,00€ für das schwarze Level". Sie können die Frage beantworten, indem Sie mit der Maus '\
        '(mit einem einfachen Klick) auf eins der beiden Felder klicken. Dabei geht es nicht um Schnelligkeit. Nachdem Sie geklickt haben, '\
        'werden sich die Level verändern und Sie können sich erneut entscheiden. Auf diese Weise werden alle Level mehrmals miteinander verglichen.\n'\
        'Zur Erinnerung:\n'\
        'Erstes Level = schwarz, zweites Level = rot, drittes Level = blau, viertes Level = grün.\n\n'\
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
    text='Welche Bezahlung würden Sie eher für welches Level annehmen?',
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
    color='', colorSpace='rgb',
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
   color='', colorSpace='rgb',
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
text = visual.TextStim(win=win, name='text',
    text='Nun ändert sich der Ablauf ein wenig.\nEs verändern sich jetzt nicht vorrangig die Level, sondern die Geldbeträge, die Ihnen angeboten werden.\n'\
        'Bitte entscheiden Sie sich wieder für eine der Optionen, es geht dabei nicht um Schnelligkeit.\n'\
        'Die Geldbeträge werden Ihnen NICHT zusätzlich zu Ihrer Teilnahme-Vergütung ausgezahlt. Es handelt sich um fiktive Beträge. '\
        'Versuchen Sie deshalb bitte nicht, die Beträge künstlich in die Höhe zu treiben, sondern entscheiden Sie sich so, '\
        'dass Sie mit dem Verhältnis der Optionen wirklich zufrieden sind.\n'\
        'Eine Ihrer Entscheidungen wird anschließend zufällig für einen erneuten Durchgang ausgewählt.\n\n'\
        'Drücken Sie die Leertaste, um zu beginnen.',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize ED question routine
EDroundClock = core.Clock()
question = visual.TextStim(win=win, name='question',
    text='Welche Bezahlung würden Sie eher für welches Level annehmen?',
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
    size=[0.5,0.1], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='', colorSpace='rgb',
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
   size=[0.5,0.1], borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=0.03,
   anchor='center',
   name='EDrightbutton')
EDrightbutton.buttonClock = core.Clock()

# Initialize ED buffer screen for between button clicks
EDbufferscreenClock = core.Clock()
EDbufferscreen = visual.TextStim(win=win, name='EDbufferscreen',
    text='Welche Bezahlung würden Sie eher für welches Level annehmen?',
    font='Open Sans',
    pos=[0,0.1], height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
bufferscreenkey = keyboard.Keyboard()
EDstorebutton = []
VS1storebutton = []

# Initialize components for the goodbye routine
GoodbyeClock = core.Clock()
GoodbyeText = visual.TextStim(win=win, name='GoodbyeText',
    text='Sie haben es geschafft!\n\nDas Experiment ist nun beendet. Bitte wenden Sie sich an die Versuchsleitung.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=0.0);

# ------------------------------
# Final n-back round components
# ------------------------------

# Initialize n-back instruction routine
finaln_instruction_Clock = core.Clock()
finaln_instructiontext = visual.TextStim(win=win, name='finaln_instructiontext',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
finaln_instructionkey = keyboard.Keyboard()

# Initialize fixation cross routine
finaln_fixcross_Clock = core.Clock()
finaln_fixcross = visual.TextStim(win=win, name='finaln_fixcross',
    text='+',
    font='Courier New',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
finaln_fixcrosskey = keyboard.Keyboard()

# Initialize n-back stimuli presentation
finaln_trial_Clock = core.Clock()
finaln_nback_trial = visual.TextStim(win=win, name='finaln_trial',
    text='',
    font='Courier New',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
finaln_trial_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
WelcomeKey.keys = []
WelcomeKey.rt = []
_WelcomeKey_allKeys = []
# hide mouse cursor
win.mouseVisible = False
# keep track of which components have finished
WelcomeScreenComponents = [WelcomeText, WelcomeKey]
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
        WelcomeText.setAutoDraw(True)
    
    # *WelcomeKey* updates
    waitOnFlip = False
    if WelcomeKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeKey.frameNStart = frameN  # exact frame index
        WelcomeKey.tStart = t  # local t and not account for scr refresh
        WelcomeKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeKey, 'tStartRefresh')  # time at next scr refresh
        WelcomeKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(WelcomeKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(WelcomeKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if WelcomeKey.status == STARTED and not waitOnFlip:
        theseKeys = WelcomeKey.getKeys(keyList=['space'], waitRelease=False)
        _WelcomeKey_allKeys.extend(theseKeys)
        if len(_WelcomeKey_allKeys):
            WelcomeKey.keys = _WelcomeKey_allKeys[-1].name  # just the last key pressed
            WelcomeKey.rt = _WelcomeKey_allKeys[-1].rt
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
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ---------------------------------------------------------------
# -------Large loop through all levels and runs of n-back--------
# ---------------------------------------------------------------


for nx in nlevel:

    # ------Prepare to start Instruction routine-------
    continueRoutine = True
    # update component parameters for each repeat
    instructionkey.keys = []
    instructionkey.rt = []
    instruction_allKey = []
    instructiontext.setColor(levelcolorList[nx])
    currenttext = str(levelcolorinwordsList[nx]) + 'es Level\n\nIhnen werden nun nacheinander Buchstaben auf dem Bildschirm präsentiert. '\
        'Wenn der aktuelle Buchstabe der gleiche ist wie der, der ' + str(levelinwordsList[nx]) + ' zuvor präsentiert wurde, dann drücken Sie bitte die rechte Pfeiltaste. '\
        'Wenn es nicht der gleiche Buchstabe ist, drücken sie bitte die linke Pfeiltaste.\nReagieren Sie bei jedem Buchstaben bitte so schnell und richtig wie möglich.\n\n'\
        'rechts = gleicher Buchstabe wie ' + str(levelinwordsList[nx]) + ' zuvor\nlinks = nicht der gleiche Buchstabe wie zuvor\n\nDrücken Sie die Leertaste, um zu beginnen.'
    instructiontext.setText(currenttext)
    # hide mouse cursor
    win.mouseVisible = False
    # keep track of which components have finished
    instruction_Components = [instructiontext, instructionkey]
    for thisComponent in instruction_Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruction_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    nback_trial.setColor(levelcolorList[nx])
    
    # -------Run Routine "Instruction nx-back"-------
    while continueRoutine:
        # get current time
        t = instruction_Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruction_Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
    
        # *Instruction nx Text* updates
        if instructiontext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructiontext.frameNStart = frameN  # exact frame index
            instructiontext.tStart = t  # local t and not account for scr refresh
            instructiontext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructiontext, 'tStartRefresh')  # time at next scr refresh
            instructiontext.setAutoDraw(True)
    
        # *Instruction nx Key* updates
        waitOnFlip = False
        if instructionkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionkey.frameNStart = frameN  # exact frame index
            instructionkey.tStart = t  # local t and not account for scr refresh
            instructionkey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionkey, 'tStartRefresh')  # time at next scr refresh
            instructionkey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructionkey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructionkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructionkey.status == STARTED and not waitOnFlip:
            theseKeys = instructionkey.getKeys(keyList=['space'], waitRelease=False)
            instruction_allKey.extend(theseKeys)
            if len(instruction_allKey):
                instructionkey.keys = instruction_allKey[-1].name  # just the last key pressed
                instructionkey.rt = instruction_allKey[-1].rt
                # a response ends the routine
                continueRoutine = False
    
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
    
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Instruction nx-back"-------
    for thisComponent in instruction_Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instruction1back" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # -----------------------------------------------------------
    # Here comes the loop that handles the 2 runs within each of the 4 n-back levels
    # -----------------------------------------------------------

    for rx in nruns:

        # set up handler to look after randomisation of conditions etc
        nback_run = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(stimuliList[nref[nx]+rx]),
            seed=None, name='nback_run')
        thisExp1.addLoop(nback_run)  # add the loop to the experiment
        this_nback_run = nback_run.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisOneback_run1.rgb)
        if this_nback_run != None:
            for paramName in this_nback_run:
                exec('{} = this_nback_run[paramName]'.format(paramName))

        for this_nback_run in nback_run:
            currentLoop = nback_run
            # abbreviate parameter names if possible (e.g. rgb = thisOneback_run1.rgb)
            if this_nback_run != None:
                for paramName in this_nback_run:
                    exec('{} = this_nback_run[paramName]'.format(paramName))
    
            # ------Prepare to start Routine "FixationCross"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            fixcrosskey.keys = []
            fixcrosskey.rt = []
            _fixcrosskey_allKeys = []
            # hide mouse cursor
            win.mouseVisible = False
            # keep track of which components have finished
            fixcross_Components = [fixcross, fixcrosskey]
            for thisComponent in fixcross_Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            fixcross_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
    
           # -------Run Routine "FixationCross"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = fixcross_Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=fixcross_Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
        
                # *fixcross* updates
                if fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixcross.frameNStart = frameN  # exact frame index
                    fixcross.tStart = t  # local t and not account for scr refresh
                    fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                    fixcross.setAutoDraw(True)
                if fixcross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixcross.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixcross.tStop = t  # not accounting for scr refresh
                        fixcross.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                        fixcross.setAutoDraw(False)
        
                # *fixcrosskey* updates
                waitOnFlip = False
                if fixcrosskey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixcrosskey.frameNStart = frameN  # exact frame index
                    fixcrosskey.tStart = t  # local t and not account for scr refresh
                    fixcrosskey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixcrosskey, 'tStartRefresh')  # time at next scr refresh
                    fixcrosskey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(fixcrosskey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(fixcrosskey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if fixcrosskey.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixcrosskey.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixcrosskey.tStop = t  # not accounting for scr refresh
                        fixcrosskey.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixcrosskey, 'tStopRefresh')  # time at next scr refresh
                        fixcrosskey.status = FINISHED
                if fixcrosskey.status == STARTED and not waitOnFlip:
                    theseKeys = fixcrosskey.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
                    _fixcrosskey_allKeys.extend(theseKeys)
                    if len(_fixcrosskey_allKeys):
                        fixcrosskey.keys = _fixcrosskey_allKeys[-1].name  # just the last key pressed
                        fixcrosskey.rt = _fixcrosskey_allKeys[-1].rt
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
        
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixcross_Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
        
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
    
            # -------Ending Routine "FixationCross"-------
            for thisComponent in fixcross_Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            nback_run.addData('fixcross.started', fixcross.tStartRefresh)
            # check responses
            if fixcrosskey.keys in ['', [], None]:  # No response was made
                fixcrosskey.keys = None

            # ------Prepare to start Routine "trial_nx-back_run1/2/3"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            nback_trial.setText(Letter)
            trial_resp.keys = []
            trial_resp.rt = []
            trial_allKey = []
            # hide mouse cursor
            win.mouseVisible = False
            # keep track of which components have finished
            trial_Components = [nback_trial, trial_resp]
            for thisComponent in trial_Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trial_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
    
            # -------Run Routine "trial_nx-back_run1/2/3"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trial_Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trial_Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
        
                # *trial_nx-back_run1/2/3* updates
                if nback_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    nback_trial.frameNStart = frameN  # exact frame index
                    nback_trial.tStart = t  # local t and not account for scr refresh
                    nback_trial.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(nback_trial, 'tStartRefresh')  # time at next scr refresh
                    nback_trial.setAutoDraw(True)
                if nback_trial.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > nback_trial.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        nback_trial.tStop = t  # not accounting for scr refresh
                        nback_trial.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(nback_trial, 'tStopRefresh')  # time at next scr refresh
                        nback_trial.setAutoDraw(False)
        
                # *trial_nx-back_run1/2/3_resp* updates
                waitOnFlip = False
                if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    trial_resp.frameNStart = frameN  # exact frame index
                    trial_resp.tStart = t  # local t and not account for scr refresh
                    trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
                    trial_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(trial_resp.clearEvents, eventType='keyboard') # clear events on next screen flip
                if trial_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > trial_resp.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        trial_resp.tStop = t  # not accounting for scr refresh
                        trial_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(trial_resp, 'tStopRefresh')  # time at next scr refresh
                        trial_resp.status = FINISHED
                if trial_resp.status == STARTED and not waitOnFlip:
                    theseKeys = trial_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                    trial_allKey.extend(theseKeys)
                    if len(trial_allKey):
                        trial_resp.keys = trial_allKey[0].name  # just the first key pressed
                        trial_resp.rt = trial_allKey[0].rt
                        # was this correct?
                        if (trial_resp.keys == str(CorrAnswer)) or (trial_resp.keys == CorrAnswer):
                            trial_resp.corr = 1
                        else:
                            trial_resp.corr = 0
        
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
        
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
        
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
    
            # -------Ending Routine "trial_nx-back_run1/2/3"-------
            for thisComponent in trial_Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            nback_run.addData('nback_trial.started', nback_trial.tStartRefresh)
            # check responses
            if trial_resp.keys in ['', [], None]:  # No response was made
                trial_resp.keys = None
                # was no response the correct answer?!
                if str(CorrAnswer).lower() == 'none':
                   trial_resp.corr = 1;  # correct non-response
                else:
                   trial_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for oneback_run1 (TrialHandler)
            nback_run.addData('trial_resp.keys', trial_resp.keys)
            nback_run.addData('trial_resp.corr', trial_resp.corr)
            nback_run.addData('currentlevel', nx+1)
            if trial_resp.keys != None:  # we had a response
                nback_run.addData('trial_resp.rt', trial_resp.rt)
            thisExp1.nextEntry()
    
        # completed 1.0 repeats of 'nx-back_run1/2/3'


        # ------Prepare to start Routine "feedback_nx-back_run1/2/3"-------
        continueRoutine = True
        # update component parameters for each repeat
        nCorr = nback_run.data['trial_resp.corr'][-64:].sum() # number of correct trials
        pCorr = (nCorr*100)/64 # percentage of correct trials
        pCorr = round(pCorr, 1) # round the percentage to 1 number after the decimal point

        nCorrTarArray = np.array(nback_run.data['trial_resp.keys'][-64:]) # extract response data as numpy array
        corrResp = np.array(nback_run.data['trial_resp.corr'][-64:]) # extract correctness data as numpy array
        nCorrTarFilter = np.where((nCorrTarArray == 'right') & (corrResp == 1)) # index where targets were correctly responded to
        nCorrTar = corrResp[nCorrTarFilter] # elements of correct responses to targets
        nCorrTar = len(nCorrTar) # calculate sum of correct responses to targets
        pCorrTar = (nCorrTar*100)/16 # percentage of correct targets
        pCorrTar = np.around(pCorrTar, 1) # round the percentage to the decimal point

        nCorrNonTarArray = np.array(nback_run.data['trial_resp.keys'][-64:]) # extract response data as numpy array
        nCorrNonTarFilter = np.where((nCorrNonTarArray == 'left') & (corrResp == 1)) # index where non-targets were correctly responded to
        nCorrNonTar = corrResp[nCorrNonTarFilter]  # elements of correct responses to non-targets
        nCorrNonTar = len(nCorrNonTar) # calculate sum of correct responses to non-targets
        pCorrNonTar = (nCorrNonTar*100)/48 # percentage of correct non-targets
        pCorrNonTar = np.around(pCorrNonTar, 1) # round the percentage to the decimal point

        # Display the feedback message depending on correct trials (encouragement) and run number (what happens next)
        if nx != 3:
            if rx == 0:
                if pCorrTar >= 50 and pCorrNonTar >= 50:
                    msg = "In diesem Block haben Sie auf " + str(pCorrTar) + "% der sich wiederholenden und auf "\
                        + str(pCorrNonTar) + "% der einzelnen Buchstaben korrekt reagiert.\n\nWeiter so!\n\nDrücken Sie die Leertaste, um einen weiteren Durchgang dieses Levels zu beginnen."
                else:
                    msg = "In diesem Block haben Sie auf " + str(pCorrTar) + "% der sich wiederholenden und auf "\
                        + str(pCorrNonTar) + "% der einzelnen Buchstaben korrekt reagiert.\n\nBitte strengen Sie sich mehr an!\n\nDrücken Sie die Leertaste, um einen weiteren Durchgang dieses Levels zu beginnen."
            else:
                if pCorrTar >= 50 and pCorrNonTar >= 50:
                    msg = "In diesem Block haben Sie auf " + str(pCorrTar) + "% der sich wiederholenden und auf "\
                        + str(pCorrNonTar) + "% der einzelnen Buchstaben korrekt reagiert.\n\nWeiter so!\n\nBeantworten Sie jetzt bitte den Fragebogen auf dem Tablet.\n\nDrücken Sie danach die Leertaste, um die Instruktion des nächsten Levels zu lesen."
                else:
                    msg = "In diesem Block haben Sie auf " + str(pCorrTar) + "% der sich wiederholenden und auf "\
                        + str(pCorrNonTar) + "% der einzelnen Buchstaben korrekt reagiert.\n\nBitte strengen Sie sich mehr an!\n\nBeantworten Sie jetzt bitte den Fragebogen auf dem Tablet.\n\nDrücken Sie danach die Leertaste, um die Instruktion des nächsten Levels zu lesen."
        else:
            if rx == 0:
                if pCorrTar >= 50 and pCorrNonTar >= 50:
                    msg = "In diesem Block haben Sie auf " + str(pCorrTar) + "% der sich wiederholenden und auf "\
                        + str(pCorrNonTar) + "% der einzelnen Buchstaben korrekt reagiert.\n\nWeiter so!\n\nDrücken Sie die Leertaste, um einen weiteren Durchgang dieses Levels zu beginnen."
                else:
                    msg = "In diesem Block haben Sie auf " + str(pCorrTar) + "% der sich wiederholenden und auf "\
                        + str(pCorrNonTar) + "% der einzelnen Buchstaben korrekt reagiert.\n\nBitte strengen Sie sich mehr an!\n\nDrücken Sie die Leertaste, um einen weiteren Durchgang dieses Levels zu beginnen."
            else:
                if pCorrTar >= 50 and pCorrNonTar >= 50:
                    msg = "In diesem Block haben Sie auf " + str(pCorrTar) + "% der sich wiederholenden und auf "\
                        + str(pCorrNonTar) + "% der einzelnen Buchstaben korrekt reagiert.\n\nWeiter so!\n\nBeantworten Sie jetzt bitte den Fragebogen auf dem Tablet.\n\nDrücken Sie danach die Leertaste, um mit dem nächsten Teil des Experiments zu beginnen."
                else:
                    msg = "In diesem Block haben Sie auf " + str(pCorrTar) + "% der sich wiederholenden und auf "\
                        + str(pCorrNonTar) + "% der einzelnen Buchstaben korrekt reagiert.\n\nBitte strengen Sie sich mehr an!\n\nBeantworten Sie jetzt bitte den Fragebogen auf dem Tablet.\n\nDrücken Sie danach die Leertaste, um mit dem nächsten Teil des Experiments zu beginnen."

        feedback.setText(msg)
        fb_key.keys = []
        fb_key.rt = []
        fb_allKey = []
        # hide mouse cursor
        win.mouseVisible = False
        # keep track of which components have finished
        fb_Components = [feedback, fb_key]
        for thisComponent in fb_Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fb_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "feedback_nx-back_run1/2/3"-------
        while continueRoutine:
            # get current time
            t = fb_Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fb_Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
    
            # *feedback_nx-back_run1/2/3* updates
            if feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback.frameNStart = frameN  # exact frame index
                feedback.tStart = t  # local t and not account for scr refresh
                feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
                feedback.setAutoDraw(True)
    
            # *feedback_nx-back_run1/2/3 key* updates
            waitOnFlip = False
            if fb_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fb_key.frameNStart = frameN  # exact frame index
                fb_key.tStart = t  # local t and not account for scr refresh
                fb_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fb_key, 'tStartRefresh')  # time at next scr refresh
                fb_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fb_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(fb_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if fb_key.status == STARTED and not waitOnFlip:
                theseKeys = fb_key.getKeys(keyList=['space'], waitRelease=False)
                fb_allKey.extend(theseKeys)
                if len(fb_allKey):
                    fb_key.keys = fb_allKey[-1].name  # just the last key pressed
                    fb_key.rt = fb_allKey[-1].rt
                    # a response ends the routine
                    continueRoutine = False
    
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
    
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fb_Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
    
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "feedback_nx-back_run1/2/3"-------
        for thisComponent in fb_Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)      
        # make mouse cursor visible again
        win.mouseVisible = True
        # the Routine "feedback_nx-back_run1/2/3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

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
leftbutton_1vs1_level = [] # a variable to store the levels of the left button
rightbutton_1vs1_level = [] # a variable to store the levels of the right button
leftbutton_1vs1_clicked = [] # whether it was clicked or not
rightbutton_1vs1_clicked = [] # whether it was clicked or not

# -----------------------------
# Loop for the 18 comparisons
# -----------------------------

# set up handler to look after randomisation of conditions etc
VS1round = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli\\VS1_Rounds.xlsx'),
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
    LB = '1 € für das ' + str(VS1levcompList[VS1comps[vsx]]) + ' Level'
    RB = '1 € für das ' + str(VS1levcompList[VS1comps[vsx]+1]) + ' Level'
    
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
            VS1leftbutton.setColor(VS1levcolorList[VS1comps[vsx]])
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
            VS1rightbutton.setColor(VS1levcolorList[VS1comps[vsx]+1])
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
    # what level each button was
    VS1round.addData('VS1leftbutton.nback', VS1levList[VS1comps[vsx]])
    VS1round.addData('VS1rightbutton.nback', VS1levList[VS1comps[vsx]+1])
    leftbutton_1vs1_level.append(VS1levList[VS1comps[vsx]])
    rightbutton_1vs1_level.append(VS1levList[VS1comps[vsx]+1])
    # store the necessary variables to be able to use it in the iteration process and for the random pick of the last n-back
    VS1storebutton.append(VS1click.clicked_name[0])
        
    # open up the next row for more data
    thisExp2.nextEntry()
    
    # the Routine was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

# ------- Calculate which levels are fixed and which are flexible in each pair ------------

# create empty variables to store the information of fixed and flexible
choices12 = []
choices13 = []
choices14 = []
choices23 = []
choices24 = []
choices34 = []

for i in VS1rounds:
    # create variables containing the levels on and choices of both buttons
    currentbuttons = [leftbutton_1vs1_level[i], rightbutton_1vs1_level[i]]
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
    elif all(x in currentbuttons for x in [1,4]):
        currentclick = list(compress(currentbuttons, currentchoices))
        choices14.append(currentclick[0])
    elif all(x in currentbuttons for x in [2,3]):
        currentclick = list(compress(currentbuttons, currentchoices))
        choices23.append(currentclick[0])
    elif all(x in currentbuttons for x in [2,4]):
        currentclick = list(compress(currentbuttons, currentchoices))
        choices24.append(currentclick[0])
    else:
        currentclick = list(compress(currentbuttons, currentchoices))
        choices34.append(currentclick[0])

# now reduce all 'choices' variables to the level that was chosen at least 2 out of 3 times
flexible12 = most_frequent(choices12)
flexible13 = most_frequent(choices13)
flexible14 = most_frequent(choices14)
flexible23 = most_frequent(choices23)
flexible24 = most_frequent(choices24)
flexible34 = most_frequent(choices34)

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
if flexible34 == 3:
    EDfixflexList.append('flexible')
    EDfixflexList.append('fixed')
else:
    EDfixflexList.append('fixed')
    EDfixflexList.append('flexible')
if flexible14 == 1:
    EDfixflexList.append('flexible')
    EDfixflexList.append('fixed')
else:
    EDfixflexList.append('fixed')
    EDfixflexList.append('flexible')
if flexible24 == 2:
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
# make mouse cursor visible
win.mouseVisible = True
# keep track of which components have finished
InstructionEDComponents = [text, key_resp]
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
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
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
thisExp3.nextEntry()
# the Routine "InstructionED" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Some variables to grow within the loop
finaln_leftbutton_level = [] # a variable to store the levels of the left button
finaln_rightbutton_level = [] # a variable to store the levels of the right button
finaln_leftbutton_value = [] # the last value displayed on the left button
finaln_rightbutton_value = [] # the last value displayed on the right button

# -----------------------------
# Loop for the 6 comparisons
# -----------------------------

for edx in EDrounds:

    # set up handler to look after randomisation of conditions etc
    EDround = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Stimuli\\ED_Steps.xlsx'),
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
        # make mouse cursor visible
        win.mouseVisible = True
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
        # hide mouse cursor
        win.mouseVisible = False
        # check responses
        if bufferscreenkey.keys in ['', [], None]:  # No response was made
            bufferscreenkey.keys = None
        
        # ------Prepare to start Routine -------
        continueRoutine = True
        # update component parameters for each repeat
        if EDfixflexList[EDcomps[edx]] == 'flexible':
            # set the right button to display 2€
            RB = str(format(EDfix[0],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]+1]) + ' Level'
            # display the flexible value on the left button
            if Currentstep == 0:
                # for the first 1-vs-2-comparison, we don't need to refer to the last buttonclick
                LB = str(format(EDsteps[0],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]]) + ' Level'
                # set the 'old' value of the flexible button to 1€ (to be used in the next iteration)
                oldvalue = EDsteps[0]
            else:
                # adapt the value of the left button depending on the previous choice
                if EDstorebutton[Currentstep-1] == 'EDleftbutton':
                    newvalue = oldvalue - EDsteps[Currentstep]
                # if the pricier option was chosen, raise the other options' value by the current EDsteps value
                else:
                    newvalue = oldvalue + EDsteps[Currentstep]
                LB = str(format(newvalue,'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]]) + ' Level'
                oldvalue = newvalue
        else:
            # set the left button to display 2€
            LB = str(format(EDfix[0],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]]) + ' Level'
            # display the flexible value on the right button
            if Currentstep == 0:
                # for the first 1-vs-2-comparison, we don't need to refer to the last buttonclick
                RB = str(format(EDsteps[0],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]+1]) + ' Level'
                # set the 'old' value of the flexible button to 1€ (to be used in the next iteration)
                oldvalue = EDsteps[0]
            else:
                # adapt the value of the right button depending on the previous choice
                if EDstorebutton[Currentstep-1] == 'EDrightbutton':
                    newvalue = oldvalue - EDsteps[Currentstep]
                # if the pricier option was chosen, raise the other options' value by the current EDsteps value
                else:
                    newvalue = oldvalue + EDsteps[Currentstep]
                RB = str(format(newvalue,'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]+1]) + ' Level'
                oldvalue = newvalue
        
        EDleftbutton.setText(LB)
        EDrightbutton.setText(RB)
        # setup some python lists for storing info about the response click
        EDclick.clicked_name = []
        gotValidClick = False  # until a click is received
        # make mouse cursor visible
        win.mouseVisible = True
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
                EDleftbutton.setColor(EDlevcolorList[EDcomps[edx]])
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
                EDrightbutton.setColor(EDlevcolorList[EDcomps[edx]+1])
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
        # what levelcolor each button had
        EDround.addData('EDleftbutton.nback', EDlevList[EDcomps[edx]])
        EDround.addData('EDrightbutton.nback', EDlevList[EDcomps[edx]+1])
        # store the necessary variables to be able to use it in the iteration process and for the random pick of the last n-back
        EDstorebutton.append(EDclick.clicked_name[0])
        if Currentstep == 0:
            finaln_leftbutton_level.append(EDlevList[EDcomps[edx]])
            finaln_rightbutton_level.append(EDlevList[EDcomps[edx]+1])
        elif Currentstep == 5:
            finaln_leftbutton_value.append(LB[0:4])
            finaln_rightbutton_value.append(RB[0:4])
        
        # open up the next row for more data
        thisExp3.nextEntry()
        
        # the Routine was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()    
        
    
# Effort Discounting is complete

# Now the participant goes through a run of an n-back level again
# The level is being randomly chosen from one of their choices in the last round of each comparison

randompick1 = random.choice(list(range(6))) # randomly picks one number from 0 to 5 (for choosing a COG-ED comparison)
randompick2 = random.choice(list(range(2))) # randomly picks 0 or 1 (for choosing the left (0) or right (1) button category)

finaln_LBvalue = finaln_leftbutton_value[randompick1] # the last value displayed on the left button
finaln_LBvalue = float(finaln_LBvalue.replace(',','.')) # convert string to float with dot notation
finaln_LBlevel = finaln_leftbutton_level[randompick1] # level of the left button
nLB = finaln_LBlevel - 1 # subtract 1 to be able to use it for indexing list elements

finaln_RBvalue = finaln_rightbutton_value[randompick1] # the last value displayed on the right button
finaln_RBvalue = float(finaln_RBvalue.replace(',','.')) # convert string to float with dot notation
finaln_RBlevel = finaln_rightbutton_level[randompick1] # level of the right button
nRB = finaln_RBlevel - 1 # subtract 1 to be able to use it for indexing list elements

if randompick2 == 0: # if the left button was chosen randomly, assign all values for the final task accordingly
    finaln_taskvalue = finaln_LBvalue
    finaln_tasklevel = nLB
else:
    finaln_taskvalue = finaln_RBvalue
    finaln_tasklevel = nRB

# ------Prepare to start Instruction routine-------
continueRoutine = True
# update component parameters for each repeat
finaln_instructionkey.keys = []
finaln_instructionkey.rt = []
finaln_instruction_allKey = []
finaln_instructiontext.setColor(levelcolorList[finaln_tasklevel])
currenttext = 'Eine Ihrer Entscheidungen lautete:\n\n"Das ' + str(levelcolorinwordsList[nLB]) + 'e Level für ' + str(format(finaln_LBvalue,'.2f')) + '€ oder das '\
    + str(levelcolorinwordsList[nRB]) + 'e Level für ' + str(format(finaln_RBvalue,'.2f')) + '€?"\n\n'\
    'Zufällig ausgewählt wurde das ' + str(levelcolorinwordsList[finaln_tasklevel]) + 'e Level für ' + str(format(finaln_taskvalue,'.2f')) + '€.\n\n'\
    'Ihnen werden nun nacheinander Buchstaben auf dem Bildschirm präsentiert. Wenn der aktuelle Buchstabe der gleiche ist wie der, der '\
    + str(levelinwordsList[finaln_tasklevel]) + ' zuvor präsentiert wurde, dann drücken Sie bitte die rechte Pfeiltaste. Wenn es nicht der gleiche Buchstabe ist, '\
    'drücken sie bitte die linke Pfeiltaste.\nReagieren Sie bei jedem Buchstaben bitte so schnell und richtig wie möglich.\n\n'\
    'rechts = gleicher Buchstabe wie ' + str(levelinwordsList[finaln_tasklevel]) + ' zuvor\nlinks = nicht der gleiche Buchstabe wie zuvor\n\nDrücken Sie die Leertaste, um zu beginnen.'
finaln_instructiontext.setText(currenttext)
# hide mouse cursor
win.mouseVisible = False
# keep track of which components have finished
finaln_instruction_Components = [finaln_instructiontext, finaln_instructionkey]
for thisComponent in finaln_instruction_Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finaln_instruction_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

finaln_nback_trial.setColor(levelcolorList[finaln_tasklevel])
    
# -------Run Routine "Instruction finaln_tasklevel-back"-------
while continueRoutine:
    # get current time
    t = finaln_instruction_Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finaln_instruction_Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Instruction finaln_tasklevel Text* updates
    if finaln_instructiontext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finaln_instructiontext.frameNStart = frameN  # exact frame index
        finaln_instructiontext.tStart = t  # local t and not account for scr refresh
        finaln_instructiontext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finaln_instructiontext, 'tStartRefresh')  # time at next scr refresh
        finaln_instructiontext.setAutoDraw(True)

    # *Instruction finaln_tasklevel Key* updates
    waitOnFlip = False
    if finaln_instructionkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finaln_instructionkey.frameNStart = frameN  # exact frame index
        finaln_instructionkey.tStart = t  # local t and not account for scr refresh
        finaln_instructionkey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finaln_instructionkey, 'tStartRefresh')  # time at next scr refresh
        finaln_instructionkey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(finaln_instructionkey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(finaln_instructionkey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if finaln_instructionkey.status == STARTED and not waitOnFlip:
        theseKeys = finaln_instructionkey.getKeys(keyList=['space'], waitRelease=False)
        finaln_instruction_allKey.extend(theseKeys)
        if len(finaln_instruction_allKey):
            finaln_instructionkey.keys = finaln_instruction_allKey[-1].name  # just the last key pressed
            finaln_instructionkey.rt = finaln_instruction_allKey[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finaln_instruction_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction finaln_tasklevel-back"-------
for thisComponent in finaln_instruction_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# set up handler to look after randomisation of conditions etc
finaln_nback_run = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(finaln_stimuliList[finaln_tasklevel]),
    seed=None, name='finaln_nback_run')
thisExp4.addLoop(finaln_nback_run)  # add the loop to the experiment
this_finaln_nback_run = finaln_nback_run.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOneback_run1.rgb)
if this_finaln_nback_run != None:
    for paramName in this_finaln_nback_run:
        exec('{} = this_finaln_nback_run[paramName]'.format(paramName))

for this_finaln_nback_run in finaln_nback_run:
    currentLoop = finaln_nback_run
    # abbreviate parameter names if possible (e.g. rgb = thisOneback_run1.rgb)
    if this_finaln_nback_run != None:
        for paramName in this_finaln_nback_run:
            exec('{} = this_finaln_nback_run[paramName]'.format(paramName))

    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    finaln_fixcrosskey.keys = []
    finaln_fixcrosskey.rt = []
    _finaln_fixcrosskey_allKeys = []
    # hide mouse cursor
    win.mouseVisible = False
    # keep track of which components have finished
    finaln_fixcross_Components = [finaln_fixcross, finaln_fixcrosskey]
    for thisComponent in finaln_fixcross_Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    finaln_fixcross_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

   # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = finaln_fixcross_Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=finaln_fixcross_Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *finaln_fixcross* updates
        if finaln_fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finaln_fixcross.frameNStart = frameN  # exact frame index
            finaln_fixcross.tStart = t  # local t and not account for scr refresh
            finaln_fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finaln_fixcross, 'tStartRefresh')  # time at next scr refresh
            finaln_fixcross.setAutoDraw(True)
        if finaln_fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finaln_fixcross.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                finaln_fixcross.tStop = t  # not accounting for scr refresh
                finaln_fixcross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finaln_fixcross, 'tStopRefresh')  # time at next scr refresh
                finaln_fixcross.setAutoDraw(False)

        # *finaln_fixcrosskey* updates
        waitOnFlip = False
        if finaln_fixcrosskey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finaln_fixcrosskey.frameNStart = frameN  # exact frame index
            finaln_fixcrosskey.tStart = t  # local t and not account for scr refresh
            finaln_fixcrosskey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finaln_fixcrosskey, 'tStartRefresh')  # time at next scr refresh
            finaln_fixcrosskey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(finaln_fixcrosskey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(finaln_fixcrosskey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if finaln_fixcrosskey.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finaln_fixcrosskey.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                finaln_fixcrosskey.tStop = t  # not accounting for scr refresh
                finaln_fixcrosskey.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finaln_fixcrosskey, 'tStopRefresh')  # time at next scr refresh
                finaln_fixcrosskey.status = FINISHED
        if finaln_fixcrosskey.status == STARTED and not waitOnFlip:
            theseKeys = finaln_fixcrosskey.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _finaln_fixcrosskey_allKeys.extend(theseKeys)
            if len(_finaln_fixcrosskey_allKeys):
                finaln_fixcrosskey.keys = _finaln_fixcrosskey_allKeys[-1].name  # just the last key pressed
                finaln_fixcrosskey.rt = _finaln_fixcrosskey_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finaln_fixcross_Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "FixationCross"-------
    for thisComponent in finaln_fixcross_Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    finaln_nback_run.addData('finaln_fixcross.started', finaln_fixcross.tStartRefresh)
    # check responses
    if finaln_fixcrosskey.keys in ['', [], None]:  # No response was made
        finaln_fixcrosskey.keys = None

    # ------Prepare to start Routine "trial_nx-back_run1/2/3"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    finaln_nback_trial.setText(Letter)
    finaln_trial_resp.keys = []
    finaln_trial_resp.rt = []
    finaln_trial_allKey = []
    # hide mouse cursor
    win.mouseVisible = False
    # keep track of which components have finished
    finaln_trial_Components = [finaln_nback_trial, finaln_trial_resp]
    for thisComponent in finaln_trial_Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial_nx-back_run1/2/3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trial_nx-back_run1/2/3* updates
        if finaln_nback_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finaln_nback_trial.frameNStart = frameN  # exact frame index
            finaln_nback_trial.tStart = t  # local t and not account for scr refresh
            finaln_nback_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finaln_nback_trial, 'tStartRefresh')  # time at next scr refresh
            finaln_nback_trial.setAutoDraw(True)
        if finaln_nback_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finaln_nback_trial.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                finaln_nback_trial.tStop = t  # not accounting for scr refresh
                finaln_nback_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finaln_nback_trial, 'tStopRefresh')  # time at next scr refresh
                finaln_nback_trial.setAutoDraw(False)

        # *trial_nx-back_run1/2/3_resp* updates
        waitOnFlip = False
        if finaln_trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finaln_trial_resp.frameNStart = frameN  # exact frame index
            finaln_trial_resp.tStart = t  # local t and not account for scr refresh
            finaln_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finaln_trial_resp, 'tStartRefresh')  # time at next scr refresh
            finaln_trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(finaln_trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(finaln_trial_resp.clearEvents, eventType='keyboard') # clear events on next screen flip
        if finaln_trial_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finaln_trial_resp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                finaln_trial_resp.tStop = t  # not accounting for scr refresh
                finaln_trial_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finaln_trial_resp, 'tStopRefresh')  # time at next scr refresh
                finaln_trial_resp.status = FINISHED
        if finaln_trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = finaln_trial_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            finaln_trial_allKey.extend(theseKeys)
            if len(finaln_trial_allKey):
                finaln_trial_resp.keys = finaln_trial_allKey[0].name  # just the first key pressed
                finaln_trial_resp.rt = finaln_trial_allKey[0].rt
                # was this correct?
                if (finaln_trial_resp.keys == str(CorrAnswer)) or (finaln_trial_resp.keys == CorrAnswer):
                    finaln_trial_resp.corr = 1
                else:
                    finaln_trial_resp.corr = 0

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finaln_trial_Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial_nx-back_run1/2/3"-------
    for thisComponent in finaln_trial_Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    finaln_nback_run.addData('finaln_nback_trial.started', finaln_nback_trial.tStartRefresh)
    # check responses
    if finaln_trial_resp.keys in ['', [], None]:  # No response was made
        finaln_trial_resp.keys = None
        # was no response the correct answer?!
        if str(CorrAnswer).lower() == 'none':
           finaln_trial_resp.corr = 1;  # correct non-response
        else:
           finaln_trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for oneback_run1 (TrialHandler)
    finaln_nback_run.addData('finaln_trial_resp.keys', finaln_trial_resp.keys)
    finaln_nback_run.addData('finaln_trial_resp.corr', finaln_trial_resp.corr)
    if finaln_trial_resp.keys != None:  # we had a response
        finaln_nback_run.addData('finaln_trial_resp.rt', finaln_trial_resp.rt)
    finaln_nback_run.addData('finaln_level', finaln_tasklevel) # the n-back level
    finaln_nback_run.addData('finaln_money', finaln_taskvalue+1) # the additional money that the participant receives (for the experimenter to look it up in case they missed it during the paradigm)
    thisExp4.nextEntry()


# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# hide mouse cursor
win.mouseVisible = False
# keep track of which components have finished
GoodbyeComponents = [GoodbyeText]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GoodbyeText* updates
    if GoodbyeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GoodbyeText.frameNStart = frameN  # exact frame index
        GoodbyeText.tStart = t  # local t and not account for scr refresh
        GoodbyeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GoodbyeText, 'tStartRefresh')  # time at next scr refresh
        GoodbyeText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make mouse cursor visible again
win.mouseVisible = True

# the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp1.saveAsWideText(filename1+'.csv', delim='auto')
thisExp1.saveAsPickle(filename1)
thisExp2.saveAsWideText(filename2+'.csv', delim='auto')
thisExp2.saveAsPickle(filename2)
thisExp3.saveAsWideText(filename3+'.csv', delim='auto')
thisExp3.saveAsPickle(filename3)
thisExp4.saveAsWideText(filename4+'.csv', delim='auto')
thisExp4.saveAsPickle(filename4)
logging.flush()
# make sure everything is closed down
thisExp1.abort()  # or data files will save again on exit
thisExp2.abort()
thisExp3.abort()
thisExp4.abort()
win.close()
core.quit()