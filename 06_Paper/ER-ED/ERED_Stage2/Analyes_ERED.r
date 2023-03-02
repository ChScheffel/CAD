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
here::i_am("flag_project_root_CAD.txt")

library(renv)
renv::activate(here("06_Paper", "ER-ED", "ERED_Stage2"))
renv::restore(here("06_Paper", "ER-ED", "ERED_Stage2"))

######################################################

#################### PACKAGES ########################
library(tidyverse)

#################### MAIN ############################

#################### DATA IMPORT #####################

# import ER ratings and ER discounting data into lists

datalist_ER <- lapply(list.files(here("04_RawData", "main", "ER-ED/logfiles"),
                                       pattern = "*_ER.*csv", full.names = TRUE),
                            read.csv, stringsAsFactors = FALSE,
                            header = TRUE)

# rename participants with wrong codes
datalist_ER[[90]][["participant"]] <- "O27K03"
datalist_ER[[75]][["participant"]] <- "L29R12"

datalist_ED <- lapply(list.files(here("04_RawData", "main", "ER-ED/logfiles"),
                                       pattern = "*_ED.*csv", full.names = TRUE),
                            read.csv, stringsAsFactors = FALSE,
                            header = TRUE)

datalist_ED[[90]][["participant"]] <- "O27K03"
datalist_ED[[75]][["participant"]] <- "L29R12"

# new empty frame to store files into
data_ER <- data.frame(ID = character(), block = character(),
                            arousal = double(), effort = double(), utility = double(),
                            trigger = double(), trigger_reg = double())

data_ED <- data.frame(ID = character(), step = double(),
                            choice = character(), LBvalue = double(),
                            LBstrat = double(), RBvalue = double(),
                            RBstrat = double())

data_choice <- data.frame(ID = character(), choice = double())

# store arousal, effort, and utility ratings in data_ER frame
for (i in seq_len(length(datalist_ER))) {
  tmp <- data.frame(datalist_ER[[i]][["participant"]],
                    datalist_ER[[i]][["instr_1"]],
                    datalist_ER[[i]][["slider_arousal.response"]],
                    datalist_ER[[i]][["slider_effort.response"]],
                    if (is.null(datalist_ER[[i]][["slider_utility.response"]])) {
                      NA
                    } else {
                      datalist_ER[[i]][["slider_utility.response"]]
                    },
                    datalist_ER[[i]][["TriggerBlockView"]],
                    datalist_ER[[i]][["TriggerBlockReg"]])
  colnames(tmp) <- names(data_ER)
  tmp <- tmp[(!is.na(tmp$arousal)), ]
  
  data_ER <- rbind(data_ER, tmp)
}

rownames(data_ER) <- seq_len(nrow(data_ER))

# loop to store trigger in one column

for (i in seq_len(nrow(data_ER))) {
  if (is.na(data_ER$trigger[i])) {
    data_ER$trigger[i] <- data_ER$trigger_reg[i]
  }
  
  if (is.na(data_ER$trigger[i])) {
    data_ER$trigger[i] <- 26
  }
}

# delete old column

data_ER$trigger_reg <- NULL

# loop to correct block indicator

data_ER$block[data_ER$trigger == 21] <- "1_view_neu"
data_ER$block[data_ER$trigger == 22] <- "2_view_neg"
data_ER$block[data_ER$trigger == 23] <- "3_distraction"
data_ER$block[data_ER$trigger == 24] <- "4_distancing"
data_ER$block[data_ER$trigger == 25] <- "5_suppression"
data_ER$block[data_ER$trigger == 26] <- "6_choice"

# create new variable with correct wording for strategy
data_ER$strategy[data_ER$block == "1_view_neu"] <- "view_neutral"
data_ER$strategy[data_ER$block == "2_view_neg"] <- "view_negative"
data_ER$strategy[data_ER$block == "3_distraction"] <- "distraction"
data_ER$strategy[data_ER$block == "4_distancing"] <- "distancing"
data_ER$strategy[data_ER$block == "5_suppression"] <- "suppression"
data_ER$strategy[data_ER$block == "6_choice"] <- "choice"

# store ER choice in data_choice frame

for (i in seq_len(length(datalist_ER))) {
  tmp <- data.frame(datalist_ER[[i]][["participant"]],
                    datalist_ER[[i]][["resp_choice.keys"]])
  colnames(tmp) <- names(data_choice)
  tmp <- tmp[(!is.na(tmp$choice)), ]
  
  data_choice <- rbind(data_choice, tmp)
}

# store ED data in data_ED frame
for (i in seq_len(length(datalist_ED))) {
  tmp <- data.frame(datalist_ED[[i]][["participant"]][2:length(datalist_ED[[i]][["participant"]])],
                   datalist_ED[[i]][["EDround.thisN"]][2:length(datalist_ED[[i]][["EDround.thisN"]])],
                   datalist_ED[[i]][["EDclick.clicked_name"]][2:length(datalist_ED[[i]][["EDclick.clicked_name"]])],
                   datalist_ED[[i]][["EDleftbutton.value"]][2:length(datalist_ED[[i]][["EDleftbutton.value"]])],
                   datalist_ED[[i]][["EDleftbutton.strat"]][2:length(datalist_ED[[i]][["EDleftbutton.strat"]])],
                   datalist_ED[[i]][["EDrightbutton.value"]][2:length(datalist_ED[[i]][["EDrightbutton.value"]])],
                   datalist_ED[[i]][["EDrightbutton.strat"]][2:length(datalist_ED[[i]][["EDrightbutton.strat"]])])
  colnames(tmp) <- names(data_ED)
  data_ED <- rbind(data_ED, tmp)
}

base::remove(tmp)

# import EMG data

datalist_EMG <- lapply(list.files(here("04_RawData", "main", "ER-ED", "EMG", "export"),
                                        pattern = "*_Peaks.txt", full.names = TRUE),
                            read.table, stringsAsFactors = FALSE, header = TRUE)
datalist_EMG_Marker <- lapply(list.files(here("04_RawData", "main", "ER-ED", "EMG", "export"),
                                              pattern = "*.Markers", full.names = TRUE),
                                   read.table, stringsAsFactors = FALSE, header = TRUE,
                                   skip = 1, row.names = NULL, sep = ",")

# new empty frame to store files into
data_EMG <- data.frame(ID = character(), trigger = double(), Corr = double(), Lev = double())

# store EMG data in data_EMG frame
for (i in seq_len(length(datalist_EMG))) {
 tmp <- data.frame(datalist_EMG[[i]][["Filename"]],
                   datalist_EMG_Marker[[i]][["Description"]],
                   datalist_EMG[[i]][["T0T6000Corr.ASNM"]],
                   datalist_EMG[[i]][["T0T6000Lev.ASNM"]])
 colnames(tmp) <- names(data_EMG)
 
 data_EMG <- rbind(data_EMG, tmp)
}

base::remove(tmp)

# create variable "block"

data_EMG$block[data_EMG$trigger == " S 21"] <- "1_view_neu"
data_EMG$block[data_EMG$trigger == " S 22"] <- "2_view_neg"
data_EMG$block[data_EMG$trigger == " S 23"] <- "3_distraction"
data_EMG$block[data_EMG$trigger == " S 24"] <- "4_distancing"
data_EMG$block[data_EMG$trigger == " S 25"] <- "5_suppression"
data_EMG$block[data_EMG$trigger == " S 26"] <- "6_choice"


# import questionnaire data from RedCap

data_survey <- read.csv(here("04_RawData", "main", "Questionnaire_Data_Full_Version.csv"),
                              stringsAsFactors = FALSE, header = TRUE,
                              na.strings = c("", "NA"))
colnames(data_survey)[1] <- "set" # rename the first column

# tidy up data frame:
# fill subject id in each row and collapse arms into one row per participant

