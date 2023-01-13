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

datalist_ED <- lapply(list.files(here("04_RawData", "main", "ER-ED/logfiles"),
                                       pattern = "*_ED.*csv", full.names = TRUE),
                            read.csv, stringsAsFactors = FALSE,
                            header = TRUE)

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
                    datalist_ER[[i]][["slider_utility.response"]],
                    datalist_ER[[i]][["TriggerBlockView"]],
                    datalist_ER[[i]][["TriggerBlockReg"]])
  colnames(tmp) <- names(data_ER)
  tmp <- tmp[(!is.na(tmp$arousal)), ]
  
  data_ER <- rbind(tmp, data_ER)
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
 
 data_EMG <- rbind(tmp, data_EMG)
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

data_survey <- read.csv(here("04_RawData", "main", "CAD_DATA.csv"),
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

for (i in seq_len(length(subjectindex)-1)) {
  
  tempone <- double()
  temptwo <- double()
  tempthree <- double()
  
  # initialize empty vectors
  
  # check for every strategy if its on the right or left button
  # devide the respective value by 2 and save the variable in new tmporary df

  for (j in seq_len(nrow(data_ED))) {
    
    # strategy distraction
    if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 1)) {
      tempone <- append(tempone, data_ED$LBvalue[j])
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 1)) {
      tempone <- append(tempone, data_ED$RBvalue[j])
    }
    
    # strategy distancing
    if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 2)) {
      temptwo <- append(temptwo, data_ED$LBvalue[j])
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 2)) {
      temptwo <- append(temptwo, data_ED$RBvalue[j])
    } 
    
    # strategy suppression
    if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$LBstrat[j] == 3)) {
      tempthree <- append(tempthree, data_ED$LBvalue[j])
    } else if ((data_ED$ID[j] == data_ED$ID[subjectindex[i]]) & (data_ED$RBstrat[j] == 3)) {
      tempthree <- append(tempthree, data_ED$RBvalue[j])
    } 
  }

  newdata <- data.frame(ID = rep(data_ED$ID[subjectindex[i]],3),
                        strategy = c("distraction","distancing","suppression"),
                        sv = c(mean(tempone), mean(temptwo), mean(tempthree)))
  data_SV <- rbind(data_SV, newdata)
  
}

# remove temporary variables
base::remove(tempone, temptwo, tempthree, newdata)

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

# figure
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

EMG_view <- data_EMG %>%
  subset(data_EMG$block == "1_view_neu" | data_EMG$block == "2_view_neg")
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
                                                                    progress = FALSE, paired = TRUE))$bf

EMGCorrView_con <- cbind(EMGCorrView_con,
                         format(effectsize::t_to_eta2(t = EMGCorrView_con$t.ratio,
                                                      df_error = EMGCorrView_con$df,
                                                      ci = 0.95),
                                digits = 2))

colnames(EMGCorrView_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
# rename contrast for table
EMGCorrView_con[1, 1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize arousal ratings

# figure
FigEMGCorrView <- ggplot2::ggplot(EMG_view, aes(x = block, y = Corr, fill = block)) +
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
                                                                   progress = FALSE, paired = TRUE))$bf

EMGLevView_con <- cbind(EMGLevView_con,
                        format(effectsize::t_to_eta2(t = EMGLevView_con$t.ratio,
                                                     df_error = EMGLevView_con$df,
                                                     ci = 0.95),
                               digits = 2))

colnames(EMGLevView_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
# rename contrast for table
EMGLevView_con[1, 1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize arousal ratings

# figure
FigEMGLevView <- ggplot2::ggplot(EMG_view, aes(x = block, y = Lev, fill = block)) +
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

SubjArousalReg_con[1, 1] <- "$View_{negative} - Distraction$"
SubjArousalReg_con[2, 1] <- "$View_{negative} - Distancing$"
SubjArousalReg_con[3, 1] <- "$View_{negative} - Suppression$"
SubjArousalReg_con[4, 1] <- "$Distraction - Distancing$"
SubjArousalReg_con[5, 1] <- "$Distraction - Suppression$"
SubjArousalReg_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize arousal ratings

# figure
FigSubjArousalReg <- ggplot2::ggplot(Ratings_reg, aes(x = block, y = arousal, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  see::geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  ylim(c(0,400))+
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  viridis::scale_color_viridis(discrete = TRUE) +
  labs(y = "Arousal Rating") +
  theme_minimal()+
  theme(legend.position = "none")

######## HYPOTHESIS 3

# Do ER strategies reduce physiological responding? (Manipulation check)

#### HYPOTHESIS 3a 

# Physiological responding (EMG corrugator activity) is lower after using an emotion regulation strategy (distraction, distancing, suppression) compared to active viewing.

#
#

#### HYPOTHESIS 3b

# Physiological responding (EMG levator activity) is lower after using an emotion regulation strategy (distraction, distancing, suppression) compared to active viewing.

#
#

######## HYPOTHESIS 4

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

SubjEffort_con$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "2_view_neg"],
                                                                     y = Ratings_reg$effort[Ratings_reg$block == "3_distraction"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "2_view_neg"],
                                                                     y = Ratings_reg$effort[Ratings_reg$block == "4_distancing"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "2_view_neg"],
                                                                     y = Ratings_reg$effort[Ratings_reg$block == "5_suppression"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "3_distraction"],
                                                                     y = Ratings_reg$effort[Ratings_reg$block == "4_distancing"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "3_distraction"],
                                                                     y = Ratings_reg$effort[Ratings_reg$block == "5_suppression"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg$effort[Ratings_reg$block == "4_distancing"],
                                                                     y = Ratings_reg$effort[Ratings_reg$block == "5_suppression"],
                                                                     progress = FALSE, paired = TRUE))$bf)
 
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

# Figure to visualize effort ratings
# figure
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


#################### SAVE WORKSPACE IMAGE #######################

save.image(file = "Workspace_ERED.RData")
