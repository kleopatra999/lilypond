\version "2.16.0"

\header {
  texidoc = "Fingering directions in directed and undirected contexts."
}

\layout { ragged-right= ##t }

{
  \relative c''
  \new Voice {
    \tempo "\\voiceTwo"
    \voiceTwo
    c2^5 <c^5>
    c_5 <c_5>
    c-5 <c-5>
    \tempo "\\oneVoice"
    \oneVoice
    c^5 <c^5>
    c_5 <c_5>
    c-5 <c-5>
  } \addlyrics {
    \override LyricText . font-size = #-2
    \override LyricText . font-series = #'bold
    "c^5" "<c^5>"
    "c_5" "<c_5>"
    "c-5" "<c-5>"
    "c^5" "<c^5>"
    "c_5" "<c_5>"
    "c-5" "<c-5>"
  }
}
