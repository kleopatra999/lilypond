%% Do not edit this file; it is auto-generated from LSR http://lsr.dsi.unimi.it
%% This file is in the public domain.
\version "2.11.48"

\header {
  lsrtags = "text, keyboards, template"

  texidoc = "
Instead of having a full staff for the melody and lyrics, lyrics can be
centered between the staves of a piano staff.

"
  doctitle = "Piano template with centered lyrics"
} % begin verbatim
upper = \relative c'' {
  \clef treble
  \key c \major
  \time 4/4
  
  a4 b c d  
}

lower = \relative c {
  \clef bass
  \key c \major
  \time 4/4
  
  a2 c  
}

text = \lyricmode {
  Aaa Bee Cee Dee
}

\score {
  \new GrandStaff <<
    \new Staff = upper { \new Voice = "singer" \upper }
    \new Lyrics \lyricsto "singer" \text
    \new Staff = lower { \lower }
  >>
  \layout {
    \context {
      \GrandStaff
      \accepts "Lyrics"
    }
    \context {
      \Lyrics
      \consists "Bar_engraver"
    }
  }
  \midi { }
}
