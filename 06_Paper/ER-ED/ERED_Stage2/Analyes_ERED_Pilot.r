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

##################### DATA IMPORT #######################

# import ER ratings and ER discounting data into lists

datalist_ER_pilot <- lapply(list.files(here("04_RawData", "pilot", "ER-ED/logfiles"),
                                       pattern = "*_ER.*csv", full.names = TRUE),
                                       read.csv, stringsAsFactors = FALSE,
                                       header = TRUE)
  
datalist_ED_pilot <- lapply(list.files(here("04_RawData", "pilot", "ER-ED/logfiles"),
                                       pattern = "*_ED.*csv", full.names = TRUE),
                                       read.csv, stringsAsFactors = FALSE,
                                       header = TRUE)

# new empty frame to store files into
data_ER_pilot <- data.frame(ID = character(), block = character(),
                            arousal = double(), effort = double(),
                            trigger = double(), trigger_reg = double())

data_ED_pilot <- data.frame(ID = character(), step = double(),
                            choice = character(), LBvalue = double(),
                            LBlevel = double(), RBvalue = double(),
                            RBlevel = double())

data_choice_pilot <- data.frame(ID = character(), choice = double())

# store arousal and effort ratings in data_ER frame
for (i in seq_len(length(datalist_ER_pilot))) {
    tmp <- data.frame(datalist_ER_pilot[[i]][["participant"]],
                     datalist_ER_pilot[[i]][["instr_1"]],
                     datalist_ER_pilot[[i]][["slider_arousal.response"]],
                     datalist_ER_pilot[[i]][["slider_effort.response"]],
                     datalist_ER_pilot[[i]][["TriggerBlockView"]],
                     datalist_ER_pilot[[i]][["TriggerBlockReg"]])
    colnames(tmp) <- names(data_ER_pilot)
    tmp <- tmp[(!is.na(tmp$arousal)), ]
    
    data_ER_pilot <- rbind(tmp, data_ER_pilot)
   }

rownames(data_ER_pilot) <- seq_len(nrow(data_ER_pilot))

# loop to store trigger in one column

for (i in seq_len(nrow(data_ER_pilot))) {
  if (is.na(data_ER_pilot$trigger[i])) {
    data_ER_pilot$trigger[i] <- data_ER_pilot$trigger_reg[i]
  }
  
  if (is.na(data_ER_pilot$trigger[i])) {
    data_ER_pilot$trigger[i] <- 26
  }
}

# delete old column

data_ER_pilot$trigger_reg <- NULL

# loop to correct block indicator

data_ER_pilot$block[data_ER_pilot$trigger == 21] <- "1_view_neu"
data_ER_pilot$block[data_ER_pilot$trigger == 22] <- "2_view_neg"
data_ER_pilot$block[data_ER_pilot$trigger == 23] <- "3_distraction"
data_ER_pilot$block[data_ER_pilot$trigger == 24] <- "4_distancing"
data_ER_pilot$block[data_ER_pilot$trigger == 25] <- "5_suppression"
data_ER_pilot$block[data_ER_pilot$trigger == 26] <- "6_choice"

# store ER choice in data_choice frame

