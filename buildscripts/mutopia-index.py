#!@PYTHON@
# mutopia-index.py

name = 'mutopia-index'

import find
import re
import os
import sys
import stat

def gulp_file (fn):
	try:
		f = open (fn)
	except:
		raise 'not there' , fn
	return f.read ()

def file_exist_b (fn):
	try:
		f = open (fn)
		return 1
	except:
		return 0


headertext= r"""
These example files are taken from the LilyPond distribution. 
LilyPond currently only outputs TeX and MIDI.  The pictures and 
PostScript files were generated using TeX, Ghostscript and some 
graphics tools.	 The papersize used for these examples is A4. 
The  images are in PNG format, and should be viewable with any current browser.
We don't use GIFS due to <a href="http://www.gnu.org/philosophy/gif.html">patent problems</a>.
<p>
If you want an accurate impression of the output quality please <em>print
out</em> the samples first.
"""

headertext_nopics = r"""This is a subdirectory of the LilyPond example
set.  We decided not to show any examples from this directory.	If you
want to view them, then you have to download LilyPond and compile them
yourself."""


#
# FIXME breaks on multiple strings.
#
def read_mudela_header (fn):
	s = open(fn).read ()
	s = re.sub('%.*$', '', s)
	s = re.sub('\n', ' ', s)		

	dict = {}
	m = re.search (r"""\\header\s*{([^}]*)}""", s)

	if m:
			s = m.group(1)
	else:
			return dict

	while s:
		m = re.search (r"""\s*(\S+)\s*=\s*([^;]+)\s*;""", s)
		if m == None:
			s = ''
		else:
			s = s[m.end (0):]
			left  = m.group	 (1)
			right = m.group (2)

			left = re.sub ('"', '', left)
			right = re.sub ('"', '', right)
			dict[left] = right

	return dict

def help ():
	sys.stdout.write (r"""Usage: mutopia-index [options] INFILE OUTFILE
Generate index for mutopia\n
Options:
  -h, --help                 print this help
  -o,-output=FILE            write output to file.
  -s, --subdirs=DIR	     add subdir
  --suffix=SUF			 specify suffix"""
					  )
	sys.exit (0)

# ugh.
def gen_list(inputs, filename):
	print "generating HTML list %s\n" % filename
	if filename:
		list = open(filename, 'w')
	else:
		list = sys.stdout
	list.write ('<html><TITLE>Rendered Examples</TITLE>\n')
	list.write ('<body bgcolor=white>')
	
	if inputs:
			list.write (headertext)
	else:
			list.write (headertext_nopics)


	for ex in inputs:
		(base, ext) = os.path.splitext (ex)
		(base, ext2) = os.path.splitext (base)		
		ext = ext2 + ext
		
		print '%s, ' % ex
		header = read_mudela_header(ex)
		
		def read_dict(s, default, h =header):
				try:
					ret = h[s]
				except KeyError:
					ret = default
				return ret
		head = read_dict('title', os.path.basename (base))
		composer = read_dict('composer', '')
		desc = read_dict('description', '')
		list.write('<hr>')
		list.write('<h1>example file: %s</h1>' % head);
		if composer <> '':
			list.write('<h2>%s</h2>\n' % composer)
		if desc <> '':
			list.write('%s<p>' % desc)
		list.write ('<ul>')
		def list_item(filename, desc, type, l = list):
			if file_exist_b(filename):
				l.write ('<li><a href=%s>%s</a>' % (filename, desc))
				size=os.stat(filename)[stat.ST_SIZE]
				l.write (' (%s %dk)' % (type, (size + 512) / 1024))
				pictures = ['jpeg', 'png', 'xpm']
				l.write ('\n')

		list_item(base + ext, 'The input', 'ASCII')
		for pageno in range(1,100):
			f  = base + '-page%d.png' % pageno
			if not file_exist_b (f):
				break
			list_item(f, 'The output, page %d' % pageno, 'png')
		list_item(base + '.ps.gz', 'The output', 'gzipped PostScript')
		list_item(base + '.midi', 'The output', 'MIDI')
		list.write ("</ul>");

	list.write( "</BODY></HTML>");
	list.close()

import getopt

(options, files) = getopt.getopt(sys.argv[1:], 
  'ho:', ['help', 'output='])
outfile = 'examples.html'

subdirs =[]
for opt in options:
	o = opt[0]
	a = opt[1]
	if o == '--help' or o == '-h':
		help()
	elif o == '--output' or o == '-o':
		outfile = a

dirs  = []
for f in files:
	dirs = dirs + find.find ('out-www', f);

if not dirs:
	dirs = ['.']

allfiles = []

for d in dirs:
	allfiles = allfiles + find.find ('*.ly.txt', d)

print allfiles

gen_list (allfiles, outfile)

