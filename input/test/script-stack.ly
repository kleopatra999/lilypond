#(ly:set-option 'old-relative)
\version "1.9.1"

\header { texidoc = "@cindex Stacked Text Articulation
You can stack text and articulations. "
}

\score {
	\notes\relative c' {
		c2_"geen gedonder"_"jij gaat onder"
		c2^^^.^|^"down"^"up"
	 }
	\paper { raggedright = ##t}
}