data_survey <- data_survey %>% 
  data.table::as.data.table() %>% 
  replace(is.na(data_survey), "")

data_survey <- data_survey[, lapply(.SD, paste0 , collapse=""), by=set]

data_survey <- as.data.frame(data_survey)

#################### QUALITY CONTROL #################################

# remove participants that misunderstood instructions
# none
# remove participants with distorted EMG recordings
# T14G09 F14A01

data_ER <- data_ER[!data_ER$ID == "T14G09",]
data_choice <- data_choice[!data_choice$ID == "T14G09",]

data_ED <- data_ED[!data_ED$ID == "T14G09",]

data_EMG <- data_EMG[!data_EMG$ID == "T14G09",]


# sets 2, 6, and 7 were dummy sets to test NASA TLX iterations (T1)

data_survey <- data_survey[!(data_survey$set == "2_final" | data_survey$set == "6_final" | data_survey$set == "7_final" | data_survey$set == "2" | data_survey$set == "6" | data_survey$set == "7"), ]

#### EMG DATA: EXCLUDE OUTLIER
# within participants but across conditions
# Exclude trials that are above 1.5 inter-quartile ranges above the third quartile of the mean

EMG.stats <- data_EMG %>% group_by(ID) %>% summarize(stats::IQR(Corr), stats::quantile(Corr, probs = 0.25, na.rm = TRUE), stats::quantile(Corr, probs = 0.75, na.rm = TRUE),
                                                     stats::IQR(Lev), stats::quantile(Lev, probs = 0.25, na.rm = TRUE), stats::quantile(Lev, probs = 0.75, na.rm = TRUE))

EMG.stats <- as.data.frame(EMG.stats)
colnames(EMG.stats) <- c("ID", "IQR.Corr", "FirstQ.Corr", "ThirdQ.Corr", "IQR.Lev", "FirstQ.Lev", "ThirdQ.Lev")

# compute upper and lower boundary
EMG.stats$Corr.ab <- EMG.stats$ThirdQ.Corr + 1.5 * EMG.stats$IQR.Corr
EMG.stats$Corr.bel <- EMG.stats$FirstQ.Corr - 1.5 * EMG.stats$IQR.Corr
EMG.stats$Lev.ab <- EMG.stats$ThirdQ.Lev + 1.5 * EMG.stats$IQR.Lev
EMG.stats$Lev.bel <- EMG.stats$FirstQ.Lev - 1.5 * EMG.stats$IQR.Lev

EMG.outlier <- data.frame(outlier = double())

# create new data frame
data_EMG.new <- data.frame()

# loop for each participant

for (i in seq_len(length(EMG.stats$ID))) {
  
  tmp.Corr <- which(data_EMG$Corr[data_EMG$ID == EMG.stats$ID[i]] > EMG.stats$Corr.ab[i] | data_EMG$Corr[data_EMG$ID == EMG.stats$ID[i]] < EMG.stats$Corr.bel[i])
  tmp.Lev <- which(data_EMG$Lev[data_EMG$ID == EMG.stats$ID[i]] > EMG.stats$Lev.ab[i] | data_EMG$Lev[data_EMG$ID == EMG.stats$ID[i]] < EMG.stats$Lev.bel[i])
  
  tmp.unique <- unique(tmp.Corr,tmp.Lev)
  
  tmp.new <- data_EMG[data_EMG$ID == EMG.stats$ID[i],]
  tmp.new <- tmp.new[-tmp.unique,]
  
  data_EMG.new <- rbind(data_EMG.new, tmp.new)
  
}

base::remove(tmp.Corr, tmp.Lev, tmp.unique, tmp.new)


#################### DESCRIBE DATA ################################# 
# describe when data acquisition took place

acqui_time <- data.frame(dates = c(t(data_survey[,grep("time", colnames(data_survey))])), stringsAsFactors = FALSE)
acqui_time <- data.frame(dates = acqui_time[!(acqui_time$dates == ""),])
acqui_time <- as.Date(acqui_time$dates, format = "%d.%m.%Y %H:%M")
acqui_time <- range(acqui_time, na.rm = TRUE)

# now remove the original data sets (which we needed for the time stamps) and keep only the edited sets

data_survey <- data_survey[grep("_final", data_survey$set), ]

# remove the "_final" in set name
data_survey$set <- gsub("_final", "", data_survey$set)

#################### PREPARATION: QUESTIONNAIRES #####################

# built new data frame with every participant that started the online survey

data_quest <- data_survey %>%
  subset(!is.na(subject_id_quest), select = c(set, subject_id_quest, subject_id_lab, record_id_2, age, gender, edu))

data_quest[, c(5:7)] <- sapply(data_quest[, c(5:7)], as.numeric)

#### Need For Cognition Scale - NFC

# store nfc items in separate df
# only keep rows with complete nfc questionnaire
nfc_items <- data_survey %>% 
  subset(select = c(set,
                    grep("nfc", colnames(data_survey)))) %>% 
  dplyr::filter((nfc_complete == 2) )

# delete column "nfc_timestamp"
nfc_items$nfc_timestamp <- NULL

# change columns to numeric
nfc_items <- dplyr::mutate_all(nfc_items, function(x) as.numeric(as.character(x)))

# recode nfc items
nfc_items[,c("nfc_04","nfc_06","nfc_07","nfc_08","nfc_09","nfc_10","nfc_11","nfc_12","nfc_15","nfc_16")] <- nfc_items[,c("nfc_04","nfc_06","nfc_07","nfc_08","nfc_09","nfc_10","nfc_11","nfc_12","nfc_15","nfc_16")]*-1

# summary score 
nfc_items$nfc_sum <- rowSums(nfc_items %>% dplyr::select("nfc_01":"nfc_16"))

# fit nfc sum score in df data_quest
data_quest <- merge(data_quest, nfc_items[,c("set","nfc_sum")], by = "set")

#### Flexible Emotion Regulation Scale - FlexER

# store flexer items in separate df
# only keep rows with complete flexer questionnaire
flexer_items <- data_survey %>% 
  subset(select = c(set,
                    grep("flexer", colnames(data_survey)))) %>% 
  dplyr::filter((flexer_complete == 2))

# delete column "flexer_timestamp"
flexer_items$flexer_timestamp <- NULL

# change all columns to numeric
flexer_items <- dplyr::mutate_all(flexer_items, function(x) as.numeric(as.character(x)))

# recode item 7
flexer_items[,"flexer_07"] <- 5 - flexer_items[,"flexer_07"]

# mean score
flexer_items$flexer_mean <- rowMeans(flexer_items %>% dplyr::select("flexer_01":"flexer_10"))

# fit flexer mean score in df data_quest
data_quest <- merge(data_quest, flexer_items[,c("set","flexer_mean")], by = "set")

#### Barratt Impulsiveness Scale - BIS-11

# store bis11 items in separate df
# only keep rows with complete bis11 questionnaire
bis11_items <- data_survey %>% 
  subset(select = c(set,
                    grep("bis", colnames(data_survey)))) %>% 
  dplyr::filter((bis_11_complete == 2))

# delete column "bis_11_timestamp"
bis11_items$bis_11_timestamp <- NULL

# change all columns to numeric
bis11_items <- dplyr::mutate_all(bis11_items, function(x) as.numeric(as.character(x)))

# recode items
bis11_items[,c("bis11_01","bis11_07","bis11_08","bis11_09","bis11_10","bis11_12","bis11_13","bis11_15","bis11_20","bis11_29","bis11_30")] <- 5 - bis11_items[,c("bis11_01","bis11_07","bis11_08","bis11_09","bis11_10","bis11_12","bis11_13","bis11_15","bis11_20","bis11_29","bis11_30")]

# sum score
bis11_items$bis11_sum <- rowSums(bis11_items %>% dplyr::select("bis11_01":"bis11_30"))

# fit bis11 sum score in df data_quest
data_quest <- merge(data_quest, bis11_items[,c("set","bis11_sum")], by = "set")

