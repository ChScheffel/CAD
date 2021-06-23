#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Juni 23, 2021, at 16:55
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
    originPath='C:\\Users\\scheffel\\Scheffel\\Forschung\\A_Projects\\2021_COG-ER-ED\\COG-ER-ED\\01_Paradigms\\ER-ED\\ER_paradigm_lastrun.py',
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
    text='Willkommen!\n\nDas Experiment besteht aus zwei Teilen.\nIm ersten Teil werden Sie  Bilder betrachten und mittels verschiedener Strategien Ihre Emotionen regulieren.\n\nIm zweiten Teil werden Sie die verschiedenen Emotionsregulationsstrategien miteinander vergleichen.\n\nZum Forfahren Leertaste drücken.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
WelcomeResponse = keyboard.Keyboard()
# #################################
# Define correct numbe of Trials
# #################################
TotalTrialNr = 15  # 125 ?!
Trials_Block = 3 # 25

# #################################
# Randomize negative picture sets across negative Blocks
# #################################

# create a list of 4 negative blocks
Block_Order = list(range(1,5))
# randomize order
shuffle(Block_Order)



# Initialize components for Routine "Instruction_View"
Instruction_ViewClock = core.Clock()
text_ActiveViewing = visual.TextStim(win=win, name='text_ActiveViewing',
    text='ANSCHAUEN\n\nIn diesem Block werden Sie eine Reihe von Bildern sehen.\nDiese sollen Sie aufmerksam ansehen. Bitte reagieren\nSie natürlich auf die Bildinhalte ohne aufkommende \nEmotionen zu verändern!.\n\nZum Starten des Blocks bitte Leertaste drücken.',
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
text = visual.TextStim(win=win, name='text',
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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_reg_resp = keyboard.Keyboard()

# Initialize components for Routine "Pics_Reg_2"
Pics_Reg_2Clock = core.Clock()
image_reg = visual.ImageStim(
    win=win,
    name='image_reg', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1,0.75),
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
blocks_view = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks_view.xlsx'),
    seed=None, name='blocks_view')
thisExp.addLoop(blocks_view)  # add the loop to the experiment
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
    if blocks_view.thisN  == 1: # only second block
        conds_view_File = 'StimuliNegative_{}.xlsx'.format(Block_Order[0])
    
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
    blocks_view.addData('text_ActiveViewing.started', text_ActiveViewing.tStartRefresh)
    blocks_view.addData('text_ActiveViewing.stopped', text_ActiveViewing.tStopRefresh)
    # check responses
    if instr_view_resp.keys in ['', [], None]:  # No response was made
        instr_view_resp.keys = None
    blocks_view.addData('instr_view_resp.keys',instr_view_resp.keys)
    if instr_view_resp.keys != None:  # we had a response
        blocks_view.addData('instr_view_resp.rt', instr_view_resp.rt)
    blocks_view.addData('instr_view_resp.started', instr_view_resp.tStartRefresh)
    blocks_view.addData('instr_view_resp.stopped', instr_view_resp.tStopRefresh)
    # the Routine "Instruction_View" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_view = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conds_view_File),
        seed=None, name='trials_view')
    thisExp.addLoop(trials_view)  # add the loop to the experiment
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
        
        # ------Prepare to start Routine "Pics_View"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        image_view.setImage(ImageFile)
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
        while continueRoutine and routineTimer.getTime() > 0:
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
                image_view.setAutoDraw(True)
            if image_view.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_view.tStartRefresh + 3.0-frameTolerance:
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
        trials_view.addData('image_view.stopped', image_view.tStopRefresh)
        
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
        trials_view.addData('text.started', text.tStartRefresh)
        trials_view.addData('text.stopped', text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_view'
    
# completed 1.0 repeats of 'blocks_view'


# set up handler to look after randomisation of conditions etc
blocks_reg = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks_reg.xlsx'),
    seed=None, name='blocks_reg')
thisExp.addLoop(blocks_reg)  # add the loop to the experiment
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
    text_Instruction.setText(instr_1 + '\n\n' + 'In diesem Block werden Sie eine Reihe von Bildern sehen. Diese sollen Sie aufmerksam ansehen.' + instr_2 + '\n\n' + 'Zum Starten des Blocks Leertaste dürcken'
)
    instr_reg_resp.keys = []
    instr_reg_resp.rt = []
    _instr_reg_resp_allKeys = []
    if blocks_reg.thisN  == 0: # first block
        conds_reg_File = 'StimuliNegative_{}.xlsx'.format(Block_Order[1])
        
    elif blocks_reg.thisN  == 1: # second block
        conds_reg_File = 'StimuliNegative_{}.xlsx'.format(Block_Order[2])
    
    elif blocks_reg.thisN  == 2: # third block
        conds_reg_File = 'StimuliNegative_{}.xlsx'.format(Block_Order[3])
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
    blocks_reg.addData('text_Instruction.started', text_Instruction.tStartRefresh)
    blocks_reg.addData('text_Instruction.stopped', text_Instruction.tStopRefresh)
    # check responses
    if instr_reg_resp.keys in ['', [], None]:  # No response was made
        instr_reg_resp.keys = None
    blocks_reg.addData('instr_reg_resp.keys',instr_reg_resp.keys)
    if instr_reg_resp.keys != None:  # we had a response
        blocks_reg.addData('instr_reg_resp.rt', instr_reg_resp.rt)
    blocks_reg.addData('instr_reg_resp.started', instr_reg_resp.tStartRefresh)
    blocks_reg.addData('instr_reg_resp.stopped', instr_reg_resp.tStopRefresh)
    # the Routine "Instruction_Reg" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_reg = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conds_reg_File),
        seed=None, name='trials_reg')
    thisExp.addLoop(trials_reg)  # add the loop to the experiment
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
        
        # ------Prepare to start Routine "Pics_Reg_2"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        image_reg.setImage(ImageFile)
        # keep track of which components have finished
        Pics_Reg_2Components = [image_reg]
        for thisComponent in Pics_Reg_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Pics_Reg_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Pics_Reg_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Pics_Reg_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Pics_Reg_2Clock)
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
                image_reg.setAutoDraw(True)
            if image_reg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_reg.tStartRefresh + 3.0-frameTolerance:
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
            for thisComponent in Pics_Reg_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Pics_Reg_2"-------
        for thisComponent in Pics_Reg_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_reg.addData('image_reg.started', image_reg.tStartRefresh)
        trials_reg.addData('image_reg.stopped', image_reg.tStopRefresh)
        
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
        trials_reg.addData('text.started', text.tStartRefresh)
        trials_reg.addData('text.stopped', text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_reg'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks_reg'


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
