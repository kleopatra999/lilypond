/*   
  property-engraver.cc --  implement Property engraver
  
  source file of the GNU LilyPond music typesetter
  
  (c) 1999--2000 Han-Wen Nienhuys <hanwen@cs.uu.nl>
  
 */

#include "lily-guile.hh"
#include "engraver.hh"
#include "protected-scm.hh"
#include "dictionary.hh"
#include "score-element.hh"

class Property_engraver : public Engraver
{
  /*
    UGH. Junk Dictionary
  */
  Dictionary<Protected_scm> prop_dict_;	// junkme
  void apply_properties (SCM, Score_element*);

protected:
  virtual void acknowledge_element (Score_element_info ei);
  virtual void do_creation_processing ();

  VIRTUAL_COPY_CONS(Translator);
};

void
Property_engraver::do_creation_processing ()
{
  SCM plist = get_property ("Generic_property_list");
  for (; SCM_NIMP (plist); plist = gh_cdr (plist))
    {
      SCM elt_props = gh_car (plist);
      prop_dict_[ly_scm2string (gh_car (elt_props))] = gh_cdr (elt_props);
    }
}

void
Property_engraver::acknowledge_element (Score_element_info i)
{
  if (prop_dict_.elem_b (i.elem_l_->name()))
    {
      SCM p = prop_dict_[i.elem_l_->name()];
      apply_properties (p,i.elem_l_);
    }
  if (prop_dict_.elem_b ("all"))
    {
      apply_properties (prop_dict_["all"], i.elem_l_);
    }
}


void
Property_engraver::apply_properties (SCM p, Score_element *e)
{  
  for (; gh_pair_p (p); p = gh_cdr (p))
    {
      /*
	Try each property in order; earlier descriptions take
	precedence over later ones, and we don't touch elt-properties if
	they're already set.
      */
      
      SCM entry = gh_car (p);
      SCM prop_sym = gh_car (entry);
      SCM type_p   = gh_cadr (entry);
      SCM elt_prop_sym = gh_caddr (entry);

      SCM preset = scm_assq(elt_prop_sym, e->element_property_alist_);
      if (preset != SCM_BOOL_F)
	continue;
  
      SCM val = get_property (prop_sym);

     
      if (val == SCM_UNDEFINED)
	;			// Not defined in context.
      else if (gh_apply (type_p, scm_listify (val, SCM_UNDEFINED))
	       == SCM_BOOL_T)	// defined and  right type: do it
	e->set_elt_property (ly_symbol2string (elt_prop_sym), val);
      else
 /*
	    we don't print a warning if VAL == #f, because we would
	    get lots of warnings when we restore stuff to default, eg.

	    slurDash = #1 [...] slurDash = ##f

	    should not cause "type error: slurDash expects number not
	    boolean"

	  */
	if (val != SCM_BOOL_F)
	{			// not the right type: error message.
	  SCM errport = scm_current_error_port ();
	  warning (_("Wrong type for property"));
	  scm_display (prop_sym, errport);
	  scm_puts (", type predicate: ", errport);
	  scm_display (type_p, errport);
	  scm_puts (", value found: ", errport);
	  scm_display (val, errport);
	  scm_puts (" type: ", errport);
	  scm_display (ly_type (val), errport);
	  scm_puts ("\n", errport);
	}
    }
}

ADD_THIS_TRANSLATOR(Property_engraver);