#### Brief Self-Control Scale - BSCS

# store bscs items in separate df
# only keep rows with complete bscs questionnaire
bscs_items <- data_survey %>% 
  subset(select = c(set,
                    grep("bscs", colnames(data_survey)))) %>% 
  dplyr::filter((bscs_complete == 2))

# delete column "bscs_timestamp"
bscs_items$bscs_timestamp <- NULL

# change all columns to numeric
bscs_items <- dplyr::mutate_all(bscs_items, function(x) as.numeric(as.character(x)))

# recode items
bscs_items[,c("bscs_2","bscs_4","bscs_5","bscs_7","bscs_10","bscs_12","bscs_13")] <- 6 - bscs_items[,c("bscs_2","bscs_4","bscs_5","bscs_7","bscs_10","bscs_12","bscs_13")]

# sum score
bscs_items$bscs_sum <- rowSums(bscs_items %>% dplyr::select("bscs_1":"bscs_13"))

# fit bscs sum score in df data_quest
data_quest <- merge(data_quest, bscs_items[,c("set","bscs_sum")], by = "set")

#### Self-Regulation Scale - SRS

# store srs items in separate df
# only keep rows with complete bis11 questionnaire
srs_items <- data_survey %>% 
  subset(select = c(set,
                    grep("srs", colnames(data_survey)))) %>% 
  dplyr::filter((srs_complete == 2))

# delete column "srs_timestamp"
srs_items$srs_timestamp <- NULL

# change all columns to numeric
srs_items <- dplyr::mutate_all(srs_items, function(x) as.numeric(as.character(x)))

# recode items
srs_items[,c("srs_05","srs_07","srs_09")] <- 5 - srs_items[,c("srs_05","srs_07","srs_09")]

# sum score
srs_items$srs_sum <- rowSums(srs_items %>% dplyr::select("srs_01":"srs_10"))

# fit bscs sum score in df data_quest
data_quest <- merge(data_quest, srs_items[,c("set","srs_sum")], by = "set")

# remove temporary dfs

base::remove(nfc_items, flexer_items, bis11_items, bscs_items, srs_items)

#################### PREPARATION: SUBJECTIVE VALUES ############

# the choice column in df data_ED will contain 1 for the left button and 2 for the right button

data_ED[data_ED == "EDleftbutton"] <- 1
data_ED[data_ED == "EDrightbutton"] <- 2
data_ED$choice <- as.numeric(data_ED$choice)

# since only the last choice of each comparison is relevant, we will keep only those rows

data_ED <- data_ED[data_ED$step == 5,]
data_ED <- subset(data_ED, select = -c(step))

# apply the addition or subtraction of 0.02 to the last choices

for (i in 1:nrow(data_ED)) {

  if (data_ED$choice[i] == 1) {
    if (data_ED$LBvalue[i] == 2.00) {
      
      data_ED$RBvalue[i] <- round(data_ED$RBvalue[i] + 0.02, digits = 2)
      
      } else {
        
        data_ED$LBvalue[i] <- round(data_ED$LBvalue[i] - 0.02, digits = 2)

        }
    } else {
      
      if (data_ED$LBvalue[i] == 2.00) {
        
        data_ED$RBvalue[i] <- round(data_ED$RBvalue[i] - 0.02, digits = 2)
        
        } else {
          
          data_ED$LBvalue[i] <- round(data_ED$LBvalue[i] + 0.02, digits = 2)
    }
  }
  
}

# devide final values in columns LBvalue and RBvalue by 2

data_ED <- data_ED %>% 
  dplyr::mutate(LBvalue = LBvalue/2) %>% 
  dplyr::mutate(RBvalue = RBvalue/2)

# create vector indicating in which rows the data of a new subject begins

subjectindex <- c(1,which(data_ED$ID != dplyr::lag(data_ED$ID)),nrow(data_ED))

# create empty data frame for the loop to feed into

data_SV <- data.frame(ID = character(), strategy= double(), sv = double())

# compute subjective values per strategy and feed into df data_SV
# SV of the flexible strategy is always 1
# SV of the fixed strategy is value of flexible strategy devided by 2

for (i in seq_len(length(subjectindex)-1)) {
  
  tempone <- double()
  temptwo <- double()
  tempthree <- double()
  
  # initialize empty vectors
  
  # check for every strategy if its on the right or left button
  # devide the respective value by 2 and save the variable in new tmporary df

  for (j in seq_len(nrow(data_ED))) {
    
    # strategy distraction
    # if LB strat == distraction and LB value == 1
    if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 1) & (data_ED$LBvalue[j] == 1)) {
      # SV would be RB value devided by 2
      tempone <- append(tempone, data_ED$RBvalue[j])
    # else if LB strat == distraction and LB value != 1  
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 1) & (data_ED$LBvalue[j] != 1)) {
      # SV would be 1 
      tempone <- append(tempone, 1)
    # else if RB strat == distraction and RB value == 1  
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 1) & (data_ED$RBvalue[j] == 1)) {
      # SV would be LB value devided by 2
      tempone <- append(tempone, data_ED$LBvalue[j])
    # else if RB strat == distraction and RB value != 1  
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 1) & (data_ED$RBvalue[j] != 1)) {
      # SV would be 1
      tempone <- append(tempone, 1)
    }
    
    # strategy distancing
    if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 2) & (data_ED$LBvalue[j] == 1)) {
      temptwo <- append(temptwo, data_ED$RBvalue[j])
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 2) & (data_ED$LBvalue[j] != 1)) {
      temptwo <- append(temptwo, 1)
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 2) & (data_ED$RBvalue[j] == 1)) {
      temptwo <- append(temptwo, data_ED$LBvalue[j])
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 2) & (data_ED$RBvalue[j] != 1)) {
      temptwo <- append(temptwo, 1)
    }
    
    # strategy suppression
    if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 3) & (data_ED$LBvalue[j] == 1)) {
      tempthree <- append(tempthree, data_ED$RBvalue[j])
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 3) & (data_ED$LBvalue[j] != 1)) {
      tempthree <- append(tempthree, 1)
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 3) & (data_ED$RBvalue[j] == 1)) {
      tempthree <- append(tempthree, data_ED$LBvalue[j])
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 3) & (data_ED$RBvalue[j] != 1)) {
      tempthree <- append(tempthree, 1)
    }
  }

  newdata <- data.frame(ID = rep(data_ED$ID[subjectindex[i]],3),
                        strategy = c("distraction","distancing","suppression"),
                        sv = c(mean(tempone), mean(temptwo), mean(tempthree)))

  # add new variable strat_c:
  # strategy with highest value gets -1, and with lowes value 1
  newdata <- dplyr::mutate(newdata, strat_c = ifelse(newdata$sv == max(sv),- 1, (ifelse(newdata$sv == min(sv), 1, 0))))
  
  data_SV <- rbind(data_SV, newdata)
  
}


# remove temporary variables
base::remove(tempone, temptwo, tempthree, newdata)

#################### STATISTICS: DESCRIPTIVES ############

data_descr <- data_ER[data_ER$block != "6_choice",]
data_descr$trigger <- NULL
data_descr$block <- NULL

for (i in seq_len(nrow(data_descr))) {
  
  data_descr$age[i] <- data_quest$age[data_quest$record_id_2 == data_descr$ID[i]]
  data_descr$gender[i] <- data_quest$gender[data_quest$record_id_2 == data_descr$ID[i]]
}

#data_descr <- reshape(data = data_descr, idvar = "ID", timevar = "strategy", direction = "wide")

#################### STATISTICS: ASSUMPTIONS ############

# test NV of predictors

