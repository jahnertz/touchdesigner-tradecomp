# touchdesigner-tradecomp

A band-aid solution to getting scores into the Trade Comp show without using an API

## Requirements:
- [TouchDesigner](derivative.ca)
- Python 3.9.5
- [Tesseract](https://tesseract-ocr.github.io/tessdoc/Home.html)
- Spout/Syphon plugin for OBS (https://github.com/Off-World-Live/obs-spout2-plugin)

## Installation:
Install any missing dependencies listed above.
Clone or download the repository and open `tradecomp-scores.toe` in Touchdesigner. Installation scripts should be created in the Dep/ directory in the project root.
Run the relevant install script: `dep_install.cmd` on Windows and `dep_install.sh` on Mac. On Mac, the file's permissions may need to be changed in order to run the script.
The script will install the required python modules (you may need to restart touchdesigner for them to be recognised).

The project can either be run in performance mode (press f1 from the TouchDesigner main window), or opened in TouchPlayer