for (i in seq_len(length(datalist_ER_pilot))) {
  tmp <- data.frame(datalist_ER_pilot[[i]][["participant"]],
                    datalist_ER_pilot[[i]][["resp_choice.keys"]])
  colnames(tmp) <- names(data_choice_pilot)
  tmp <- tmp[(!is.na(tmp$choice)), ]
  
  data_choice_pilot <- rbind(tmp, data_choice_pilot)
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

datalist_EMG_pilot <- lapply(list.files(here("04_RawData", "pilot", "ER-ED", "EMG", "analysis"),
                                        pattern = "*_Peaks.txt", full.names = TRUE),
                            read.table, stringsAsFactors = FALSE, header = TRUE)
datalist_EMG_Marker_pilot <- lapply(list.files(here("04_RawData", "pilot", "ER-ED", "EMG", "analysis"),
                                               pattern = "*.Markers", full.names = TRUE),
                                    read.table, stringsAsFactors = FALSE, header = TRUE,
                                    skip = 1, row.names = NULL, sep = ",")

# new empty frame to store files into
data_EMG_pilot <- data.frame(ID = character(), trigger = double(), Corr = double(),
                     Lev = double())

# store EMG data in data_EMG frame
for (i in seq_len(length(datalist_EMG_pilot))) {
  tmp <- data.frame(datalist_EMG_pilot[[i]][["Filename"]],
                   datalist_EMG_Marker_pilot[[i]][["Description"]],
                   datalist_EMG_pilot[[i]][["T0T6000Corr.ASNM"]],
                   datalist_EMG_pilot[[i]][["T0T6000Lev.ASNM"]])
  colnames(tmp) <- names(data_EMG_pilot)
  
  data_EMG_pilot <- rbind(tmp, data_EMG_pilot)
}

# create variable "block"

data_EMG_pilot$block[data_EMG_pilot$trigger == " S 21"] <- "1_view_neu"
data_EMG_pilot$block[data_EMG_pilot$trigger == " S 22"] <- "2_view_neg"
data_EMG_pilot$block[data_EMG_pilot$trigger == " S 23"] <- "3_distraction"
data_EMG_pilot$block[data_EMG_pilot$trigger == " S 24"] <- "4_distancing"
data_EMG_pilot$block[data_EMG_pilot$trigger == " S 25"] <- "5_suppression"
data_EMG_pilot$block[data_EMG_pilot$trigger == " S 26"] <- "6_choice"


# import questionnaire data from RedCap
  
data_redcap_pilot <- read.csv(here("04_RawData", "pilot", "CERED_DATA.csv"),
                              stringsAsFactors = FALSE, header = TRUE,
                              na.strings = c("", "NA"))
colnames(data_redcap_pilot)[1] <- "set" # rename the first column

# remove unnecessary variables from questionnaire data frame
  
data_quest_raw_pilot <- data_redcap_pilot %>%
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

data_quest_pilot <- data_redcap_pilot %>%
    subset(!is.na(subject), select = c(subject, age, gender, edu))

##################### EFFECTS OF ER ON SUBJECTIVE AND PHYSIOLOGICAL MARKERS #######################

## Subjective arousal

# ANOVA subjective arousal ratings
# View condition

Ratings_view_pilot <- data_ER_pilot %>%
  subset(data_ER_pilot$block == "1_view_neu" | data_ER_pilot$block == "2_view_neg")
Ratings_view_pilot$block <- as.factor(Ratings_view_pilot$block)

SubjArousalView_pilot_aov <- afex::aov_ez(data = Ratings_view_pilot,
                                          id = "ID",
                                          dv = "arousal",
                                          within = "block",
                                          fun_aggregate = mean,
                                          include_aov = TRUE)

# compute posthoc tests for within measures
SubjArousalView_pilot_emm <- emmeans::emmeans(SubjArousalView_pilot_aov$aov, specs = "block")

SubjArousalView_pilot_con <- as.data.frame(pairs(SubjArousalView_pilot_emm, adjust = "bonferroni"))

# Bayes Factors
SubjArousalView_pilot_BF <- BayesFactor::anovaBF(formula = arousal ~ block,
                                                 data = Ratings_view_pilot,
                                                 progress = FALSE)
SubjArousalView_pilot_con$BF10 <- BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_view_pilot$arousal[Ratings_view_pilot$block == "1_view_neu"],
                                                                              y = Ratings_view_pilot$arousal[Ratings_view_pilot$block == "2_view_neg"],
                                                                              progress = FALSE, paired = TRUE))$bf

SubjArousalView_pilot_con <- cbind(SubjArousalView_pilot_con,
                                  format(effectsize::t_to_eta2(t = SubjArousalView_pilot_con$t.ratio,
                                                               df_error = SubjArousalView_pilot_con$df,
                                                               ci = 0.95),
                                                               digits = 2))

