% Do not edit this file; it is automatically
% generated from Documentation/snippets/new
% This file is in the public domain.
%% Note: this file works from version 2.13.26
\version "2.13.31"
\header {
%% Translation of GIT committish: 158658dc75b6f6553e77ff53119ac802eb91f50c
  texidocfr = "LilyPond dispose de trois styles de barre différents
pour indiquer une succession de reprises.  Vous devez opter pour un
  style par défaut, à l'aide de la propriété @code{doubleRepeatType}.

"

  doctitlefr = "Succession de reprise et style de barre par défaut"


  lsrtags = "repeats"
  texidoc = "There are three different styles of double repeats for
volte, that can be set using @code{doubleRepeatType}."

  doctitle = "Setting the double repeat default for volte"
} % begin verbatim



\relative c'' {
  \repeat volta 1 { c1 }
  \set Score.doubleRepeatType = #":|:"
  \repeat volta 1 { c1 }
  \set Score.doubleRepeatType = #":|.|:"
  \repeat volta 1 { c1 }
  \set Score.doubleRepeatType = #":|.:"
  \repeat volta 1 { c1 }
}