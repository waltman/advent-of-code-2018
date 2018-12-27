// -*- mode: c++; -*-
// DESCRIPTION: Header file for utility functions
//
// Copyright(C) 3/13/2007 by Walt Mankowski
// walt@cs.drexel.edu
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//
// $Id: util.h 612 2007-03-13 19:18:40Z walt $

#ifndef _UTIL_H_
#define _UTIL_H_

#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <iostream>

using std::vector;
using std::map;
using std::set;
using std::string;
using std::cout;
using std::endl;

extern bool DEBUG;

/*******************************************************************************
** Function Name: in_map
**
** Parameters: map<T, U>& m, T element
**
** Description: Checks whether element is a key in the map m.  This is like the
**              exists function in Perl.
**
** Returns: true if element is in m, false if not.
**
*******************************************************************************/
template <typename T, typename U>
bool in_map(const map<T, U>& m, const T element) {
        return m.find(element) != m.end();
}

/*******************************************************************************
** Function Name: in_set
**
** Parameters: set<T, U>& m, T element
**
** Description: Checks whether element is a key in the set m.  This is like the
**              exists function in Perl.
**
** Returns: true if element is in m, false if not.
**
*******************************************************************************/
template <typename T, typename U>
bool in_set(const set<T, U>& s, const T element) {
        return s.find(element) != s.end();
}


/*******************************************************************************
** Function Name: squ
**
** Parameters: T n
**
** Description: squares n
**
** Returns: n * n
**
*******************************************************************************/
template <typename T>
T sqr(const T n) {
        return n * n;
}

template <typename T>
void dump_opengl_matrix(const T *m) {
        for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                        cout.width(8);
                        cout << m[j*4 + i] << "\t";
                }
                cout << endl;
        }
        cout << endl;
}

/*******************************************************************************
** DeleteObject: function object which deletes a generic pointer.
**   From Scott Meyers' "Effective STL", p. 38
**
*******************************************************************************/
struct DeleteObject {
        template<typename T>
        void operator()(const T *ptr) const {
                delete ptr;
        }
};

void dprintf(char *fmt, ...);
void warn(const char *fmt, ...);
void die(const char *fmt, ...);
vector<string> vec_split(const char *str, const char delim);
void chop(char *s);
void chomp(char *s);

inline double deg2rad(double d) { return d * M_PI / 180.0; }
inline double rad2deg(double r) { return r * 180.0 / M_PI; }

#endif