colnames(SubjArousalView_pilot_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
# rename contrast for table
SubjArousalView_pilot_con[1, 1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize arousal ratings

FigSubjArousalViewPilot <- ggplot2::ggplot(Ratings_view_pilot, aes(x = block, y = arousal, fill = block)) +
  geom_boxplot(width = .2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  ylim(c(0,400))+
  scale_x_discrete(name = "Active viewing",
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative")) +
  scale_color_viridis() +
  labs(y = "Arousal Rating") +
  theme_minimal()+
  theme(legend.position = "none")

# View neg and regulate conditions

Ratings_reg_pilot <- data_ER_pilot %>%
  subset(data_ER_pilot$block != "1_view_neu" & data_ER_pilot$block != "6_choice")
Ratings_reg_pilot$block <- as.factor(Ratings_reg_pilot$block)


SubjArousalReg_pilot_aov <- afex::aov_ez(data = Ratings_reg_pilot,
                                         id = "ID",
                                         dv = "arousal",
                                         within = "block",
                                         fun_aggregate = mean,
                                         include_aov = TRUE)

# compute posthoc tests for within measures
SubjArousalReg_pilot_emm <- emmeans::emmeans(SubjArousalReg_pilot_aov$aov, specs = "block")

SubjArousalReg_pilot_con <- as.data.frame(pairs(SubjArousalReg_pilot_emm, adjust = "bonferroni"))

# Bayes Factors
SubjArousalReg_pilot_BF <- BayesFactor::anovaBF(formula = arousal ~ block,
                                                data = Ratings_reg_pilot,
                                                progress = FALSE)

SubjArousalReg_pilot_con$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "2_view_neg"],
                                                                               y = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "3_distraction"],
                                                                               progress = FALSE, paired = TRUE))$bf,
                                   BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "2_view_neg"],
                                                                               y = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "4_distancing"],
                                                                               progress = FALSE, paired = TRUE))$bf,
                                   BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "2_view_neg"],
                                                                               y = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "5_suppression"],
                                                                               progress = FALSE, paired = TRUE))$bf,
                                   BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "3_distraction"],
                                                                               y = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "4_distancing"],
                                                                               progress = FALSE, paired = TRUE))$bf,
                                   BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "3_distraction"],
                                                                               y = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "5_suppression"],
                                                                               progress = FALSE, paired = TRUE))$bf,
                                   BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "4_distancing"],
                                                                               y = Ratings_reg_pilot$arousal[Ratings_reg_pilot$block == "5_suppression"],
                                                                               progress = FALSE, paired = TRUE))$bf)
 
SubjArousalReg_pilot_con <- cbind(SubjArousalReg_pilot_con,
                                  format(effectsize::t_to_eta2(t = SubjArousalReg_pilot_con$t.ratio,
                                                              df_error = SubjArousalReg_pilot_con$df,
                                                              ci = 0.95),
                                        digits = 2))

colnames(SubjArousalReg_pilot_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

SubjArousalReg_pilot_con[1, 1] <- "$View_{negative} - Distraction$"
SubjArousalReg_pilot_con[2, 1] <- "$View_{negative} - Distancing$"
SubjArousalReg_pilot_con[3, 1] <- "$View_{negative} - Suppression$"
SubjArousalReg_pilot_con[4, 1] <- "$Distraction - Distancing$"
SubjArousalReg_pilot_con[5, 1] <- "$Distraction - Suppression$"
SubjArousalReg_pilot_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize arousal ratings

# figure
FigSubjArousalRegPilot <- ggplot2::ggplot(Ratings_reg_pilot, aes(x = block, y = arousal, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  ylim(c(0,400))+
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  scale_color_viridis(discrete = TRUE) +
  labs(y = "Arousal Rating") +
  theme_minimal()+
  theme(legend.position = "none")


## Subjective effort

SubjEffort_pilot_aov <- afex::aov_ez(data = Ratings_reg_pilot,
                                     id = "ID",
                                     dv = "effort",
                                     within = "block",
                                     fun_aggregate = mean,
                                     include_aov = TRUE)

# compute posthoc tests for within measure
SubjEffort_pilot_emm <- emmeans::emmeans(SubjEffort_pilot_aov$aov, specs = "block")

SubjEffort_pilot_con <- as.data.frame(pairs(SubjEffort_pilot_emm, adjust = "bonferroni"))

# Bayes Factors
SubjEffort_pilot_BF <- BayesFactor::anovaBF(formula = effort ~ block,
                                            data = Ratings_reg_pilot,
                                            progress = FALSE)

SubjEffort_pilot_con$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "2_view_neg"],
                                                                           y = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "3_distraction"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "2_view_neg"],
                                                                           y = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "4_distancing"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "2_view_neg"],
                                                                           y = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "5_suppression"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "3_distraction"],
                                                                           y = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "4_distancing"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "3_distraction"],
                                                                           y = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "5_suppression"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "4_distancing"],
                                                                           y = Ratings_reg_pilot$effort[Ratings_reg_pilot$block == "5_suppression"],
                                                                           progress = FALSE, paired = TRUE))$bf)
 
