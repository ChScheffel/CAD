################################################################################
#
# Analysis script for the Registered Report
# "When easy is not preferred: A discounting paradigm for load-independent task preference"
# by Zerna, J., Scheffel, C., Kührt, C., & Strobel., A. (2022)
#
# Corresponding author: Josephine Zerna (josephine.zerna@tu-dresden.de)
#
# Please download the repsitory from github.com/ChScheffel/CAD
#
#
################################################################################

##### Setup ####################################################################

# load here-library for path-independent project structure (install here by calling install.packages("here") if necessary)
# set top level directory to source file

library(here)

here::i_am("flag_project_root_CAD.txt")

# load reproducible environment library to get all packages with correct versions form the renv.lock file
# install renv by calling install.packages("renv") if necessary

library(renv)
source(here("06_Paper","COG-ED", "Stage 2", "renv", "activate.R"))


# the required packages are:
# "bibtex", "here", "tidyverse", "bayestestR", "papaja", "lmerTest", "afex", "emmeans", "sjPlot", "purrr", "broom",
# "kableExtra", "interactions", "glmmTMB", "BayesFactor", "ggplot2", "egg", "knitr", "effectsize", "pracma", "MuMIn",
# "MetBrewer", "lubridate", "nlraa" and "ggprism"
library(tidyverse) # as an explicit call because renv somehow refuses to remember it

# sets orthogonal contrasts for mixed-effects model and rmANOVA globally in order to get meaningful Type-III tests

afex::set_sum_contrasts()

##### Import ###################################################################

# set top level directory to source file

here::i_am("flag_project_root_CAD.txt")

# import n-back and effort discounting data into a list each

datalist_nback = lapply(list.files(here("04_RawData", "main", "COG-ED"), pattern = '.*nback.*csv', full.names = TRUE),
                        read.csv, stringsAsFactors = FALSE, header = TRUE)
datalist_ED = lapply(list.files(here("04_RawData", "main", "COG-ED"), pattern = '.*_ED.*csv', full.names = TRUE),
                     read.csv, stringsAsFactors = FALSE, header = TRUE)

# create empty data frames for loops to feed into

data_nback <- data.frame(subject = character(), level = double(), target = character(),
                         response = character(), correct = double(), rt = double())
data_ED <- data.frame(subject = character(), step = double(), choice = character(),
                      LBvalue = double(), LBlevel = double(), RBvalue = double(), RBlevel = double())


# put relevant data into data frames

for (i in 1:length(datalist_nback)) {
  
  newdata <- data.frame(datalist_nback[[i]][["Participant"]], datalist_nback[[i]][["currentlevel"]],
                        datalist_nback[[i]][["Stimulus"]], datalist_nback[[i]][["trial_resp.keys"]],
                        datalist_nback[[i]][["trial_resp.corr"]], datalist_nback[[i]][["trial_resp.rt"]])
  colnames(newdata) <- names(data_nback)
  data_nback <- rbind(data_nback, newdata)
}

for (i in 1:length(datalist_ED)) {
  
  newdata <- data.frame(datalist_ED[[i]][["Participant"]][2:length(datalist_ED[[i]][["Participant"]])],
                        datalist_ED[[i]][["EDround.thisN"]][2:length(datalist_ED[[i]][["EDround.thisN"]])],
                        datalist_ED[[i]][["EDclick.clicked_name"]][2:length(datalist_ED[[i]][["EDclick.clicked_name"]])],
                        datalist_ED[[i]][["EDleftbutton.value"]][2:length(datalist_ED[[i]][["EDleftbutton.value"]])],
                        datalist_ED[[i]][["EDleftbutton.nback"]][2:length(datalist_ED[[i]][["EDleftbutton.nback"]])],
                        datalist_ED[[i]][["EDrightbutton.value"]][2:length(datalist_ED[[i]][["EDrightbutton.value"]])],
                        datalist_ED[[i]][["EDrightbutton.nback"]][2:length(datalist_ED[[i]][["EDrightbutton.nback"]])])
  colnames(newdata) <- names(data_ED)
  data_ED <- rbind(data_ED, newdata)
}

# remove the following subjects for misunderstanding the instruction: E17T12, Z15R03, C18D18, H25N04, D24A05, T14G09, D29N05
# remove the following subject for not remembering the level colours correctly during effort discounting: W16C01
# sets 2, 6, and 7 were dummy sets to test the NASA TLX iterations

data_nback <- data_nback[!(data_nback$subject == "E17T12" | data_nback$subject == "Z15R03" | data_nback$subject == "C18D18" | data_nback$subject == "H25N04" |
                           data_nback$subject == "D24A05" | data_nback$subject == "T14G09" | data_nback$subject == "D29N05" | data_nback$subject == "W16C01"), ]
data_ED <- data_ED[!(data_ED$subject == "E17T12" | data_ED$subject == "Z15R03" | data_ED$subject == "C18D18" | data_ED$subject == "H25N04" |
                     data_ED$subject == "D24A05" | data_ED$subject == "T14G09" | data_ED$subject == "D29N05" | data_ED$subject == "W16C01"), ]

# replace some columns with 'easy to work with' values

# the target column will contain 1 for targets and 0 for all non-targets

data_nback[data_nback == "Target"] <- 1
data_nback[data_nback == "Pretarget"|data_nback == "Lure"|data_nback == "Distractor"] <- 0
data_nback$target <- as.numeric(data_nback$target)

# the response column will contain 1 for responses and 0 for all non-responses

data_nback[data_nback == "left"|data_nback == "right"] <- 1
data_nback[data_nback == "None"] <- 0
data_nback$response <- as.numeric(data_nback$response)

# for reaction time preprocessing we account for post-error trials, that we will exclude from aggregated reaction time
# so the nback data frame will contain a column of ones and zeros

# add the "correct" column, but shifted down by one row

data_nback$postcorrect = c(1,data_nback$correct[1:(length(data_nback$correct)-1)])

# make sure to avoid transfer from the previous block by marking the first trial of each block as correct

data_nback$postcorrect[c(1,seq(64,length(data_nback$postcorrect),64))] <- 1

# the choice column will contain 1 for the left button and 2 for the right button

data_ED[data_ED == "EDleftbutton"] <- 1
data_ED[data_ED == "EDrightbutton"] <- 2
data_ED$choice <- as.numeric(data_ED$choice)

# since only the last choice of each comparison is relevant, we will keep only those rows

data_ED <- data_ED[data_ED$step == 5,]
data_ED <- subset(data_ED, select = -c(step))

# import questionnaire data from RedCap

all_quest <- read.csv(here("04_RawData", "main", "Questionnaire_Data_Full_Version.csv"), stringsAsFactors = FALSE, header = TRUE)
colnames(all_quest)[1] <- "set" # rename the first column

# compute index of rows in which the data sets change

setindex <- c(1,which(all_quest$set != dplyr::lag(all_quest$set)),nrow(all_quest))

# reshape the data frame for better handling (currently three rows per subject, lots of NAs)

data_quest <- data.frame(set = all_quest$set[setindex],
                         subject = all_quest$subject_id_quest[setindex],
                         time_quest = all_quest$information_timestamp[setindex])
data_quest <- cbind(data_quest, all_quest[setindex,] %>% select(nfc_01:nfc_16))
data_quest <- cbind(data_quest, time_lab = all_quest$general_questions_timestamp[setindex+1],
                    age = all_quest$age[setindex+1], gender = all_quest$gender[setindex+1],
                    edu = all_quest$edu[setindex+1])
data_quest <- cbind(data_quest, all_quest[setindex+1,] %>% select(nasa_tlx_1:avers,nasa_tlx_1b:aversb,nasa_tlx_1c:aversc,nasa_tlx_1d:aversd))
data_quest <- cbind(data_quest, adherence = all_quest$followup_adherence[setindex+1],
                    motivation = all_quest$followup_motivation[setindex+1],
                    motivation_other = all_quest$followup_motivation_other[setindex+1])

# some participants started filling out the questionnaires two times, so their code appears twice

data_quest <- data_quest %>% filter(complete.cases(.))

# make a copy for counting the amount of participants who filled out the questionnaires

n_quest <- data_quest

# remove the following subjects for misunderstanding the instruction: E17T12, Z15R03, C18D18, H25N04, D24A05, T14G09, D29N05
# remove the following subject for not remembering the level colours correctly during effort discounting: W16C01
# sets 2, 6, and 7 were dummy sets to test the NASA TLX iterations

data_quest <- data_quest[!(data_quest$subject == "E17T12" | data_quest$subject == "Z15R03" | data_quest$subject == "C18D18" | data_quest$subject == "H25N04" |
                             data_quest$subject == "D24A05" | data_quest$subject == "T14G09" | data_quest$subject == "D29N05" | data_quest$subject == "W16C01"), ]

# keep only the data from participants who have both questionnaire and behavioural data

showups <- intersect(data_quest$subject, data_nback$subject)
data_quest <- data_quest[data_quest$subject %in% showups, ]

# describe when data acquisition took place

acqui_time <- data.frame(dates = c(t(data_quest[,grep("time", colnames(data_quest))])), stringsAsFactors = FALSE)
acqui_time <- data.frame(dates = acqui_time[!(acqui_time$dates == ""),])
acqui_time <- as.Date(acqui_time$dates, format = "%d.%m.%Y %H:%M")
acqui_time <- range(acqui_time, na.rm = TRUE)

# now remove the original data sets (which we needed for the time stamps) and keep only the edited sets

data_quest <- data_quest[grep("_final", data_quest$set), ]
data_quest <- subset(data_quest, select = -c(set, time_quest, time_lab))

# remove them from the counting variable as well

n_quest <- n_quest[grep("_final", n_quest$set), ]
n_quest <- nrow(n_quest)

# remove temporary variables

remove(all_quest,showups)

##### Subjective value computation #############################################

# apply the addition or subtraction of 0.02 to the last choices

for (i in 1:nrow(data_ED)) {
  
  data_ED$fixedlevel[i] <- data_ED[i,grep("Bvalue", colnames(data_ED))[which(data_ED[i,grep("Bvalue", colnames(data_ED))] == 2.00)] + 1]
  data_ED$flexlevel[i] <- data_ED[i,grep("Bvalue", colnames(data_ED))[which(data_ED[i,grep("Bvalue", colnames(data_ED))] != 2.00)] + 1]
  
  if (data_ED$choice[i] == 1) {
    if (data_ED$LBvalue[i] == 2.00) {
      data_ED$flexvalue[i] <- round(data_ED$RBvalue[i] + 0.02, digits = 2)
    } else {
      data_ED$flexvalue[i] <- round(data_ED$LBvalue[i] - 0.02, digits = 2)
    }
  } else {
    if (data_ED$RBvalue[i] == 2.00) {
      data_ED$flexvalue[i] <- round(data_ED$LBvalue[i] + 0.02, digits = 2)
    } else {
      data_ED$flexvalue[i] <- round(data_ED$RBvalue[i] - 0.02, digits = 2)
    }
  }
  
}

# create vector indicating in which rows the data of a new subject begins

subjectindex <- c(1,which(data_ED$subject != dplyr::lag(data_ED$subject)),nrow(data_ED))

# create empty data frame for the loop to feed into

data_SV <- data.frame(subject = character(), level = double(), sv = double())

# compute subjective values per n-back level and feed into data frame

