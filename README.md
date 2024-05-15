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
> Python ≥ 3.9 & ≤ 3.11
> 
> conda ≥ 24.0.0
> 
> TensorFlow ≥ 2.9 & ≤ 2.15
> 

---

## Required Packages

### Python dependencies:

Anaconda 3 Installation: [Documentation](https://docs.anaconda.com/free/anaconda/install/index.html)

Hugging Face Hub Installation: [Documentation](https://huggingface.co/docs/huggingface_hub/en/installation)

Youdao BCE Embedding Installation: [Documentation](https://github.com/netease-youdao/BCEmbedding/blob/master/README.md)


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

---

## Data Acquisition

Weibo Data is scrapped from the legacy web version of [People's Daily](https://weibo.cn/rmrb) from 01-01-2014 to 12-31-2023.

Crawler is forked from:

```
@misc{WeiboSuperSpider,
    author = {Tao Xiao},
    title = {微博超级爬虫，最强微博爬虫，用户、话题、评论一网打尽。图片下载、情感分析，地理位置、关系网络等功能应有尽有。},
    year = {2019},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/Python3Spiders/WeiboSuperSpider}},
}
```
