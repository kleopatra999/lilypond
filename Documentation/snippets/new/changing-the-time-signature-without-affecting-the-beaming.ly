\version "2.13.5"

\header {
  lsrtags = "rhythms"

%% Translation of GIT committish: b2d4318d6c53df8469dfa4da09b27c15a374d0ca
  texidoces = "
La instrucción @code{\time} establece las propiedades
@code{timeSignatureFraction}, @code{beatLength}, @code{beatGrouping} y
@code{measureLength} en el contexto @code{Timing}, que normalmente
tiene el alias @code{Score}.  La modificación del valor de
@code{timeSignatureFraction} hace que se imprima la nueva indicación
de compás sin que cambie ninguna de las demás propiedades:

"
  doctitlees = "Cambio de compás sin afectar al barrado"


%% Translation of GIT committish: d96023d8792c8af202c7cb8508010c0d3648899d
  texidocde = "
Der @code{\\time}-Befehl verändert die Eigenschaften
@code{timeSignatureFraction}, @code{beatLength}, @code{beatGrouping}
und @code{measureLength} im @code{Timing}-Kontext, welcher normalerweise
gleichbedeutend mit @code{Score} ist.  Wenn der Wert von
@code{timeSignatureFraction} verändert wird, wird die neue
Taktart ausgegeben, ohne die anderen Eigenschaften zu beeinflussen:

"
  doctitlede = "Die Taktart verändern ohne die Bebalkung zu beeinflussen"


%% Translation of GIT committish: e71f19ad847d3e94ac89750f34de8b6bb28611df
  texidocfr = "
La commande @code{\\time} gère les propriétés
@code{timeSignatureFraction}, @code{beatLength}, @code{beatGrouping}
et @code{measureLength} dans le contexte @code{Timing}, normallement
rattaché à @code{Score}.  Le fait de modifier la valeur de
@code{timeSignatureFraction} aura pour effet de changer l'apparence du
symbole affiché sans pour autant affecter les autres propriétés de la
métrique :

"
  doctitlefr = "Changement de métrique sans affecter les règles de ligature"

  texidoc = "
The @code{\\time} command sets the properties
@code{timeSignatureFraction}, @code{beatLength}, @code{beatGrouping}
and @code{measureLength} in the @code{Timing} context, which is
normally aliased to @code{Score}. Changing the value of
@code{timeSignatureFraction} causes the new time signature symbol to be
printed without changing any of the other properties:

"
  doctitle = "Changing the time signature without affecting the beaming"
} % begin verbatim

\markup {This snippet is deprecated as of 2.13.5 and will be removed in 2.14}