SubjEffort_pilot_con <- cbind(SubjEffort_pilot_con,
                        format(effectsize::t_to_eta2(t = SubjEffort_pilot_con$t.ratio,
                                                     df_error = SubjEffort_pilot_con$df,
                                                     ci = 0.95),
                               digits = 2))

colnames(SubjEffort_pilot_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

SubjEffort_pilot_con[1, 1] <- "$View_{negative} - Distancing$"
SubjEffort_pilot_con[2, 1] <- "$View_{negative} - Distraction$"
SubjEffort_pilot_con[3, 1] <- "$View_{negative} - Suppression$"
SubjEffort_pilot_con[4, 1] <- "$Distraction - Distancing$"
SubjEffort_pilot_con[5, 1] <- "$Distraction - Suppression$"
SubjEffort_pilot_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize effort ratings
# figure
FigSubjEffortPilot <- ggplot2::ggplot(Ratings_reg_pilot, aes(x = block, y = effort, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  ylim(c(0,400))+
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  scale_color_viridis(discrete = TRUE) +
  labs(y = "Effort Rating") +
  theme_minimal()+
  theme(legend.position = "none")


### EMG

# effect of valence on EMG
# corrugator

EMG_view_pilot <- data_EMG_pilot %>%
  subset(data_EMG_pilot$block == "1_view_neu" | data_EMG_pilot$block == "2_view_neg")
EMG_view_pilot$block <- as.factor(EMG_view_pilot$block)

EMGCorrView_pilot_aov <- afex::aov_ez(data = EMG_view_pilot,
                                      id = "ID",
                                      dv = "Corr",
                                      within = "block",
                                      fun_aggregate = mean,
                                      include_aov = TRUE)

# compute posthoc tests for within measures
EMGCorrView_pilot_emm <- emmeans::emmeans(EMGCorrView_pilot_aov$aov, specs = "block")

EMGCorrView_pilot_con <- as.data.frame(pairs(EMGCorrView_pilot_emm, adjust = "bonferroni"))

# Bayes Factors
EMGCorrView_pilot_BF <- BayesFactor::anovaBF(formula = Corr ~ block,
                                             data = EMG_view_pilot,
                                             progress = FALSE)
EMGCorrView_pilot_con$BF10 <- BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_view_pilot$Corr[EMG_view_pilot$block == "1_view_neu"],
                                                                          y = EMG_view_pilot$Corr[EMG_view_pilot$block == "2_view_neg"],
                                                                          progress = FALSE, paired = TRUE))$bf

EMGCorrView_pilot_con <- cbind(EMGCorrView_pilot_con,
                         format(effectsize::t_to_eta2(t = EMGCorrView_pilot_con$t.ratio,
                                                      df_error = EMGCorrView_pilot_con$df,
                                                      ci = 0.95),
                                                      digits = 2))

colnames(EMGCorrView_pilot_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
# rename contrast for table
EMGCorrView_pilot_con[1, 1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize  corrugator

# figure
FigEMGCorrViewPilot <- ggplot2::ggplot(EMG_view_pilot, aes(x = block, y = Corr, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  scale_x_discrete(name = "Active viewing",
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative")) +
  scale_color_viridis(discrete = TRUE) +
  labs(y = "Corrugator activity") +
  theme_minimal() +
  theme(legend.position = "none")

# levator

EMGLevView_pilot_aov <- afex::aov_ez(data = EMG_view_pilot,
                                     id = "ID",
                                     dv = "Lev",
                                     within = "block",
                                     fun_aggregate = mean,
                                     include_aov = TRUE)

# compute posthoc tests for within measures
EMGLevView_pilot_emm <- emmeans::emmeans(EMGLevView_pilot_aov$aov, specs = "block")

EMGLevView_pilot_con <- as.data.frame(pairs(EMGLevView_pilot_emm, adjust = "bonferroni"))

# Bayes Factors
EMGLevView_pilot_BF <- BayesFactor::anovaBF(formula = Lev ~ block,
                                            data = EMG_view_pilot,
                                            progress = FALSE)
EMGLevView_pilot_con$BF10 <- BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_view_pilot$Lev[EMG_view_pilot$block == "1_view_neu"],
                                                                         y = EMG_view_pilot$Lev[EMG_view_pilot$block == "2_view_neg"],
                                                                         progress = FALSE, paired = TRUE))$bf

EMGLevView_pilot_con <- cbind(EMGLevView_pilot_con,
                        format(effectsize::t_to_eta2(t = EMGLevView_pilot_con$t.ratio,
                                                     df_error = EMGLevView_pilot_con$df,
                                                     ci = 0.95),
                                                     digits = 2))

colnames(EMGLevView_pilot_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")
# rename contrast for table
EMGLevView_pilot_con[1, 1] <- "$View_{neutral} - View_{negative}$"

# Figure to visualize levator activity

# figure
FigEMGLevViewPilot=ggplot2::ggplot(EMG_view_pilot, aes(x = block, y = Lev, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  scale_x_discrete(name = "Active viewing",
                   limits = c("1_view_neu", "2_view_neg"),
                   labels = c("Neutral", "Negative")) +
  scale_color_viridis(discrete = TRUE) +
  labs(y = "Levator activity") +
  theme_minimal() +
  theme(legend.position = "none")


# effect of strategy on EMG

EMG_reg_pilot <- data_EMG_pilot %>%
  subset(data_EMG_pilot$block != "1_view_neu" & data_EMG_pilot$block != "6_choice")
EMG_reg_pilot$block <- as.factor(EMG_reg_pilot$block)

# corrugator
EMGCorrReg_pilot_aov <- afex::aov_ez(data = EMG_reg_pilot,
                                     id = "ID",
                                     dv = "Corr",
                                     within = "block",
                                     fun_aggregate = mean,
                                     include_aov = TRUE)

# compute posthoc tests for within measures
EMGCorrReg_pilot_emm <- emmeans::emmeans(EMGCorrReg_pilot_aov$aov, specs = "block")

EMGCorrReg_pilot_con <- as.data.frame(pairs(EMGCorrReg_pilot_emm, adjust = "bonferroni"))

# Bayes Factors
EMGCorrReg_pilot_BF <- BayesFactor::anovaBF(formula = Corr ~ block,
                                            data = EMG_reg_pilot,
                                            progress = FALSE)

EMGCorrReg_pilot_con$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "2_view_neg"],
                                                                           y = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "3_distraction"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "2_view_neg"],
                                                                           y = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "4_distancing"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "2_view_neg"],
                                                                           y = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "5_suppression"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "3_distraction"],
                                                                           y = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "4_distancing"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "3_distraction"],
                                                                           y = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "5_suppression"],
                                                                           progress = FALSE, paired = TRUE))$bf,
                               BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "4_distancing"],
                                                                           y = EMG_reg_pilot$Corr[EMG_reg_pilot$block == "5_suppression"],
                                                                           progress = FALSE, paired = TRUE))$bf)
 
