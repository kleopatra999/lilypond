/*
  staff-gravs.cc -- implement Line_group_engraver

  source file of the GNU LilyPond music typesetter

  (c) 1997 Han-Wen Nienhuys <hanwen@stack.nl>
*/

#include "staff-sym.hh"
#include "staff-gravs.hh"
#include "command-request.hh"
#include "bar.hh"
#include "debug.hh"
#include "staffline.hh"


Line_group_engraver::Line_group_engraver()
{
    staffline_p_ =0;
}

void
Line_group_engraver::acknowledge_element(Score_elem_info  elem)
{
    staffline_p_->add_element(elem.elem_l_);
}


void
Line_group_engraver::do_removal_processing()
{
    staffline_p_->right_col_l_ = get_staff_info().command_pcol_l();
    typeset_element(staffline_p_);
    staffline_p_ = 0;
}

void
Line_group_engraver::do_creation_processing()
{
    staffline_p_ = new Line_of_staff;
    staffline_p_->left_col_l_ = get_staff_info().command_pcol_l();

    // don't broadcast to self.
    announce_element(Score_elem_info(staffline_p_,0));
}


IMPLEMENT_STATIC_NAME(Line_group_engraver);
IMPLEMENT_IS_TYPE_B1(Line_group_engraver,Engraver);
ADD_THIS_ENGRAVER(Line_group_engraver);

