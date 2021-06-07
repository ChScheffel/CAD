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

# Initialize components for Routine "Instruction1back"
Instruction1backClock = core.Clock()
InstructionText = visual.TextStim(win=win, name='InstructionText',
    text='1-back\n\nIhnen werden nun nacheinander Buchstaben auf dem Bildschirm präsentiert. Wenn der aktuelle Buchstabe der gleiche ist wie der, der direkt davor präsentiert wurde, dann drücken Sie bitte die rechte Pfeiltaste. Wenn es nicht der gleiche Buchstabe ist, drücken sie bitte die linke Pfeiltaste.\nReagieren Sie bei jedem Konsonanten bitte so schnell und richtig wie möglich.\n\nrechts = gleicher Buchstabe wie zuvor\nlinks = nicht der gleiche Buchstabe wie zuvor\n\nDrücken Sie die Leertaste, um zu beginnen.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Instruction1Key = keyboard.Keyboard()

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Courier New',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Trial_oneback_run1"
Trial_oneback_run1Clock = core.Clock()
trial_1back_run1 = visual.TextStim(win=win, name='trial_1back_run1',
    text='',
    font='Courier New',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_1back_run1_resp = keyboard.Keyboard()

# Initialize components for Routine "Feedback_1back_run1"
Feedback_1back_run1Clock = core.Clock()
msg='doh!'#if this comes up we forgot to update the msg!
fb_1back_run1 = visual.TextStim(win=win, name='fb_1back_run1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fb_key_1_1 = keyboard.Keyboard()

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

# ------Prepare to start Routine "Instruction1back"-------
continueRoutine = True
# update component parameters for each repeat
Instruction1Key.keys = []
Instruction1Key.rt = []
_Instruction1Key_allKeys = []
# keep track of which components have finished
Instruction1backComponents = [InstructionText, Instruction1Key]
for thisComponent in Instruction1backComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruction1backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruction1back"-------
while continueRoutine:
    # get current time
    t = Instruction1backClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruction1backClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionText* updates
    if InstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionText.frameNStart = frameN  # exact frame index
        InstructionText.tStart = t  # local t and not account for scr refresh
        InstructionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionText, 'tStartRefresh')  # time at next scr refresh
        InstructionText.setAutoDraw(True)
    
    # *Instruction1Key* updates
    waitOnFlip = False
    if Instruction1Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction1Key.frameNStart = frameN  # exact frame index
        Instruction1Key.tStart = t  # local t and not account for scr refresh
        Instruction1Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction1Key, 'tStartRefresh')  # time at next scr refresh
        Instruction1Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instruction1Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instruction1Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instruction1Key.status == STARTED and not waitOnFlip:
        theseKeys = Instruction1Key.getKeys(keyList=['space'], waitRelease=False)
        _Instruction1Key_allKeys.extend(theseKeys)
        if len(_Instruction1Key_allKeys):
            Instruction1Key.keys = _Instruction1Key_allKeys[-1].name  # just the last key pressed
            Instruction1Key.rt = _Instruction1Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction1backComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction1back"-------
for thisComponent in Instruction1backComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction1back" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
oneback_run1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('..\\\\..\\\\..\\\\Stimuli\\\\ForTestingTheParadigm.xlsx'),
    seed=None, name='oneback_run1')
thisExp.addLoop(oneback_run1)  # add the loop to the experiment
thisOneback_run1 = oneback_run1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOneback_run1.rgb)
if thisOneback_run1 != None:
    for paramName in thisOneback_run1:
        exec('{} = thisOneback_run1[paramName]'.format(paramName))