EMGCorrReg_pilot_con <- cbind(EMGCorrReg_pilot_con,
                              format(effectsize::t_to_eta2(t = EMGCorrReg_pilot_con$t.ratio,
                                                          df_error = EMGCorrReg_pilot_con$df,
                                                          ci = 0.95),digits = 2))

colnames(EMGCorrReg_pilot_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

EMGCorrReg_pilot_con[1, 1] <- "$View_{negative} - Distraction$"
EMGCorrReg_pilot_con[2, 1] <- "$View_{negative} - Distancing$"
EMGCorrReg_pilot_con[3, 1] <- "$View_{negative} - Suppression$"
EMGCorrReg_pilot_con[4, 1] <- "$Distraction - Distancing$"
EMGCorrReg_pilot_con[5, 1] <- "$Distraction - Suppression$"
EMGCorrReg_pilot_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize corrugator activity

# figure
FigEMGCorrRegPilot <- ggplot2::ggplot(EMG_reg_pilot, aes(x = block, y = Corr, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  scale_color_viridis(discrete = TRUE) +
  labs(y = "Corrugator activity") +
  theme_minimal() +
  theme(legend.position = "none")

# levator

EMGLevReg_pilot_aov <- afex::aov_ez(data = EMG_reg_pilot,
                                    id = "ID",
                                    dv = "Lev",
                                    within = "block",
                                    fun_aggregate = mean,
                                    include_aov = TRUE)

# compute posthoc tests for within measures
EMGLevReg_pilot_emm <- emmeans::emmeans(EMGLevReg_pilot_aov$aov, specs = "block")

EMGLevReg_pilot_con <- as.data.frame(pairs(EMGLevReg_pilot_emm, adjust = "bonferroni"))

# Bayes Factors
EMGLevReg_pilot_BF <- BayesFactor::anovaBF(formula = Lev ~ block,
                                           data = EMG_reg_pilot,
                                           progress = FALSE)
 
EMGLevReg_pilot_con$BF10 <- c(BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "2_view_neg"],
                                                                          y = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "3_distraction"],
                                                                          progress = FALSE, paired = TRUE))$bf,
                              BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "2_view_neg"],
                                                                          y = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "4_distancing"],
                                                                          progress = FALSE, paired = TRUE))$bf,
                              BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "2_view_neg"],
                                                                          y = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "5_suppression"],
                                                                          progress = FALSE, paired = TRUE))$bf,
                              BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "3_distraction"],
                                                                          y = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "4_distancing"],
                                                                          progress = FALSE, paired = TRUE))$bf,
                              BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "3_distraction"],
                                                                          y = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "5_suppression"],
                                                                          progress = FALSE, paired = TRUE))$bf,
                              BayesFactor::extractBF(BayesFactor::ttestBF(x = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "4_distancing"],
                                                                          y = EMG_reg_pilot$Lev[EMG_reg_pilot$block == "5_suppression"],
                                                                          progress = FALSE, paired = TRUE))$bf)

