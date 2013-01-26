% DO NOT EDIT this file manually; it is automatically
% generated from Documentation/snippets/new
% Make any changes in Documentation/snippets/new/
% and then run scripts/auxiliar/makelsr.py
%
% This file is in the public domain.
%% Note: this file works from version 2.16.0
\version "2.17.11"

\header {
  lsrtags = "pitches, real-music, really-cool, scheme-language"

  texidoc = "
In music that contains many occurrences of the same sequence of notes
at different pitches, the following music function may prove useful.
It takes a note, of which only the pitch is used.   This example
creates the rhythm used throughout Mars, from Gustav Holst's The
Planets.

"
  doctitle = "Creating a sequence of notes on various pitches"
} % begin verbatim


rhythm =
#(define-music-function (parser location p) (ly:pitch?)
   "Make the rhythm in Mars (the Planets) at the given pitch"
  #{ \tuplet 3/2 { $p 8 $p $p } $p 4 $p $p 8 $p $p 4 #})

\new Staff {
  \time 5/4
  \rhythm c'
  \rhythm c''
  \rhythm g
}
