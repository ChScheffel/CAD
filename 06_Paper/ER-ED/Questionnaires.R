# Script for preprocessing of questionnaire data

# load packages
library(targets)
library(readxl)
library(here)

# set top level directory to source file
here::i_am("flag_project_root_CERED.txt")

# import questionnaire data from RedCap
  
data_redcap <- read.csv(here("04_RawData", "pilot", "CERED_DATA.csv"),
                        stringsAsFactors = FALSE, header = TRUE)
colnames(data_redcap)[1] <- "set" # rename the first column

# remove unnecessary variables from questionnaire data frame
  
data_quest <- subset(data_REDCap, 
                    select = c(subject, age, gender, edu,
                               nfc_01, nfc_02, nfc_03, nfc_04, nfc_05, nfc_06, nfc_07, nfc_08, nfc_09, nfc_10, nfc_11, nfc_12, nfc_13, nfc_14, nfc_15, nfc_16,
                               bis11_01, bis11_02, bis11_03, bis11_04, bis11_05, bis11_06, bis11_07, bis11_08, bis11_09, bis11_10, bis11_11, bis11_12, bis11_13, bis11_14, bis11_15, bis11_16, bis11_17, bis11_18, bis11_19, bis11_20, bis11_21, bis11_22, bis11_23, bis11_24, bis11_25, bis11_26, bis11_27, bis11_28, bis11_29, bis11_30))