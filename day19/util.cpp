// -*- mode: c++; -*-
// DESCRIPTION: module containing various utility functions
//
// Copyright(C) 2/12/2007 by Walt Mankowski
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
// $Id: util.cpp 308 2007-02-13 04:16:54Z walt $

#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <stdlib.h>
#include <errno.h>
#include "util.h"

/*******************************************************************************
** Function Name: dprintf
**
** Parameters: char *fmt, ...
**
** Description: If DEBUG is true, print a debugging message to stderr and
**              continue.  Format is the same as printf().
**
** Returns: void
**
*******************************************************************************/
void dprintf(char *fmt, ...) {
        if (!DEBUG)
                return;

        va_list ap;

        va_start(ap, fmt);
        vfprintf(stderr, fmt, ap);
        va_end(ap);
}

/*******************************************************************************
** Function Name: warn
**
** Parameters: char *fmt, ...
**
** Description: Print a warning to stderr and continue.  Format is the same as
**              printf().  It errno is set, it's converted to an error string
**              and printed.
**
** Returns: void
**
*******************************************************************************/
void warn(const char *fmt, ...) {
        int save_errno = errno;

        va_list ap;

        va_start(ap, fmt);
        vfprintf(stderr, fmt, ap);
        va_end(ap);

        if (save_errno)
                fprintf(stderr, ": %s", strerror(save_errno));

        fprintf(stderr, "\n");
}

/*******************************************************************************
** Function Name: die
**
** Parameters: char *fmt, ...
**
** Description: Print a warning to stderr and exit.  Format is the same as
**              printf().  It errno is set, it's converted to an error string
**              and printed.
**
** Returns: Sets exit status to errno upon exiting.
**
*******************************************************************************/
void die(const char *fmt, ...) {
        int save_errno = errno;

        va_list ap;

        va_start(ap, fmt);
        vfprintf(stderr, fmt, ap);
        va_end(ap);

        if (save_errno)
                fprintf(stderr, ": %s", strerror(save_errno));

        fprintf(stderr, "\n");

        exit(save_errno);
}

/*******************************************************************************                                  
** Function Name: vec_split
**
** Parameters: char *str, char delim
**
** Description: This works like the Perl split function.  str is expected to be
**              a list of strings, separated by delim.  It splits on the
**              delimiter and creates a vector of strings.
**
** Returns: a vector of strings
**
*******************************************************************************/
vector<string> vec_split(const char *str, const char delim) {
        std::vector<string> v;

        string s;
        for (size_t i = 0; i < strlen(str); i++) {
                if (str[i] == delim) {
                        if (s.size() > 0) {
                                v.push_back(s);
                                s.clear();
                        }
                } else {
                        s += str[i];;
                }
        }

        if (s.size() > 0)
                v.push_back(s);

        return v;
}

// Removes the final character from s, like perl's chop
void chop(char *s) {
        int n;

        if ((n = strlen(s)) > 0)
                s[n-1] = '\0';
}

// Removes the final character from s if it's a newline, like a
// simplified version of perl's chomp
void chomp(char *s) {
        int n;

        if ((n = strlen(s)) > 0 && s[n-1] == '\n')
                s[n-1] = '\0';
}