for (i in 1:(length(subjectindex)-1)) {
  
  # initialize empty vectors
  
  tempone <- double()
  temptwo <- double()
  tempthree <- double()
  tempfour <- double()
  
  # check for every number, whether it appears in the fixedlevel and flexlevel columns
  # divide flexvalue by 2 if it appears in the fixedlevel columns
  # append 1 if it appears in the flexlevel column
  
  # for 1-back
  
  if (rlang::is_empty(which(data_ED$fixedlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 1)) == FALSE) {
    tempone <- append(tempone, data_ED$flexvalue[subjectindex[i]-1 +
                                                   which(data_ED$fixedlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 1)]/2)
  } else {
    # do nothing
  }
  
  if (rlang::is_empty(which(data_ED$flexlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 1)) == FALSE) {
    tempone <- append(tempone, rep(1, length(which(data_ED$flexlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 1))))
  } else {
    # do nothing
  }
  
  # for 2-back
  
  if (rlang::is_empty(which(data_ED$fixedlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 2)) == FALSE) {
    temptwo <- append(temptwo, data_ED$flexvalue[subjectindex[i]-1 +
                                                   which(data_ED$fixedlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 2)]/2)
  } else {
    # do nothing
  }
  
  if (rlang::is_empty(which(data_ED$flexlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 2)) == FALSE) {
    temptwo <- append(temptwo, rep(1, length(which(data_ED$flexlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 2))))
  } else {
    # do nothing
  }
  
  # for 3-back
  
  if (rlang::is_empty(which(data_ED$fixedlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 3)) == FALSE) {
    tempthree <- append(tempthree, data_ED$flexvalue[subjectindex[i]-1 +
                                                       which(data_ED$fixedlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 3)]/2)
  } else {
    # do nothing
  }
  
  if (rlang::is_empty(which(data_ED$flexlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 3)) == FALSE) {
    tempthree <- append(tempthree, rep(1, length(which(data_ED$flexlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 3))))
  } else {
    # do nothing
  }
  
  # for 4-back
  
  if (rlang::is_empty(which(data_ED$fixedlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 4)) == FALSE) {
    tempfour <- append(tempfour, data_ED$flexvalue[subjectindex[i]-1 +
                                                     which(data_ED$fixedlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 4)]/2)
  } else {
    # do nothing
  }
  
  if (rlang::is_empty(which(data_ED$flexlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 4)) == FALSE) {
    tempfour <- append(tempfour, rep(1, length(which(data_ED$flexlevel[c(subjectindex[i]:(subjectindex[i+1]-1))] == 4))))
  } else {
    # do nothing
  }
  
  # put the mean subjective value of the three values per n-back level in the respective column and add to data frame
  
  newdata <- data.frame(subject = rep(data_ED$subject[subjectindex[i]],4),
                        level = c(1:4),
                        sv = c(mean(tempone), mean(temptwo), mean(tempthree), mean(tempfour)))
  data_SV <- rbind(data_SV, newdata)
  
}

# remove temporary variables

base::remove(tempone, temptwo, tempthree, tempfour)

# add the SVs trial-wise to the nback-data-frame for the multi-level-model

for (i in 1:nrow(data_nback)) {
  
  data_nback$sv[i] <- data_SV$sv[data_SV$subject == data_nback$subject[i] & data_SV$level == data_nback$level[i]]
  
}

##### Need for Cognition Score computation #####################################

# prepare data frame for loop to feed into

data_nfc <- data.frame(subject = character(), nfc = double())

# calculate NFC scores for every subject

for (i in 1:nrow(data_quest)) {
  
  nfc <- data_quest[i, grep("nfc", colnames(data_quest))]
  
  # define and invert items to be recoded
  
  nfc[ ,c(4,6,7,8,9,10,11,12,15,16)] <-  nfc[ ,c(4,6,7,8,9,10,11,12,15,16)] * -1
  
  data_nfc <- rbind(data_nfc, data.frame(subject = data_quest$subject[i],
                                         nfc = sum(nfc)))
}

# add the NFC scores trial-wise to the nback-data-frame for the multi-level-model

data_nback <- left_join(data_nback, data_nfc, by = "subject")

# remove the temporary variables

base::remove(nfc, data_nfc)

##### Preprocessing pipelines for the SCA ######################################

# create new data frames for the specification curve analysis
# the data frame names are a combination of the letters from each of these categories, indicating how they will be preprocessed:
#
# across which dimensions the transformation and outlier exclusion will be done:
#   (AA) across subjects, across n-back levels
#   (AW) across subjects, within n-back levels
#   (WW) within subjects, within n-back levels
#   (WA) within subjects, across n-back levels
# RT transformations:
#   (R) raw/none
#   (L) log
#   (I) inverse
#   (S) square-root
# RT outlier exclusion:
#   (N) none
#   (2) 2 MADs from the median
#   (5) 2.5 MADs from the median
#   (3) 3 MADs from the median
#   (O) 0-100 ms after stimulus onset
#   (T) 0-200 ms after stimulus onset
#
# Example: the data frame "AWL3" has log-transformed RT data with no data points beyond 3 MADs
# from the median
#
# Some combinations are nonsensical, so we will not include them: Raw data sets (__R__) with either no outlier
# exclusion (___N_) or time-based outlier exclusion (___T_) do not need the different dimensions (A/W), and
# time-based exclusion is nonsensical for transformed data sets.


# create a list that contains the basic data frame of the n-back data for each of the pipelines

pipelines_data <- replicate(63, data_nback, simplify = FALSE)
pipelines_data <- setNames(pipelines_data, c("AARN","AAR2","AAR5","AAR3","AARO","AART",
                                             "AALN","AAL2","AAL5","AAL3",
                                             "AAIN","AAI2","AAI5","AAI3",
                                             "AASN","AAS2","AAS5","AAS3",
                                             "AWR2","AWR5","AWR3",
                                             "AWLN","AWL2","AWL5","AWL3",
                                             "AWIN","AWI2","AWI5","AWI3",
                                             "AWSN","AWS2","AWS5","AWS3",
                                             "WWR2","WWR5","WWR3",
                                             "WWLN","WWL2","WWL5","WWL3",
                                             "WWIN","WWI2","WWI5","WWI3",
                                             "WWSN","WWS2","WWS5","WWS3",
                                             "WAR2","WAR5","WAR3",
                                             "WALN","WAL2","WAL5","WAL3",
                                             "WAIN","WAI2","WAI5","WAI3",
                                             "WASN","WAS2","WAS5","WAS3"))

for (i in 1:length(pipelines_data)) {
  
  # extract the name of the current data frame
  
  pipeline_name <- strsplit(names(pipelines_data)[i], "")
  
  # the first decision is whether transformations and exclusions will be applied across/within subjects/levels
  
  if (pipeline_name[[1]][1] == "A" & pipeline_name[[1]][2] == "A") {
    
    # the numbers of all rows in which response, correct, and postcorrect are 1 (i.e. the ones where we will analyze reaction time )
    # (we will still keep the other rows until we have calculated d prime, then we will remove them)
    
    piperows <- row.names(pipelines_data[[i]][pipelines_data[[i]]$response == 1 & pipelines_data[[i]]$correct == 1 & pipelines_data[[i]]$postcorrect == 1, ])
    
    # the second decision is the type of transformation, depending on the third letter in the data frame name
    
    if (pipeline_name[[1]][3] == "L") {
      
      pipelines_data[[i]][piperows, "rt"] <- log10(pipelines_data[[i]][piperows, "rt"])
      
    } else if (pipeline_name[[1]][3] == "I") {
      
      pipelines_data[[i]][piperows, "rt"] <- 1/(pipelines_data[[i]][piperows, "rt"])
      
    } else if (pipeline_name[[1]][3] == "S") {
      
      pipelines_data[[i]][piperows, "rt"] <- sqrt(pipelines_data[[i]][piperows, "rt"])
      
    }
    
    # compute median and median absolute deviation
    
    pipemedian <- median(pipelines_data[[i]][piperows, "rt"], na.rm = TRUE)
    pipemad <- mad(pipelines_data[[i]][piperows, "rt"], na.rm = TRUE)
    
    # the third decision is the outlier exclusion
    
    if (pipeline_name[[1]][4] == "2") {
      
      # logical vector of which of the piperows are out of the defined range
      pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 2 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 2 * pipemad)
      
      # exclude the rows out of range from the data frame
      if (sum(pipeexclude) != 0) {
        pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
        pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
      }
      
    } else if (pipeline_name[[1]][4] == "5") {
      
      # logical vector of which of the piperows are out of the defined range
      pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 2.5 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 2.5 * pipemad)
      
      # exclude the rows out of range from the data frame
      if (sum(pipeexclude) != 0) {
        pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
        pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
      }
      
    } else if (pipeline_name[[1]][4] == "3") {
      
      # logical vector of which of the piperows are out of the defined range
      pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 3 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 3 * pipemad)
      
      # exclude the rows out of range from the data frame
      if (sum(pipeexclude) != 0) {
        pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
        pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
      }                
    }
    
  } else if (pipeline_name[[1]][1] == "A" & pipeline_name[[1]][2] == "W") {
    
    # apply the transformations and exclusions across subjects but within levels
    
    for (x in 1:4) {
      
      # the numbers of all rows in which response, correct, and postcorrect are 1 within that level
      
      piperows <- row.names(pipelines_data[[i]][pipelines_data[[i]]$level == x & pipelines_data[[i]]$response == 1 &
                                                  pipelines_data[[i]]$correct == 1 & pipelines_data[[i]]$postcorrect == 1, ])
      
      # the second decision is the type of transformation, depending on the third letter in the data frame name
      
      if (pipeline_name[[1]][3] == "L") {
        
        pipelines_data[[i]][piperows, "rt"] <- log10(pipelines_data[[i]][piperows, "rt"])
        
      } else if (pipeline_name[[1]][3] == "I") {
        
        pipelines_data[[i]][piperows, "rt"] <- 1/log10(pipelines_data[[i]][piperows, "rt"])
        
      } else if (pipeline_name[[1]][3] == "S") {
        
        pipelines_data[[i]][piperows, "rt"] <- sqrt(pipelines_data[[i]][piperows, "rt"])
        
      }
      
      # compute median and median absolute deviation
      
      pipemedian <- median(pipelines_data[[i]][piperows, "rt"], na.rm = TRUE)
      pipemad <- mad(pipelines_data[[i]][piperows, "rt"], na.rm = TRUE)
      
      # the third decision is the outlier exclusion
      
      if (pipeline_name[[1]][4] == "2") {
        
        pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 2 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 2 * pipemad)
        if (sum(pipeexclude) != 0) {
          pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
          pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
        }                  
      } else if (pipeline_name[[1]][4] == "5") {
        
        pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 2.5 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 2.5 * pipemad)
        if (sum(pipeexclude) != 0) {
          pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
          pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
        }                  
      } else if (pipeline_name[[1]][4] == "3") {
        
        pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 3 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 3 * pipemad)
        if (sum(pipeexclude) != 0) {
          pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
          pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
        }                  
      }
    }
    
    
  } else if (pipeline_name[[1]][1] == "W" & pipeline_name[[1]][2] == "W") {
    
    # apply the transformations and exclusions within subjects and within levels
    
    for (x in 1:4) {
      
      for (y in 1:length(table(pipelines_data[[i]]$subject))) {
        
        # the numbers of all rows in which response, correct, and postcorrect are 1 within that level within that subject
        
        piperows <- row.names(pipelines_data[[i]][pipelines_data[[i]]$subject == names(table(pipelines_data[[i]]$subject))[y] & pipelines_data[[i]]$level == x &
                                                    pipelines_data[[i]]$response == 1 & pipelines_data[[i]]$correct == 1 & pipelines_data[[i]]$postcorrect == 1, ])
        
        # the second decision is the type of transformation, depending on the third letter in the data frame name
        
        if (pipeline_name[[1]][3] == "L") {
          
          pipelines_data[[i]][piperows, "rt"] <- log10(pipelines_data[[i]][piperows, "rt"])
          
        } else if (pipeline_name[[1]][3] == "I") {
          
          pipelines_data[[i]][piperows, "rt"] <- 1/(pipelines_data[[i]][piperows, "rt"])
          
        } else if (pipeline_name[[1]][3] == "S") {
          
          pipelines_data[[i]][piperows, "rt"] <- sqrt(pipelines_data[[i]][piperows, "rt"])
        }
        
        # compute median and median absolute deviation
        
        pipemedian <- median(pipelines_data[[i]][piperows, "rt"], na.rm = TRUE)
        pipemad <- mad(pipelines_data[[i]][piperows, "rt"], na.rm = TRUE)
        
        # the third decision is the outlier exclusion
        
        if (pipeline_name[[1]][4] == "2") {
          
          pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 2 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 2 * pipemad)
          if (sum(pipeexclude) != 0) {
            pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
            pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
          }                    
        } else if (pipeline_name[[1]][4] == "5") {
          
          pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 2.5 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 2.5 * pipemad)
          if (sum(pipeexclude) != 0) {
            pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
            pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
          }                    
        } else if (pipeline_name[[1]][4] == "3") {
          
          pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 3 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 3 * pipemad)
          if (sum(pipeexclude) != 0) {
            pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
            pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
          }                  }
      }
    }
    
  } else if (pipeline_name[[1]][1] == "W" & pipeline_name[[1]][2] == "A") {
    
    # apply the transformations and exclusions within subjects but across levels
    
    for (y in 1:length(table(pipelines_data[[i]]$subject))) {
      
      # the numbers of all rows in which response, correct, and postcorrect are 1 within that level within that subject
      
      piperows <- row.names(pipelines_data[[i]][pipelines_data[[i]]$subject == names(table(pipelines_data[[i]]$subject))[y] & pipelines_data[[i]]$response == 1 &
                                                  pipelines_data[[i]]$correct == 1 & pipelines_data[[i]]$postcorrect == 1, ])
      
      # the second decision is the type of transformation, depending on the third letter in the data frame name
      
      if (pipeline_name[[1]][3] == "L") {
        
        pipelines_data[[i]][piperows, "rt"] <- log10(pipelines_data[[i]][piperows, "rt"])
        
      } else if (pipeline_name[[1]][3] == "I") {
        
        pipelines_data[[i]][piperows, "rt"] <- 1/(pipelines_data[[i]][piperows, "rt"])
        
      } else if (pipeline_name[[1]][3] == "S") {
        
        pipelines_data[[i]][piperows, "rt"] <- sqrt(pipelines_data[[i]][piperows, "rt"])
        
      }
      
      # compute median and median absolute deviation
      
      pipemedian <- median(pipelines_data[[i]]$rt[pipelines_data[[i]]$subject == names(table(pipelines_data[[i]]$subject))[y] & pipelines_data[[i]]$response == 1 & pipelines_data[[i]]$correct == 1], na.rm = TRUE)
      pipemad <- mad(pipelines_data[[i]]$rt[pipelines_data[[i]]$subject == names(table(pipelines_data[[i]]$subject))[y] & pipelines_data[[i]]$response == 1 & pipelines_data[[i]]$correct == 1], na.rm = TRUE)
      
      # the third decision is the outlier exclusion
      
      if (pipeline_name[[1]][4] == "2") {
        
        pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 2 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 2 * pipemad)
        if (sum(pipeexclude) != 0) {
          pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
          pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
        }                  
      } else if (pipeline_name[[1]][4] == "5") {
        
        pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 2.5 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 2.5 * pipemad)
        if (sum(pipeexclude) != 0) {
          pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
          pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
        }                  
      } else if (pipeline_name[[1]][4] == "3") {
        
        pipeexclude <- pipelines_data[[i]][piperows, "rt"] > (pipemedian + 3 * pipemad) | pipelines_data[[i]][piperows, "rt"] < (pipemedian - 3 * pipemad)
        if (sum(pipeexclude) != 0) {
          pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
          pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
        }
      }
    }
    
  }
  
  # the time-based exclusions are done outside of the A/A-A/W-W/W-W/A-conditions because they are independent of dimension:
  
  # exclude RTs faster than 100 or 200 ms after stimulus onset if the fourth letter in the data frame name is an "O" or a "T"
  # also making sure that there are even any trials below 100/200 ms, otherwise you get an error message
  
  if (pipeline_name[[1]][4] == "O") {
    
    piperows <- row.names(pipelines_data[[i]][pipelines_data[[i]]$response == 1 &
                                                pipelines_data[[i]]$correct == 1 & pipelines_data[[i]]$postcorrect == 1, ])
    pipeexclude <- pipelines_data[[i]][piperows, "rt"] < 0.1
    if (sum(pipeexclude) != 0) {
      pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
      pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
    }
    
  } else if (pipeline_name[[1]][4] == "T") {
    
    piperows <- row.names(pipelines_data[[i]][pipelines_data[[i]]$response == 1 &
                                                pipelines_data[[i]]$correct == 1 & pipelines_data[[i]]$postcorrect == 1, ])
    pipeexclude <- pipelines_data[[i]][piperows, "rt"] < 0.2
    if (sum(pipeexclude) != 0) {
      pipedrop <- which(rownames(pipelines_data[[i]]) %in% piperows[pipeexclude])
      pipelines_data[[i]] <- pipelines_data[[i]][-pipedrop, ]
    }      
  }
  
}

