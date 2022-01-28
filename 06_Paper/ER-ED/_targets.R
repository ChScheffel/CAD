library(targets)
library(tarchetypes)

# Set target-specific options such as packages.
tar_option_set(packages = "tidyverse")
options(tidyverse.quiet = TRUE)

# End this file with a list of target objects.
list(
  tar_target(whole.paper, "Manuscript_ERED_Stage1.Rmd"),
  tar_target(intro, "TheoreticalBackground.Rmd"),
  tar_target(method, "Method.Rmd"),
  tar_target(Quest, "Questionnaires.R")
)
