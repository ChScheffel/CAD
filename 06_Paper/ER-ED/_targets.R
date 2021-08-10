library(targets)
library(tarchetypes)

# Set target-specific options such as packages.
tar_option_set(packages = "tidyverse")
options(tidyverse.quiet = TRUE)

# End this file with a list of target objects.
list(
  tar_target(method.section, "method.Rmd")
)