# remove the temporary variables

base::remove(pipedrop, pipeexclude, pipemad, pipemedian, piperows, pipeline_name)

##### d prime for every pipeline ###############################################

# calculate d' for every pipeline because it depends on the total number of target and non-target trials

for (j in 1:length(pipelines_data)) {
  
  # compute index of rows in which the levels change
  
  levelindex <- c(1,which(pipelines_data[[j]]$level != dplyr::lag(pipelines_data[[j]]$level)),nrow(pipelines_data[[j]]))
  
  # set up empty data frame for the loop to feed into
  
  dprime <- data.frame(subject = character(), level = double(), hitrate = double(), falsealarmrate = double())
  
  # calculate hits and false alarms per participant
  
  for (i in 1:(length(levelindex)-1)) {
    
    # set the number of targets and non-targets
    num_targets <- length(which(pipelines_data[[j]]$target[c(levelindex[i]:(levelindex[i+1])-1)] == 1))
    num_nontargets <- length(which(pipelines_data[[j]]$target[c(levelindex[i]:(levelindex[i+1])-1)] == 0))
    
    hits <- length(which(pipelines_data[[j]]$target[c(levelindex[i]:(levelindex[i+1])-1)] == 1 &
                           pipelines_data[[j]]$correct[c(levelindex[i]:(levelindex[i+1])-1)] == 1) + (levelindex[i]-1))
    falsealarms <- length(which(pipelines_data[[j]]$response[c(levelindex[i]:(levelindex[i+1])-1)] == 1 &
                                  pipelines_data[[j]]$correct[c(levelindex[i]:(levelindex[i+1])-1)] == 0) + (levelindex[i]-1))
    newdata <- data.frame(subject = pipelines_data[[j]]$subject[levelindex[i]],
                          level = pipelines_data[[j]]$level[levelindex[i]],
                          hitrate = hits/num_targets,
                          falsealarmrate = falsealarms/num_nontargets)
    dprime <- rbind(dprime, newdata)
    
  }
  
  # z-transform the hit rate and the false alarm rate
  
  dprime$hitrate.z = NA
  dprime$falsealarmrate.z = NA
  
  for (i in 1:4) {
    
    dprime$hitrate.z[which(dprime$level == i)]        <- scale(dprime$hitrate[which(dprime$level == i)])
    dprime$falsealarmrate.z[which(dprime$level == i)] <- scale(dprime$falsealarmrate[which(dprime$level == i)])
    
  }
  
  # calculate d'
  
  dprime$d <- dprime$hitrate.z - dprime$falsealarmrate.z
  
  # feed d' trialwise into the pipeline data frame
  
  for (i in 1:nrow(pipelines_data[[j]])) {
    
    pipelines_data[[j]]$dprime[i] <- dprime$d[dprime$subject == pipelines_data[[j]]$subject[i] & dprime$level == pipelines_data[[j]]$level[i]]
    
  }
}

# remove the temporary variables

base::remove(falsealarms, hits)

##### median RT for every pipeline #############################################

# calculate the median RT for correct and post-correct trials for every pipeline
# per subject and per condition
# the median RT will be another column in the data frames, and will be the same
# within one subject and level, just like the SVs and d prime

for (j in 1:length(pipelines_data)) {
  
  # compute index of rows in which the levels change
  
  levelindex <- c(1,which(pipelines_data[[j]]$level != dplyr::lag(pipelines_data[[j]]$level)),nrow(pipelines_data[[j]]))
  
  # set up empty data frame for the loop to feed into
  
  medianRT <- data.frame(subject = character(), level = double(), medianRT = double())
  
  # calculate median RT per subject and level (only for correct & post-correct trials)
  
  for (i in 1:(length(levelindex)-1)) {
    
    # current level and current subject
    x <- pipelines_data[[j]]$level[levelindex[i]]
    mysubject <- pipelines_data[[j]]$subject[levelindex[i]]
    
    # compute median reaction time
    mymedianRT <- median(pipelines_data[[j]]$rt[pipelines_data[[j]]$level == x & pipelines_data[[j]]$response == 1 & pipelines_data[[j]]$correct == 1 & pipelines_data[[j]]$subject == mysubject], na.rm = TRUE)
    
    # bind data to data frame
    newdata <- data.frame(subject = pipelines_data[[j]]$subject[levelindex[i]],
                          level = pipelines_data[[j]]$level[levelindex[i]],
                          medianRT = mymedianRT)
    medianRT <- rbind(medianRT, newdata)
    
  }
  
  # feed the median RT trialwise into the pipeline data frame
  
  for (i in 1:nrow(pipelines_data[[j]])) {
    
    pipelines_data[[j]]$medianRT[i] <- medianRT$medianRT[medianRT$subject == pipelines_data[[j]]$subject[i] & medianRT$level == pipelines_data[[j]]$level[i]]
    
  }
}

# remove the temporary variables

base::remove(x, mysubject, mymedianRT, newdata, medianRT)

##### Boil all pipelines down to levels per subject, not trials ################

for (j in 1:length(pipelines_data)) {
  
  pipelines_data[[j]] <- unique(pipelines_data[[j]][ ,c("subject","level","sv","nfc","dprime","medianRT")])
  
}

##### Hypothesis 1a ############################################################

# H1a: The signal detection measure d’ declines with increasing n-back level.

# repeated measures ANOVA with three linear contrasts, contrasting the d’ of two n-back levels (2,3,4) at a time

# make a temporary copy of the data frame without 1-back

h1a_data <- pipelines_data[["AARN"]]
h1a_data$level <- as.factor(h1a_data$level)

# calculate ANOVA

hypothesis1a_rmanova <- afex::aov_ez(data = h1a_data,
                                     dv = "dprime",
                                     id = "subject",
                                     within = "level",
                                     type = 3,
                                     include_aov = TRUE)

# obtain estimated marginal means for ANOVA model

hypothesis1a_emm <- emmeans::emmeans(object = hypothesis1a_rmanova$aov,
                                     specs = "level")

# calculate pairwise comparisons on estimated marginal means

hypothesis1a_contrasts <- as.data.frame(pairs(hypothesis1a_emm))

# get Bayes factors

hypothesis1a_BF <- BayesFactor::anovaBF(formula = dprime ~ level, data = h1a_data, progress = FALSE)
hypothesis1a_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h1a_data$dprime[h1a_data$level == 1], y = h1a_data$dprime[h1a_data$level == 2],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1a_data$dprime[h1a_data$level == 1], y = h1a_data$dprime[h1a_data$level == 3],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1a_data$dprime[h1a_data$level == 1], y = h1a_data$dprime[h1a_data$level == 4],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1a_data$dprime[h1a_data$level == 2], y = h1a_data$dprime[h1a_data$level == 3],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1a_data$dprime[h1a_data$level == 2], y = h1a_data$dprime[h1a_data$level == 4],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1a_data$dprime[h1a_data$level == 3], y = h1a_data$dprime[h1a_data$level == 4],
                                                                             progress = FALSE, paired = TRUE))$bf)

# get effect size and confidence interval

hypothesis1a_contrasts <- cbind(hypothesis1a_contrasts,
                                format(effectsize::t_to_eta2(t = hypothesis1a_contrasts$t.ratio, df_error = hypothesis1a_contrasts$df, ci = 0.95), digits = 2))

# rename contrasts and column names, round to two decimals

colnames(hypothesis1a_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis1a_contrasts$Contrast <- gsub("X", "", hypothesis1a_contrasts$Contrast)
hypothesis1a_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- signif(hypothesis1a_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 3)
hypothesis1a_contrasts$`$p$` <- format(round(hypothesis1a_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis1a_contrasts$`$p$`[hypothesis1a_contrasts$`$p$` == "0.000"] <- "<.001"

# remove the temporary variable

base::remove(h1a_data)

##### Hypothesis 1b ############################################################

# H1b: Reaction time increases with increasing n-back level.

# ANOVA with three linear contrasts, contrasting the median rt of two n-back levels (2,3,4) at a time

# make a temporary copy of the data frame

h1b_data <- pipelines_data[["AARO"]]
h1b_data$level <- as.factor(h1b_data$level)

# calculate ANOVA

hypothesis1b_rmanova <- afex::aov_ez(data = h1b_data,
                                     dv = "medianRT",
                                     id = "subject",
                                     within = "level",
                                     type = 3,
                                     include_aov = TRUE)

# obtain estimated marginal means for ANOVA model

hypothesis1b_emm <- emmeans::emmeans(object = hypothesis1b_rmanova$aov,
                                     specs = "level")
# calculate pairwise comparisons on estimated marginal means

hypothesis1b_contrasts <- as.data.frame(pairs(hypothesis1b_emm))

# get Bayes factors

hypothesis1b_BF <- BayesFactor::anovaBF(formula = medianRT ~ level, data = h1b_data, progress = FALSE)
hypothesis1b_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h1b_data$medianRT[h1b_data$level == 1], y = h1b_data$medianRT[h1b_data$level == 2],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1b_data$medianRT[h1b_data$level == 1], y = h1b_data$medianRT[h1b_data$level == 3],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1b_data$medianRT[h1b_data$level == 1], y = h1b_data$medianRT[h1b_data$level == 4],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1b_data$medianRT[h1b_data$level == 2], y = h1b_data$medianRT[h1b_data$level == 3],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1b_data$medianRT[h1b_data$level == 2], y = h1b_data$medianRT[h1b_data$level == 4],
                                                                             progress = FALSE, paired = TRUE))$bf,
                                 BayesFactor::extractBF(BayesFactor::ttestBF(x = h1b_data$medianRT[h1b_data$level == 3], y = h1b_data$medianRT[h1b_data$level == 4],
                                                                             progress = FALSE, paired = TRUE))$bf)

