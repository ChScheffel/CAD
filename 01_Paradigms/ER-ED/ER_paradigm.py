#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Juni 22, 2021, at 16:11
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
expName = 'ER_paradigm'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\scheffel\\Scheffel\\Forschung\\A_Projects\\2021_emotED\\CogEmotED\\01_Paradigms\\ER-ED\\ER_paradigm.py',
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
    size=[1536, 864], fullscr=True, screen=1, 
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
WelcomeText = visual.TextBox2(
     win, text='Willkommen!\n\nDas Experiment besteht aus zwei Teilen.\nIm ersten Teil werden Sie  Bilder betrachten und mittels verschiedener Strategien Ihre Emotionen regulieren.\n\nIm zweiten Teil werden Sie die verschiedenen Emotionsregulationsstrategien miteinander vergleichen.\n\nZum Forfahren <b>Leertaste</b> drücken.', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     #alignment='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='WelcomeText',
     autoLog=True,
     )
WelcomeResponse = keyboard.Keyboard()

# Initialize components for Routine "instr_ActiveViewing"
instr_ActiveViewingClock = core.Clock()
text_ActiveViewing = visual.TextBox2(
     win, text='<b>ANSCHAUEN!</b>\n\nIn diesem Block werden Sie eine Reihe von Bildern sehen. Diese sollen Sie aufmerksam ansehen. Bitte reagieren Sie natürlich auf die Bildinhalte ohne aufkommende Emotionen zu verändern!\n\nZum Starten des Experiments bitte rechte Taste drücken.', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='text_ActiveViewing',
     autoLog=True,
)
instr_ActiveViewing_resp = keyboard.Keyboard()

# Initialize components for Routine "Stimuli"
StimuliClock = core.Clock()
stimuli_neutral = visual.ImageStim(
    win=win,
    name='stimuli_neutral', 
    image='Stimuli\\\\001.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fix_cross = visual.TextStim(win=win, name='fix_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
WelcomeResponse.keys = []
WelcomeResponse.rt = []
_WelcomeResponse_allKeys = []
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
thisExp.addData('WelcomeText.started', WelcomeText.tStartRefresh)
thisExp.addData('WelcomeText.stopped', WelcomeText.tStopRefresh)
# check responses
if WelcomeResponse.keys in ['', [], None]:  # No response was made
    WelcomeResponse.keys = None
thisExp.addData('WelcomeResponse.keys',WelcomeResponse.keys)
if WelcomeResponse.keys != None:  # we had a response
    thisExp.addData('WelcomeResponse.rt', WelcomeResponse.rt)
thisExp.addData('WelcomeResponse.started', WelcomeResponse.tStartRefresh)
thisExp.addData('WelcomeResponse.stopped', WelcomeResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_ActiveViewing"-------
continueRoutine = True
# update component parameters for each repeat
instr_ActiveViewing_resp.keys = []
instr_ActiveViewing_resp.rt = []
_instr_ActiveViewing_resp_allKeys = []
# keep track of which components have finished
instr_ActiveViewingComponents = [text_ActiveViewing, instr_ActiveViewing_resp]
for thisComponent in instr_ActiveViewingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_ActiveViewingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_ActiveViewing"-------
while continueRoutine:
    # get current time
    t = instr_ActiveViewingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_ActiveViewingClock)
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
        text_ActiveViewing.setAutoDraw(True)
    
    # *instr_ActiveViewing_resp* updates
    waitOnFlip = False
    if instr_ActiveViewing_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        instr_ActiveViewing_resp.frameNStart = frameN  # exact frame index
        instr_ActiveViewing_resp.tStart = t  # local t and not account for scr refresh
        instr_ActiveViewing_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_ActiveViewing_resp, 'tStartRefresh')  # time at next scr refresh
        instr_ActiveViewing_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_ActiveViewing_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_ActiveViewing_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_ActiveViewing_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr_ActiveViewing_resp.getKeys(keyList=['space'], waitRelease=False)
        _instr_ActiveViewing_resp_allKeys.extend(theseKeys)
        if len(_instr_ActiveViewing_resp_allKeys):
            instr_ActiveViewing_resp.keys = _instr_ActiveViewing_resp_allKeys[-1].name  # just the last key pressed
            instr_ActiveViewing_resp.rt = _instr_ActiveViewing_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_ActiveViewingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_ActiveViewing"-------
for thisComponent in instr_ActiveViewingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_ActiveViewing.started', text_ActiveViewing.tStartRefresh)
thisExp.addData('text_ActiveViewing.stopped', text_ActiveViewing.tStopRefresh)
# check responses
if instr_ActiveViewing_resp.keys in ['', [], None]:  # No response was made
    instr_ActiveViewing_resp.keys = None
thisExp.addData('instr_ActiveViewing_resp.keys',instr_ActiveViewing_resp.keys)
if instr_ActiveViewing_resp.keys != None:  # we had a response
    thisExp.addData('instr_ActiveViewing_resp.rt', instr_ActiveViewing_resp.rt)
thisExp.addData('instr_ActiveViewing_resp.started', instr_ActiveViewing_resp.tStartRefresh)
thisExp.addData('instr_ActiveViewing_resp.stopped', instr_ActiveViewing_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_ActiveViewing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stimuli"-------
continueRoutine = True
routineTimer.add(10.500000)
# update component parameters for each repeat
# keep track of which components have finished
StimuliComponents = [stimuli_neutral, fix_cross]
for thisComponent in StimuliComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Stimuli"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = StimuliClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StimuliClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stimuli_neutral* updates
    if stimuli_neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stimuli_neutral.frameNStart = frameN  # exact frame index
        stimuli_neutral.tStart = t  # local t and not account for scr refresh
        stimuli_neutral.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stimuli_neutral, 'tStartRefresh')  # time at next scr refresh
        stimuli_neutral.setAutoDraw(True)
    if stimuli_neutral.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > stimuli_neutral.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            stimuli_neutral.tStop = t  # not accounting for scr refresh
            stimuli_neutral.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stimuli_neutral, 'tStopRefresh')  # time at next scr refresh
            stimuli_neutral.setAutoDraw(False)
    
    # *fix_cross* updates
    if fix_cross.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
        # keep track of start time/frame for later
        fix_cross.frameNStart = frameN  # exact frame index
        fix_cross.tStart = t  # local t and not account for scr refresh
        fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
        fix_cross.setAutoDraw(True)
    if fix_cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix_cross.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            fix_cross.tStop = t  # not accounting for scr refresh
            fix_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StimuliComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stimuli"-------
for thisComponent in StimuliComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stimuli_neutral.started', stimuli_neutral.tStartRefresh)
thisExp.addData('stimuli_neutral.stopped', stimuli_neutral.tStopRefresh)
thisExp.addData('fix_cross.started', fix_cross.tStartRefresh)
thisExp.addData('fix_cross.stopped', fix_cross.tStopRefresh)

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
