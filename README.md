# Decoding State Media Tweets' Impact on a Decade of Chinese Government Policy

Final project for the Machine Learning and Economics course by Jiaxin He and Valentina Simon

---

## Environment Requirements:

> Ubuntu 22.04 or later with CUDA
>
> Windows 10 or later with CUDA
> 
> macOS 11 (Big Sur) with MPS
> 
> R ≥ 3.6
> 
> Python = 3.10
> 
> conda ≥ 24.0.0
> 
> TensorFlow ≤ 2.9.0
> 

---

## Required Packages

### R packages:
```
install_packages("ggplot2")
install_packages("outliers")
install_packages("dplyr")
install_packages("tidyverse")
install_packages(remotes)
install_packages(reticulate)
remotes::install_github("rstudio/tensorflow")
install_packages(keras)

reticulate::install_python(version = "3.10:latest")
keras::install_keras(version = "default", method = "conda", conda = "auto")
use_condaenv("r-tensorflow")
```

