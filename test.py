#!/usr/bin/env python

"""
Install:

virtualenv -p python3 .venv
source .venv/bin/activate


pip install uninstall pymetharray
pip install .
pip list | grep pymetharray

mkdir cache
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6379nnn/GSM6379997/suppl/GSM6379997%5F203927450093%5FR01C01%5FRed.idat.gz --output-document=cache/GSM6379997_203927450093_R01C01_Red.idat.gz
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6379nnn/GSM6379997/suppl/GSM6379997%5F203927450093%5FR01C01%5FGrn.idat.gz --output-document=cache/GSM6379997_203927450093_R01C01_Grn.idat.gz

gunzip cache/GSM6379997_203927450093_R01C01_Red.idat.gz
gunzip cache/GSM6379997_203927450093_R01C01_Grn.idat.gz

python
"""

import logging
logging.basicConfig(level=logging.DEBUG)

from pymetharray.files import create_sample_sheet
print(create_sample_sheet('cache/', output_file='cache/samplesheet.csv', output_path = "."))

