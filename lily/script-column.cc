/*
  script-column.cc -- implement Script_column

  source file of the GNU LilyPond music typesetter

  (c) 1997 Han-Wen Nienhuys <hanwen@stack.nl>
*/

#include "script-column.hh"
#include "debug.hh"
#include "script.hh"
#include "note-head.hh"
#include "stem.hh"

IMPLEMENT_STATIC_NAME(Script_column);
IMPLEMENT_IS_TYPE_B1(Script_column,Horizontal_vertical_group_item);


void
Script_column::add(Script*s_l)
{
    script_l_arr_.push(s_l);
    add_element(s_l);
}


void
Script_column::do_print()const
{
#ifndef NPRINT
    mtor << "scripts: " << script_l_arr_.size() << '\n'; 
#endif
}

static int
idx(bool inside, int dir)
{
    int j = (dir+1);
    if ( !inside )
	j ++;
    return j;
}

void
Script_column::do_pre_processing()
{
    if (!script_l_arr_.size()) 
	return;
    
    /* up+inside, up+outside, down+inside, down+outside */
    Array<Script*> placed_l_arr_a[4];
    for (int i=0; i < script_l_arr_.size(); i++) {
	Script*s_l = script_l_arr_[i];
	placed_l_arr_a[idx( s_l->inside_staff_b_ , s_l->dir_i_) ].push(s_l);
    }
    
    for (int j =0; j <4; j++) {
	placed_l_arr_a[j].sort( Script::compare);
    }


    for (int j =0; j < 4; j++) {
	if (placed_l_arr_a[j].size())
	    for (int i=0; i  < support_l_arr_.size(); i++)
		placed_l_arr_a[j][0]->add_support( support_l_arr_[i]);
    }
    
    Item * support_l=0;
    int j = 0;
    for (; j < 2; j++ ) {
	for (int i=0; i < placed_l_arr_a[j].size(); i++) {
	    if (support_l)
		placed_l_arr_a[j][i]->add_support(support_l);
	    support_l = placed_l_arr_a[j][i];
	}
    }
    support_l = 0;
    for (; j < 4; j++ ) {
	for (int i=0; i < placed_l_arr_a[j].size(); i++) {
	    if (support_l)
		placed_l_arr_a[j][i]->add_support(support_l);
	    support_l = placed_l_arr_a[j][i];
	}
    }
}


void
Script_column::add_support(Item*i_l)
{
    support_l_arr_.push(i_l);
    add_element(i_l);
}

void
Script_column::do_substitute_dependency(Score_elem*o,Score_elem*n)
{
    Horizontal_vertical_group::do_substitute_dependency(o,n);
    if (o->item()) {
	script_l_arr_.substitute((Script*)o->item(),(Script*) (n?n->item():0));
	support_l_arr_.substitute(o->item(), (n?n->item():0));
    }
}