# get effect size and confidence interval

hypothesis1b_contrasts <- cbind(hypothesis1b_contrasts,
                                format(effectsize::t_to_eta2(t = hypothesis1b_contrasts$t.ratio, df_error = hypothesis1b_contrasts$df, ci = 0.95), digits = 2))

# rename contrasts and column names, round to two decimals

colnames(hypothesis1b_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis1b_contrasts$Contrast <- gsub("X", "", hypothesis1b_contrasts$Contrast)
hypothesis1b_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- signif(hypothesis1b_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 3)
hypothesis1b_contrasts$`$p$` <- format(round(hypothesis1b_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis1b_contrasts$`$p$`[hypothesis1b_contrasts$`$p$` == 0.000] <- "<.001"

# remove the temporary variable

base::remove(h1b_data)

##### Hypothesis 1c ############################################################

# H1c: Ratings on all NASA-TLX dimensions increase with increasing n-back level.

# set up empty data frame for the loop to feed into

data_ntlx <- data.frame(subject = character(), level = double(),
                        mental = double(), physical = double(), time = double(),
                        performance = double(), effort = double(), frustration = double(), aversion = double())

# feed NASA-TLX data per participant per level into data frame

for (i in 1:nrow(data_quest)) {
  
  newdata <- data.frame(subject = rep(data_quest$subject[i],4),
                        level = c(1:4),
                        mental = t(data_quest[i,grep("nasa_tlx_1", colnames(data_quest))])[1:4],
                        physical = t(data_quest[i,grep("nasa_tlx_2", colnames(data_quest))])[1:4],
                        time = t(data_quest[i,grep("nasa_tlx_3", colnames(data_quest))])[1:4],
                        performance = t(data_quest[i,grep("nasa_tlx_4", colnames(data_quest))])[1:4],
                        effort = t(data_quest[i,grep("nasa_tlx_5", colnames(data_quest))])[1:4],
                        frustration = t(data_quest[i,grep("nasa_tlx_6", colnames(data_quest))])[1:4],
                        aversion = t(data_quest[i,grep("avers", colnames(data_quest))])[1:4])
  data_ntlx <- rbind(data_ntlx, newdata)
}

# six ANOVAs with six linear contrasts, contrasting the subscale scores of two n-back levels (1,2,3,4) at a time

# make a temporary copy of the NASA-TLX data frame

h1c_data <- data_ntlx
h1c_data$level <- as.factor(h1c_data$level)

# calculate ANOVAs

hypothesis1c_mental_rmanova <- afex::aov_ez(data = h1c_data,
                                            dv = "mental", id = "subject", within = "level",
                                            type = 3, include_aov = TRUE)
hypothesis1c_physical_rmanova <- afex::aov_ez(data = h1c_data,
                                              dv = "physical", id = "subject", within = "level",
                                              type = 3, include_aov = TRUE)
hypothesis1c_time_rmanova <- afex::aov_ez(data = h1c_data,
                                          dv = "time", id = "subject", within = "level",
                                          type = 3, include_aov = TRUE)
hypothesis1c_performance_rmanova <- afex::aov_ez(data = h1c_data,
                                                 dv = "performance", id = "subject", within = "level",
                                                 type = 3, include_aov = TRUE)
hypothesis1c_effort_rmanova <- afex::aov_ez(data = h1c_data,
                                            dv = "effort", id = "subject", within = "level",
                                            type = 3, include_aov = TRUE)
hypothesis1c_frustration_rmanova <- afex::aov_ez(data = h1c_data,
                                                 dv = "frustration", id = "subject", within = "level",
                                                 type = 3, include_aov = TRUE)

# obtain estimated marginal means for ANOVA model and
# calculate pairwise comparisons on estimated marginal means

hypothesis1c_mental_emm <- emmeans::emmeans(object = hypothesis1c_mental_rmanova$aov, specs = "level")
hypothesis1c_mental_contrasts <- as.data.frame(pairs(hypothesis1c_mental_emm))

hypothesis1c_physical_emm <- emmeans::emmeans(object = hypothesis1c_physical_rmanova$aov, specs = "level")
hypothesis1c_physical_contrasts <- as.data.frame(pairs(hypothesis1c_physical_emm))

hypothesis1c_time_emm <- emmeans::emmeans(object = hypothesis1c_time_rmanova$aov, specs = "level")
hypothesis1c_time_contrasts <- as.data.frame(pairs(hypothesis1c_time_emm))

hypothesis1c_performance_emm <- emmeans::emmeans(object = hypothesis1c_performance_rmanova$aov, specs = "level")
hypothesis1c_performance_contrasts <- as.data.frame(pairs(hypothesis1c_performance_emm))

hypothesis1c_effort_emm <- emmeans::emmeans(object = hypothesis1c_effort_rmanova$aov, specs = "level")
hypothesis1c_effort_contrasts <- as.data.frame(pairs(hypothesis1c_effort_emm))

hypothesis1c_frustration_emm <- emmeans::emmeans(object = hypothesis1c_frustration_rmanova$aov, specs = "level")
hypothesis1c_frustration_contrasts <- as.data.frame(pairs(hypothesis1c_frustration_emm))

# get Bayes factors

hypothesis1c_mental_BF <- BayesFactor::anovaBF(formula = mental ~ level, data = h1c_data, progress = FALSE)
hypothesis1c_mental_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$mental[h1c_data$level == 1], y = h1c_data$mental[h1c_data$level == 2],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$mental[h1c_data$level == 1], y = h1c_data$mental[h1c_data$level == 3],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$mental[h1c_data$level == 1], y = h1c_data$mental[h1c_data$level == 4],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$mental[h1c_data$level == 2], y = h1c_data$mental[h1c_data$level == 3],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$mental[h1c_data$level == 2], y = h1c_data$mental[h1c_data$level == 4],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$mental[h1c_data$level == 3], y = h1c_data$mental[h1c_data$level == 4],
                                                                                    progress = FALSE, paired = TRUE))$bf)
hypothesis1c_physical_BF <- BayesFactor::anovaBF(formula = physical ~ level, data = h1c_data, progress = FALSE)
hypothesis1c_physical_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$physical[h1c_data$level == 1], y = h1c_data$physical[h1c_data$level == 2],
                                                                                      progress = FALSE, paired = TRUE))$bf,
                                          BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$physical[h1c_data$level == 1], y = h1c_data$physical[h1c_data$level == 3],
                                                                                      progress = FALSE, paired = TRUE))$bf,
                                          BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$physical[h1c_data$level == 1], y = h1c_data$physical[h1c_data$level == 4],
                                                                                      progress = FALSE, paired = TRUE))$bf,
                                          BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$physical[h1c_data$level == 2], y = h1c_data$physical[h1c_data$level == 3],
                                                                                      progress = FALSE, paired = TRUE))$bf,
                                          BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$physical[h1c_data$level == 2], y = h1c_data$physical[h1c_data$level == 4],
                                                                                      progress = FALSE, paired = TRUE))$bf,
                                          BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$physical[h1c_data$level == 3], y = h1c_data$physical[h1c_data$level == 4],
                                                                                      progress = FALSE, paired = TRUE))$bf)
hypothesis1c_time_BF <- BayesFactor::anovaBF(formula = time ~ level, data = h1c_data, progress = FALSE)
hypothesis1c_time_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$time[h1c_data$level == 1], y = h1c_data$time[h1c_data$level == 2],
                                                                                  progress = FALSE, paired = TRUE))$bf,
                                      BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$time[h1c_data$level == 1], y = h1c_data$time[h1c_data$level == 3],
                                                                                  progress = FALSE, paired = TRUE))$bf,
                                      BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$time[h1c_data$level == 1], y = h1c_data$time[h1c_data$level == 4],
                                                                                  progress = FALSE, paired = TRUE))$bf,
                                      BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$time[h1c_data$level == 2], y = h1c_data$time[h1c_data$level == 3],
                                                                                  progress = FALSE, paired = TRUE))$bf,
                                      BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$time[h1c_data$level == 2], y = h1c_data$time[h1c_data$level == 4],
                                                                                  progress = FALSE, paired = TRUE))$bf,
                                      BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$time[h1c_data$level == 3], y = h1c_data$time[h1c_data$level == 4],
                                                                                  progress = FALSE, paired = TRUE))$bf)
hypothesis1c_performance_BF <- BayesFactor::anovaBF(formula = performance ~ level, data = h1c_data, progress = FALSE)
hypothesis1c_performance_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$performance[h1c_data$level == 1], y = h1c_data$performance[h1c_data$level == 2],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$performance[h1c_data$level == 1], y = h1c_data$performance[h1c_data$level == 3],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$performance[h1c_data$level == 1], y = h1c_data$performance[h1c_data$level == 4],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$performance[h1c_data$level == 2], y = h1c_data$performance[h1c_data$level == 3],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$performance[h1c_data$level == 2], y = h1c_data$performance[h1c_data$level == 4],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$performance[h1c_data$level == 3], y = h1c_data$performance[h1c_data$level == 4],
                                                                                         progress = FALSE, paired = TRUE))$bf)
hypothesis1c_effort_BF <- BayesFactor::anovaBF(formula = effort ~ level, data = h1c_data, progress = FALSE)
hypothesis1c_effort_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$effort[h1c_data$level == 1], y = h1c_data$effort[h1c_data$level == 2],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$effort[h1c_data$level == 1], y = h1c_data$effort[h1c_data$level == 3],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$effort[h1c_data$level == 1], y = h1c_data$effort[h1c_data$level == 4],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$effort[h1c_data$level == 2], y = h1c_data$effort[h1c_data$level == 3],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$effort[h1c_data$level == 2], y = h1c_data$effort[h1c_data$level == 4],
                                                                                    progress = FALSE, paired = TRUE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$effort[h1c_data$level == 3], y = h1c_data$effort[h1c_data$level == 4],
                                                                                    progress = FALSE, paired = TRUE))$bf)
hypothesis1c_frustration_BF <- BayesFactor::anovaBF(formula = frustration ~ level, data = h1c_data, progress = FALSE)
hypothesis1c_frustration_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$frustration[h1c_data$level == 1], y = h1c_data$frustration[h1c_data$level == 2],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$frustration[h1c_data$level == 1], y = h1c_data$frustration[h1c_data$level == 3],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$frustration[h1c_data$level == 1], y = h1c_data$frustration[h1c_data$level == 4],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$frustration[h1c_data$level == 2], y = h1c_data$frustration[h1c_data$level == 3],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$frustration[h1c_data$level == 2], y = h1c_data$frustration[h1c_data$level == 4],
                                                                                         progress = FALSE, paired = TRUE))$bf,
                                             BayesFactor::extractBF(BayesFactor::ttestBF(x = h1c_data$frustration[h1c_data$level == 3], y = h1c_data$frustration[h1c_data$level == 4],
                                                                                         progress = FALSE, paired = TRUE))$bf)

# get effect sizes and confidence intervals

hypothesis1c_mental_contrasts <- cbind(hypothesis1c_mental_contrasts,
                                       format(effectsize::t_to_eta2(t = hypothesis1c_mental_contrasts$t.ratio,
                                                                    df_error = hypothesis1c_mental_contrasts$df, ci = 0.95), digits = 2))

hypothesis1c_physical_contrasts <- cbind(hypothesis1c_physical_contrasts,
                                         format(effectsize::t_to_eta2(t = hypothesis1c_physical_contrasts$t.ratio,
                                                                      df_error = hypothesis1c_physical_contrasts$df, ci = 0.95), digits = 2))

