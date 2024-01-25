#!/usr/bin/env python

"""
Install & prep test:

virtualenv -p python3 .venv
source .venv/bin/activate


pip install uninstall pymetharray
pip install .
pip list | grep pymetharray

mkdir -p cache

rm -rf cache/GSM6379997_203927450093_R01C01_Red.idat.gz
rm -rf cache/GSM6379997_203927450093_R01C01_Grn.idat.gz

wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6379nnn/GSM6379997/suppl/GSM6379997%5F203927450093%5FR01C01%5FRed.idat.gz --output-document=cache/GSM6379997_203927450093_R01C01_Red.idat.gz
wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6379nnn/GSM6379997/suppl/GSM6379997%5F203927450093%5FR01C01%5FGrn.idat.gz --output-document=cache/GSM6379997_203927450093_R01C01_Grn.idat.gz

gunzip cache/GSM6379997_203927450093_R01C01_Red.idat.gz
gunzip cache/GSM6379997_203927450093_R01C01_Grn.idat.gz

python

"""

import logging
logging.basicConfig(level=logging.DEBUG)

from pymetharray.files import create_sample_sheet
ss = create_sample_sheet('cache/', output_file='cache/samplesheet.csv', output_path = ".")


ss.build_samples()
sls = ss.get_samples()

from pymetharray.models.raw_dataset import *

sls[0].get_filepath("idat")

#ds1 = RawDataset(sls[0])
ds1 = RawDataset(12334456)

