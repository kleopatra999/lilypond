%% DO NOT EDIT this file manually; it is automatically
%% generated from LSR http://lsr.dsi.unimi.it
%% Make any changes in LSR itself, or in Documentation/snippets/new/ ,
%% and then run scripts/auxiliar/makelsr.py
%%
%% This file is in the public domain.
\version "2.17.11"

\header {
  lsrtags = "rhythms"

  texidoc = "
By default, only the numerator of the tuplet number is printed over the
tuplet bracket, i.e., the denominator of the argument to the
@code{\\times} command. Alternatively, num:den of the tuplet number may
be printed, or the tuplet number may be suppressed altogether.

"
  doctitle = "Changing the tuplet number"
} % begin verbatim


\relative c'' {
  \tuplet 3/2 { c8 c c }
  \tuplet 3/2 { c8 c c }
  \override TupletNumber.text = #tuplet-number::calc-fraction-text
  \tuplet 3/2 { c8 c c }
  \override TupletNumber.stencil = ##f
  \tuplet 3/2 { c8 c c }
}