hypothesis1c_time_contrasts <- cbind(hypothesis1c_time_contrasts,
                                     format(effectsize::t_to_eta2(t = hypothesis1c_time_contrasts$t.ratio,
                                                                  df_error = hypothesis1c_time_contrasts$df, ci = 0.95), digits = 2))

hypothesis1c_effort_contrasts <- cbind(hypothesis1c_effort_contrasts,
                                       format(effectsize::t_to_eta2(t = hypothesis1c_effort_contrasts$t.ratio,
                                                                    df_error = hypothesis1c_effort_contrasts$df, ci = 0.95), digits = 2))

hypothesis1c_frustration_contrasts <- cbind(hypothesis1c_frustration_contrasts,
                                            format(effectsize::t_to_eta2(t = hypothesis1c_frustration_contrasts$t.ratio,
                                                                         df_error = hypothesis1c_frustration_contrasts$df, ci = 0.95), digits = 2))

hypothesis1c_performance_contrasts <- cbind(hypothesis1c_performance_contrasts,
                                            format(effectsize::t_to_eta2(t = hypothesis1c_performance_contrasts$t.ratio,
                                                                         df_error = hypothesis1c_performance_contrasts$df, ci = 0.95), digits = 2))

# rename columns and contrasts, round to two decimals

colnames(hypothesis1c_mental_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis1c_mental_contrasts$Contrast <- gsub("X", "", hypothesis1c_mental_contrasts$Contrast)
hypothesis1c_mental_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- signif(hypothesis1c_mental_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 3)
hypothesis1c_mental_contrasts$`$p$` <- format(round(hypothesis1c_mental_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis1c_mental_contrasts$`$p$`[hypothesis1c_mental_contrasts$`$p$` == "0.000"] <- "<.001"

colnames(hypothesis1c_physical_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis1c_physical_contrasts$Contrast <- gsub("X", "", hypothesis1c_physical_contrasts$Contrast)
hypothesis1c_physical_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- signif(hypothesis1c_physical_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 3)
hypothesis1c_physical_contrasts$`$p$` <- format(round(hypothesis1c_physical_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis1c_physical_contrasts$`$p$`[hypothesis1c_physical_contrasts$`$p$` == "0.000"] <- "<.001"

colnames(hypothesis1c_performance_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis1c_performance_contrasts$Contrast <- gsub("X", "", hypothesis1c_performance_contrasts$Contrast)
hypothesis1c_performance_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- signif(hypothesis1c_performance_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 3)
hypothesis1c_performance_contrasts$`$p$` <- format(round(hypothesis1c_performance_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis1c_performance_contrasts$`$p$`[hypothesis1c_performance_contrasts$`$p$` == "0.000"] <- "<.001"

colnames(hypothesis1c_effort_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis1c_effort_contrasts$Contrast <- gsub("X", "", hypothesis1c_effort_contrasts$Contrast)
hypothesis1c_effort_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- signif(hypothesis1c_effort_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 3)
hypothesis1c_effort_contrasts$`$p$` <- format(round(hypothesis1c_effort_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis1c_effort_contrasts$`$p$`[hypothesis1c_effort_contrasts$`$p$` == "0.000"] <- "<.001"

colnames(hypothesis1c_frustration_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis1c_frustration_contrasts$Contrast <- gsub("X", "", hypothesis1c_frustration_contrasts$Contrast)
hypothesis1c_frustration_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- signif(hypothesis1c_frustration_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 3)
hypothesis1c_frustration_contrasts$`$p$` <- format(round(hypothesis1c_frustration_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis1c_frustration_contrasts$`$p$`[hypothesis1c_frustration_contrasts$`$p$` == "0.000"] <- "<.001"

colnames(hypothesis1c_time_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis1c_time_contrasts$Contrast <- gsub("X", "", hypothesis1c_time_contrasts$Contrast)
hypothesis1c_time_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- signif(hypothesis1c_time_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 3)
hypothesis1c_time_contrasts$`$p$` <- format(round(hypothesis1c_time_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis1c_time_contrasts$`$p$`[hypothesis1c_time_contrasts$`$p$` == "0.000"] <- "<.001"


##### Hypothesis 2a ############################################################

# H2a: Subjective values decline with increasing n-back level.

# ANOVA with six linear contrasts, contrasting the SVs of two n-back levels (1,2,3,4) at a time

# make a temporary copy of the data frame

h2a_data <- pipelines_data[["AARO"]][ ,c("subject","level","sv")]
h2a_data$level <- as.factor(h2a_data$level)

# calculate ANOVA

hypothesis2a_rmanova <- afex::aov_ez(data = h2a_data,
                                     dv = "sv", id = "subject", within = "level",
                                     type = 3, include_aov = TRUE)

# obtain estimated marginal means for ANOVA model

hypothesis2a_emm <- emmeans::emmeans(object = hypothesis2a_rmanova$aov,
                                     specs = "level")

# calculate pairwise comparisons on estimated marginal means

hypothesis2a_contrasts <- emmeans::contrast(hypothesis2a_emm, method = list("Declining Linear" = c(3,1,-1,-3),
                                                                            "Ascending Quadratic" = c(-1,1,1,-1),
                                                                            "Declining Logistic" = c(3,2,-2,-3),
                                                                            "Positively Skewed Normal" = c(1,2,-1,-2)))

# we still have to get the Bayes Factors here, but we'll do that in the main study

# get effect size and confidence intervals

hypothesis2a_contrasts <- as.data.frame(hypothesis2a_contrasts)
hypothesis2a_contrasts <- cbind(hypothesis2a_contrasts,
                                format(effectsize::t_to_eta2(t = hypothesis2a_contrasts$t.ratio, df_error = hypothesis2a_contrasts$df, ci = 0.95), digits = 2))

# rename columns and contrasts

colnames(hypothesis2a_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis2a_contrasts$Contrast <- gsub("X", "", hypothesis2a_contrasts$Contrast)
hypothesis2a_contrasts[ ,c("Estimate","$SE$","$t$")] <- signif(hypothesis2a_contrasts[ ,c("Estimate","$SE$","$t$")], digits = 3)
hypothesis2a_contrasts$`$p$` <- format(round(hypothesis2a_contrasts$`$p$`, digits = 3), nsmall = 2)
hypothesis2a_contrasts$`$p$`[hypothesis2a_contrasts$`$p$` == "0.000"] <- "<.001"

# remove the temporary variable

base::remove(h2a_data)

##### Hypothesis 2b ############################################################

# H2b: Subjective values decline with increasing n-back level, even after controlling for declining task
# performance measured by signal detection d’ and reaction time.

# detach afex in order to use lmerTest

detach_package <- function(pkg, character.only = FALSE){
  if(!character.only){
    pkg <- deparse(substitute(pkg))
  }
  search_item <- paste("package", pkg, sep = ":")
  while(search_item %in% search()){
    detach(search_item, unload = TRUE, character.only = TRUE)
  }
}

detach_package(afex)

## get all relevant variables ------------------------------------------------

h2b_data <- pipelines_data[["AARO"]]

# get subset for MLM without RT = NA

h2b_data <- droplevels(subset(h2b_data[ ,c("subject", "level", "sv", "dprime", "medianRT")],
                              subset = !is.na(sv)))


## center predictors ---------------------------------------------------------

## center level 1 predictors
# two ways: centering at the grand mean (CGM) vs. centering within cluster (CWC) = group mean centering
# level 1 predictor (SV) is of substantive interest
# > CWC

# dprime
h2b_data$dprime.cwc <- h2b_data$dprime - (ave(h2b_data$dprime, h2b_data$subject, FUN = function(x) mean(x, na.rm = T)))

# medianRT
h2b_data$medianRT.cwc <- h2b_data$medianRT - (ave(h2b_data$medianRT, h2b_data$subject, FUN = function(x) mean(x, na.rm = T)))

# level
h2b_data$level.cwc <- h2b_data$level - (ave(h2b_data$level, h2b_data$subject, FUN = function(x) mean(x, na.rm = T)))


## no level 2 predictors
# > CGM



## the following analyses for h2b depend on the actual relation of sv and level
# that is examined by the previous ANOVAs in H2a and indicated by model fit

## A - linear relation (linear mixed model) ----------------------------------

### null model ----

m0_h2b <- lmerTest::lmer(sv ~ 1 + (1|subject), 
                         data = h2b_data,
                         REML = T)

# intraclass correlation (ICC)
var_m0_h2b <- as.data.frame(lme4::VarCorr(m0_h2b))
icc_h2b <- var_m0_h2b$vcov[1] / (var_m0_h2b$vcov[1] + var_m0_h2b$vcov[2]) 


### random slopes model ----

## maximal model
m1_h2b <- lmerTest::lmer(sv ~ level.cwc + dprime.cwc + medianRT.cwc + (level.cwc|subject), 
                         data = h2b_data,
                         REML = T) # parameters estimated by restricted log-likelihood maximization
# boundary (singular) fit: see help('isSingular') <- model is over-specified

# check different optimizer
m2_h2b <- lmerTest::lmer(sv ~ level.cwc + dprime.cwc + medianRT.cwc + (level.cwc|subject), 
                         data = h2b_data,
                         REML = T, # parameters estimated by restricted log-likelihood maximization
                         control = lme4::lmerControl(optimizer = "nloptwrap", optCtrl = list(algorithm = "NLOPT_LN_NELDERMEAD")))

## perform model criticism

# identify potential outliers that do not fit within the model
potential_outliers_m2_h2b <- subset(h2b_data, abs(scale(resid(m2_h2b))) > 3)    # 1 obs.
100/60*1
# [1] 1.666667 = 1.7 %

# exclude outliers
h2b_data_norm <- droplevels(subset(h2b_data, abs(scale(resid(m2_h2b))) < 3))

m3_h2b <- lmerTest::lmer(sv ~ level.cwc + dprime.cwc + medianRT.cwc + (level.cwc|subject),
                         data = h2b_data_norm,
                         REML = T) # parameters estimated by restricted log-likelihood maximization
# boundary (singular) fit: see help('isSingular')

# check different optimizer  
m4_h2b <- lmerTest::lmer(sv ~ level.cwc + dprime.cwc + medianRT.cwc + (level.cwc|subject),
                         data = h2b_data_norm,
                         REML = T,
                         control = lme4::lmerControl(optimizer = "nmkbw"))
# m4_h2b is the final model

## plot model fit of the final model
m4_h2b_fit <- sjPlot::plot_model(m4_h2b, type = "diag")


### get pseudo-r-squared ----

## for the whole model
h2b_total_r2 <- MuMIn::r.squaredGLMM(m4_h2b, pj2014 = T)

## for n-back level
# model without effect
m4_h2b_without <- lmerTest::lmer(sv ~ 1 + dprime.cwc + medianRT.cwc + (level.cwc|subject),
                                 data = h2b_data_norm,
                                 control = lme4::lmerControl(optimizer = "nmkbw"))
# calculate R²
h2b_without_r2 <- MuMIn::r.squaredGLMM(m4_h2b_without, pj2014 = T)

# calculate f² with conditional R²
h2b_f2 <- (h2b_total_r2[1,2] - h2b_without_r2[1,2]) / (1 - h2b_total_r2[1,2])


### get Bayes Factors ----

# the random factor needs to be a factor
h2b_data$subject <- factor(h2b_data$subject)

# H2b
h2b_full_BF <- BayesFactor::lmBF(sv ~ level.cwc + dprime.cwc + medianRT.cwc + subject,
                                 data = h2b_data_norm, whichRandom = 'subject', progress = FALSE)
h2b_null_BF <- BayesFactor::lmBF(sv ~ 1 + dprime.cwc + medianRT.cwc + subject,
                                 data = h2b_data_norm, whichRandom = 'subject', progress = FALSE)
h2b_BF <- h2b_full_BF / h2b_null_BF


### prepare MLM results for reporting ----

# get random and fixed effects
m4_h2b.ranef <- as.data.frame(base::summary(m4_h2b)$varcor)
m4_h2b.fixef <- base::summary(m4_h2b)$coefficients

# prepare table
h2b_result.table <- as.data.frame(cbind(row.names(m4_h2b.fixef), 
                                        m4_h2b.fixef[,c(1, 2, 5)]))
h2b_result.table$ranef.sd <- NA
h2b_result.table$ranef.sd[c(1,2)] <- m4_h2b.ranef$sdcor[c(1,2)]

colnames(h2b_result.table)[1] <- "Parameter"
colnames(h2b_result.table)[2] <- "Beta"
colnames(h2b_result.table)[3] <- "$SE$"
colnames(h2b_result.table)[4] <- "$p$-value"
colnames(h2b_result.table)[5] <- "Random Effects (SD)"

row.names(h2b_result.table) <- NULL
h2b_result.table$Parameter[1:4] <- c("Intercept", "$N$-back level", "d'", "median RT")

h2b_result.table[2:5] <- lapply(h2b_result.table[2:5], as.numeric)
h2b_result.table[c(2,3,5)] <- round(h2b_result.table[c(2,3,5)], digits = 2)
h2b_result.table[4] <- round(h2b_result.table[4], digits = 3)

h2b_result.table$ `$p$-value`[which(h2b_result.table$ `$p$-value`<.01)] <- 
  paste0(h2b_result.table$ `$p$-value`[which(h2b_result.table$ `$p$-value`<.01)],"*")
h2b_result.table$ `$p$-value`[which(h2b_result.table$ `$p$-value`<.05)] <- 
  paste0(h2b_result.table$ `$p$-value`[which(h2b_result.table$ `$p$-value`<.05)],"*")
h2b_result.table$ `$p$-value`[which(h2b_result.table$ `$p$-value`<.001)] <- 
  paste0("<.001***")

h2b_result.table$ `Random Effects (SD)`[3:4] <- paste0("")



## B - declining linear relation (nonlinear mixed model) ---------------------
## C - ascending quadratic relation (nonlinear mixed model) ------------------
## D - declining logistic relation (nonlinear mixed model) -------------------

# H2b: Subjective values decline with increasing n-back level, even after controlling for declining task
# performance measured by signal detection d’ and reaction time.

# detach afex in order to use lmerTest

detach_package <- function(pkg, character.only = FALSE){
  if(!character.only){
    pkg <- deparse(substitute(pkg))
  }
  search_item <- paste("package", pkg, sep = ":")
  while(search_item %in% search()){
    detach(search_item, unload = TRUE, character.only = TRUE)
  }
}

detach_package(afex)

# make a temporary copy of the data frame

h2b_data <- pipelines_data[["AARO"]]

# get a subset without NFC

h2b_data <- droplevels(subset(h2b_data[ ,c("subject", "level", "sv", "dprime", "medianRT")]))


# turn n-back levels into contrasts

#h2b_data$levelcontrast <- rep(c(3,2,-2,-3),nrow(h2b_data)/4)

# center the level 1 predictors within cluster

#h2b_data$dprime.cwc         <- h2b_data$dprime - (ave(h2b_data$dprime, h2b_data$subject, FUN = function(x) mean(x, na.rm = T)))
#h2b_data$medianRT.cwc       <- h2b_data$medianRT - (ave(h2b_data$medianRT, h2b_data$subject, FUN = function(x) mean(x, na.rm = T)))
#h2b_data$levelcontrast.cwc  <- h2b_data$levelcontrast - (ave(h2b_data$levelcontrast, h2b_data$subject, FUN = function(x) mean(x, na.rm = T)))
#h2b_data$level.cwc          <- h2b_data$level - (ave(h2b_data$level, h2b_data$subject, FUN = function(x) mean(x, na.rm = T)))

#h2b_data$level.cwc <- as.factor(h2b_data$level.cwc)

# define contrasts

#h2b_contrasts <- c(3,2,-2,-3)
#contrasts(h2b_data$level) <- cbind(h2b_contrasts, c(-1,1,0,0), c(0,0,-1,1))

# define the null model

#m0_h2b <- lmerTest::lmer(sv ~ 1 + (1|subject), data = h2b_data, REML = T)

# get intraclass correlation (ICC)

#var_m0_h2b <- as.data.frame(lme4::VarCorr(m0_h2b))
#icc_h2b <- var_m0_h2b$vcov[1] / (var_m0_h2b$vcov[1] + var_m0_h2b$vcov[2]) 

# our model (this is not a random slopes model, because we have to replace (level.cwc|subject) with (1|subject), because
# this model contains the level as a factor which does not allow repeated measures)


#m1_h2b <- lmerTest::lmer(sv ~ levelcontrast.cwc + dprime.cwc + medianRT.cwc + (levelcontrast.cwc|subject),
#                         data = h2b_data, REML = T)

# model 2 with an actual contrast matrix

#m2_h2b <- lmerTest::lmer(sv ~ level.cwc + dprime.cwc + medianRT.cwc + (level.cwc|subject),
#                         data = h2b_data, REML = T)



# A custom model structure (inspired by the answer to this post
# https://stackoverflow.com/questions/15141952/nlmer-longitudinal-data):
# 
# customlog <- function(level, asym, asym2, asym3, a2, xmid, scal, dprime, medianRT) 
# {
#   # taken from ?SSdlf:
#   # y = ((asym - a2) / (1 + exp((xmid - time)/scal))) + a2
#   # add dprime- and medianRT-specific terms to Asym2
#   (((asym - a2) + ((asym2*dprime)-a2) + ((asym3*medianRT)-a2)) / (1 + exp((xmid - level)/scal))) + a2
#   # evaluation of above form is returned by this function
# }
# 
# model gradient which includes all fixed effects but no covariates
# 
# customlog_gradient <- deriv(
#   body(customlog)[[2]], 
#   namevec = c("asym", "asym2", "asym3", "a2", "xmid", "scal"), 
#   function.arg=customlog
# )
# 
# # fit nonlinear models to get starting values (the cwc-variables didn't work because log turned 0 to infinity)
# 
# fit1 <- nls(formula = sv ~ SSdlf(level, asym, a2, xmid, scal), data = h2b_data)
# fit2 <- nls(formula = sv ~ SSdlf(dprime, asym, a2, xmid, scal), data = h2b_data)
# fit3 <- nls(formula = sv ~ SSdlf(medianRT, asym, a2, xmid, scal), data = h2b_data) # this one gives a singular gradient error
#
# if you want to see how the predicted curve looks like
# plot(sv ~ level.cwc, dat = h2b_data)
# curve(predict(fit1, newdata = data.frame(level.cwc=x)), add=TRUE
#
# m3_h2b <- lme4::nlmer(
#   # response
#   sv ~ 
#   # fixed effects
#   customlog_gradient(level = level, asym, asym2, asym3, a2, xmid, scal, dprime = dprime, medianRT = medianRT) ~ 
#   # random effects
#   (asym | subject) + (xmid | subject), 
#   # Data
#   data = h2b_data,
#   start = c(asym = summary(fit1)$parameters["asym","Estimate"],
#             asym2 = summary(fit2)$parameters["asym","Estimate"],
#             asym3 = summary(fit3)$parameters["asym","Estimate"],
#             a2 = 0.5, xmid = 0, scal = -0.6))





## E - positively skewed normal (nonlinear mixed model) ----------------------


##### Hypothesis 3a ############################################################

# H3a: Participants with higher NFC scores have higher subjective values for
# 2- and 3-back but lower subjective values for 1-back than participants with
# lower NFC scores.

# make a temporary copy of the data frame

data_SV <- pipelines_data[["AARO"]][ ,c("subject","level","sv","nfc")]

# create a data frame with the difference scores per subject (2-1,3-2)

diffscores <- diff(data_SV$sv)
h3a_data <- data.frame(subject = data_SV$subject[c(seq(from = 1, to = nrow(data_SV), length.out = nrow(data_SV)/2))],
                       nlevels = as.factor(rep(c("1-2","2-3"), nrow(data_SV)/4)),
                       svdiff = c(rbind(diffscores[c(seq(from = 1, to = nrow(data_SV), by = 4))],diffscores[c(seq(from = 2, to = nrow(data_SV), by = 4))])),
                       nfc = data_SV$nfc[c(seq(from = 1, to = nrow(data_SV), length.out = nrow(data_SV)/2))])

# add column indicating NFC score above or below median

mediannfc <- median(h3a_data$nfc, na.rm = TRUE)
h3a_data$nfcmedian <- ifelse(h3a_data$nfc < mediannfc, "low", "high")
h3a_data$nfcmedian <- as.factor(h3a_data$nfcmedian)

# compute two-way ANOVA

hypothesis3a_model <- afex::aov_ez("subject", "svdiff", h3a_data,
                                   between = c("nfcmedian"), within = c("nlevels"))

# format S3 class into data frame

hypothesis3a_rmanova <- summary(hypothesis3a_model)
hypothesis3a_rmanova <- hypothesis3a_rmanova[["univariate.tests"]]
hypothesis3a_rmanova <- as.data.frame(matrix(hypothesis3a_rmanova, nrow = 4, ncol = 6))


# get effect size

hypothesis3a_rmanova <- cbind(hypothesis3a_rmanova,
                              format(effectsize::F_to_eta2(f = hypothesis3a_rmanova[,5], df = hypothesis3a_rmanova[,2],
                                                           df_error = hypothesis3a_rmanova[,4], ci = 0.95), digits = 2))

# formatting

colnames(hypothesis3a_rmanova) <- c("Sum Sq", "$df$", "error Sum Sq", "error $df$", "$F$", "$p$", "$\\eta_{p}^{2}$", "$95\\% CI$")
rownames(hypothesis3a_rmanova) <- c("Intercept", "NFC group", "n-back level", "NFC group x n-back level")
hypothesis3a_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")] <- signif(hypothesis3a_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")], digits = 3)
hypothesis3a_rmanova$`$p$` <- format(round(hypothesis3a_rmanova$`$p$`, digits = 3), nsmall = 2)
hypothesis3a_rmanova$`$p$`[hypothesis3a_rmanova$`$p$` == "0.000"] <- "<.001"

## post-hoc tests for the n-back levels

# obtain estimated marginal means for ANOVA model

hypothesis3a_emm_nlevel <- emmeans::emmeans(object = hypothesis3a_model, "nlevels")

# calculate pairwise comparisons on estimated marginal means

hypothesis3a_contrasts_nlevel <- as.data.frame(pairs(hypothesis3a_emm_nlevel))

# get Bayes factors

hypothesis3a_BF_nlevel <- BayesFactor::anovaBF(formula = svdiff ~ nlevels * nfcmedian, data = h3a_data, progress = FALSE)
hypothesis3a_contrasts_nlevel$BF10 <- extractBF(hypothesis3a_BF_nlevel[1])$bf

# get effect size

hypothesis3a_contrasts_nlevel <- cbind(hypothesis3a_contrasts_nlevel,
                                    format(effectsize::t_to_eta2(t = hypothesis3a_contrasts_nlevel$t.ratio,
                                                                 df_error = hypothesis3a_contrasts_nlevel$df, ci = 0.95), digits = 2))

# rename columns and contrasts, round to two decimals

colnames(hypothesis3a_contrasts_nlevel) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis3a_contrasts_nlevel$Contrast <- c("1-2 - 2-3")
hypothesis3a_contrasts_nlevel[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis3a_contrasts_nlevel[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
hypothesis3a_contrasts_nlevel$`$p$` <- format(round(hypothesis3a_contrasts_nlevel$`$p$`, digits = 3), nsmall = 2)
hypothesis3a_contrasts_nlevel$`$p$`[hypothesis3a_contrasts_nlevel$`$p$` == "0.000"] <- "<.001"

# prepare raincloud plot for main effect of n-back levels

plot_h3a_data_nlevel <- raincloudplots::data_1x1(array_1 = h3a_data$svdiff[h3a_data$nlevels == "1-2"],
                          array_2 = h3a_data$svdiff[h3a_data$nlevels == "2-3"],
                          jit_distance = .09,
                          jit_seed = 73)

raincloudplots::raincloud_1x1_repmes(data_1x1 = plot_h3a_data_nlevel,
                                 size = 2,
                                 alpha = .6) +
  xlab("n-back levels") + 
  ylab("Difference in subjective values") +
  ggprism::theme_prism(base_size = 12, base_line_size = 0.8, base_fontface = "plain", base_family = "sans") +
  scale_x_continuous(breaks=c(1,2), labels=c("1-2", "2-3"), limits=c(0, 3))

# prepare another raincloud plot to show the (non-significant) effect of NFC

plot_h3a_data_nfc <- raincloudplots::data_2x2(array_1 = h3a_data$svdiff[h3a_data$nlevels == "1-2" & h3a_data$nfcmedian == "low"],
                                          array_2 = h3a_data$svdiff[h3a_data$nlevels == "2-3" & h3a_data$nfcmedian == "low"],
                                          array_3 = h3a_data$svdiff[h3a_data$nlevels == "1-2" & h3a_data$nfcmedian == "high"],
                                          array_4 = h3a_data$svdiff[h3a_data$nlevels == "2-3" & h3a_data$nfcmedian == "high"],
                                          labels = (c("NFC below median","NFC above median")), # blue is below, orange is above
                                          jit_distance = .09,
                                          jit_seed = 73,
                                          spread_x_ticks = FALSE)

raincloudplots::raincloud_2x2_repmes(data_2x2 = plot_h3a_data_nfc,
                                     size = 2,
                                     alpha = .6,
                                     spread_x_ticks = FALSE) +
  xlab("n-back levels") + 
  ylab("Difference in subjective values") +
  ggprism::theme_prism(base_size = 12, base_line_size = 0.8, base_fontface = "plain", base_family = "sans") +
  scale_x_continuous(breaks=c(1,2), labels=c("1-2", "2-3"), limits=c(0, 3))

# remove temporary variables

base::remove(diffscores, mediannfc, h3a_data, plot_h3a_data)

##### Hypothesis 3b ############################################################

# H3b: NASA-TLX scores are lower in every n-back level for participants with high NFC.

# make a temporary copy of the data frame

h3b_data <- pipelines_data[["AARO"]][ ,c("subject","level","nfc")]

# compute column containing the average of the NASA-TLX subscales per level per subject

ntlx <- data.frame(subject = data_ntlx$subject,
                   level = data_ntlx$level,
                   ntlx = rowMeans(data_ntlx[ ,c("physical","mental","time","effort","performance","frustration")]))

# merge data frames based on subject

h3b_data <- merge(h3b_data, ntlx)

# add column indicating NFC score above or below median

mediannfc <- median(h3b_data$nfc)
h3b_data$nfcmedian <- ifelse(h3b_data$nfc < mediannfc, "low", "high")
h3b_data$nfcmedian <- as.factor(h3b_data$nfcmedian)
h3b_data$level <- as.factor(h3b_data$level)

# compute two-way ANOVA

hypothesis3b_model <- afex::aov_ez("subject", "ntlx", h3b_data,
                                   between = c("nfcmedian"), within = c("level"))

# format S3 class into data frame

hypothesis3b_rmanova <- summary(hypothesis3b_model)
hypothesis3b_rmanova <- hypothesis3b_rmanova[["univariate.tests"]]
hypothesis3b_rmanova <- as.data.frame(matrix(hypothesis3b_rmanova, nrow = 4, ncol = 6))


# get effect size

hypothesis3b_rmanova <- cbind(hypothesis3b_rmanova,
                              format(effectsize::F_to_eta2(f = hypothesis3b_rmanova[,5], df = hypothesis3b_rmanova[,2],
                                                           df_error = hypothesis3b_rmanova[,4], ci = 0.95), digits = 2))

# formatting

colnames(hypothesis3b_rmanova) <- c("Sum Sq", "$df$", "error Sum Sq", "error $df$", "$F$", "$p$", "$\\eta_{p}^{2}$", "$95\\% CI$")
rownames(hypothesis3b_rmanova) <- c("Intercept", "NFC group", "n-back level", "NFC group x n-back level")
hypothesis3b_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")] <- signif(hypothesis3b_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")], digits = 3)
hypothesis3b_rmanova$`$p$` <- format(round(hypothesis3b_rmanova$`$p$`, digits = 3), nsmall = 2)
hypothesis3b_rmanova$`$p$`[hypothesis3b_rmanova$`$p$` == "0.000"] <- "<.001"

## post-hoc tests for the n-back levels

# obtain estimated marginal means for ANOVA model

hypothesis3b_emm_levels <- emmeans::emmeans(object = hypothesis3b_model, "level")

# calculate pairwise comparisons on estimated marginal means

hypothesis3b_contrasts_levels <- as.data.frame(pairs(hypothesis3b_emm_levels))

# get Bayes factors

hypothesis3b_BF_levels <- anovaBF(formula = ntlx ~ level * nfcmedian, data = h3b_data, progress = FALSE)
hypothesis3b_contrasts_levels$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 1], y = h3b_data$ntlx[h3b_data$level == 2],
                                                                                    progress = FALSE, paired = FALSE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 1], y = h3b_data$ntlx[h3b_data$level == 3],
                                                                                    progress = FALSE, paired = FALSE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 1], y = h3b_data$ntlx[h3b_data$level == 4],
                                                                                    progress = FALSE, paired = FALSE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 2], y = h3b_data$ntlx[h3b_data$level == 3],
                                                                                    progress = FALSE, paired = FALSE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 2], y = h3b_data$ntlx[h3b_data$level == 4],
                                                                                    progress = FALSE, paired = FALSE))$bf,
                                        BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 3], y = h3b_data$ntlx[h3b_data$level == 4],
                                                                                    progress = FALSE, paired = FALSE))$bf)

# get effect size

hypothesis3b_contrasts_levels <- cbind(hypothesis3b_contrasts_levels,
                                       format(effectsize::t_to_eta2(t = hypothesis3b_contrasts_levels$t.ratio,
                                                                    df_error = hypothesis3b_contrasts_levels$df, ci = 0.95), digits = 2))

# rename columns and contrasts, round to two decimals

colnames(hypothesis3b_contrasts_levels) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis3b_contrasts_levels$Contrast <- gsub("X", "", hypothesis3b_contrasts_levels$Contrast)
hypothesis3b_contrasts_levels[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis3b_contrasts_levels[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
hypothesis3b_contrasts_levels$`$p$` <- format(round(hypothesis3b_contrasts_levels$`$p$`, digits = 3), nsmall = 2)
hypothesis3b_contrasts_levels$`$p$`[hypothesis3b_contrasts_levels$`$p$` == "0.000"] <- "<.001"

## post-hoc tests for the interaction

# obtain estimated marginal means for ANOVA model

hypothesis3b_emm_interact <- emmeans::emmeans(hypothesis3b_model, ~ nfcmedian|level)

# calculate pairwise comparisons on estimated marginal means

hypothesis3b_contrasts_interact <- as.data.frame(pairs(hypothesis3b_emm_interact))

# get Bayes factors

hypothesis3b_BF_interact <- anovaBF(formula = ntlx ~ level * nfcmedian, data = h3b_data, progress = FALSE)
hypothesis3b_contrasts_interact$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 1 & h3b_data$nfcmedian == "high"],
                                                                                      y = h3b_data$ntlx[h3b_data$level == 1 & h3b_data$nfcmedian == "low"],
                                                                                      progress = FALSE, paired = FALSE))$bf,
                                          BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 2 & h3b_data$nfcmedian == "high"],
                                                                                      y = h3b_data$ntlx[h3b_data$level == 2 & h3b_data$nfcmedian == "low"],
                                                                                      progress = FALSE, paired = FALSE))$bf,
                                          BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 3 & h3b_data$nfcmedian == "high"],
                                                                                      y = h3b_data$ntlx[h3b_data$level == 3 & h3b_data$nfcmedian == "low"],
                                                                                      progress = FALSE, paired = FALSE))$bf,
                                          BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 4 & h3b_data$nfcmedian == "high"],
                                                                                      y = h3b_data$ntlx[h3b_data$level == 4 & h3b_data$nfcmedian == "low"],
                                                                                      progress = FALSE, paired = FALSE))$bf)

