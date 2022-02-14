# Script for preprocessing of questionnaire data

# load packages
library(targets)
library(readxl)
library(here)
library(dplyr)

# set top level directory to source file
here::i_am("flag_project_root_CERED.txt")

# import questionnaire data from RedCap
  
data_redcap <- read.csv(here("04_RawData", "pilot", "CERED_DATA.csv"),
                        stringsAsFactors = FALSE, header = TRUE,
                        na.strings = c("", "NA"))
colnames(data_redcap)[1] <- "set" # rename the first column

# remove unnecessary variables from questionnaire data frame
  
data_quest_raw <- data_redcap %>%
    subset(select = c(set, subject, age, gender, edu,
    nfc_01, nfc_02, nfc_03, nfc_04, nfc_05, nfc_06, nfc_07, nfc_08, nfc_09, nfc_10, nfc_11, nfc_12, nfc_13, nfc_14, nfc_15, nfc_16,
    bis11_01, bis11_02, bis11_03, bis11_04, bis11_05, bis11_06, bis11_07, bis11_08, bis11_09, bis11_10, bis11_11, bis11_12, bis11_13, bis11_14, bis11_15, bis11_16, bis11_17, bis11_18, bis11_19, bis11_20, bis11_21, bis11_22, bis11_23, bis11_24, bis11_25, bis11_26, bis11_27, bis11_28, bis11_29, bis11_30,
    bscs_1, bscs_2, bscs_3, bscs_4, bscs_5, bscs_6, bscs_7, bscs_8, bscs_9, bscs_10, bscs_11, bscs_12, bscs_13,
    srs_01, srs_02, srs_03, srs_04, srs_05, srs_06, srs_07, srs_08, srs_09, srs_10,
    erq_01, erq_02, erq_03, erq_04, erq_05, erq_06, erq_07, erq_08, erq_10,
    who5_1, who5_2, who5_3, who5_4, who5_5,
    acs_01, acs_02, acs_03, acs_04, acs_05, acs_06, acs_07, acs_08, acs_09, acs_10, acs_11, acs_12, acs_13, acs_14, acs_15, acs_16, acs_17, acs_18, acs_19, acs_20,
    risc_01, risc_04, risc_06, risc_07, risc_08, risc_11, risc_14, risc_16, risc_17, risc_19,
    flexer_01, flexer_02, flexer_03, flexer_04, flexer_05, flexer_06, flexer_07, flexer_08, flexer_09, flexer_10,
    layb_01, layb_02, layb_03, layb_04))

# built new data frame without empty rows

data_quest <- data_redcap %>%
    subset(!is.na(subject), select = c(subject, age, gender, edu))

# compute questionnaire scores for all participants


# save data frame

write.csv(data_quest, here("04_RawData", "pilot", "ER-ED", "dfs","df_quest.csv"), row.names = FALSE)
