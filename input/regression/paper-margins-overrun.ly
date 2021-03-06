\version "2.16.0"

#(ly:set-option 'warning-as-error #f)
#(ly:expect-warning (_ "systems run off the page due to improper paper settings, setting default values"))

\header {
  texidoc = "Normally, margin settings must not cause systems to run off the page."
}

#(set-default-paper-size "a4")

someNotes = \relative c' { \repeat unfold 40 { c4 d e f } }

\paper {
  left-margin = 20 \mm
  line-width = 200 \mm
}

\book {
  \score { \someNotes }
}
