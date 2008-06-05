\version "2.11.6"
\header {
  lsrtags = "pitches"
  texidoc = "Makam is a type of melody from Turkey using 1/9th-tone
microtonal alterations.  Consult the initialization file
@code{makam-init.ly) (see the `Learning Manual @version{},
4.6.3 Other sources of information' for the location of this file)
for details of pitch names and alterations."
  doctitle = "Makam"
}

% Initialize makam settings
\include "makam-init.ly"

\relative c' {
  \set Staff.keySignature = #`((3 . ,BAKIYE) (6 . ,(- KOMA)))
  c4 cc db fk
  gbm4 gfc gfb efk
  fk4 db cc c
}
