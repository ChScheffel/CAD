######################################################
# R Script for analyses of the Registered Report
# "Estimating individual subjective values of emotion regulation strategies"
# Scheffel, C., Zerna, J., Gärtner, A., Dörfel, D., & Strobel, A. (2022)
#
# Christoph Scheffel
# (christoph_scheffel@tu-dresden.de)
#
######################################################

#################### SETUP ###########################

# Open relevant packages

library(here)       # to set directories without defined paths

# set top level directory to source file
here::i_am("flag_project_root_CERED.txt")

library(papaja)     # APA conform output
library(afex)       # for ANOVA
library(emmeans)
library(ggplot2)    # for nice plots
library(dplyr)
library(BayesFactor)
library(effectsize)
library(targets)    # to keep track of all relevant files
library(readxl)     # import excel files

##################### DATA IMPORT #######################

