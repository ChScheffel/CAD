# R Script for Analysis of CERED T2

# Open relevant packages
library(targets)    # to keep track of all relevant files
library(readxl)     # import excel files
library(here)       # to set directories without defined paths
library(papaja)     # APA conform output
library(afex)       # for ANOVA
library(emmeans)
library(ggplot2)    # for nice plots
library(dplyr)
library(BayesFactor)
library(effectsize)

# set top level directory to source file
here::i_am("flag_project_root_CERED.txt")