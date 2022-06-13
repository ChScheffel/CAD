################################################################################
#
# Analysis script for the Registered Report
# "When easy is not preferred: An effort discounting paradigm for estimating subjective values of tasks"
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
  source(here("06_Paper","COG-ED", "renv", "activate.R"))
  
  
  # the required packages are:
  # "bibtex", "here", "tidyverse", "bayestestR", "papaja", "lmerTest", "afex", "emmeans", "sjPlot", "purrr", "broom",
  # "kableExtra", "interactions", "glmmTMB", "BayesFactor", "ggplot2", "egg", "knitr", "effectsize", "pracma", and "MuMIn"
  
  # sets orthogonal contrasts for mixed-effects model and rmANOVA globally in order to get meaningful Type-III tests
  
  afex::set_sum_contrasts()

##### Import ###################################################################
  
  # set top level directory to source file
  
  here::i_am("flag_project_root_CAD.txt")
  
  # import n-back and effort discounting data into a list each
  
  datalist_nback = lapply(list.files(here("04_RawData", "pilot", "COG-ED"), pattern = '.*nback.*csv', full.names = TRUE),
                          read.csv, stringsAsFactors = FALSE, header = TRUE)
  datalist_ED = lapply(list.files(here("04_RawData", "pilot", "COG-ED"), pattern = '.*_ED.*csv', full.names = TRUE),
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
  
  # change the name of a subject (it has the suffix "_neu" because the paradigm didn't start properly the first time)
  
  data_nback$subject[data_nback$subject == "E12K08_neu"] <- "E12K08"
  data_ED$subject[data_ED$subject == "E12K08_neu"] <- "E12K08"
  
  # remove one subject who did not understand the instructions of the n-back task and reacted only to every n-th stimulus
  
  data_nback <- data_nback[data_nback$subject != "M28B11", ]
  data_ED <- data_ED[data_ED$subject != "M28B11", ]
  
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
  
  # correct subject code
  data_nback$subject[which(data_nback$subject == "E12K08_neu")] <- "E12K08"
  data_ED$subject[which(data_ED$subject == "E12K08_neu")] <- "E12K08"
  
  
  # the choice column will contain 1 for the left button and 2 for the right button
  
  data_ED[data_ED == "EDleftbutton"] <- 1
  data_ED[data_ED == "EDrightbutton"] <- 2
  data_ED$choice <- as.numeric(data_ED$choice)
  
  # since only the last choice of each comparison is relevant, we will keep only those rows
  
  data_ED <- data_ED[data_ED$step == 6,]
  data_ED <- subset(data_ED, select = -c(step))
  
  # import questionnaire data from RedCap
  
  data_quest <- read.csv(here("04_RawData", "pilot", "CERED_DATA.csv"), stringsAsFactors = FALSE, header = TRUE)
  colnames(data_quest)[1] <- "set" # rename the first column
  
  # remove the subject who misunderstood the instruction
  
  data_quest <- data_quest[data_quest$set != "M28B11", ]
  
  # remove unnecessary variables from questionnaire data frame
  
  data_quest <- subset(data_quest, select = -c(vl, date, preparatory_coged_complete, general_questions_timestamp, state,
                                               general_questions_complete, inclusion, inclusion_0___1, inclusion_0___2, inclusion_0_2,
                                               researcher_questions_complete, nasatlx_timestamp, nasatlx_complete, t1_psychopy_ed_csv,
                                               t1_psychopy_nback_csv, files_coged_complete, record_id_2, vl_er,
                                               date_er, preparatory_ered_complete, emg_eeg, emg_vhdr, emg_vmrk,
                                               files_ered_complete, followup_ered_timestamp,
                                               nachb_01, nachb_01_inhalt, nachb_02, nachb_02_inhalt, nachb_03, nachb_07, nachb_07_inhalt,
                                               nachb_08, nachb_08_inhalt, nachb_08_haeufig, nachb_08_zurueck, followup_ered_complete,
                                               nfc_timestamp, nfc_complete, bis_11_timestamp, bis_11_complete, bscs_timestamp,
                                               bscs_complete, srs_timestamp, srs_complete, erq_erqse_timestamp, erq_erqse_complete,
                                               who5_timestamp, who5_complete, acs_timestamp, acs_complete, cdrisc_timestamp,
                                               cdrisc_complete, flexer_timestamp, flexer_complete))
  
  # compute index of rows in which the data sets change
  
  setindex <- c(1,which(data_quest$set != dplyr::lag(data_quest$set)),nrow(data_quest))
  
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
  
  # prepare temporary data frame for loop to feed into
  
  data_nfc <- data.frame(subject = character(), nfc = double())
  
  # compute index of rows in which the data sets change
  
  setindex <- c(1,which(data_quest$set != dplyr::lag(data_quest$set)),nrow(data_quest))
  
  # calculate NFC scores for every subject
  
  for (i in 1:(length(setindex)-1)) {
    
    nfc <- data_quest[setindex[i] + 2, grep("nfc", colnames(data_quest))]
    
    # define and invert items to be recoded
    
    nfc[ ,c(4,6,7,8,9,10,11,12,15,16)] <-  nfc[ ,c(4,6,7,8,9,10,11,12,15,16)] * -1
    
    data_nfc <- rbind(data_nfc, data.frame(subject = data_quest$subject[setindex[i]],
                                           nfc = sum(nfc)))
  }
  
  # add the NFC scores trial-wise to the nback-data-frame for the multi-level-model
  
  for (i in 1:nrow(data_nback)) {
    
    data_nback$nfc[i] <- data_nfc$nfc[data_nfc$subject == data_nback$subject[i]]
    
  }
  
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
  hypothesis1a_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis1a_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis1a_contrasts$`$p$` <- format(round(hypothesis1a_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis1a_contrasts$`$p$`[hypothesis1a_contrasts$`$p$` == 0.000] <- "<.001"
  
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
  hypothesis1b_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis1b_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis1b_contrasts$`$p$` <- format(round(hypothesis1b_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis1b_contrasts$`$p$`[hypothesis1b_contrasts$`$p$` == 0.000] <- "<.001"
  
  # remove the temporary variable
  
  base::remove(h1b_data)
  
##### Hypothesis 1c ############################################################
  
  # H1c: Ratings on all NASA-TLX dimensions increase with increasing n-back level.
  
  # set up empty data frame for the loop to feed into
  
  data_ntlx <- data.frame(subject = character(), level = double(),
                          mental = double(), physical = double(), time = double(),
                          performance = double(), effort = double(), frustration = double())
  
  # feed NASA-TLX data per participant per level into data frame
  
  for (i in c(1:5,7:(length(setindex)-1))) { # we exclude the sixth subject (ID F30T02) here, because their NTLX data for n = 1 is missing
    
    for (j in 1:4) {
      
      newdata <- data.frame(subject = data_quest$subject[setindex[i]],
                            level = j,
                            mental = data_quest$nasa_tlx_01[setindex[i]+j+2],
                            physical = data_quest$nasa_tlx_02[setindex[i]+j+2],
                            time = data_quest$nasa_tlx_03[setindex[i]+j+2],
                            performance = data_quest$nasa_tlx_04[setindex[i]+j+2],
                            effort = data_quest$nasa_tlx_05[setindex[i]+j+2],
                            frustration = data_quest$nasa_tlx_06[setindex[i]+j+2])
      data_ntlx <- rbind(data_ntlx, newdata)
    }
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
  
  hypothesis1c_emm <- emmeans::emmeans(object = hypothesis1c_mental_rmanova$aov, specs = "level")
  hypothesis1c_mental_contrasts <- as.data.frame(pairs(hypothesis1c_emm))
  
  hypothesis1c_emm <- emmeans::emmeans(object = hypothesis1c_physical_rmanova$aov, specs = "level")
  hypothesis1c_physical_contrasts <- as.data.frame(pairs(hypothesis1c_emm))
  
  hypothesis1c_emm <- emmeans::emmeans(object = hypothesis1c_time_rmanova$aov, specs = "level")
  hypothesis1c_time_contrasts <- as.data.frame(pairs(hypothesis1c_emm))
  
  hypothesis1c_emm <- emmeans::emmeans(object = hypothesis1c_performance_rmanova$aov, specs = "level")
  hypothesis1c_performance_contrasts <- as.data.frame(pairs(hypothesis1c_emm))
  
  hypothesis1c_emm <- emmeans::emmeans(object = hypothesis1c_effort_rmanova$aov, specs = "level")
  hypothesis1c_effort_contrasts <- as.data.frame(pairs(hypothesis1c_emm))
  
  hypothesis1c_emm <- emmeans::emmeans(object = hypothesis1c_frustration_rmanova$aov, specs = "level")
  hypothesis1c_frustration_contrasts <- as.data.frame(pairs(hypothesis1c_emm))
  
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
  hypothesis1c_mental_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis1c_mental_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis1c_mental_contrasts$`$p$` <- format(round(hypothesis1c_mental_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis1c_mental_contrasts$`$p$`[hypothesis1c_mental_contrasts$`$p$` == "0.000"] <- "<.001"
  
  colnames(hypothesis1c_physical_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
  hypothesis1c_physical_contrasts$Contrast <- gsub("X", "", hypothesis1c_physical_contrasts$Contrast)
  hypothesis1c_physical_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis1c_physical_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis1c_physical_contrasts$`$p$` <- format(round(hypothesis1c_physical_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis1c_physical_contrasts$`$p$`[hypothesis1c_physical_contrasts$`$p$` == "0.000"] <- "<.001"
  
  colnames(hypothesis1c_performance_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
  hypothesis1c_performance_contrasts$Contrast <- gsub("X", "", hypothesis1c_performance_contrasts$Contrast)
  hypothesis1c_performance_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis1c_performance_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis1c_performance_contrasts$`$p$` <- format(round(hypothesis1c_performance_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis1c_performance_contrasts$`$p$`[hypothesis1c_performance_contrasts$`$p$` == "0.000"] <- "<.001"
  
  colnames(hypothesis1c_effort_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
  hypothesis1c_effort_contrasts$Contrast <- gsub("X", "", hypothesis1c_effort_contrasts$Contrast)
  hypothesis1c_effort_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis1c_effort_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis1c_effort_contrasts$`$p$` <- format(round(hypothesis1c_effort_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis1c_effort_contrasts$`$p$`[hypothesis1c_effort_contrasts$`$p$` == "0.000"] <- "<.001"
  
  colnames(hypothesis1c_frustration_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
  hypothesis1c_frustration_contrasts$Contrast <- gsub("X", "", hypothesis1c_frustration_contrasts$Contrast)
  hypothesis1c_frustration_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis1c_frustration_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis1c_frustration_contrasts$`$p$` <- format(round(hypothesis1c_frustration_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis1c_frustration_contrasts$`$p$`[hypothesis1c_frustration_contrasts$`$p$` == "0.000"] <- "<.001"
  
  colnames(hypothesis1c_time_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
  hypothesis1c_time_contrasts$Contrast <- gsub("X", "", hypothesis1c_time_contrasts$Contrast)
  hypothesis1c_time_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis1c_time_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis1c_time_contrasts$`$p$` <- format(round(hypothesis1c_time_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis1c_time_contrasts$`$p$`[hypothesis1c_time_contrasts$`$p$` == "0.000"] <- "<.001"
  
  # remove the temporary variable
  
  base::remove(h1c_data, hypothesis1c_emm)
  
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
  hypothesis2a_contrasts[ ,c("Estimate","$SE$","$t$")] <- format(round(hypothesis2a_contrasts[ ,c("Estimate","$SE$","$t$")], digits = 2), nsmall = 2)
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
                           control = lmerControl(optimizer = "nloptwrap", optCtrl = list(algorithm = "NLOPT_LN_NELDERMEAD")))

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
                           control = lmerControl(optimizer = "nmkbw"))
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
                                   control = lmerControl(optimizer = "nmkbw"))
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
  ## E - positively skewed normal (nonlinear mixed model) ----------------------
  

##### Hypothesis 3a ############################################################
  
  # H3a: Subjective values positively predict individual NFC scores.
  
  # make a temporary copy of the data frame

  data_SV <- pipelines_data[["AARO"]][ ,c("subject","level","sv","nfc")]
  
  # create a data frame with the difference scores per subject (2-1,3-2,4-3)
  
  diffscores <- diff(data_SV$sv)
  h3a_data <- data.frame(subject = data_SV$subject[-c(seq(from = 4, to = nrow(data_SV), by = 4))],
                        nlevels = as.factor(rep(c("1-2","2-3","3-4"), nrow(data_SV)/4)),
                        svdiff = diffscores[-c(seq(from = 4, to = nrow(data_SV)-4, by = 4))],
                        nfc = data_SV$nfc[-c(seq(from = 4, to = nrow(data_SV), by = 4))])
  
  # add column indicating NFC score above or below median
  
  mediannfc <- median(h3a_data$nfc)
  h3a_data$nfcmedian <- ifelse(h3a_data$nfc < mediannfc, "low", "high")
  h3a_data$nfcmedian <- as.factor(h3a_data$nfcmedian)
  
  # compute two-way ANOVA
  
  hypothesis3a_rmanova <- afex::aov_ez("subject", "svdiff", h3a_data,
                                       between = c("nfcmedian"), within = c("nlevels"))
  
  # format S3 class into data frame
  
  hypothesis3a_rmanova <- summary(hypothesis3a_rmanova)
  hypothesis3a_rmanova <- hypothesis3a_rmanova[["univariate.tests"]]
  hypothesis3a_rmanova <- as.data.frame(matrix(hypothesis3a_rmanova, nrow = 4, ncol = 6))
  
  
  # get effect size
  
  hypothesis3a_rmanova <- cbind(hypothesis3a_rmanova,
                            format(effectsize::F_to_eta2(f = hypothesis3a_rmanova[,5], df = hypothesis3a_rmanova[,2],
                                                         df_error = hypothesis3a_rmanova[,4], ci = 0.95), digits = 2))
  
  # formatting
  
  colnames(hypothesis3a_rmanova) <- c("Sum Sq", "$df$", "error Sum Sq", "error $df$", "$F$", "$p$", "$\\eta_{p}^{2}$", "$95\\% CI$")
  rownames(hypothesis3a_rmanova) <- c("Intercept", "NFC group", "n-back level", "NFC group x n-back level")
  hypothesis3a_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")] <- format(round(hypothesis3a_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")], digits = 2), nsmall = 2)
  hypothesis3a_rmanova$`$p$` <- format(round(hypothesis3a_rmanova$`$p$`, digits = 3), nsmall = 2)
  hypothesis3a_rmanova$`$p$`[hypothesis3a_rmanova$`$p$` == "0.000"] <- "<.001"
  
  # obtain estimated marginal means for ANOVA model
  
  #hypothesis3a_emm <- emmeans::emmeans(object = hypothesis3a_rmanova, c("nfcmedian","nlevels"))
  
  # calculate pairwise comparisons on estimated marginal means
  
  #hypothesis3a_contrasts <- as.data.frame(pairs(hypothesis3a_emm))
  
  # get Bayes factors
  
  #hypothesis3a_BF <- anovaBF(formula = svdiff ~ nlevels * nfcmedian, data = h3a_data, progress = FALSE)
  #hypothesis3a_contrasts$BF10 <- BayesFactor::extractBF(BayesFactor::ttestBF(x = h3a_data$svdiff[h3a_data$nfcmedian == "high"],
  #                                                                           y = h3a_data$svdiff[h3a_data$nfcmedian == "low"],
  #                                                                           progress = FALSE, paired = FALSE))$bf
  
  # remove temporary variables
  
  base::remove(diffscores, mediannfc, h3a_data)

  
##### Hypothesis 3b ############################################################
  
  # H3b: NASA-TLX scores negatively predict individual NCS scores.
  
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
  hypothesis3b_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")] <- format(round(hypothesis3b_rmanova[ ,c("Sum Sq","error Sum Sq","$F$")], digits = 2), nsmall = 2)
  hypothesis3b_rmanova$`$p$` <- format(round(hypothesis3b_rmanova$`$p$`, digits = 3), nsmall = 2)
  hypothesis3b_rmanova$`$p$`[hypothesis3b_rmanova$`$p$` == "0.000"] <- "<.001"
  
  # obtain estimated marginal means for ANOVA model
  
  hypothesis3b_emm <- emmeans::emmeans(object = hypothesis3b_model, "level")
  
  # calculate pairwise comparisons on estimated marginal means
  
  hypothesis3b_contrasts <- as.data.frame(pairs(hypothesis3b_emm))
  
  # get Bayes factors
  
  hypothesis3b_BF <- anovaBF(formula = ntlx ~ level * nfcmedian, data = h3b_data, progress = FALSE)
  hypothesis3b_contrasts$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = h3b_data$ntlx[h3b_data$level == 1], y = h3b_data$ntlx[h3b_data$level == 2],
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
  
  hypothesis3b_contrasts <- cbind(hypothesis3b_contrasts,
                                  format(effectsize::t_to_eta2(t = hypothesis3b_contrasts$t.ratio,
                                                               df_error = hypothesis3b_contrasts$df, ci = 0.95), digits = 2))
  
  # rename columns and contrasts, round to two decimals
  
  colnames(hypothesis3b_contrasts) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
  hypothesis3b_contrasts$Contrast <- gsub("X", "", hypothesis3b_contrasts$Contrast)
  hypothesis3b_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")] <- format(round(hypothesis3b_contrasts[ ,c("Estimate","$SE$","$t$","$BF10$")], digits = 2), nsmall = 2)
  hypothesis3b_contrasts$`$p$` <- format(round(hypothesis3b_contrasts$`$p$`, digits = 3), nsmall = 2)
  hypothesis3b_contrasts$`$p$`[hypothesis3b_contrasts$`$p$` == "0.000"] <- "<.001"
  
  # delete temporary data frame
  
  base::remove(ntlx, h3b_data, mediannfc)
  
##### Hypothesis 3c ############################################################
  
  # Here we will repeat the same method of hypothesis 3a, but with the aversiveness-scores
  # in place of the SV scores. Since we did not assess those in the pilot study, we
  # do not have the data to analyze it at the moment.
  
##### Specification Curve Analysis #############################################
  
  # # Repeat the analysis of hypothesis 3a will all pipelines
  # 
  # # prepare empty data frame for the loop to feed into
  # 
  # sca_results <- data.frame(pipeline = character(), effect = double(), pvalue = double(), f = character(), BF10 = double())
  # 
  # # loop through the pipelines
  # 
  # for (i in 1:length(pipelines_data)) {
  #   
  #   # make a temporary copy of the data frame
  #   
  #   mydata <- pipelines_data[[i]][ ,c("subject","level","sv","nfc")]
  #   
  #   # create a data frame with the difference scores per subject (2-1,3-2,4-3)
  #   
  #   diffscores <- diff(mydata$sv)
  #   sca_data <- data.frame(subject = mydata$subject[-c(seq(from = 4, to = nrow(mydata), by = 4))],
  #                          nlevels = as.factor(rep(c("1-2","2-3","3-4"), nrow(mydata)/4)),
  #                          svdiff = diffscores[-c(seq(from = 4, to = nrow(mydata)-4, by = 4))],
  #                          nfc = mydata$nfc[-c(seq(from = 4, to = nrow(mydata), by = 4))])
  #   
  #   # add column indicating NFC score above or below median
  #   
  #   mediannfc <- median(sca_data$nfc)
  #   sca_data$nfcmedian <- ifelse(sca_data$nfc < mediannfc, "low", "high")
  #   sca_data$nfcmedian <- as.factor(sca_data$nfcmedian)
  #   
  #   # compute two-way ANOVA
  #   
  #   sca_rmanova <- afex::aov_ez("subject", "svdiff", sca_data,
  #                                        between = c("nfcmedian"), within = c("nlevels"))
  #   
  #   # obtain estimated marginal means for ANOVA model
  #   
  #   sca_emm <- emmeans::emmeans(object = sca_rmanova, c("nfcmedian","nlevels"))
  #   
  #   # calculate pairwise comparisons on estimated marginal means
  #   
  #   sca_contrasts <- as.data.frame(pairs(sca_emm))
  #   
  #   # get Bayes factors
  #   
  #   sca_BF <- anovaBF(formula = svdiff ~ nlevels * nfcmedian, data = sca_data, progress = FALSE)
  #   sca_contrasts$BF10 <- BayesFactor::extractBF(BayesFactor::ttestBF(x = sca_data$svdiff[sca_data$nfcmedian == "high"],
  #                                                                              y = sca_data$svdiff[sca_data$nfcmedian == "low"],
  #                                                                              progress = FALSE, paired = FALSE))$bf
  #   
  #   # combine current results and the bigger data frame
  #   # (still has to be coded)
  #   
  # }
  # 
  # # remove temporary variables
  # 
  # base::remove(diffscores, mediannfc, sca_data, sca_rmanova, sca_contrasts, sca_BF, sca_emm)
  
##### Save variables ###########################################################
  
  save.image(file = "Workspace.RData")
  
  