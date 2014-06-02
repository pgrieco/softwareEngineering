#!/usr/bin/env python
''' This script provisions the required software environment to ensure
	full recomputability of John Eric's  breakthrough script
	*WorkingWithData.R*. After an intial setup, we first prepare the computing 
	environment and then run the analysis. 
'''

# standard library
import shutil
import glob
import os

''' Set up provisioning script.
'''
host, guest  = '/vagrant', '/home/vagrant'

os.chdir(host)

''' Prepare Computing Environment.
'''
# Install viewer
os.system('sudo apt-get install vim ')

# Check out the repository.
os.system('git clone https://github.com/practComp2014/humphries_rapidRIntro.git')

# Install packages.
os.system('sudo Rscript r-packages.r')

''' Run analysis.
'''
os.chdir('humphries_rapidRIntro')

os.system(' Rscript WorkingWithData.R')