# wrapper for shapiro.test(), works with data.frames
sw <- function(x) {
  x = data.frame(x)                                             # make data.frame
  n = colnames(x)                                               # get variable names
  r = NULL                                                      # create container
  for (i in 1:dim(x)[2]) {                                      # for every variable in data ...
    y = shapiro.test(x[,i])                                     # perform Shapiro-Wilks test ...
    v = cbind(y$statistic,y$p.value)                            # get statistic and p-value ...
    colnames(v) = c("W","p")                                    # assign names for columns ...
    rownames(v) = n[i]                                          # and rows, i.e., variable names ...
    r = rbind(r,v)                                              # and add to container
  }
  return(round(r,3))
}

# prepare df for reporting results of shapiro wilk test
df.NV.subj <- data.frame(M = double(), SD = double(), W = double(), p = double())

# mean and sd of every variable without choice block
# arousal
for (i in seq_len(length(unique(data_ER$block))-1)) {
  
  df.NV.subj[i,1] <-mean(data_ER$arousal[data_ER$block == unique(data_ER$block)[i]])
  df.NV.subj[i,2] <-sd(data_ER$arousal[data_ER$block == unique(data_ER$block)[i]])
  df.NV.subj[i,3:4] <- sw(data_ER$arousal[data_ER$block == unique(data_ER$block)[i]])
  
}

# arousal
for (i in seq_len(length(unique(data_ER$block))-1)) {
  
  df.NV.subj[i+(length(unique(data_ER$block))-1),1] <-mean(data_ER$effort[data_ER$block == unique(data_ER$block)[i]])
  df.NV.subj[i+(length(unique(data_ER$block))-1),2] <-sd(data_ER$effort[data_ER$block == unique(data_ER$block)[i]])
  df.NV.subj[i+(length(unique(data_ER$block))-1),3:4] <- sw(data_ER$effort[data_ER$block == unique(data_ER$block)[i]])
  
}

rownames(df.NV.subj) <- c("Arousal View Neu", "Arousal View Neg", "Arousal Distraction", "Arousal Distancing", "Arousal Suppression",
                     "Effort View Neu", "Effort View Neg", "Effort Distraction", "Effort Distancing", "Effort Suppression")
colnames(df.NV.subj) <- c("$M$", "$SD$", "$W$", "$p$")

# EMG activity
df.NV.EMG <- data.frame(M = double(), SD = double(), W = double(), p = double())

# mean and sd of every variable without choice block
# Corrugator
for (i in seq_len(length(unique(data_EMG$block))-1)) {
  
  df.NV.EMG[i,1] <-mean(data_EMG$Corr[data_EMG$block == unique(data_EMG$block)[i]])
  df.NV.EMG[i,2] <-sd(data_EMG$Corr[data_EMG$block == unique(data_EMG$block)[i]])
  df.NV.EMG[i,3:4] <- sw(data_EMG$Corr[data_EMG$block == unique(data_EMG$block)[i]])
  
}

# Levator
for (i in seq_len(length(unique(data_EMG$block))-1)) {
  
  df.NV.EMG[i+(length(unique(data_EMG$block))-1),1] <-mean(data_EMG$Lev[data_EMG$block == unique(data_EMG$block)[i]])
  df.NV.EMG[i+(length(unique(data_EMG$block))-1),2] <-sd(data_EMG$Lev[data_EMG$block == unique(data_EMG$block)[i]])
  df.NV.EMG[i+(length(unique(data_EMG$block))-1),3:4] <- sw(data_EMG$Lev[data_EMG$block == unique(data_EMG$block)[i]])
  
}

rownames(df.NV.EMG) <- c("Corrgator View Neu", "Corrgator View Neg", "Corrgator Distraction", "Corrgator Distancing", "Corrgator Suppression",
                          "Levator View Neu", "Levator View Neg", "Levator Distraction", "Levator Distancing", "Levator Suppression")
colnames(df.NV.EMG) <- c("$M$", "$SD$", "$W$", "$p$")

#################### STATISTICAL ANALYSES: KONFIRMATORY ANALYSES ############

######## HYPOTHESIS 1

# Do negative pictures (compared to neutral pictures) evoke subjective arousal and physiological responding? (Manipulation Check)

#### HYPOTHESIS 1a 

# Subjective arousal (arousal rating) is lower after actively viewing neutral pictures compared to actively viewing negative pictures.

Ratings_view <- data_ER %>%
  subset(data_ER$block == "1_view_neu" | data_ER$block == "2_view_neg")
Ratings_view$block <- as.factor(Ratings_view$block)

SubjArousalView_aov <- afex::aov_ez(data = Ratings_view,
                                    id = "ID",
                                    dv = "arousal",
                                    within = "block",
                                    fun_aggregate = mean,
                                    include_aov = TRUE)

# compute posthoc tests for within measures
SubjArousalView_emm <- emmeans::emmeans(SubjArousalView_aov$aov, specs = "block")

SubjArousalView_con <- as.data.frame(pairs(SubjArousalView_emm, adjust = "bonferroni"))

# Bayes Factors
SubjArousalView_BF <- BayesFactor::anovaBF(formula = arousal ~ block,
                                           data = Ratings_view,
                                           progress = FALSE)
SubjArousalView_con$BF10 <- BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_view$arousal[Ratings_view$block == "1_view_neu"],
                                                                        y = Ratings_view$arousal[Ratings_view$block == "2_view_neg"],
                                                                        progress = FALSE, paired = TRUE))$bf

SubjArousalView_con <- cbind(SubjArousalView_con,
                             format(effectsize::t_to_eta2(t = SubjArousalView_con$t.ratio,
                                                          df_error = SubjArousalView_con$df,
                                                          ci = 0.95),
                                    digits = 2))

