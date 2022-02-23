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

library(renv)
renv::activate(here("06_Paper", "ER-ED"))
renv::restore(here("06_Paper", "ER-ED"))

library(dplyr)
library(ggplot2)

##################### DATA IMPORT #######################

# import ER ratings and ER discounting data into lists

datalist_ER <- lapply(list.files(here("04_RawData", "pilot", "ER-ED/logfiles"),
                                pattern = "*_ER.*csv", full.names = TRUE),
                                read.csv, stringsAsFactors = FALSE,
                                header = TRUE)
  
datalist_ED <- lapply(list.files(here("04_RawData", "pilot", "ER-ED/logfiles"),
                                pattern = "*_ED.*csv", full.names = TRUE),
                                read.csv, stringsAsFactors = FALSE,
                                header = TRUE)

# new empty frame to store files into
data_ER <- data.frame(ID = character(), block = character(),
                      arousal = double(), effort = double(),
                      trigger = double(), trigger_reg = double())

data_ED <- data.frame(ID = character(), step = double(),
                      choice = character(), LBvalue = double(),
                      LBlevel = double(), RBvalue = double(),
                      RBlevel = double())

data_choice <- data.frame(ID = character(), choice = double())

# store arousal and effort ratings in data_ER frame
for (i in seq_len(length(datalist_ER))) {
    tmp <- data.frame(datalist_ER[[i]][["participant"]],
                     datalist_ER[[i]][["instr_1"]],
                     datalist_ER[[i]][["slider_arousal.response"]],
                     datalist_ER[[i]][["slider_effort.response"]],
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
  
  data_choice <- rbind(tmp, data_choice)
}

# store ED data in data_ED frame
#for (i in 1:length(datalist_ED)) {
  
#  tmp = data.frame(datalist_ED[[i]][["participant"]][2:length(datalist_ED[[i]][["participant"]])],
#                   datalist_ED[[i]][["EDround.thisN"]][2:length(datalist_ED[[i]][["EDround.thisN"]])],
#                   datalist_ED[[i]][["EDclick.clicked_name"]][2:length(datalist_ED[[i]][["EDclick.clicked_name"]])],
#                   datalist_ED[[i]][["EDleftbutton.value"]][2:length(datalist_ED[[i]][["EDleftbutton.value"]])],
#                   datalist_ED[[i]][["EDleftbutton.nback"]][2:length(datalist_ED[[i]][["EDleftbutton.nback"]])],
#                   datalist_ED[[i]][["EDrightbutton.value"]][2:length(datalist_ED[[i]][["EDrightbutton.value"]])],
#                   datalist_ED[[i]][["EDrightbutton.nback"]][2:length(datalist_ED[[i]][["EDrightbutton.nback"]])])
  
#  colnames(tmp) = names(data_ED)
#  data_ED = rbind(data_ED, tmp)
#}

# import EMG data

datalist_EMG <- lapply(list.files(here("04_RawData", "pilot", "ER-ED", "EMG", "analysis"),
                                  pattern = '*_Peaks.txt', full.names = TRUE),
                       read.table, stringsAsFactors = FALSE, header = TRUE)
datalist_EMG_Marker <- lapply(list.files(here("04_RawData", "pilot", "ER-ED", "EMG", "analysis"),
                                         pattern = "*.Markers", full.names = TRUE),
                              read.table, stringsAsFactors = FALSE, header = TRUE,
                              skip = 1, row.names = NULL, sep = ",")

# new empty frame to store files into
data_emg <- data.frame(ID = character(), trigger = double(), Corr = double(),
                     Lev = double())

# store EMG data in data_EMG frame
for (i in seq_len(length(datalist_EMG))) {
  tmp <- data.frame(datalist_EMG[[i]][["Filename"]],
                   datalist_EMG_Marker[[i]][["Description"]],
                   datalist_EMG[[i]][["T0T6000Corr.ASNM"]],
                   datalist_EMG[[i]][["T0T6000Lev.ASNM"]])
  colnames(tmp) <- names(data_EMG)
  
  data_EMG = rbind(tmp, data_EMG)
  
}

# create variable "block"

data_EMG$block[data_EMG$trigger == " S 21"] <- "1_view_neu"
data_EMG$block[data_EMG$trigger == " S 22"] <- "2_view_neg"
data_EMG$block[data_EMG$trigger == " S 23"] <- "3_distraction"
data_EMG$block[data_EMG$trigger == " S 24"] <- "4_distancing"
data_EMG$block[data_EMG$trigger == " S 25"] <- "5_suppression"
data_EMG$block[data_EMG$trigger == " S 26"] <- "6_choice"


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


## Subjective arousal

# ANOVA subjective arousal ratings
# View condition

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
SubjArousalView_con[1,1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize arousal ratings

# figure
FigSubjArousalViewPilot=ggplot2::ggplot(Ratings_view, aes(x = block, y = arousal))+
  geom_boxplot(width = 0.7, position = position_dodge(0.8))+
  scale_x_discrete(name = "Active viewing", 
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative"))+
  geom_jitter(size = 0.4)+
  labs(y = "Arousal Rating")

# View neg and regulate conditions 

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

SubjArousalReg_con[1,1] <- "$View_{negative} - Distraction$"
SubjArousalReg_con[2,1] <- "$View_{negative} - Distancing$"
SubjArousalReg_con[3,1] <- "$View_{negative} - Suppression$"
SubjArousalReg_con[4,1] <- "$Distraction - Distancing$"
SubjArousalReg_con[5,1] <- "$Distraction - Suppression$"
SubjArousalReg_con[6,1] <- "$Distancing - Suppression$"

# Figure to visualize arousal ratings

# figure
FigSubjArousalRegPilot <- ggplot2::ggplot(Ratings_reg, aes(x = block, y = arousal))+
  geom_boxplot(width = 0.7, position = position_dodge(0.8))+
  scale_x_discrete(name = "Strategy", 
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression"))+
  geom_jitter(size = 0.4)+
  labs(y = "Arousal Rating")

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

SubjEffort_con[1,1] <- "$View_{negative} - Distancing$"
SubjEffort_con[2,1] <- "$View_{negative} - Distraction$"
SubjEffort_con[3,1] <- "$View_{negative} - Suppression$"
SubjEffort_con[4,1] <- "$Distraction - Distancing$"
SubjEffort_con[5,1] <- "$Distraction - Suppression$"
SubjEffort_con[6,1] <- "$Distancing - Suppression$"

# Figure to visualize effort ratings
# figure
FigSubjEffortPilot = ggplot2::ggplot(Ratings_reg, aes(x = block, y = effort))+
  geom_boxplot(width = 0.7, position = position_dodge(0.8))+
  scale_x_discrete(name = "Strategy", 
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression"))+
  geom_jitter(size = 0.4)+
  labs(y = "Effort Rating")


### EMG

# effect of valence on EMG
# corrugator

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
EMGCorrView_con[1,1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize arousal ratings

# figure
FigEMGCorrViewPilot=ggplot2::ggplot(EMG_view, aes(x = block, y = Corr))+
  geom_boxplot(width = 0.7, position = position_dodge(0.8))+
  scale_x_discrete(name = "Active viewing", 
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative"))+
  geom_jitter(size = 0.4)+
  labs(y = "Corrugator activity")

# levator

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
EMGLevView_con[1,1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize arousal ratings

# figure
FigEMGLevViewPilot=ggplot2::ggplot(EMG_view, aes(x = block, y = Lev))+
  geom_boxplot(width = 0.7, position = position_dodge(0.8))+
  scale_x_discrete(name = "Active viewing", 
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative"))+
  geom_jitter(size = 0.4)+
  labs(y = "Levator activity")

# effect of strategy on EMG

EMG_reg <- data_EMG %>%
  subset(data_EMG$block != "1_view_neu" & data_EMG$block != "6_choice")
EMG_reg$block <- as.factor(EMG_reg$block)

# corrugator
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

EMGCorrReg_con$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "2_view_neg"],
                                                                     y = EMG_reg$Corr[EMG_reg$block == "3_distraction"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "2_view_neg"],
                                                                     y = EMG_reg$Corr[EMG_reg$block == "4_distancing"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "2_view_neg"],
                                                                     y = EMG_reg$Corr[EMG_reg$block == "5_suppression"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "3_distraction"],
                                                                     y = EMG_reg$Corr[EMG_reg$block == "4_distancing"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "3_distraction"],
                                                                     y = EMG_reg$Corr[EMG_reg$block == "5_suppression"],
                                                                     progress = FALSE, paired = TRUE))$bf,
                         BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Corr[EMG_reg$block == "4_distancing"],
                                                                     y = EMG_reg$Corr[EMG_reg$block == "5_suppression"],
                                                                     progress = FALSE, paired = TRUE))$bf)

EMGCorrReg_con <- cbind(EMGCorrReg_con,
                        format(effectsize::t_to_eta2(t = EMGCorrReg_con$t.ratio,
                                                     df_error = EMGCorrReg_con$df,
                                                     ci = 0.95),digits = 2))

colnames(EMGCorrReg_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

EMGCorrReg_con[1,1] <- "$View_{negative} - Distraction$"
EMGCorrReg_con[2,1] <- "$View_{negative} - Distancing$"
EMGCorrReg_con[3,1] <- "$View_{negative} - Suppression$"
EMGCorrReg_con[4,1] <- "$Distraction - Distancing$"
EMGCorrReg_con[5,1] <- "$Distraction - Suppression$"
EMGCorrReg_con[6,1] <- "$Distancing - Suppression$"

# Figure to visualize arousal ratings

# figure
FigEMGCorrRegPilot <- ggplot2::ggplot(EMG_reg, aes(x = block, y = Corr))+
  geom_boxplot(width = 0.7, position = position_dodge(0.8))+
  scale_x_discrete(name = "Strategy", 
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression"))+
  geom_jitter(size = 0.4)+
  labs(y = "Corrugator activity")

# levator

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

EMGLevReg_con$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "2_view_neg"],
                                                                    y = EMG_reg$Lev[EMG_reg$block == "3_distraction"],
                                                                    progress = FALSE, paired = TRUE))$bf,
                        BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "2_view_neg"],
                                                                    y = EMG_reg$Lev[EMG_reg$block == "4_distancing"],
                                                                    progress = FALSE, paired = TRUE))$bf,
                        BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "2_view_neg"],
                                                                    y = EMG_reg$Lev[EMG_reg$block == "5_suppression"],
                                                                    progress = FALSE, paired = TRUE))$bf,
                        BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "3_distraction"],
                                                                    y = EMG_reg$Lev[EMG_reg$block == "4_distancing"],
                                                                    progress = FALSE, paired = TRUE))$bf,
                        BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "3_distraction"],
                                                                    y = EMG_reg$Lev[EMG_reg$block == "5_suppression"],
                                                                    progress = FALSE, paired = TRUE))$bf,
                        BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg$Lev[EMG_reg$block == "4_distancing"],
                                                                    y = EMG_reg$Lev[EMG_reg$block == "5_suppression"],
                                                                    progress = FALSE, paired = TRUE))$bf)

EMGLevReg_con <- cbind(EMGLevReg_con,
                       format(effectsize::t_to_eta2(t = EMGLevReg_con$t.ratio,
                                                    df_error = EMGLevReg_con$df,
                                                    ci = 0.95),digits = 2))

colnames(EMGLevReg_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

EMGLevReg_con[1,1] <- "$View_{negative} - Distraction$"
EMGLevReg_con[2,1] <- "$View_{negative} - Distancing$"
EMGLevReg_con[3,1] <- "$View_{negative} - Suppression$"
EMGLevReg_con[4,1] <- "$Distraction - Distancing$"
EMGLevReg_con[5,1] <- "$Distraction - Suppression$"
EMGLevReg_con[6,1] <- "$Distancing - Suppression$"

# Figure to visualize arousal ratings

# figure
FigEMGLevRegPilot <- ggplot2::ggplot(EMG_reg, aes(x = block, y = Lev))+
  geom_boxplot(width = 0.7, position = position_dodge(0.8))+
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  geom_jitter(size = 0.4) +
  labs(y = "Levator activity")

##################### SAVE WORKSPACE IMAGE #######################

save.image(file = "Workspace_ERED.RData")