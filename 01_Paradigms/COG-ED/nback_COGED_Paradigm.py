#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Juni 02, 2021, at 15:13
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

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'nback_COGED_Paradigm'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\josep\\Documents\\04_Projekte\\01_COG-ED_Revision\\CogEmotED\\01_Paradigms\\COG-ED\\nback_COGED_Paradigm.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
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

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Willkommen!\n\nDas Experiment besteht aus zwei Teilen.\nIm ersten Teil werden Sie eine sogenannte n-back Aufgabe mit verschiedenen Schwierigkeitsstufen durchführen.\nIm zweiten Teil werden Sie die verschiedenen Schwierigkeitsstufen des ersten Teils miteinander vergleichen.\n\nDrücken Sie die Leertaste, um mit dem ersten Teil zu beginnen und die Instruktion des ersten Levels zu lesen.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WelcomeKey = keyboard.Keyboard()

# Create lists with all the different variable names for each n-back level, so the loops can refer to it
levelList = ['1', '2', '3', '4']
levelinwordsList = ['direkt', 'zwei', 'drei', 'vier']
levelcolorList = ['black', 'darkred', 'darkblue', 'darkgreen']
levelcolorinwordsList = ['Schwarz', 'Rot', 'Blau', 'Grün']
instructionclockList = ['Instruction1backClock', 'Instruction2backClock', 'Instruction2backClock', 'Instruction2backClock']
instructiontextList = ['Instruction1Text', 'Instruction2Text', 'Instruction3Text', 'Instruction4Text']
instructionkeyList = ['Instruction1Key', 'Instruction2Key', 'Instruction3Key', 'Instruction4Key']
instructionallkeyList = ['_Instruction1Key_allKeys', '_Instruction2Key_allKeys', '_Instruction3Key_allKeys', '_Instruction4Key_allKeys']
instructioncompoList = ['Instruction1backComponents', 'Instruction2backComponents', 'Instruction2backComponents', 'Instruction2backComponents']
fixcrossList = ['fixcross1', 'fixcross2', 'fixcross3', 'fixcross4']
fixcrossclockList = ['fixcross1Clock', 'fixcross2Clock', 'fixcross3Clock', 'fixcross4Clock']
fixcrosscompoList = ['fixcross1Components', 'fixcross2Components', 'fixcross3Components', 'fixcross4Components']

runList = ['run_1back_run1', 'run_1back_run2',
'run_2back_run1', 'run_2back_run2',
'run_3back_run1', 'run_3back_run2',
'run_4back_run1', 'run_4back_run2']
runthisList = ['this1back_run1', 'this1back_run2',
'this2back_run1', 'this2back_run2',
'this3back_run1', 'this3back_run2',
'this4back_run1', 'this4back_run2']


trialclockList = ['trial_1back_run1Clock', 'trial_1back_run2Clock',
'trial_2back_run1Clock', 'trial_2back_run2Clock',
'trial_3back_run1Clock', 'trial_3back_run2Clock',
'trial_4back_run1Clock', 'trial_4back_run2Clock']
trialsList = ['trial_1back_run1', 'trial_1back_run2',
'trial_2back_run1', 'trial_2back_run2',
'trial_3back_run1', 'trial_3back_run2',
'trial_4back_run1', 'trial_4back_run2']
trialcompoList = ['trial_1back_run1Components', 'trial_1back_run2Components',
'trial_2back_run1Components', 'trial_2back_run2Components',
'trial_3back_run1Components', 'trial_3back_run2Components',
'trial_4back_run1Components', 'trial_4back_run2Components']
trialrespList = ['trial_1back_run1_resp', 'trial_1back_run2_resp',
'trial_2back_run1_resp', 'trial_2back_run2_resp',
'trial_3back_run1_resp', 'trial_3back_run2_resp',
'trial_4back_run1_resp', 'trial_4back_run2_resp']
trialallkeyList = ['_trial_1back_run1_resp_allKeys', '_trial_1back_run2_resp_allKeys',
'_trial_2back_run1_resp_allKeys', '_trial_2back_run2_resp_allKeys',
'_trial_3back_run1_resp_allKeys', '_trial_3back_run2_resp_allKeys',
'_trial_4back_run1_resp_allKeys', '_trial_4back_run2_resp_allKeys']