colnames(SubjArousalView_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
# rename contrast for table
SubjArousalView_con[1, 1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize arousal ratings

FigSubjArousalView <- ggplot2::ggplot(Ratings_view, aes(x = block, y = arousal, fill = block)) +
  geom_boxplot(width = .2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  see::geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  ylim(c(0,400))+
  scale_x_discrete(name = "Active viewing",
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative")) +
  viridis::scale_color_viridis() +
  labs(y = "Arousal Rating") +
  theme_minimal()+
  theme(legend.position = "none")

#### HYPOTHESIS 1b 

# Physiological responding (EMG corrugator activity) is lower while actively viewing neutral pictures compared to actively viewing negative pictures.

EMG_view <- data_EMG.new %>%
  subset(data_EMG.new$block == "1_view_neu" | data_EMG.new$block == "2_view_neg")
EMG_view$block <- as.factor(EMG_view$block)

EMGCorrView_aov <- afex::aov_ez(data = EMG_view,
                                id = "ID",
                                dv = "Corr",
                                within = "block",
                                fun_aggregate = mean,
                                include_aov = TRUE)

# compute posthoc tests for within measures
EMGCorrView_emm <- emmeans::emmeans(EMGCorrView_aov$aov, specs = "block")

EMGCorrView_con <- as.data.frame(pairs(EMGCorrView_emm, adjust = "bonferroni"))

# Bayes Factors
EMGCorrView_BF <- BayesFactor::anovaBF(formula = Corr ~ block,
                                       data = EMG_view,
                                       progress = FALSE)
EMGCorrView_con$BF10 <- BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_view$Corr[EMG_view$block == "1_view_neu"],
                                                                    y = EMG_view$Corr[EMG_view$block == "2_view_neg"],
                                                                    progress = FALSE, paired = FALSE))$bf

EMGCorrView_con <- cbind(EMGCorrView_con,
                         format(effectsize::t_to_eta2(t = EMGCorrView_con$t.ratio,
                                                      df_error = EMGCorrView_con$df,
                                                      ci = 0.95),
                                digits = 2))

colnames(EMGCorrView_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
# rename contrast for table
EMGCorrView_con[1, 1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize corrugator activity across view conditions

# create DF with mean value of each participant

EMG_view_plot <- EMG_view %>% group_by(ID, block) %>% summarise_at(vars("Corr","Lev"), list(mean)) 

FigEMGCorrView <- ggplot2::ggplot(EMG_view_plot, aes(x = block, y = Corr, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  see::geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  scale_x_discrete(name = "Active viewing",
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative")) +
  viridis::scale_color_viridis(discrete = TRUE) +
  labs(y = "Corrugator activity") +
  theme_minimal() +
  theme(legend.position = "none")


#### HYPOTHESIS 1c 

# Physiological responding (EMG levator activity) is lower while actively viewing neutral pictures compared to actively viewing negative pictures.

EMGLevView_aov <- afex::aov_ez(data = EMG_view,
                               id = "ID",
                               dv = "Lev",
                               within = "block",
                               fun_aggregate = mean,
                               include_aov = TRUE)

# compute posthoc tests for within measures
EMGLevView_emm <- emmeans::emmeans(EMGLevView_aov$aov, specs = "block")

EMGLevView_con <- as.data.frame(pairs(EMGLevView_emm, adjust = "bonferroni"))

# Bayes Factors
EMGLevView_BF <- BayesFactor::anovaBF(formula = Lev ~ block,
                                      data = EMG_view,
                                      progress = FALSE)
EMGLevView_con$BF10 <- BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_view$Lev[EMG_view$block == "1_view_neu"],
                                                                   y = EMG_view$Lev[EMG_view$block == "2_view_neg"],
                                                                   progress = FALSE, paired = FALSE))$bf

EMGLevView_con <- cbind(EMGLevView_con,
                        format(effectsize::t_to_eta2(t = EMGLevView_con$t.ratio,
                                                     df_error = EMGLevView_con$df,
                                                     ci = 0.95),
                               digits = 2))

colnames(EMGLevView_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
# rename contrast for table
EMGLevView_con[1, 1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize levator activity across view conditions

FigEMGLevView <- ggplot2::ggplot(EMG_view_plot, aes(x = block, y = Lev, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  see::geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  scale_x_discrete(name = "Active viewing",
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative")) +
  viridis::scale_color_viridis(discrete = TRUE) +
  labs(y = "Levator activity") +
  theme_minimal() +
  theme(legend.position = "none")

######## HYPOTHESIS 2

# Do ER strategies reduce emotional arousal? (Manipulation check)

#### HYPOTHESIS 2a 

# Subjective arousal (arousal rating) is lower after using an emotion regulation strategy (distraction, distancing, suppression) compared to active viewing.

Ratings_reg <- data_ER %>%
  subset(data_ER$block != "1_view_neu" & data_ER$block != "6_choice")
Ratings_reg$block <- as.factor(Ratings_reg$block)


SubjArousalReg_aov <- afex::aov_ez(data = Ratings_reg,
                                   id = "ID",
                                   dv = "arousal",
                                   within = "block",
                                   fun_aggregate = mean,
                                   include_aov = TRUE)

# compute posthoc tests for within measures
SubjArousalReg_emm <- emmeans::emmeans(SubjArousalReg_aov$aov, specs = "block")

SubjArousalReg_con <- as.data.frame(pairs(SubjArousalReg_emm, adjust = "bonferroni"))

# Bayes Factors
SubjArousalReg_BF <- BayesFactor::anovaBF(formula = arousal ~ block,
                                          data = Ratings_reg,
                                          progress = FALSE)

SubjArousalReg_con$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$arousal[Ratings_reg$block == "2_view_neg"],
                                                                         y = Ratings_reg$arousal[Ratings_reg$block == "3_distraction"],
                                                                         progress = FALSE, paired = TRUE))$bf,
                             BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$arousal[Ratings_reg$block == "2_view_neg"],
                                                                         y = Ratings_reg$arousal[Ratings_reg$block == "4_distancing"],
                                                                         progress = FALSE, paired = TRUE))$bf,
                             BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$arousal[Ratings_reg$block == "2_view_neg"],
                                                                         y = Ratings_reg$arousal[Ratings_reg$block == "5_suppression"],
                                                                         progress = FALSE, paired = TRUE))$bf,
                             BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$arousal[Ratings_reg$block == "3_distraction"],
                                                                         y = Ratings_reg$arousal[Ratings_reg$block == "4_distancing"],
                                                                         progress = FALSE, paired = TRUE))$bf,
                             BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$arousal[Ratings_reg$block == "3_distraction"],
                                                                         y = Ratings_reg$arousal[Ratings_reg$block == "5_suppression"],
                                                                         progress = FALSE, paired = TRUE))$bf,
                             BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$arousal[Ratings_reg$block == "4_distancing"],
                                                                         y = Ratings_reg$arousal[Ratings_reg$block == "5_suppression"],
                                                                         progress = FALSE, paired = TRUE))$bf)

SubjArousalReg_con <- cbind(SubjArousalReg_con,
                            format(effectsize::t_to_eta2(t = SubjArousalReg_con$t.ratio,
                                                         df_error = SubjArousalReg_con$df,
                                                         ci = 0.95),
                                   digits = 2))

colnames(SubjArousalReg_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

SubjArousalReg_con[1, 1] <- "$View_{neg} - Distraction$"
SubjArousalReg_con[2, 1] <- "$View_{neg} - Distancing$"
SubjArousalReg_con[3, 1] <- "$View_{neg} - Suppression$"
SubjArousalReg_con[4, 1] <- "$Distraction - Distancing$"
SubjArousalReg_con[5, 1] <- "$Distraction - Suppression$"
SubjArousalReg_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize arousal ratings

# figure
FigSubjArousalReg <- ggplot2::ggplot(Ratings_reg, aes(x = block, y = arousal, fill = factor(block))) +
  ggdist::stat_halfeye(adjust = 0.5, justification = -0.2, .width = 0, point_colour = NA, limits = c(.05, .95)) +
  geom_boxplot(width = 0.12, outlier.color = NA, alpha = 0.5)+
  geom_point(size = 1, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), aes(col = factor(block)))+
  ggthemes::scale_fill_tableau(palette = "Tableau 10")+
  ggthemes::scale_color_tableau(palette = "Tableau 10")+
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  theme_minimal() +
  theme(legend.position = "none")


######## HYPOTHESIS 3

# Do ER strategies reduce physiological responding? (Manipulation check)

#### HYPOTHESIS 3a 

# Physiological responding (EMG corrugator activity) is lower after using an emotion regulation strategy (distraction, distancing, suppression) compared to active viewing.


EMG_reg <- data_EMG.new %>%
  subset(data_EMG.new$block != "1_view_neu" & data_EMG.new$block != "6_choice")
EMG_reg$block <- as.factor(EMG_reg$block)

EMGCorrReg_aov <- afex::aov_ez(data = EMG_reg,
                               id = "ID",
                               dv = "Corr",
                               within = "block",
                               fun_aggregate = mean,
                               include_aov = TRUE)

# compute posthoc tests for within measures
EMGCorrReg_emm <- emmeans::emmeans(EMGCorrReg_aov$aov, specs = "block")

EMGCorrReg_con <- as.data.frame(pairs(EMGCorrReg_emm, adjust = "bonferroni"))

# Bayes Factors
EMGCorrReg_BF <- BayesFactor::anovaBF(formula = Corr ~ block,
                                       data = EMG_reg,
                                       progress = FALSE)

EMGCorrReg_con$BF10 <- c(papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "2_view_neg"],
                                                                y = EMG_reg$Corr[EMG_reg$block == "3_distraction"],
                                                                progress = FALSE, paired = FALSE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "2_view_neg"],
                                                                y = EMG_reg$Corr[EMG_reg$block == "4_distancing"],
                                                                progress = FALSE, paired = FALSE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "2_view_neg"],
                                                                y = EMG_reg$Corr[EMG_reg$block == "5_suppression"],
                                                                progress = FALSE, paired = FALSE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "3_distraction"],
                                                                y = EMG_reg$Corr[EMG_reg$block == "4_distancing"],
                                                                progress = FALSE, paired = FALSE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "3_distraction"],
                                                                y = EMG_reg$Corr[EMG_reg$block == "5_suppression"],
                                                                progress = FALSE, paired = FALSE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "4_distancing"],
                                                                y = EMG_reg$Corr[EMG_reg$block == "5_suppression"],
                                                                progress = FALSE, paired = FALSE))$table[1,"statistic"])

