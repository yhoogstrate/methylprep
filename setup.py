# Lib
from setuptools import setup, find_packages

exec(open('pymetharray/version.py').read())
requirements=open('requirements.txt').readlines()

test_requirements = [
    'methylcheck', # 'git+https://github.com/FoxoTech/methylcheck.git@feature/v0.7.7#egg=methylcheck',
    'pytest',
    'pytest_mock',
    'matplotlib',
    'scikit-learn', # openpyxl uses this, and forcing it to install the best version, not sklearn 0.0
    'openpyxl',
    'coverage',
    'beartype'
]

setup(
    name='pymetharray',
    version=__version__,
    description='Python-based Illumina methylation array preprocessing software, fork of methylprep',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls = {
        "Documentation": "https://life-epigenetics-methylprep.readthedocs-hosted.com/en/latest/",
        "Source": "https://github.com/FOXOBioScience/methylprep/",
        "Funding": "https://FOXOBioScience.com/"
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
      ],
    keywords='methylation dna data processing epigenetics illumina',
    url='https://github.com/yhoogstrate/pymetharray',
    license='MIT',
    author=['Dr. Youri Hoogstrate', 'Life Epigenetics'],
    author_email=['y.hoogstrate@erasmusmc.nl','info@FOXOBioScience.com'],
    packages=find_packages(),
    include_package_data=True,
    package_data={"":["*.txt.gz"]},
    install_requires=requirements,
    extras_require={
        'dev': test_requirements
    },
    setup_requires=['pytest-runner'],
    tests_require= test_requirements,
    entry_points='''
        [console_scripts]
        methylprep-cli=methylprep.cli:app
    ''',
)
