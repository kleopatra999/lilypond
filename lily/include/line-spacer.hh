/*
  line-spacer.hh -- declare Line_spacer

  source file of the GNU LilyPond music typesetter

  (c) 1997 Han-Wen Nienhuys <hanwen@stack.nl>
*/


#ifndef LINE_SPACER_HH
#define LINE_SPACER_HH
#include "lily-proto.hh"
#include "varray.hh"
#include "vector.hh"
#include "interval.hh"

/**
  abstract interface to Line spacing.

  TODO
  add estimate of "force" or energy.
 */

class Line_spacer 
{
    
public:
    Paper_def * paper_l_;
    Paper_def *paper_l()const;
    Line_spacer();
    
    virtual Array<PCol*> error_pcol_l_arr() const=0;

    /** solve the spacing problem
      
      @return the column positions, and the energy (last element)

      */
    virtual Array<Real> solve() const=0;

    /** add a col to the problem. columns have to be added left to
      right. The column contains info on it's minimum width.  */
    virtual void add_column(PCol  *, bool fixed=false, Real fixpos=0.0)=0;

    /**
      can the posed problem be solved?
      
      @pre

      prepare() was called
      
     */
    virtual bool check_constraints(Vector v) const=0;

    /**
      generate a solution which can't fail
     */
    virtual Vector default_solution() const=0;
    
    virtual void OK() const{}
    virtual void print() const{}
    
    /**
      Call after construction before solving
     */
    virtual void prepare(){}
};

#endif