EMGCorrReg_con <- cbind(EMGCorrReg_con,
                        format(effectsize::t_to_eta2(t = EMGCorrReg_con$t.ratio,
                                                     df_error = EMGCorrReg_con$df,
                                                     ci = 0.95),digits = 2))

colnames(EMGCorrReg_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

EMGCorrReg_con[1, 1] <- "$View_{neg} - Distraction$"
EMGCorrReg_con[2, 1] <- "$View_{neg} - Distancing$"
EMGCorrReg_con[3, 1] <- "$View_{neg} - Suppression$"
EMGCorrReg_con[4, 1] <- "$Distraction - Distancing$"
EMGCorrReg_con[5, 1] <- "$Distraction - Suppression$"
EMGCorrReg_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize corrugator activity across blocks

# 
EMG_reg_plot <- EMG_reg %>% group_by(ID, block) %>% summarise_at(vars("Corr","Lev"), list(mean))

FigEMGCorrReg <- ggplot2::ggplot(EMG_reg_plot, aes(x = block, y = Corr, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  see::geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  viridis::scale_color_viridis(discrete = TRUE) +
  labs(y = "Corrugator activity") +
  theme_minimal() +
  theme(legend.position = "none")

#### HYPOTHESIS 3b

# Physiological responding (EMG levator activity) is lower after using an emotion regulation strategy (distraction, distancing, suppression) compared to active viewing.

EMGLevReg_aov <- afex::aov_ez(data = EMG_reg,
                              id = "ID",
                              dv = "Lev",
                              within = "block",
                              fun_aggregate = mean,
                              include_aov = TRUE)

# compute posthoc tests for within measures
EMGLevReg_emm <- emmeans::emmeans(EMGLevReg_aov$aov, specs = "block")

EMGLevReg_con <- as.data.frame(pairs(EMGLevReg_emm, adjust = "bonferroni"))

# Bayes Factors
EMGLevReg_BF <- BayesFactor::anovaBF(formula = Lev ~ block,
                                     data = EMG_reg,
                                     progress = FALSE)

EMGLevReg_con$BF10 <- c(papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "2_view_neg"],
                                                               y = EMG_reg$Lev[EMG_reg$block == "3_distraction"],
                                                               progress = FALSE, paired = FALSE))$table[1,"statistic"],
                        papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "2_view_neg"],
                                                               y = EMG_reg$Lev[EMG_reg$block == "4_distancing"],
                                                               progress = FALSE, paired = FALSE))$table[1,"statistic"],
                        papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "2_view_neg"],
                                                               y = EMG_reg$Lev[EMG_reg$block == "5_suppression"],
                                                               progress = FALSE, paired = FALSE))$table[1,"statistic"],
                        papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "3_distraction"],
                                                               y = EMG_reg$Lev[EMG_reg$block == "4_distancing"],
                                                               progress = FALSE, paired = FALSE))$table[1,"statistic"],
                        papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "3_distraction"],
                                                               y = EMG_reg$Lev[EMG_reg$block == "5_suppression"],
                                                               progress = FALSE, paired = FALSE))$table[1,"statistic"],
                        papaja::apa_print(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "4_distancing"],
                                                               y = EMG_reg$Lev[EMG_reg$block == "5_suppression"],
                                                               progress = FALSE, paired = FALSE))$table[1,"statistic"])

EMGLevReg_con <- cbind(EMGLevReg_con,
                       format(effectsize::t_to_eta2(t = EMGLevReg_con$t.ratio,
                                                    df_error = EMGLevReg_con$df,
                                                    ci = 0.95),digits = 2))

colnames(EMGLevReg_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

EMGLevReg_con[1, 1] <- "$View_{neg} - Distraction$"
EMGLevReg_con[2, 1] <- "$View_{neg} - Distancing$"
EMGLevReg_con[3, 1] <- "$View_{neg} - Suppression$"
EMGLevReg_con[4, 1] <- "$Distraction - Distancing$"
EMGLevReg_con[5, 1] <- "$Distraction - Suppression$"
EMGLevReg_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize levator activity across regulation blocks

# figure
FigEMGLevReg <- ggplot2::ggplot(EMG_reg_plot, aes(x = block, y = Lev, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  see::geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  viridis::scale_color_viridis(discrete = TRUE) +
  labs(y = "Levator activity") +
  theme_minimal() +
  theme(legend.position = "none")

######## HYPOTHESIS 4

# Do ER strategies require cognitive effort?

#### HYPOTHESIS 4a 

# Subjective effort (effort rating) is greater after using an emotion regulation strategy (distraction, distancing, suppression) compared to active viewing.

## Subjective effort

SubjEffort_aov <- afex::aov_ez(data = Ratings_reg,
                               id = "ID",
                               dv = "effort",
                               within = "block",
                               fun_aggregate = mean,
                               include_aov = TRUE)

# compute posthoc tests for within measure
SubjEffort_emm <- emmeans::emmeans(SubjEffort_aov$aov, specs = "block")

SubjEffort_con <- as.data.frame(pairs(SubjEffort_emm, adjust = "bonferroni"))

# Bayes Factors
SubjEffort_BF <- BayesFactor::anovaBF(formula = effort ~ block,
                                      data = Ratings_reg,
                                      progress = FALSE)

SubjEffort_con$BF10 <- c(papaja::apa_print(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "2_view_neg"],
                                                                y = Ratings_reg$effort[Ratings_reg$block == "3_distraction"],
                                                                progress = FALSE, paired = TRUE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "2_view_neg"],
                                                                y = Ratings_reg$effort[Ratings_reg$block == "4_distancing"],
                                                                progress = FALSE, paired = TRUE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "2_view_neg"],
                                                                y = Ratings_reg$effort[Ratings_reg$block == "5_suppression"],
                                                                progress = FALSE, paired = TRUE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "3_distraction"],
                                                                y = Ratings_reg$effort[Ratings_reg$block == "4_distancing"],
                                                                progress = FALSE, paired = TRUE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "3_distraction"],
                                                                y = Ratings_reg$effort[Ratings_reg$block == "5_suppression"],
                                                                progress = FALSE, paired = TRUE))$table[1,"statistic"],
                         papaja::apa_print(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "4_distancing"],
                                                                y = Ratings_reg$effort[Ratings_reg$block == "5_suppression"],
                                                                progress = FALSE, paired = TRUE))$table[1,"statistic"])
 
SubjEffort_con <- cbind(SubjEffort_con,
                        format(effectsize::t_to_eta2(t = SubjEffort_con$t.ratio,
                                                     df_error = SubjEffort_con$df,
                                                     ci = 0.95),
                               digits = 2))

