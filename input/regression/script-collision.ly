#(ly:set-option 'old-relative)
\version "1.9.1"

\header {

    texidoc = "Scripts are put on the utmost head, so they are
      positioned correctly when there are collisions."
}

\score  {
\notes \relative c'' {
  c4
  <<c d c'>>\marcato
  < \context Voice = VA { \voiceOne c4^^ }
    \context Voice = VB { \voiceTwo d4_^} >
    }
\paper { raggedright = ##t}
    }

