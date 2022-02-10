library(targets)
library(tarchetypes)
library(here)

# set top level directory to source file
here::i_am("flag_project_root_CERED.txt")

# Set target-specific options such as packages.
tar_option_set(packages = "tidyverse")
options(tidyverse.quiet = TRUE)

# End this file with a list of target objects.
list(
  tar_target(intro, "TheoreticalBackground.Rmd", format = "file"),
  tar_target(method, "Method.Rmd", format = "file"),
  tar_target(Quest, "Questionnaires.R", format = "file"),
  tar_target(raw_data_file, here("04_RawData", "pilot", "CERED_DATA.csv"), format = "file"),
  tar_target(raw_data, read.csv(here("04_RawData", "pilot", "CERED_DATA.csv"),
                                 stringsAsFactors = FALSE, header = TRUE,
                                 na.strings = c("", "NA"))),
  tar_render(whole.paper, "Manuscript_ERED_Stage1.Rmd")
)