# get effect size

hypothesis3b_contrasts_interact <- cbind(hypothesis3b_contrasts_interact,
                                         format(effectsize::t_to_eta2(t = hypothesis3b_contrasts_interact$t.ratio,
                                                                      df_error = hypothesis3b_contrasts_interact$df, ci = 0.95), digits = 2))

# rename columns and contrasts, round to two decimals

colnames(hypothesis3b_contrasts_interact) <- c("Contrast", "Level", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis3b_contrasts_interact$Level <- gsub("X", "", hypothesis3b_contrasts_interact$Level)
hypothesis3b_contrasts_interact[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis3b_contrasts_interact[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
hypothesis3b_contrasts_interact$`$p$` <- format(round(hypothesis3b_contrasts_interact$`$p$`, digits = 3), nsmall = 2)
hypothesis3b_contrasts_interact$`$p$`[hypothesis3b_contrasts_interact$`$p$` == "0.000"] <- "<.001"

# plot these results

plot_h3b <- ggplot(h3b_data, aes(level, ntlx, fill = nfcmedian, color = nfcmedian)) +
            geom_rain(alpha = .5,
                      violin.args = list(color = NA, alpha = .7), # removes the lines around the violins
                      boxplot.args.pos = list(width = .1, position = ggpp::position_dodgenudge(
                                                x = rep(-.13,8)))) +
            ggprism::theme_prism(base_size = 12, base_line_size = 0.8, base_fontface = "plain", base_family = "sans") +
            scale_fill_manual(values=c("#B30B0B", "#0941DB")) +
            scale_color_manual(values=c("#B30B0B", "#0941DB")) +
            labs(x = "n-back levels", y = "NASA-TLX sum score") +
            guides(fill = 'none', color = 'none')

# save the plot as an eps file with high resolution

ggsave(filename = "Figure_4.eps", plot = plot_h3b, device = "eps",
       path = here("06_Paper","COG-ED","Stage 1","Figures"),
       dpi = "retina", bg = NULL)

# delete temporary data frame

base::remove(ntlx, h3b_data, mediannfc)

##### Hypothesis 3c ############################################################

# H3c: Participants with higher NFC scores have lower aversiveness scores for
# 2- and 3-back but higher aversiveness scores for 1-back than participants with
# lower NFC scores.

# make a temporary copy of the data frame

data_avers <- data_ntlx[ ,c("subject","level","aversion")]

# attach NFC scores

data_avers <- left_join(data_avers, unique(data_nback[,c("subject","nfc")]), by = "subject")

# create a data frame with the difference scores per subject (2-1,3-2)

diffscores <- diff(data_avers$aversion)
h3c_data <- data.frame(subject = data_avers$subject[c(seq(from = 1, to = nrow(data_avers), length.out = nrow(data_avers)/2))],
                       nlevels = as.factor(rep(c("1-2","2-3"), nrow(data_avers)/4)),
                       aversdiff = c(rbind(diffscores[c(seq(from = 1, to = nrow(data_avers), by = 4))],diffscores[c(seq(from = 2, to = nrow(data_avers), by = 4))])),
                       nfc = data_avers$nfc[c(seq(from = 1, to = nrow(data_avers), length.out = nrow(data_avers)/2))])

# add column indicating NFC score above or below median

mediannfc <- median(h3c_data$nfc)
h3c_data$nfcmedian <- ifelse(h3c_data$nfc < mediannfc, "low", "high")
h3c_data$nfcmedian <- as.factor(h3c_data$nfcmedian)

# compute two-way ANOVA

hypothesis3c_model <- afex::aov_ez("subject", "aversdiff", h3c_data,
                                   between = c("nfcmedian"), within = c("nlevels"))

# format S3 class into data frame

hypothesis3c_rmanova <- summary(hypothesis3c_model)
hypothesis3c_rmanova <- hypothesis3c_rmanova[["univariate.tests"]]
hypothesis3c_rmanova <- as.data.frame(matrix(hypothesis3c_rmanova, nrow = 4, ncol = 6))


# get effect size

hypothesis3c_rmanova <- cbind(hypothesis3c_rmanova,
                              format(effectsize::F_to_eta2(f = hypothesis3c_rmanova[,5], df = hypothesis3c_rmanova[,2],
                                                           df_error = hypothesis3c_rmanova[,4], ci = 0.95), digits = 2))

# formatting

colnames(hypothesis3c_rmanova) <- c("Sum Sq", "$df$", "error Sum Sq", "error $df$", "$F$", "$p$", "$\\eta_{p}^{2}$", "$95\\% CI$")
rownames(hypothesis3c_rmanova) <- c("Intercept", "NFC group", "n-back level", "NFC group x n-back level")
hypothesis3c_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")] <- signif(hypothesis3c_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")], digits = 3)
hypothesis3c_rmanova$`$p$` <- format(round(hypothesis3c_rmanova$`$p$`, digits = 3), nsmall = 2)
hypothesis3c_rmanova$`$p$`[hypothesis3c_rmanova$`$p$` == "0.000"] <- "<.001"

