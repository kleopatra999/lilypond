#(ly:set-option 'old-relative)
\version "1.9.1"

% test for ascii-art output

\include "paper-as9.ly"

\score {
	\notes\relative c'{
		\time 4/4
		c8( e g )b
		d( d d )d
		\bar "|."
	}
	\paper {
		linewidth=65.0\char
    		\translator { \StaffContext barSize = #9 }
		%\translator { \VoiceContext beamHeight = #0 }
		\translator { \VoiceContext beamHeight = ##f }
	}

}

