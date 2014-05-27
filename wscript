#!/usr/bin/env python

# imports
import os
import shutil
import glob
import sys
import fnmatch

# directory structure
top = '.'
out = '.bld'

def options(opt):

	opt.load('tex')

def configure(conf):

    conf.load('tex')

def build(bld):

    bld.recurse('slides')
   
    bld.recurse('doc')

    bld.add_post_fun(post_build)

def distclean(ctx):

    remove_for_distclean('.bld')

    remove_for_distclean('tmp')

    filelist = glob.glob('*.pdf')

    for filename in filelist:

        os.remove(filename)

    remove_for_distclean('.waf-1.6.4-8c7ad4bb8e1ca65b04e5d8dd9d0dac54')

    remove_filetypes_distclean('.')


''' Auxiliary functions. 
'''
def post_build(bld):
    ''' Copy files from build directory for easy access.
    '''    
    source = '.bld/slides/introduction/doc.pdf'
    target = 'introduction-slides.pdf'

    shutil.copy(source, target)


    source = '.bld/slides/git/main.pdf'
    target = 'git-slides.pdf'

    shutil.copy(source, target)

    source = '.bld/doc/syllabus/doc.pdf'
    target = 'syllabus.pdf'

    shutil.copy(source, target)

    source = '.bld/slides/recomputation/doc.pdf'
    target = 'recomputation-slides.pdf'

    shutil.copy(source, target)

def remove_for_distclean(path):
    ''' Remove path, where path can be either a directory or a file. The
        appropriate function is selected. Note, however, that if an 
        OSError occurs, the function will just path.
    '''

    if os.path.isdir(path):

        shutil.rmtree(path)
    
    if os.path.isfile(path):

        os.remove(path)

def remove_filetypes_distclean(path):
    ''' Remove nuisance files from the directory tree.
    '''
    matches = []

    for root, dirnames, filenames in os.walk('.'):

        for filetypes in ['*.pyc', '*.bak', '*.so', '*~', '*.aux', '*.log', '*.toc', '*.nav', '*.snm', '.*.xml', '*.blg', '*.bbl', 'notes.pdf', '*.fff*', 'doc.pdf', '*.ttt', '*.out', '*.fdb_*','*.gz']:

                for filename in fnmatch.filter(filenames, filetypes):
                    
                    matches.append(os.path.join(root, filename))

    matches.append('.lock-wafbuild')

    for files in matches:

        remove_for_distclean(files)
	
	
