library(targets)
library(tarchetypes)

# Set target-specific options such as packages.
tar_option_set(packages = "tidyverse")
options(tidyverse.quiet = TRUE)

# End this file with a list of target objects.
list(
  tar_target(whole.report, "report.Rmd"),
  tar_target(intro, "intro.Rmd"),
  tar_target(method, "method.Rmd")
)
