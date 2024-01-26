#PATH = '/Volumes/LEGX/Barnes/44668_MURMETVEP/204617710009'
#PATH = '/Volumes/LEGX/Barnes/48230_MURMETVEP/361821/204879580038'
PATH = '/docs/example_data/mouse'
import pymetharray
from pathlib import Path
import pytest

def _test_noob_df_same_size():
    print('* loading mouse manifest')
    manifest = pymetharray.files.Manifest(pymetharray.models.ArrayType('mouse'))
    print('* loading one idat pair of files')
    #green_filepath = Path(PATH, '204617710009_R06C02_Grn.idat')
    red_filepath = Path(PATH, '204879580038_R06C02_Red.idat')
    #red_filepath = Path(PATH, '204617710009_R06C02_Red.idat')
    greeb_filepath = Path(PATH, '204879580038_R06C02_Grn.idat')
    print(f"* GREEN --> {green_filepath.name}")
    print(f"* RED --> {red_filepath.name}")
    green_idat = pymetharray.files.IdatDataset(green_filepath, channel=pymetharray.models.Channel.GREEN)
    red_idat = pymetharray.files.IdatDataset(red_filepath, channel=pymetharray.models.Channel.RED)
    sample = 1
    sigset = pymetharray.models.SigSet(sample, green_idat, red_idat, manifest, debug=True)
    #print('* raw_dataset')
    #raw_dataset = pymetharray.processing.raw_dataset.RawDataset(sample, green_idat, red_idat)
    #print('* meth_dataset.unmethylated')
    #unmethylated = pymetharray.models.MethylationDataset.unmethylated(raw_dataset, manifest)
    #print('* meth_dataset.methylated')
    #methylated = pymetharray.models.MethylationDataset.methylated(raw_dataset, manifest)
    return green_idat, red_idat

    #grn, red = test_noob_df_same_size()


    manifest = pymetharray.files.Manifest(pymetharray.models.ArrayType('450k'))
    green_filepath = Path(PATH, '9247377085_R04C02_Grn.idat')
    red_filepath = Path(PATH, '9247377085_R04C02_Red.idat')
    print(f"* GREEN --> {green_filepath.name}")
    print(f"* RED --> {red_filepath.name}")
    green_idat = pymetharray.files.IdatDataset(green_filepath, channel=pymetharray.models.Channel.GREEN)
    red_idat = pymetharray.files.IdatDataset(red_filepath, channel=pymetharray.models.Channel.RED)
    sample = 1
    sigset = pymetharray.models.SigSet(sample, green_idat, red_idat, manifest, debug=True)


def test_run_pipeline_all_the_invalid_kwargs():
    test_data_dir = 'docs/example_data/GSE69852'
    with pytest.raises(ValueError) as excinfo:
        pymetharray.run_pipeline(test_data_dir, bit='float')
        if "must be one of" not in str(excinfo.value):
            raise AssertionError("bit should throw error but didn't throw right message")
    with pytest.raises( (KeyError,SystemExit) ):
        pymetharray.run_pipeline(test_data_dir, blah='blah')
    with pytest.raises(ValueError):
        pymetharray.run_pipeline(test_data_dir, batch_size='blah')
    with pytest.raises(SystemExit) as excinfo:
        pymetharray.run_pipeline('docs/example_data')
        # should be multiple arrays error
        if "This folder contains idats for multiple types of arrays." not in str(excinfo.value):
            raise AssertionError("docs/example_data contains idats for multiple types of arrays, but did not throw exception.")

# untested parts of code:
#  test_run_pipeline_noname_samplesheet

def test_check_array_folder():
    test_data_dir = 'docs/example_data/GSE69852'
    pymetharray.processing.multi_array_idat_batches.check_array_folders(test_data_dir)