fbclockList = ['fb_1back_run1Clock', 'fb_1back_run2Clock',
'fb_2back_run1Clock', 'fb_2back_run2Clock',
'fb_3back_run1Clock', 'fb_3back_run2Clock',
'fb_4back_run1Clock', 'fb_4back_run2Clock']
fbList = ['fb_1back_run1', 'fb_1back_run2',
'fb_2back_run1', 'fb_2back_run2',
'fb_3back_run1', 'fb_3back_run2',
'fb_4back_run1', 'fb_4back_run2']
fbcompoList = ['fb_1back_run1Components', 'fb_1back_run2Components',
'fb_2back_run1Components', 'fb_2back_run2Components',
'fb_3back_run1Components', 'fb_3back_run2Components',
'fb_4back_run1Components', 'fb_4back_run2Components']
fbkeyList = ['fb_1back_run1_key', 'fb_1back_run2_key',
'fb_2back_run1_key', 'fb_2back_run2_key',
'fb_3back_run1_key', 'fb_3back_run2_key',
'fb_4back_run1_key', 'fb_4back_run2_key']
fballkeyList = ['_fb_1back_run1_allKey', '_fb_1back_run2_allKey',
'_fb_2back_run1_allKey', '_fb_2back_run2_allKey',
'_fb_3back_run1_allKey', '_fb_3back_run2_allKey',
'_fb_4back_run1_allKey', '_fb_4back_run2_allKey']

stimuliList = ['..\\\\..\\\\..\\\\Stimuli\\\\1back_run1.xlsx',
'..\\\\..\\\\..\\\\Stimuli\\\\1back_run2.xlsx',
'..\\\\..\\\\..\\\\Stimuli\\\\2back_run1.xlsx',
'..\\\\..\\\\..\\\\Stimuli\\\\2back_run2.xlsx',
'..\\\\..\\\\..\\\\Stimuli\\\\3back_run1.xlsx',
'..\\\\..\\\\..\\\\Stimuli\\\\3back_run2.xlsx',
'..\\\\..\\\\..\\\\Stimuli\\\\4back_run1.xlsx',
'..\\\\..\\\\..\\\\Stimuli\\\\4back_run2.xlsx']

# Create array corresponding to levels of n-back aka the list elements
nlevel = list(range(4))

# Consecutive numbers corresponding to the total number of runs
nruns = list(range(2))

# Create array to correctly refer to the different runs depending on n-back in the loops
# e.g. for 3-back run1 you will have nref[2]+nruns[0] = 6 -> 6th element in trialsList is 'trial_3back_run1'
nref = [0,2,4,6]

