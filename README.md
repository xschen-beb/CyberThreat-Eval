# Automating Threat Research from OSINT Feeds

This project aims to build a threat research agent that can leverage the internet to find more information about a given threat, ane then iteratively augment the threat intelligece report. You can find the detailed project description [here](https://microsoft-my.sharepoint.com/:w:/p/aditsha/EV3BKXo3dEpGgICcUf9S67AB8F_7uHGtpaCDlGirGOKW8g?e=uolKOP).


## Install

Pre-requisites: `pdm` is required to install the dependencies. You can follow [the official PDM documentation](https://pdm-project.org/en/latest/#recommended-installation-method) for installation instructions.

Alternatively, if you are using Python >= 3.13, you can directly install dependencies from `requirements.txt`:

```bash
# install dependencies using pdm
pdm install

# or using pip (requires Python >= 3.13)
pip install -r requirements.txt
```

## Usage
```bash
# run the script with pdm
pdm run python run.py

# run the script
python run.py
```
