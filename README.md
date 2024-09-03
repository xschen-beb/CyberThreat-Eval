# Automating Threat Research from OSINT Feeds

This project aims to build a threat research agent that can leverage the internet to find more information about a given threat, ane then iteratively augment the threat intelligece report. You can find the detailed project description [here](https://microsoft-my.sharepoint.com/:w:/p/aditsha/EV3BKXo3dEpGgICcUf9S67AB8F_7uHGtpaCDlGirGOKW8g?e=uolKOP).


## Install

Pre-requisites: `pdm` is required to install the dependencies. You can follow https://pdm-project.org/en/latest/#recommended-installation-method to install pdm.


```bash
# install dependencies
pdm install
```

## Usage
```bash
# run the script
pdm run python llm4osint_enhance.py
```