# Initialize Instruction routines with a loop
for nx in nlevel:
    globals()[instructionclockList[nx]] = core.Clock()
    globals()[instructiontextList[nx]] = visual.TextStim(win=win, name=instructiontextList[nx],
        text = str(levelcolorinwordsList[nx]) + 'es Level\n\nIhnen werden nun nacheinander Buchstaben auf dem Bildschirm präsentiert. Wenn der aktuelle Buchstabe der gleiche ist wie der, der ' + str(levelinwordsList[nx]) + ' zuvor präsentiert wurde, dann drücken Sie bitte die rechte Pfeiltaste. Wenn es nicht der gleiche Buchstabe ist, drücken sie bitte die linke Pfeiltaste.\nReagieren Sie bei jedem Buchstaben bitte so schnell und richtig wie möglich.\n\nrechts = gleicher Buchstabe wie ' + str(levelinwordsList[nx]) + ' zuvor\nlinks = nicht der gleiche Buchstabe wie zuvor\n\nDrücken Sie die Leertaste, um zu beginnen.',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color=levelcolorList[nx], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    globals()[instructionkeyList[nx]] = keyboard.Keyboard()

# Initialize components for Routine "FixationCross"
for nx in nlevel:
    globals()[fixcrossclockList[nx]] = core.Clock()
    globals()[fixcrossList[nx]] = visual.TextStim(win=win, name=fixcrossclockList[nx],
        text='+',
        font='Courier New',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color=levelcolorList[nx], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    fixcrosskey = keyboard.Keyboard()

# Initialize Trial routines with a loop
for nx in nref:
    for r in nruns:
        globals()[trialclockList[nx+r]] = core.Clock()
        globals()[trialsList[nx+r]] = visual.TextStim(win=win, name=trialsList[nx+r],
            text='',
            font='Courier New',
            pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
            color=levelcolorList[round(nx/2)], colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=0.0);
        globals()[trialrespList[nx+r]] = keyboard.Keyboard()

# Initialize Feedback routines with a loop
for nx in nref:
    for r in nruns:
        globals()[fbclockList[nx+r]] = core.Clock()
        msg='doh!'#if this comes up we forgot to update the msg!
        globals()[fbList[nx+r]] = visual.TextStim(win=win, name=fbList[nx+r],
            text='',
            font='Open Sans',
            pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
            color='black', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=-1.0);
        globals()[fbkeyList[nx+r]] = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
WelcomeKey.keys = []
WelcomeKey.rt = []
_WelcomeKey_allKeys = []
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
    globals()[instructionkeyList[nx]].keys = []
    globals()[instructionkeyList[nx]].rt = []
    globals()[instructionallkeyList[nx]] = []
    # keep track of which components have finished
    globals()[instructioncompoList[nx]] = [globals()[instructiontextList[nx]], globals()[instructionkeyList[nx]]]
    for thisComponent in globals()[instructioncompoList[nx]]:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    globals()[instructionclockList[nx]].reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Instruction nx-back"-------
    while continueRoutine:
        # get current time
        t = globals()[instructionclockList[nx]].getTime()
        tThisFlip = win.getFutureFlipTime(clock=globals()[instructionclockList[nx]])
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
    
        # *Instruction nx Text* updates
        if globals()[instructiontextList[nx]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            globals()[instructiontextList[nx]].frameNStart = frameN  # exact frame index
            globals()[instructiontextList[nx]].tStart = t  # local t and not account for scr refresh
            globals()[instructiontextList[nx]].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(globals()[instructiontextList[nx]], 'tStartRefresh')  # time at next scr refresh
            globals()[instructiontextList[nx]].setAutoDraw(True)
    
        # *Instruction nx Key* updates
        waitOnFlip = False
        if globals()[instructionkeyList[nx]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            globals()[instructionkeyList[nx]].frameNStart = frameN  # exact frame index
            globals()[instructionkeyList[nx]].tStart = t  # local t and not account for scr refresh
            globals()[instructionkeyList[nx]].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(globals()[instructionkeyList[nx]], 'tStartRefresh')  # time at next scr refresh
            globals()[instructionkeyList[nx]].status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(globals()[instructionkeyList[nx]].clock.reset)  # t=0 on next screen flip
            win.callOnFlip(globals()[instructionkeyList[nx]].clearEvents, eventType='keyboard')  # clear events on next screen flip
        if globals()[instructionkeyList[nx]].status == STARTED and not waitOnFlip:
            theseKeys = globals()[instructionkeyList[nx]].getKeys(keyList=['space'], waitRelease=False)
            globals()[instructionallkeyList[nx]].extend(theseKeys)
            if len(globals()[instructionallkeyList[nx]]):
                globals()[instructionkeyList[nx]].keys = globals()[instructionallkeyList[nx]][-1].name  # just the last key pressed
                globals()[instructionkeyList[nx]].rt = globals()[instructionallkeyList[nx]][-1].rt
                # a response ends the routine
                continueRoutine = False
    
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in globals()[instructioncompoList[nx]]:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
    
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Instruction nx-back"-------
    for thisComponent in globals()[instructioncompoList[nx]]:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instruction1back" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # -----------------------------------------------------------
    # Here comes the loop that handles the 3 runs within each of the 4 n-back levels
    # -----------------------------------------------------------

    for rx in nruns:

        # create variable that will indicate the correct element within the variable name lists for every run depending on the n-back level    
        y = nref[nx]+rx

        # set up handler to look after randomisation of conditions etc
        globals()[runList[y]] = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(stimuliList[y]),
            seed=None, name=runList[y])
        thisExp.addLoop(globals()[runList[y]])  # add the loop to the experiment
        globals()[runthisList[y]] = globals()[runList[y]].trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisOneback_run1.rgb)
        if globals()[runthisList[y]] != None:
            for paramName in globals()[runthisList[y]]:
                vari = ['{} = ' + str(runthisList[y]) + '[paramName]']
                exec(vari[0].format(paramName))

        for globals()[runthisList[y]] in globals()[runList[y]]:
            currentLoop = globals()[runList[y]]
            # abbreviate parameter names if possible (e.g. rgb = thisOneback_run1.rgb)
            if globals()[runthisList[y]] != None:
                for paramName in globals()[runthisList[y]]:
                    vari = ['{} = ' + str(runthisList[y]) + '[paramName]']
                    exec(vari[0].format(paramName))
    
            # ------Prepare to start Routine "FixationCross"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            fixcrosskey.keys = []
            fixcrosskey.rt = []
            _fixcrosskey_allKeys = []
            # keep track of which components have finished
            globals()[fixcrosscompoList[nx]] = [globals()[fixcrossList[nx]], fixcrosskey]
            for thisComponent in globals()[fixcrosscompoList[nx]]:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            globals()[fixcrossclockList[nx]].reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
    
           # -------Run Routine "FixationCross"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = globals()[fixcrossclockList[nx]].getTime()
                tThisFlip = win.getFutureFlipTime(clock=globals()[fixcrossclockList[nx]])
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
        
                # *fixcross* updates
                if globals()[fixcrossList[nx]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    globals()[fixcrossList[nx]].frameNStart = frameN  # exact frame index
                    globals()[fixcrossList[nx]].tStart = t  # local t and not account for scr refresh
                    globals()[fixcrossList[nx]].tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(globals()[fixcrossList[nx]], 'tStartRefresh')  # time at next scr refresh
                    globals()[fixcrossList[nx]].setAutoDraw(True)
                if globals()[fixcrossList[nx]].status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > globals()[fixcrossList[nx]].tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        globals()[fixcrossList[nx]].tStop = t  # not accounting for scr refresh
                        globals()[fixcrossList[nx]].frameNStop = frameN  # exact frame index
                        win.timeOnFlip(globals()[fixcrossList[nx]], 'tStopRefresh')  # time at next scr refresh
                        globals()[fixcrossList[nx]].setAutoDraw(False)
        
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
                for thisComponent in globals()[fixcrosscompoList[nx]]:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
        
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
    
            # -------Ending Routine "FixationCross"-------
            for thisComponent in globals()[fixcrosscompoList[nx]]:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            globals()[runList[y]].addData(str(fixcrossList[nx]) + '.started', globals()[fixcrossList[nx]].tStartRefresh)
            globals()[runList[y]].addData(str(fixcrossList[nx]) + '.stopped', globals()[fixcrossList[nx]].tStopRefresh)
            # check responses
            if fixcrosskey.keys in ['', [], None]:  # No response was made
                fixcrosskey.keys = None
            globals()[runList[y]].addData('fixcrosskey.keys',fixcrosskey.keys)
            if fixcrosskey.keys != None:  # we had a response
                globals()[runList[y]].addData('fixcrosskey.rt', fixcrosskey.rt)
            globals()[runList[y]].addData('fixcrosskey.started', fixcrosskey.tStartRefresh)
            globals()[runList[y]].addData('fixcrosskey.stopped', fixcrosskey.tStopRefresh)

            # ------Prepare to start Routine "trial_nx-back_run1/2/3"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            globals()[trialsList[y]].setText(Letter)
            globals()[trialrespList[y]].keys = []
            globals()[trialrespList[y]].rt = []
            globals()[trialallkeyList[y]] = []
            # keep track of which components have finished
            globals()[trialcompoList[y]] = [globals()[trialsList[y]], globals()[trialrespList[y]]]
            for thisComponent in globals()[trialcompoList[y]]:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            globals()[trialclockList[y]].reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
    
            # -------Run Routine "trial_nx-back_run1/2/3"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = globals()[trialclockList[y]].getTime()
                tThisFlip = win.getFutureFlipTime(clock=globals()[trialclockList[y]])
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
        
                # *trial_nx-back_run1/2/3* updates
                if globals()[trialsList[y]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    globals()[trialsList[y]].frameNStart = frameN  # exact frame index
                    globals()[trialsList[y]].tStart = t  # local t and not account for scr refresh
                    globals()[trialsList[y]].tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(globals()[trialsList[y]], 'tStartRefresh')  # time at next scr refresh
                    globals()[trialsList[y]].setAutoDraw(True)
                if globals()[trialsList[y]].status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > globals()[trialsList[y]].tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        globals()[trialsList[y]].tStop = t  # not accounting for scr refresh
                        globals()[trialsList[y]].frameNStop = frameN  # exact frame index
                        win.timeOnFlip(globals()[trialsList[y]], 'tStopRefresh')  # time at next scr refresh
                        globals()[trialsList[y]].setAutoDraw(False)
        
                # *trial_nx-back_run1/2/3_resp* updates
                waitOnFlip = False
                if globals()[trialrespList[y]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    globals()[trialrespList[y]].frameNStart = frameN  # exact frame index
                    globals()[trialrespList[y]].tStart = t  # local t and not account for scr refresh
                    globals()[trialrespList[y]].tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(globals()[trialrespList[y]], 'tStartRefresh')  # time at next scr refresh
                    globals()[trialrespList[y]].status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(globals()[trialrespList[y]].clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(globals()[trialrespList[y]].clearEvents, eventType='keyboard') # clear events on next screen flip
                if globals()[trialrespList[y]].status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > globals()[trialrespList[y]].tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        globals()[trialrespList[y]].tStop = t  # not accounting for scr refresh
                        globals()[trialrespList[y]].frameNStop = frameN  # exact frame index
                        win.timeOnFlip(globals()[trialrespList[y]], 'tStopRefresh')  # time at next scr refresh
                        globals()[trialrespList[y]].status = FINISHED
                if globals()[trialrespList[y]].status == STARTED and not waitOnFlip:
                    theseKeys = globals()[trialrespList[y]].getKeys(keyList=['left', 'right'], waitRelease=False)
                    globals()[trialallkeyList[y]].extend(theseKeys)
                    if len(globals()[trialallkeyList[y]]):
                        globals()[trialrespList[y]].keys = globals()[trialallkeyList[y]][0].name  # just the first key pressed
                        globals()[trialrespList[y]].rt = globals()[trialallkeyList[y]][0].rt
                        # was this correct?
                        if (globals()[trialrespList[y]].keys == str(CorrAnswer)) or (globals()[trialrespList[y]].keys == CorrAnswer):
                            globals()[trialrespList[y]].corr = 1
                        else:
                            globals()[trialrespList[y]].corr = 0
        
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
        
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in globals()[trialcompoList[y]]:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
        
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
    
            # -------Ending Routine "trial_nx-back_run1/2/3"-------
            for thisComponent in globals()[trialcompoList[y]]:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            globals()[runList[y]].addData(str(trialsList[y]) + '.started', globals()[trialsList[y]].tStartRefresh)
            globals()[runList[y]].addData(str(trialsList[y]) + '.stopped', globals()[trialsList[y]].tStopRefresh)
            # check responses
            if globals()[trialrespList[y]].keys in ['', [], None]:  # No response was made
                globals()[trialrespList[y]].keys = None
                # was no response the correct answer?!
                if str(CorrAnswer).lower() == 'none':
                   globals()[trialrespList[y]].corr = 1;  # correct non-response
                else:
                   globals()[trialrespList[y]].corr = 0;  # failed to respond (incorrectly)
            # store data for oneback_run1 (TrialHandler)
            globals()[runList[y]].addData(str(trialrespList[y]) + '.keys', globals()[trialrespList[y]].keys)
            globals()[runList[y]].addData(str(trialrespList[y]) + '.corr', globals()[trialrespList[y]].corr)
            if globals()[trialrespList[y]].keys != None:  # we had a response
                globals()[runList[y]].addData(str(trialrespList[y]) + '.rt', globals()[trialrespList[y]].rt)
            globals()[runList[y]].addData(str(trialrespList[y]) + '.started', globals()[trialrespList[y]].tStartRefresh)
            globals()[runList[y]].addData(str(trialrespList[y]) + '.stopped', globals()[trialrespList[y]].tStopRefresh)
            thisExp.nextEntry()
    
        # completed 1.0 repeats of 'nx-back_run1/2/3'


        # ------Prepare to start Routine "feedback_nx-back_run1/2/3"-------
        continueRoutine = True
        # update component parameters for each repeat
        nCorr = globals()[runList[y]].data[str(trialrespList[y]) + '.corr'].sum() # number of correct trials
        pCorr = (nCorr*100)/64 # percentage of correct trials
        pCorr = round(pCorr, 1) # round the percentage to 1 number after the decimal point

        nCorrTarArray = globals()[runList[y]].data[str(trialrespList[y]) + '.keys'] # extract response data
        nCorrTarFilter = nCorrTarArray == 'right' # index the data of the targets
        nCorrTar = sum(nCorrTarFilter) # calculate sum of correct targets aka sum of TRUE output of the filter
        pCorrTar = (nCorrTar*100)/16 # percentage of correct targets
        pCorrTar = np.around(pCorrTar, 1) # round the percentage to the decimal point

        nCorrNonTarArray = globals()[runList[y]].data[str(trialrespList[y]) + '.keys'] # extract response data
        nCorrNonTarFilter = nCorrNonTarArray == 'left' # index the data of the non-targets
        nCorrNonTar = sum(nCorrNonTarFilter) # calculate sum of correct non-targets aka sum of TRUE output of the filter
        pCorrNonTar = (nCorrNonTar*100)/48 # percentage of correct non-targets
        pCorrNonTar = np.around(pCorrNonTar, 1) # round the percentage to the decimal point

        if pCorrTar >= 50 and pCorrNonTar >= 50:
            msg = "In diesem Block haben Sie auf " + str(pCorrTar[0]) + "% der sich wiederholenden und auf " + str(pCorrNonTar[0]) + "% der einzelnen Buchstaben korrekt reagiert.\n\nWeiter so!"
        else:
            msg = "In diesem Block haben Sie auf " + str(pCorrTar[0]) + "% der sich wiederholenden und auf " + str(pCorrNonTar[0]) + "% der einzelnen Buchstaben korrekt reagiert.\n\nBitte strengen Sie sich mehr an!"
        globals()[fbList[y]].setText(msg)
        globals()[fbkeyList[y]].keys = []
        globals()[fbkeyList[y]].rt = []
        globals()[fballkeyList[y]] = []
        # keep track of which components have finished
        globals()[fbcompoList[y]] = [globals()[fbList[y]], globals()[fbkeyList[y]]]
        for thisComponent in globals()[fbcompoList[y]]:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        globals()[fbclockList[y]].reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "feedback_nx-back_run1/2/3"-------
        while continueRoutine:
            # get current time
            t = globals()[fbclockList[y]].getTime()
            tThisFlip = win.getFutureFlipTime(clock=globals()[fbclockList[y]])
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
    
            # *feedback_nx-back_run1/2/3* updates
            if globals()[fbList[y]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                globals()[fbList[y]].frameNStart = frameN  # exact frame index
                globals()[fbList[y]].tStart = t  # local t and not account for scr refresh
                globals()[fbList[y]].tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(globals()[fbList[y]], 'tStartRefresh')  # time at next scr refresh
                globals()[fbList[y]].setAutoDraw(True)
    
            # *feedback_nx-back_run1/2/3 key* updates
            waitOnFlip = False
            if globals()[fbkeyList[y]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                globals()[fbkeyList[y]].frameNStart = frameN  # exact frame index
                globals()[fbkeyList[y]].tStart = t  # local t and not account for scr refresh
                globals()[fbkeyList[y]].tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(globals()[fbkeyList[y]], 'tStartRefresh')  # time at next scr refresh
                globals()[fbkeyList[y]].status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(globals()[fbkeyList[y]].clock.reset)  # t=0 on next screen flip
                win.callOnFlip(globals()[fbkeyList[y]].clearEvents, eventType='keyboard')  # clear events on next screen flip
            if globals()[fbkeyList[y]].status == STARTED and not waitOnFlip:
                theseKeys = globals()[fbkeyList[y]].getKeys(keyList=['space'], waitRelease=False)
                globals()[fballkeyList[y]].extend(theseKeys)
                if len(globals()[fballkeyList[y]]):
                    globals()[fbkeyList[y]].keys = globals()[fballkeyList[y]][-1].name  # just the last key pressed
                    globals()[fbkeyList[y]].rt = globals()[fballkeyList[y]][-1].rt
                    # a response ends the routine
                    continueRoutine = False
    
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
    
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in globals()[fbcompoList[y]]:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
    
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "feedback_nx-back_run1/2/3"-------
        for thisComponent in globals()[fbcompoList[y]]:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)      
        # the Routine "feedback_nx-back_run1/2/3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()