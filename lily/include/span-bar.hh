/*
  span-bar.hh -- declare Span_bar

  source file of the GNU LilyPond music typesetter

  (c) 1997 Han-Wen Nienhuys <hanwen@stack.nl>
*/


#ifndef SPAN_BAR_HH
#define SPAN_BAR_HH

#include "bar.hh"

class Span_bar : public Bar
{
    Link_array<Bar> spanning_l_arr_;

public:
    NAME_MEMBERS();
    SCORE_ELEM_CLONE(Span_bar);
    void add(Bar* );
    void set( Vertical_align_element *);

protected:
    virtual Interval do_width()const;
    virtual void do_pre_processing();
    virtual void translate_y(Real y);
    
    virtual void do_substitute_dependency(Score_elem*,Score_elem*);
    virtual Molecule * brew_molecule_p()const;
    virtual Symbol get_bar_sym(Real dy) const;
};

#endif // SPAN_BAR_HH
