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
levelinwordsList = ['direkt', 'zwei', 'drei', 'vier']
levelcolorList = ['black', 'darkred', 'darkblue', 'darkgreen']
levelcolorinwordsList = ['Schwarz', 'Rot', 'Blau', 'Grün']
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

# Consecutive numbers corresponding to the total number of runs per n-back level
nruns = list(range(2))

# Create array to correctly refer to the different runs depending on n-back in the loops
nref = [0,2,4,6]

# Initialize Instruction routines with a loop
instruction_Clock = core.Clock()
instructiontext = visual.TextStim(win=win, name='instructiontext',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructionkey = keyboard.Keyboard()

# Initialize components for Routine "FixationCross"
fixcross_Clock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Courier New',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fixcrosskey = keyboard.Keyboard()

# Initialize Trial routines with a loop
trial_Clock = core.Clock()
nback_trial = visual.TextStim(win=win, name='trial',
    text='',
    font='Courier New',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_resp = keyboard.Keyboard()

# Initialize Feedback routines with a loop
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
    instructionkey.keys = []
    instructionkey.rt = []
    instruction_allKey = []
    instructiontext.setColor(levelcolorList[nx])
    currenttext = str(levelcolorinwordsList[nx]) + 'es Level\n\nIhnen werden nun nacheinander Buchstaben auf dem Bildschirm präsentiert. Wenn der aktuelle Buchstabe der gleiche ist wie der, der ' + str(levelinwordsList[nx]) + ' zuvor präsentiert wurde, dann drücken Sie bitte die rechte Pfeiltaste. Wenn es nicht der gleiche Buchstabe ist, drücken sie bitte die linke Pfeiltaste.\nReagieren Sie bei jedem Buchstaben bitte so schnell und richtig wie möglich.\n\nrechts = gleicher Buchstabe wie ' + str(levelinwordsList[nx]) + ' zuvor\nlinks = nicht der gleiche Buchstabe wie zuvor\n\nDrücken Sie die Leertaste, um zu beginnen.'
    instructiontext.setText(currenttext)
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

        # create variable that will indicate the correct element within the variable name lists for every run depending on the n-back level    
        y = nref[nx]+rx

        # set up handler to look after randomisation of conditions etc
        nback_run = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(stimuliList[y]),
            seed=None, name='nback_run')
        thisExp.addLoop(nback_run)  # add the loop to the experiment
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
            if trial_resp.keys != None:  # we had a response
                nback_run.addData('trial_resp.rt', trial_resp.rt)
            nback_run.addData('trial_resp.started', trial_resp.tStartRefresh)
            thisExp.nextEntry()
    
        # completed 1.0 repeats of 'nx-back_run1/2/3'


        # ------Prepare to start Routine "feedback_nx-back_run1/2/3"-------
        continueRoutine = True
        # update component parameters for each repeat
        nCorr = nback_run.data['trial_resp.corr'][-14:].sum() # number of correct trials
        pCorr = (nCorr*100)/64 # percentage of correct trials
        pCorr = round(pCorr, 1) # round the percentage to 1 number after the decimal point

        nCorrTarArray = nback_run.data['trial_resp.keys'][-14:] # extract response data
        nCorrTarFilter = nCorrTarArray == 'right' # index the data of the targets
        nCorrTar = sum(nCorrTarFilter) # calculate sum of correct targets aka sum of TRUE output of the filter
        pCorrTar = (nCorrTar*100)/16 # percentage of correct targets
        pCorrTar = np.around(pCorrTar, 1) # round the percentage to the decimal point

        nCorrNonTarArray = nback_run.data['trial_resp.keys'][-14:] # extract response data
        nCorrNonTarFilter = nCorrNonTarArray == 'left' # index the data of the non-targets
        nCorrNonTar = sum(nCorrNonTarFilter) # calculate sum of correct non-targets aka sum of TRUE output of the filter
        pCorrNonTar = (nCorrNonTar*100)/48 # percentage of correct non-targets
        pCorrNonTar = np.around(pCorrNonTar, 1) # round the percentage to the decimal point

        if pCorrTar >= 50 and pCorrNonTar >= 50:
            msg = "In diesem Block haben Sie auf " + str(pCorrTar[0]) + "% der sich wiederholenden und auf " + str(pCorrNonTar[0]) + "% der einzelnen Buchstaben korrekt reagiert.\n\nWeiter so!"
        else:
            msg = "In diesem Block haben Sie auf " + str(pCorrTar[0]) + "% der sich wiederholenden und auf " + str(pCorrNonTar[0]) + "% der einzelnen Buchstaben korrekt reagiert.\n\nBitte strengen Sie sich mehr an!"
        feedback.setText(msg)
        fb_key.keys = []
        fb_key.rt = []
        fb_allKey = []
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