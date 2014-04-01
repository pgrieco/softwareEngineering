#!/usr/bin/env python
''' This script automatically updates the GitHub repository with the     
    most recent files.

    This script is executed in /dev/py

    Note:
    
        Push message and requested password not automatic.
'''

# standard library
import os
import shutil
import glob 

''' Auxiliary functions.
'''
def copy(src, dst):
    ''' Copy from source to destination.
    ''' 

    if(os.path.isdir(src)):

        shutil.copytree(src, dst, symlinks = True)

    else:

        shutil.copy(src, dst)

''' Setup of directory structure.
'''
private = '/home/peisenha/office/writings/express/practComputing'

public  = '/home/peisenha/office/workspace/softwarePackages/public/teaching/practComputing'

''' Create public distribution.
'''
os.chdir(private)

if(os.path.isdir('tmp')): shutil.rmtree('tmp')

os.system('./waf distclean')

files = glob.glob('*')

files.remove('dev')

files.remove('material')

for file_ in files:

    copy(file_, 'tmp/' + file_)

os.chdir('tmp')

# Check integrity of distribution.

os.system('chmod -R 755 . ')

os.system('./waf configure build')
     
os.system('./waf distclean')   
       
''' Update GitHub directory.
'''
# Cleanup.
os.chdir(public)

list_ = glob.glob('*')
        
for obj in list_:
        
    try:
            
        shutil.rmtree(obj)

    except OSError:
        
        os.unlink(obj)

# Update.
os.chdir(private + '/tmp')

list_ = glob.glob('*')
        
for obj in list_:
        
    src = private + '/tmp/' + obj
        
    dst = public  + '/' + obj

    copy(src, dst)

shutil.rmtree(private + '/tmp')

''' Update GitHub repository.
'''     
os.chdir(public)
        
os.system('chmod -R 444 COPYING')
        
os.system('git add -A')
        
os.system('git commit -m" update of public version"')
        
os.system('git push')   