for thisOneback_run1 in oneback_run1:
    currentLoop = oneback_run1
    # abbreviate parameter names if possible (e.g. rgb = thisOneback_run1.rgb)
    if thisOneback_run1 != None:
        for paramName in thisOneback_run1:
            exec('{} = thisOneback_run1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationCrossComponents = [fixcross]
    for thisComponent in FixationCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationCrossClock)
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
            if tThisFlipGlobal > fixcross.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                fixcross.tStop = t  # not accounting for scr refresh
                fixcross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    oneback_run1.addData('fixcross.started', fixcross.tStartRefresh)
    oneback_run1.addData('fixcross.stopped', fixcross.tStopRefresh)
    
    # ------Prepare to start Routine "Trial_oneback_run1"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    trial_1back_run1.setText(Letter)
    trial_1back_run1_resp.keys = []
    trial_1back_run1_resp.rt = []
    _trial_1back_run1_resp_allKeys = []
    # keep track of which components have finished
    Trial_oneback_run1Components = [trial_1back_run1, trial_1back_run1_resp]
    for thisComponent in Trial_oneback_run1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_oneback_run1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_oneback_run1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Trial_oneback_run1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_oneback_run1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_1back_run1* updates
        if trial_1back_run1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_1back_run1.frameNStart = frameN  # exact frame index
            trial_1back_run1.tStart = t  # local t and not account for scr refresh
            trial_1back_run1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_1back_run1, 'tStartRefresh')  # time at next scr refresh
            trial_1back_run1.setAutoDraw(True)
        if trial_1back_run1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_1back_run1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                trial_1back_run1.tStop = t  # not accounting for scr refresh
                trial_1back_run1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_1back_run1, 'tStopRefresh')  # time at next scr refresh
                trial_1back_run1.setAutoDraw(False)
        
        # *trial_1back_run1_resp* updates
        waitOnFlip = False
        if trial_1back_run1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_1back_run1_resp.frameNStart = frameN  # exact frame index
            trial_1back_run1_resp.tStart = t  # local t and not account for scr refresh
            trial_1back_run1_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_1back_run1_resp, 'tStartRefresh')  # time at next scr refresh
            trial_1back_run1_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_1back_run1_resp.clock.reset)  # t=0 on next screen flip
        if trial_1back_run1_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_1back_run1_resp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                trial_1back_run1_resp.tStop = t  # not accounting for scr refresh
                trial_1back_run1_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_1back_run1_resp, 'tStopRefresh')  # time at next scr refresh
                trial_1back_run1_resp.status = FINISHED
        if trial_1back_run1_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_1back_run1_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _trial_1back_run1_resp_allKeys.extend(theseKeys)
            if len(_trial_1back_run1_resp_allKeys):
                trial_1back_run1_resp.keys = _trial_1back_run1_resp_allKeys[0].name  # just the first key pressed
                trial_1back_run1_resp.rt = _trial_1back_run1_resp_allKeys[0].rt
                # was this correct?
                if (trial_1back_run1_resp.keys == str(CorrAnswer)) or (trial_1back_run1_resp.keys == CorrAnswer):
                    trial_1back_run1_resp.corr = 1
                else:
                    trial_1back_run1_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_oneback_run1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_oneback_run1"-------
    for thisComponent in Trial_oneback_run1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    oneback_run1.addData('trial_1back_run1.started', trial_1back_run1.tStartRefresh)
    oneback_run1.addData('trial_1back_run1.stopped', trial_1back_run1.tStopRefresh)
    # check responses
    if trial_1back_run1_resp.keys in ['', [], None]:  # No response was made
        trial_1back_run1_resp.keys = None
        # was no response the correct answer?!
        if str(CorrAnswer).lower() == 'none':
           trial_1back_run1_resp.corr = 1;  # correct non-response
        else:
           trial_1back_run1_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for oneback_run1 (TrialHandler)
    oneback_run1.addData('trial_1back_run1_resp.keys',trial_1back_run1_resp.keys)
    oneback_run1.addData('trial_1back_run1_resp.corr', trial_1back_run1_resp.corr)
    if trial_1back_run1_resp.keys != None:  # we had a response
        oneback_run1.addData('trial_1back_run1_resp.rt', trial_1back_run1_resp.rt)
    oneback_run1.addData('trial_1back_run1_resp.started', trial_1back_run1_resp.tStartRefresh)
    oneback_run1.addData('trial_1back_run1_resp.stopped', trial_1back_run1_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'oneback_run1'


# ------Prepare to start Routine "Feedback_1back_run1"-------
continueRoutine = True
# update component parameters for each repeat
nCorr = oneback_run1.data['trial_1back_run1_resp.corr'].sum() # number of correct trials
pCorr = (nCorr*100)/64 # percentage of correct trials
pCorr = round(pCorr, 1) # round the percentage to 1 number after the decimal point

nCorrTarArray = oneback_run1.data['trial_1back_run1_resp.keys'] # extract response data
nCorrTarFilter = nCorrTarArray == 'right' # index the data of the targets
nCorrTar = sum(nCorrTarFilter) # calculate sum of correct targets aka sum of TRUE output of the filter
pCorrTar = (nCorrTar*100)/16 # percentage of correct targets
pCorrTar = np.around(pCorrTar, 1) # round the percentage to the decimal point

nCorrNonTarArray = oneback_run1.data['trial_1back_run1_resp.keys'] # extract response data
nCorrNonTarFilter = nCorrNonTarArray == 'left' # index the data of the non-targets
nCorrNonTar = sum(nCorrNonTarFilter) # calculate sum of correct non-targets aka sum of TRUE output of the filter
pCorrNonTar = (nCorrNonTar*100)/48 # percentage of correct non-targets
pCorrNonTar = np.around(pCorrNonTar, 1) # round the percentage to the decimal point

if pCorrTar >= 50 and pCorrNonTar >= 50:
    msg = "In diesem Block haben Sie auf " + str(pCorrTar[0]) + "% der sich wiederholenden und auf " + str(pCorrNonTar[0]) + "% der einzelnen Buchstaben korrekt reagiert.\n\nWeiter so!"
else:
    msg = "In diesem Block haben Sie auf " + str(pCorrTar[0]) + "% der sich wiederholenden und auf " + str(pCorrNonTar[0]) + "% der einzelnen Buchstaben korrekt reagiert.\n\nBitte strengen Sie sich mehr an!"
fb_1back_run1.setText(msg)
fb_key_1_1.keys = []
fb_key_1_1.rt = []
_fb_key_1_1_allKeys = []
# keep track of which components have finished
Feedback_1back_run1Components = [fb_1back_run1, fb_key_1_1]
for thisComponent in Feedback_1back_run1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Feedback_1back_run1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Feedback_1back_run1"-------
while continueRoutine:
    # get current time
    t = Feedback_1back_run1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Feedback_1back_run1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fb_1back_run1* updates
    if fb_1back_run1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fb_1back_run1.frameNStart = frameN  # exact frame index
        fb_1back_run1.tStart = t  # local t and not account for scr refresh
        fb_1back_run1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fb_1back_run1, 'tStartRefresh')  # time at next scr refresh
        fb_1back_run1.setAutoDraw(True)
    
    # *fb_key_1_1* updates
    waitOnFlip = False
    if fb_key_1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fb_key_1_1.frameNStart = frameN  # exact frame index
        fb_key_1_1.tStart = t  # local t and not account for scr refresh
        fb_key_1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fb_key_1_1, 'tStartRefresh')  # time at next scr refresh
        fb_key_1_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fb_key_1_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fb_key_1_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fb_key_1_1.status == STARTED and not waitOnFlip:
        theseKeys = fb_key_1_1.getKeys(keyList=['space'], waitRelease=False)
        _fb_key_1_1_allKeys.extend(theseKeys)
        if len(_fb_key_1_1_allKeys):
            fb_key_1_1.keys = _fb_key_1_1_allKeys[-1].name  # just the last key pressed
            fb_key_1_1.rt = _fb_key_1_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Feedback_1back_run1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Feedback_1back_run1"-------
for thisComponent in Feedback_1back_run1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Feedback_1back_run1" was not non-slip safe, so reset the non-slip timer
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