colnames(SubjEffort_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

SubjEffort_con[1, 1] <- "$View_{negative} - Distraction$"
SubjEffort_con[2, 1] <- "$View_{negative} - Distancing$"
SubjEffort_con[3, 1] <- "$View_{negative} - Suppression$"
SubjEffort_con[4, 1] <- "$Distraction - Distancing$"
SubjEffort_con[5, 1] <- "$Distraction - Suppression$"
SubjEffort_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize effort ratings across blocks

FigSubjEffort <- ggplot2::ggplot(Ratings_reg, aes(x = block, y = effort, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  see::geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  ylim(c(0,400))+
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  viridis::scale_color_viridis(discrete = TRUE) +
  labs(y = "Effort Rating") +
  theme_minimal()+
  theme(legend.position = "none")

######## HYPOTHESIS 5

# Which variables can predict individual subjective values of ER strategies?

# mainly oriented on: 
#   https://rpubs.com/favstats/multilevel
#   https://ademos.people.uic.edu/Chapter16.html#5_random_effects_model
#   https://quantdev.ssri.psu.edu/tutorials/r-bootcamp-introduction-multilevel-model-and-interactions

# build new df for MLM
data_MLM <- data_EMG.new %>%
  subset(data_EMG.new$block != "2_view_neg" & data_EMG.new$block != "1_view_neu" & data_EMG.new$block != "6_choice")

# drop unnecessary columns
data_MLM$trigger <- NULL

# rename column block
data_MLM <- data_MLM %>% 
  rename("strategy" = "block")

data_MLM[data_MLM == "3_distraction"] <- "distraction"
data_MLM[data_MLM == "4_distancing"] <- "distancing"
data_MLM[data_MLM == "5_suppression"] <- "suppression"

# fit SVs and recoded strats from df data_SV in df data_MLM
for (i in seq_len(nrow(data_MLM))) {
  
  data_MLM$sv[i] <- data_SV$sv[data_SV$ID == data_MLM$ID[i] & data_SV$strategy == data_MLM$strategy[i]]
  data_MLM$strat_c[i] <- data_SV$strat_c[data_SV$ID == data_MLM$ID[i] & data_SV$strategy == data_MLM$strategy[i]]
}

# fit subjective arousal, effort, and utility ratings in df data_MLM


for (i in seq_len(nrow(data_MLM))) {
  
  data_MLM$arousal[i] <- data_ER$arousal[data_ER$ID == data_MLM$ID[i] & data_ER$strategy == data_MLM$strategy[i]]
  data_MLM$effort[i] <- data_ER$effort[data_ER$ID == data_MLM$ID[i] & data_ER$strategy == data_MLM$strategy[i]]
  data_MLM$utility[i] <- data_ER$utility[data_ER$ID == data_MLM$ID[i] & data_ER$strategy == data_MLM$strategy[i]]
  
}


# Centering of Level 1 Predictors
# credits to Philipp Masur:
# https://philippmasur.de/2018/05/23/how-to-center-in-multilevel-models/

data_MLM <- data_MLM %>% 
  dplyr::group_by(ID) %>% 
  dplyr::mutate(arousal.cwc = arousal - mean(arousal)) %>% 
  dplyr::mutate(effort.cwc = effort - mean(effort)) %>% 
  dplyr::mutate(utility.cwc = utility - mean(utility)) %>% 
  dplyr::mutate(Corr.cwc = Corr - mean(Corr)) %>% 
  dplyr::mutate(Lev.cwc = Lev - mean(Lev))

# only keep complete cases
data_MLM <- stats::na.omit(data_MLM)

#### MLM - NULL MODEL

MLM_0 <- lmerTest::lmer(formula = sv ~ 1 + (1 | ID),
                        data = data_MLM,
                        REML = FALSE)

## Intra-class correlation (ICC)

ICC.Model<-function(Model.Name) {
  tau.Null<-as.numeric(lapply(summary(Model.Name)$varcor, diag))
  sigma.Null <- as.numeric(attr(summary(Model.Name)$varcor, "sc")^2)
  ICC.Null <- tau.Null/(tau.Null+sigma.Null)
  return(ICC.Null)
}

# compute ICC
ICC_between_MLM_0 <- ICC.Model(MLM_0)

#### MLM - random effects

MLM_1 <- lmerTest::lmer(formula = sv ~ strat_c + effort.cwc + arousal.cwc + utility.cwc + Corr.cwc + Lev.cwc + (strat_c | ID),
                        data = data_MLM,
                        REML = TRUE)

### Effect size R-squared for MLM
# R2m: variance explained by the fixed effects
# R2c: variance explained by the entire model, including both fixed and random effects

MLM1_r2 <- MuMIn::r.squaredGLMM(MLM_1, pj2014 = T)

### Bayes Factor of strat_c

# https://rstudio-pubs-static.s3.amazonaws.com/358672_09291d0b37ce43f08cf001cfd25c16c2.html

data_MLM$ID <- factor(data_MLM$ID)

MLM_1_full_BF <- BayesFactor::lmBF(sv ~ strat_c + effort.cwc + arousal.cwc + utility.cwc + Corr.cwc + Lev.cwc + ID,
                                   data = data_MLM, whichRandom = "ID", progress = FALSE)

MLM_1_null_BF <- BayesFactor::lmBF(sv ~ 1 + effort.cwc + arousal.cwc + utility.cwc + Corr.cwc + Lev.cwc + ID,
                                   data = data_MLM, whichRandom = "ID", progress = FALSE)

MLM_1_BF <- MLM_1_full_BF / MLM_1_null_BF

# as variance explained by whole model is relatively high, due to variable strat_c, a new model without this predictor was built
# we assume that this variable captured too much variance which resulted in a "overfitted" model

MLM_2 <- lmerTest::lmer(formula = sv ~ effort.cwc + arousal.cwc + utility.cwc + Corr.cwc + Lev.cwc + (1 | ID),
                        data = data_MLM,
                        REML = TRUE)


MLM_2_r2 <- r2mlm::r2mlm(MLM_2)
MLM2_r2 <- MuMIn::r.squaredGLMM(MLM_2, pj2014 = T)

##### f² of predictors

# create lists for no effect models (for better clarity)

# for Models
MLM2_no_effect <- list()
# for R²
MLM2_no_effect_r2 <- list()

#df for f²
MLM2_f2 <- data.frame(f2 = double())

# EFFORT
MLM2_no_effect[["e"]] <- lmerTest::lmer(sv ~ 1 + arousal.cwc + utility.cwc + Corr.cwc + Lev.cwc + (1 | ID),
                                        data = data_MLM, REML = T)

MLM2_no_effect_r2[["e"]] <- MuMIn::r.squaredGLMM(MLM2_no_effect[["e"]], pj2014 = T)

# compute f² with conditional R²

MLM2_f2 <- rbind(MLM2_f2, (MLM2_r2[1,2] - MLM2_no_effect_r2[["e"]][1,2]) / (1 - MLM2_r2[1,2]))

# AROUSAL

MLM2_no_effect[["a"]] <- lmerTest::lmer(sv ~ effort.cwc + 1 + utility.cwc + Corr.cwc + Lev.cwc + (1 | ID),
                                        data = data_MLM, REML = T)

MLM2_no_effect_r2[["a"]] <- MuMIn::r.squaredGLMM(MLM2_no_effect[["a"]], pj2014 = T)

# compute f² with conditional R²

MLM2_f2 <- rbind(MLM2_f2, (MLM2_r2[1,2] - MLM2_no_effect_r2[["a"]][1,2]) / (1 - MLM2_r2[1,2]))

# UTILITY

MLM2_no_effect[["u"]] <- lmerTest::lmer(sv ~ effort.cwc + arousal.cwc + 1 + Corr.cwc + Lev.cwc + (1 | ID),
                                        data = data_MLM, REML = T)

MLM2_no_effect_r2[["u"]] <- MuMIn::r.squaredGLMM(MLM2_no_effect[["u"]], pj2014 = T)

# compute f² with conditional R²

MLM2_f2 <- rbind(MLM2_f2, (MLM2_r2[1,2] - MLM2_no_effect_r2[["u"]][1,2]) / (1 - MLM2_r2[1,2]))

# CORRUGATOR
MLM2_no_effect[["Corr"]] <- lmerTest::lmer(sv ~ effort.cwc + arousal.cwc + utility.cwc + 1 + Lev.cwc + (1 | ID),
                                        data = data_MLM, REML = T)

MLM2_no_effect_r2[["Corr"]] <- MuMIn::r.squaredGLMM(MLM2_no_effect[["Corr"]], pj2014 = T)

# compute f² with conditional R²

MLM2_f2 <- rbind(MLM2_f2, (MLM2_r2[1,2] - MLM2_no_effect_r2[["Corr"]][1,2]) / (1 - MLM2_r2[1,2]))

# LEVATOR

MLM2_no_effect[["Lev"]] <- lmerTest::lmer(sv ~ effort.cwc + arousal.cwc + utility.cwc + Corr.cwc + 1 + (1 | ID),
                                        data = data_MLM, REML = T)

MLM2_no_effect_r2[["Lev"]] <- MuMIn::r.squaredGLMM(MLM2_no_effect[["Lev"]], pj2014 = T)

# compute f² with conditional R²

MLM2_f2 <- rbind(MLM2_f2, (MLM2_r2[1,2] - MLM2_no_effect_r2[["Lev"]][1,2]) / (1 - MLM2_r2[1,2]))

colnames(MLM2_f2) <- "f2"
# a little bit of preparation for proper reporting of MLM results

M_H5.ranef <- as.data.frame(base::summary(MLM_2)$varcor)
M_H5.fixef <- base::summary(MLM_2)$coefficients

H5_M2_table <- as.data.frame(cbind(rownames(M_H5.fixef),
                                papaja::printnum(M_H5.fixef[,1], format = "e"),
                                M_H5.fixef[,c(2,5)]))
# add f2
H5_M2_table$f2 <- NA
H5_M2_table$f2[2:6] <- cbind(MLM2_f2$f2)

H5_M2_table$ranef.sd <- NA
H5_M2_table$ranef.sd[1] <- cbind(M_H5.ranef$sdcor[1])

colnames(H5_M2_table)[1] <- "Parameter"
colnames(H5_M2_table)[2] <- "Beta"
colnames(H5_M2_table)[3] <- "$SE$"
colnames(H5_M2_table)[4] <- "$p$-value"
colnames(H5_M2_table)[5] <- "$f^{2}$"
colnames(H5_M2_table)[6] <- "Random Effects (SD)"

row.names(H5_M2_table) <- NULL
H5_M2_table$Parameter[1:6] <- c("Intercept", "Effort", "Arousal", "Utility", "Corrugator activity", "Levator activity")

H5_M2_table[3:6] <- lapply(H5_M2_table[3:6], as.numeric)

######## HYPOTHESIS 6

# 
#

######## HYPOTHESIS 7

# Are subjective values related to flexible emotion regulation?

# fit predicted choice (strategy with highest SV per participant) in df data_choice

for (i in seq_len(nrow(data_choice))) {
  data_choice$pred_choice[i] <- data_SV$strategy[data_SV$ID == data_choice$ID[i] & data_SV$strat_c == -1]
}

# change variable pred_choice to values
# distraction -> 1
# distancing -> 2
# suppression -> 3

data_choice$pred_choice[data_choice$pred_choice == "distraction"] <- 1
data_choice$pred_choice[data_choice$pred_choice == "distancing"] <- 2
data_choice$pred_choice[data_choice$pred_choice == "suppression"] <- 3

data_choice <- transform(data_choice, pred_choice = as.numeric(pred_choice))

# fit individual SVs in df data_choice
for (i in seq_len(nrow(data_choice))) {
  data_choice$distraction.sv[i] <- data_SV$sv[data_SV$ID == data_choice$ID[i] & data_SV$strategy == "distraction"]
  data_choice$distancing.sv[i] <- data_SV$sv[data_SV$ID == data_choice$ID[i] & data_SV$strategy == "distancing"]
  data_choice$suppression.sv[i] <- data_SV$sv[data_SV$ID == data_choice$ID[i] & data_SV$strategy == "suppression"]
}

#### HYPOTHESIS 7a

# The higher the subjective value, the more likely the respective strategy is chosen

# Chi-Squared test with variables choice and predicted choice

choice_chisq <- stats::chisq.test(data_choice$choice, data_choice$pred_choice)

choice_chisq_BF <- BayesFactor::contingencyTableBF(x = choice_chisq[["observed"]],
                                                   sampleType = "jointMulti")
# ORDINAL REGRESSION

# https://marissabarlaz.github.io/portfolio/ols/

data_choice$choice <- as.factor(data_choice$choice)

Choice_OrdReg <- glm(choice ~ distraction.sv + distancing.sv + suppression.sv, data = data_choice, family = "binomial")

Choice_OrdReg_R2 <- with(summary(Choice_OrdReg), 1 - deviance/null.deviance)

# Bayes Factors
Choice_OrdReg_Posterior <- BFpack::BF(Choice_OrdReg)

#### HYPOTHESIS 7b

# Subjective values are lower and decline stronger when ER flexibility is lower.

# add new variable strat_r (0,1,2) to df data_SV

data_SV$strat_r[data_SV$strat_c == -1] <- 0
data_SV$strat_r[data_SV$strat_c == 0] <- 1
data_SV$strat_r[data_SV$strat_c == 1] <- 2

# create empty df to store slope, intercept, and FlexER value for each person

data_flex <- data.frame(ID = character(), intercept = double(),
                        slope = double(), FlexER = double())


# create variable for IDs
subjectindex <- unique(data_SV$ID)

# get SVs for each individual participant 
# SVs are ordered descending by magnitude

for (i in seq_len(length(unique(data_SV$ID)))) {
  
  tmp_glm <- stats::glm(data_SV$sv[data_SV$ID == subjectindex[i]] ~ data_SV$strat_r[data_SV$ID == subjectindex[i]])
  
  tmp <- data.frame(ID = subjectindex[i],
                    intercept = tmp_glm$coefficients[1],
                    slope = tmp_glm$coefficients[2],
                    FlexER = data_quest$flexer_mean[data_quest$record_id_2 == subjectindex[i]])
  
  data_flex <- rbind(data_flex, tmp)
}

base::remove(tmp_glm, tmp)

# linear regression with individual slopes and intercepts as predictors and FlexER Score as outcome

Flex_LM <- stats::lm(formula = FlexER ~ intercept + slope, data = data_flex)

Flex_LM_BF <- BayesFactor::regressionBF(formula = FlexER ~ intercept + slope, data = data_flex)


# ggplot2::ggplot(data_SV, aes(x = strat_r, y = sv, color  = ID))+
#   geom_point(color = "black") +
#   geom_smooth(method = "lm", fill = NA)+
#   theme(legend.position = "none")+
#   ylim(0,1.5)

#################### STATISTICAL ANALYSES: EXPLORATORY ANALYSES ############

# Are individuel subjective values of ER strategies related to personality traits?

# preparation: compute self control index from three questionnaires (BIS-11, BSCS, SRS) for each participant

PCA.SC <- psych::principal(data_quest[,c("bscs_sum","srs_sum","bis11_sum")], rotate="none")

# fill self-control value in data_quest

data_quest$SC <- PCA.SC[["scores"]][,1]

# fill SC values in df data_MLM

for (i in seq_len(nrow(data_MLM))) {
  
  data_MLM$SC[i] <- data_quest$SC[data_quest$record_id_2 == data_MLM$ID[i]]
  data_MLM$NFC[i] <- data_quest$nfc_sum[data_quest$record_id_2 == data_MLM$ID[i]]
}

# grand mean centering of SC
# https://philippmasur.de/2018/05/23/how-to-center-in-multilevel-models/

data_MLM$SC.gmc <- data_MLM$SC - mean(data_MLM$SC)
data_MLM$NFC.gmc <- data_MLM$NFC - mean(data_MLM$NFC)

MLM_3 <- lmerTest::lmer(formula = sv ~ effort.cwc + utility.cwc + Corr.cwc + SC.gmc + (1 | ID),
                     data = data_MLM,
                     REML = TRUE)
#################### SAVE WORKSPACE IMAGE #######################

save.image(file = "Workspace_ERED.RData")
