#!/usr/bin/env python
''' This script provisions the required software environment to ensure
	full recomputability of John Eric's  breakthrough script
	*WorkingWithData.R*. After an initial setup, we first prepare the computing 
	environment and then run the analysis. 
'''

# standard library
import shutil
import glob
import os

''' Set up provisioning script.
'''
host, guest  = '/vagrant', '/home/vagrant'

''' Prepare Computing Environment.
'''
os.chdir(host)

# Install viewer
os.system('sudo apt-get install vim ')

# Install packages.
os.system('sudo Rscript r-packages.r')

''' Run analysis.
'''
os.chdir(guest)

# Check out the repository.
os.system('git clone https://github.com/practComp2014/humphries_rapidRIntro.git')

os.chdir('humphries_rapidRIntro')

os.system(' Rscript WorkingWithData.R')