EMGLevReg_pilot_con <- cbind(EMGLevReg_pilot_con,
                             format(effectsize::t_to_eta2(t = EMGLevReg_pilot_con$t.ratio,
                                                           df_error = EMGLevReg_pilot_con$df,
                                                           ci = 0.95),digits = 2))
 
colnames(EMGLevReg_pilot_con) <- c("Contrast", "Estimate", "$SE$", "$df$", "$t$", "$p$", "$BF10$", "$\\eta_{p}^{2}$", "$95\\% CI$")

EMGLevReg_pilot_con[1, 1] <- "$View_{negative} - Distraction$"
EMGLevReg_pilot_con[2, 1] <- "$View_{negative} - Distancing$"
EMGLevReg_pilot_con[3, 1] <- "$View_{negative} - Suppression$"
EMGLevReg_pilot_con[4, 1] <- "$Distraction - Distancing$"
EMGLevReg_pilot_con[5, 1] <- "$Distraction - Suppression$"
EMGLevReg_pilot_con[6, 1] <- "$Distancing - Suppression$"

# Figure to visualize levator activity

# figure
FigEMGLevRegPilot <- ggplot2::ggplot(EMG_reg_pilot, aes(x = block, y = Lev, fill = block)) +
  geom_boxplot(width = 0.2, alpha = .95) +
  geom_jitter(size = .3, position = position_jitterdodge(jitter.width = 0.2, dodge.width = 0.2), alpha = .3)+
  geom_violinhalf(position = position_nudge(x = .12), alpha = .3) +
  scale_x_discrete(name = "Strategy",
                   limits = c("2_view_neg", "3_distraction", "4_distancing", "5_suppression"),
                   labels = c("View", "Distraction", "Distancing", "Suppression")) +
  scale_color_viridis(discrete = TRUE) +
  labs(y = "Levator activity") +
  theme_minimal() +
  theme(legend.position = "none")

##################### SAVE WORKSPACE IMAGE #######################

save.image(file = "Workspace_ERED_pilot.RData")