## post-hoc tests for the NFC groups

# obtain estimated marginal means for ANOVA model

hypothesis3c_emm_nfc <- emmeans::emmeans(object = hypothesis3c_model, "nfcmedian")

# calculate pairwise comparisons on estimated marginal means

hypothesis3c_contrasts_nfc <- as.data.frame(pairs(hypothesis3c_emm_nfc))

# get Bayes factors

hypothesis3c_BF_nfc <- anovaBF(formula = aversdiff ~ nlevels * nfcmedian, data = h3c_data, progress = FALSE)
hypothesis3c_contrasts_nfc$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h3c_data$aversdiff[h3c_data$nfcmedian == "high"], y = h3c_data$aversdiff[h3c_data$nfcmedian == "low"],
                                                                                 progress = FALSE, paired = FALSE))$bf)

# get effect size

hypothesis3c_contrasts_nfc <- cbind(hypothesis3c_contrasts_nfc,
                                    format(effectsize::t_to_eta2(t = hypothesis3c_contrasts_nfc$t.ratio,
                                                                 df_error = hypothesis3c_contrasts_nfc$df, ci = 0.95), digits = 2))

# rename columns and contrasts, round to two decimals

colnames(hypothesis3c_contrasts_nfc) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis3c_contrasts_nfc$Contrast <- c("High NFC - Low NFC")
hypothesis3c_contrasts_nfc[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis3c_contrasts_nfc[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
hypothesis3c_contrasts_nfc$`$p$` <- format(round(hypothesis3c_contrasts_nfc$`$p$`, digits = 3), nsmall = 2)
hypothesis3c_contrasts_nfc$`$p$`[hypothesis3c_contrasts_nfc$`$p$` == "0.000"] <- "<.001"

## post-hoc tests for the n-back levels

# obtain estimated marginal means for ANOVA model

hypothesis3c_emm_levels <- emmeans::emmeans(object = hypothesis3c_model, "nlevels")

# calculate pairwise comparisons on estimated marginal means

hypothesis3c_contrasts_levels <- as.data.frame(pairs(hypothesis3c_emm_levels))

# get Bayes factors

hypothesis3c_BF_levels <- anovaBF(formula = aversdiff ~ nlevels * nfcmedian, data = h3c_data, progress = FALSE)
hypothesis3c_contrasts_levels$BF10 <- extractBF(hypothesis3c_BF_levels[1])$bf

# get effect size

hypothesis3c_contrasts_levels <- cbind(hypothesis3c_contrasts_levels,
                                    format(effectsize::t_to_eta2(t = hypothesis3c_contrasts_levels$t.ratio,
                                                                 df_error = hypothesis3c_contrasts_levels$df, ci = 0.95), digits = 2))

# rename columns and contrasts, round to two decimals

colnames(hypothesis3c_contrasts_levels) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
hypothesis3c_contrasts_levels$Contrast <- c("1-2 - 2-3")
hypothesis3c_contrasts_levels[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis3c_contrasts_levels[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
hypothesis3c_contrasts_levels$`$p$` <- format(round(hypothesis3c_contrasts_levels$`$p$`, digits = 3), nsmall = 2)
hypothesis3c_contrasts_levels$`$p$`[hypothesis3c_contrasts_levels$`$p$` == "0.000"] <- "<.001"

# prepare raincloud plot

plot_h3c_data <- raincloudplots::data_2x2(array_1 = h3c_data$aversdiff[h3c_data$nlevels == "1-2" & h3c_data$nfcmedian == "low"],
                          array_2 = h3c_data$aversdiff[h3c_data$nlevels == "2-3" & h3c_data$nfcmedian == "low"],
                          array_3 = h3c_data$aversdiff[h3c_data$nlevels == "1-2" & h3c_data$nfcmedian == "high"],
                          array_4 = h3c_data$aversdiff[h3c_data$nlevels == "2-3" & h3c_data$nfcmedian == "high"],
                          labels = (c("NFC below median","NFC above median")), # below is blue, above is orange
                          jit_distance = .04,
                          jit_seed = 73,
                          spread_x_ticks = FALSE)

raincloudplots::raincloud_2x2_repmes(data_2x2 = plot_h3c_data,
                                 size = 2,
                                 alpha = .6,
                                 spread_x_ticks = FALSE) +
  xlab("n-back levels") + 
  ylab("Aversiveness ratings") +
  ggprism::theme_prism(base_size = 12, base_line_size = 0.8, base_fontface = "plain", base_family = "sans") +
  scale_x_continuous(breaks=c(1,2), labels=c("1-2", "2-3"), limits=c(0, 3))

# remove temporary variables

base::remove(diffscores, mediannfc, h3c_data)


##### Specification Curve Analysis #############################################

# here we repeat the multi level model of H2b with all analysis pipelines

# prepare empty data frame for the loop to feed into

sca_results <- data.frame(pipeline = character(), beta = double(), SE = double(), pvalue = double(), BF10 = double())

# loop through the pipelines

for (i in 1:length(pipelines_data)) {
  
  # make a temporary copy of the data frame
  
  sca_data <- pipelines_data[[i]]
  
  # get a subset without RT = NA
  
  sca_data <- droplevels(subset(sca_data[ ,c("subject", "level", "sv", "dprime", "medianRT")]))
  
  # centering the level 1 predictors (d', medianRT, level) within cluster
  
  sca_data$dprime.cwc       <- sca_data$dprime - (ave(sca_data$dprime, sca_data$subject, FUN = function(x) mean(x, na.rm = T)))
  sca_data$medianRT.cwc     <- sca_data$medianRT - (ave(sca_data$medianRT, sca_data$subject, FUN = function(x) mean(x, na.rm = T)))
  sca_data$level.cwc        <- sca_data$level - (ave(sca_data$level, sca_data$subject, FUN = function(x) mean(x, na.rm = T)))
  
  # assuming that we have a linear model:
  
  # define the null model
  
  m0_sca <- lmerTest::lmer(sv ~ 1 + (1|subject), data = sca_data, REML = T)
  
  # random slopes model
  
  m1_sca <- lmerTest::lmer(sv ~ level.cwc * dprime.cwc + medianRT.cwc + (level.cwc|subject),
                           data = sca_data, REML = T)
  
  # convert random factor to type factor
  
  sca_data$subject <- factor(sca_data$subject)
  
  # compute Bayes factor
  
  sca_full_BF <- lmBF(sv ~ level.cwc + dprime.cwc + medianRT.cwc + subject,
                      data = sca_data, whichRandom = 'subject', progress = FALSE)
  sca_null_BF <- lmBF(sv ~ 1 + dprime.cwc + medianRT.cwc + subject,
                      data = sca_data, whichRandom = 'subject', progress = FALSE)
  sca_BF <- sca_full_BF / sca_null_BF
  
  # combine current results and the bigger data frame
  
  newdata <- data.frame(pipeline = c(names(pipelines_data[i])),
                        beta = c(base::summary(m1_sca)$coefficients[2,1]),
                        SE = c(base::summary(m1_sca)$coefficients[3,1]),
                        pvalue = c(base::summary(m1_sca)$coefficients[2,5]),
                        BF10 = c(extractBF(sca_BF)$bf))
  sca_results <- rbind(sca_results, newdata)
  
}

##### SCA plot preparation #####################################################

# add a row number and sort the data frame by the fixed effects estimate of the predictor 'level'

sca_results <- cbind(sca_results, num = c(1:nrow(sca_results)))
sca_results <- sca_results[order(sca_results$beta, decreasing = TRUE), ]

# lock it in place by turning it into a factor

sca_results$num <- factor(sca_results$num)

# add new column with consecutive numbers

sca_results$xaxis <- c(1:nrow(sca_results))

# add columns to the data frame that describe the pipeline

sca_results$Dim <- ifelse(substr(sca_results$pipeline,1,2) == "AA", 2,
                          ifelse(substr(sca_results$pipeline,1,2) == "AW", 3,
                                 ifelse(substr(sca_results$pipeline,1,2) == "WW", 4,
                                        ifelse(substr(sca_results$pipeline,1,2) == "WA", 5, NA))))
sca_results$Trans <- ifelse(substr(sca_results$pipeline,3,3) == "R", 7,
                            ifelse(substr(sca_results$pipeline,3,3) == "L", 8,
                                   ifelse(substr(sca_results$pipeline,3,3) == "L", 8,
                                          ifelse(substr(sca_results$pipeline,3,3) == "I", 9,
                                                 ifelse(substr(sca_results$pipeline,3,3) == "S", 10, NA)))))
sca_results$Excl <- ifelse(substr(sca_results$pipeline,4,4) == "N", 12,
                           ifelse(substr(sca_results$pipeline,4,4) == "2", 13,
                                  ifelse(substr(sca_results$pipeline,4,4) == "5", 14,
                                         ifelse(substr(sca_results$pipeline,4,4) == "3", 15,
                                                ifelse(substr(sca_results$pipeline,4,4) == "O", 16, 
                                                       ifelse(substr(sca_results$pipeline,4,4) == "T", 17, NA))))))

##### SCA plot #################################################################

# based on the SCA plot by Michael Kossmeier at https://osf.io/e4bs8

# melt pipelines specifications into useful format

sca_lower <- melt(sca_results[c("xaxis","BF10","Dim","Trans","Excl")], id = c("xaxis","BF10"))
sca_lower <- sca_lower[,c("xaxis","BF10","value")]

# create the lower panel with the pipeline specifications

ggplot(sca_lower, aes(x = xaxis, y = value, fill = BF10)) +
  geom_vline(xintercept = c(0,10,20,30,40,50,60), colour = "grey", linetype = 3) +
  geom_tile(aes(fill = BF10), color = "white") +
  geom_hline(yintercept = c(6,11)) +
  ggprism::theme_prism(base_size = 12, base_line_size = 0.5, base_fontface = "plain", base_family = "sans") +
  labs(x = "Analysis pipeline", y = NULL) +
  scale_y_reverse(breaks = c(1:17), lim = c(18,0), labels = c(expression(bold("Dimension")),
                                                              "Across S, across C", "Across S, within C",
                                                              "Within S, within C", "Within S, across C",
                                                              expression(bold("Transformation")),
                                                              "Raw/None", "Log", "Inverse", "Square-root",
                                                              expression(bold("Exclusion")),
                                                              "None", "2 MAD from median", " 2.5 MAD from median",
                                                              "3 MAD from median", "100ms after onset", "200ms after onset")) +
  scale_fill_gradientn(colors = MetBrewer::met.brewer("Homer2")) +
  guides(fill = guide_colourbar(barwidth = 1, barheight = 15, title = "BF10"))

# create the middle panel with the p-values

ggplot(sca_results, aes(x = xaxis, y = pvalue)) +
  geom_vline(xintercept = c(0,10,20,30,40,50,60), colour = "grey", linetype = 3) +
  geom_line() +
  ggprism::theme_prism(base_size = 12, base_line_size = 0.5, base_fontface = "plain", base_family = "sans") +
  labs(x = NULL, y = "p-value") +
  scale_x_continuous(labels = NULL)

# create upper panel with beta weights

ggplot(sca_results, aes(x = xaxis, y = beta)) +
  geom_vline(xintercept = c(0,10,20,30,40,50,60), colour = "grey", linetype = 3) +
  geom_errorbar(aes(ymin = beta-SE,ymax = beta+SE, col = BF10), 
                width = 0, size = 2, alpha = .9, show.legend = FALSE) +
  scale_color_gradientn(colors = met.brewer("Homer2")) +
  geom_line(col = "black", size = 0.25) +
  ggprism::theme_prism(base_size = 12, base_line_size = 0.5, base_fontface = "plain", base_family = "sans") +
  labs(x = NULL, y = "Fixed effects beta of the predictor n-back level") +
  scale_x_continuous(labels = NULL)

##### Extra plots ##############################################################

# plot showing SVs per subject, colors depend on NFC

ggplot2::ggplot(pipelines_data[["AARO"]], aes(x = level, y = sv, group = subject, color = nfc)) +
  geom_line(size = 1, alpha = 0.5, position = position_jitter(w = 0, h = 0.04)) +
  scale_color_gradient2(midpoint = 0, low = "blue", mid = "grey", high = "red", space = "Lab" ) +
  ggprism::theme_prism(base_size = 12, base_line_size = 0.5, base_fontface = "plain", base_family = "sans")


##### Save variables ###########################################################

save.image(file = "Workspace.RData")