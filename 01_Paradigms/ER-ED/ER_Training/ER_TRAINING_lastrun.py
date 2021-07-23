#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Juli 23, 2021, at 14:08
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
    originPath='C:\\Users\\scheffel\\Scheffel\\Forschung\\A_Projects\\2021_COG-ER-ED\\COG-ER-ED\\01_Paradigms\\ER-ED\\ER_Training\\ER_TRAINING_lastrun.py',
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

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Willkommen!\n\nIn diesem Training sollen Sie drei Emotionsregulations-Strategien kennen lernen und diese erproben. Außerdem sollen Sie die verschiedenen Fragen am Ende jedes Blockes kennen lernen.\n\nWährend des Experimentes werden noch keine Messungen vorgenommen.\n\nZum Forfahren Leertaste drücken.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WelcomeResponse = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
text_instruction = visual.TextStim(win=win, name='text_instruction',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_view_resp = keyboard.Keyboard()

# Initialize components for Routine "Pics"
PicsClock = core.Clock()
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
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
    style='rating', styleTweaks=(), opacity=None,
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
    style='rating', styleTweaks=(), opacity=None,
    color='black', fillColor='black', borderColor='black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Das Training ist nun beendet.\n\nBitte wenden Sie sich an die Versuchsleitung!\n\nZum Beenden bitte Leertaste drücken.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_end = keyboard.Keyboard()

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

# set up handler to look after randomisation of conditions etc
blocks_training = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks_training.xlsx'),
    seed=None, name='blocks_training')
thisExp.addLoop(blocks_training)  # add the loop to the experiment
thisBlocks_training = blocks_training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_training.rgb)
if thisBlocks_training != None:
    for paramName in thisBlocks_training:
        exec('{} = thisBlocks_training[paramName]'.format(paramName))

for thisBlocks_training in blocks_training:
    currentLoop = blocks_training
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_training.rgb)
    if thisBlocks_training != None:
        for paramName in thisBlocks_training:
            exec('{} = thisBlocks_training[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_instruction.setText(instr_1 + '\n\n' + 'In diesem Block werden Sie eine Reihe von Bildern sehen. Diese sollen Sie aufmerksam ansehen.' + instr_2 + '\n\n' + instr_3 + '\n\n' + 'Zum Starten des Blocks Leertaste dürcken')
    instr_view_resp.keys = []
    instr_view_resp.rt = []
    _instr_view_resp_allKeys = []
    # keep track of which components have finished
    InstructionComponents = [text_instruction, instr_view_resp]
    for thisComponent in InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instruction"-------
    while continueRoutine:
        # get current time
        t = InstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_instruction* updates
        if text_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_instruction.frameNStart = frameN  # exact frame index
            text_instruction.tStart = t  # local t and not account for scr refresh
            text_instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_instruction, 'tStartRefresh')  # time at next scr refresh
            text_instruction.setAutoDraw(True)
        
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
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruction"-------
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks_training.addData('text_instruction.started', text_instruction.tStartRefresh)
    blocks_training.addData('text_instruction.stopped', text_instruction.tStopRefresh)
    # check responses
    if instr_view_resp.keys in ['', [], None]:  # No response was made
        instr_view_resp.keys = None
    blocks_training.addData('instr_view_resp.keys',instr_view_resp.keys)
    if instr_view_resp.keys != None:  # we had a response
        blocks_training.addData('instr_view_resp.rt', instr_view_resp.rt)
    blocks_training.addData('instr_view_resp.started', instr_view_resp.tStartRefresh)
    blocks_training.addData('instr_view_resp.stopped', instr_view_resp.tStopRefresh)
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conds_File),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Pics"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        image_view.setImage(ImageFile)
        # keep track of which components have finished
        PicsComponents = [image_view]
        for thisComponent in PicsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PicsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Pics"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PicsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PicsClock)
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
            for thisComponent in PicsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Pics"-------
        for thisComponent in PicsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('image_view.started', image_view.tStartRefresh)
        trials.addData('image_view.stopped', image_view.tStopRefresh)
        
        # ------Prepare to start Routine "fixcross"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixcrossComponents = [text]
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
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixcrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixcrossClock)
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
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
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
        trials.addData('text.started', text.tStartRefresh)
        trials.addData('text.stopped', text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # ------Prepare to start Routine "Slider_Arousal"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_arousal.reset()
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
    blocks_training.addData('text_slider_arousal.started', text_slider_arousal.tStartRefresh)
    blocks_training.addData('text_slider_arousal.stopped', text_slider_arousal.tStopRefresh)
    blocks_training.addData('slider_arousal.response', slider_arousal.getRating())
    blocks_training.addData('slider_arousal.rt', slider_arousal.getRT())
    blocks_training.addData('slider_arousal.started', slider_arousal.tStartRefresh)
    blocks_training.addData('slider_arousal.stopped', slider_arousal.tStopRefresh)
    # the Routine "Slider_Arousal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Slider_Effort"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_effort.reset()
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
    blocks_training.addData('text_slider_effort.started', text_slider_effort.tStartRefresh)
    blocks_training.addData('text_slider_effort.stopped', text_slider_effort.tStopRefresh)
    blocks_training.addData('slider_effort.response', slider_effort.getRating())
    blocks_training.addData('slider_effort.rt', slider_effort.getRT())
    blocks_training.addData('slider_effort.started', slider_effort.tStartRefresh)
    blocks_training.addData('slider_effort.stopped', slider_effort.tStopRefresh)
    # the Routine "Slider_Effort" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'blocks_training'


# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
# update component parameters for each repeat
resp_end.keys = []
resp_end.rt = []
_resp_end_allKeys = []
# keep track of which components have finished
EndScreenComponents = [text_end, resp_end]
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
    
    # *resp_end* updates
    waitOnFlip = False
    if resp_end.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        resp_end.frameNStart = frameN  # exact frame index
        resp_end.tStart = t  # local t and not account for scr refresh
        resp_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_end, 'tStartRefresh')  # time at next scr refresh
        resp_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_end.status == STARTED and not waitOnFlip:
        theseKeys = resp_end.getKeys(keyList=['space'], waitRelease=False)
        _resp_end_allKeys.extend(theseKeys)
        if len(_resp_end_allKeys):
            resp_end.keys = _resp_end_allKeys[-1].name  # just the last key pressed
            resp_end.rt = _resp_end_allKeys[-1].rt
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
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)
# check responses
if resp_end.keys in ['', [], None]:  # No response was made
    resp_end.keys = None
thisExp.addData('resp_end.keys',resp_end.keys)
if resp_end.keys != None:  # we had a response
    thisExp.addData('resp_end.rt', resp_end.rt)
thisExp.addData('resp_end.started', resp_end.tStartRefresh)
thisExp.addData('resp_end.stopped', resp_end.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
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
