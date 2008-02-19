#!/usr/bin/env python

import sys
import os
import glob
import re

USAGE = '''  Usage: makelsr.py LSR_SNIPPETS_DIR
This script must be run from top of the source tree;
it updates snippets input/lsr with snippets in input/new or LSR_SNIPPETS_DIR.
'''

LY_HEADER_LSR = '''%% Do not edit this file; it is auto-generated from LSR http://lsr.dsi.unimi.it
%% This file is in the public domain.
'''

LY_HEADER_NEW = '''%% Do not edit this file; it is auto-generated from input/new
%% This file is in the public domain.
'''

DEST = os.path.join ('input', 'lsr')
NEW_LYS = os.path.join ('input', 'new')

TAGS = []
# NR 1
TAGS.extend (['pitches', 'rhythms', 'expressive-marks',
'repeats', 'simultaneous-notes', 'staff-notation',
'editorial-and-educational-use', 'text'])
# NR 2
TAGS.extend (['vocal-music', 'chords', 'piano-music',
'percussion', 'guitar', 'strings', 'bagpipes', 'ancient-notation'])

# other
TAGS.extend (['contexts-and-engravers', 'tweaks-and-overrides',
'paper-and-layout', 'breaks', 'spacing', 'midi', 'titles', 'template'])

def exit_with_usage (n=0):
	sys.stderr.write (USAGE)
	sys.exit (n)

try:
	in_dir = sys.argv[1]
except:
	exit_with_usage (2)

if not (os.path.isdir (DEST) and os.path.isdir (NEW_LYS)):
	exit_with_usage (3)

unsafe = []
unconverted = []
notags_files = []

# mark the section that will be printed verbatim by lilypond-book
end_header_re = re.compile ('(\\header {.+?(?:"\\s*|\\s+)}\n)\n', re.M | re.S)

def mark_verbatim_section (ly_code):
	return end_header_re.sub ('\\1% begin verbatim\n', ly_code)

# add tags to ly files from LSR
add_tags_re = re.compile ('\\header\\s*{', re.M)

def add_tags (ly_code, tags):
	return add_tags_re.sub ('\\g<0>\n  lsrtags = "' + tags + '"\n', ly_code, 1)

def copy_ly (srcdir, name, tags):
	global unsafe
	global unconverted
	dest = os.path.join (DEST, name)
	tags = ', '.join (tags)
	s = open (os.path.join (srcdir, name)).read ()
	if in_dir in srcdir:
		s = LY_HEADER_LSR + add_tags (s, tags)
	else:
		s = LY_HEADER_NEW + s
	s = mark_verbatim_section (s)
	open (dest, 'w').write (s)
	e = os.system('convert-ly -e ' + dest)
	if e:
		unconverted.append (dest)
	if os.path.exists (dest + '~'):
		os.remove (dest + '~')
	# -V seems to make unsafe snippets fail nicer/sooner
	e = os.system ('nice lilypond -V -dno-print-pages -dsafe -o /tmp/lsrtest ' + dest)
	if e:
		unsafe.append (dest)

def read_source_with_dirs (src):
	s = {}
	l = {}
	for tag in TAGS:
		srcdir = os.path.join (src, tag)
		l[tag] = set (map (os.path.basename, glob.glob (os.path.join (srcdir, '*.ly'))))
		for f in l[tag]:
			if f in s.keys ():
				s[f][1].append (tag)
			else:
				s[f] = (srcdir, [tag])
	return s, l


tags_re = re.compile ('lsrtags\\s*=\\s*"(.+?)"')

def read_source (src):
	s = {}
	l = dict ([(tag, set()) for tag in TAGS])
	for f in glob.glob (os.path.join (src, '*.ly')):
		basename = os.path.basename (f)
		m = tags_re.search (open (f, 'r').read ())
		if m:
			file_tags = [tag.strip() for tag in m.group (1). split(',')]
			s[basename] = (src, file_tags)
			[l[tag].add (basename) for tag in file_tags if tag in TAGS]
		else:
			notags_files.append (f)
	return s, l


def dump_file_list (file, list):
	f = open (file, 'w')
	f.write ('\n'.join (list) + '\n')

## clean out existing lys and generated files
map (os.remove, glob.glob (os.path.join (DEST, '*.ly')) +
     glob.glob (os.path.join (DEST, '*.snippet-list')))

# read LSR source where tags are defined by subdirs
snippets, tag_lists = read_source_with_dirs (in_dir)
# read input/new where tags are directly
s, l = read_source (NEW_LYS)
snippets.update (s)
for t in TAGS:
	tag_lists[t].update (l[t])

for (name, (srcdir, tags)) in snippets.items ():
	copy_ly (srcdir, name, tags)

for (tag, file_set) in tag_lists.items ():
	dump_file_list (os.path.join (DEST, tag + '.snippet-list'), file_set)

if unconverted:
	sys.stderr.write ('These files could not be converted successfully by convert-ly:\n')
	sys.stderr.write ('\n'.join (unconverted) + '\n\n')

if notags_files:
	sys.stderr.write ('No tags could be found in these files:\n')
	sys.stderr.write ('\n'.join (notags_files) + '\n\n')

dump_file_list ('lsr-unsafe.txt', unsafe)
sys.stderr.write ('''

Unsafe files printed in lsr-unsafe.txt: CHECK MANUALLY!
  git add input/lsr
  xargs git-diff HEAD < lsr-unsafe.txt

''')

