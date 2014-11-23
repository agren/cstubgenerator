#!/usr/bin/env python

"""
	Copyright 2014 Mikael Agren

    This file is part of cstubgenerator.

    cstubgenerator is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    cstubgenerator is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with cstubgenerator. If not, see <http://www.gnu.org/licenses/>.
"""

from pycparser import c_parser, c_ast, parse_file
import argparse
import os

def format_identifiertype(identifiertype):
    if identifiertype == None:
        return ""
    s = " ".join(identifiertype.names).lstrip().rstrip()
    
    return s

def format_quals(quals):
    if quals == None:
        return ""
    s = " ".join(quals).lstrip().rstrip()

    return s

def format_typedecl(typedecl):
    if typedecl == None:
        return ""
    s = format_identifiertype(typedecl.type) + " "
    quals = format_quals(typedecl.quals)
    if quals:
        s = s + quals + " "
    s = s + typedecl.declname

    return s

def format_decl(decl):
    if decl == None:
        return ""
    s = format_typedecl(decl.type)

    return s

def format_funcdecl(funcdecl):
    if funcdecl == None:
        return ""
    s = format_typedecl(funcdecl.type).lstrip().rstrip()
    s = s + "("
    decls = []
    for arg in funcdecl.args.params:
        decls.append(format_decl(arg))
    s = s + ", ".join(decls)
    s = s + ")"

    return s

def create_function_definition(funcdecl, faulty=False):
    if funcdecl == None:
        return ""
    s = format_funcdecl(funcdecl) + " { // "
    s = s + str(funcdecl.coord) + "\n"
    if faulty:
        s = s + "    (Function not defined)\n"
    else:
        s = s + "\n"
    s = s + "}"

    return s

class FuncDeclVisitor(c_ast.NodeVisitor):
    buffer = ""

    def visit_FuncDecl(self, node):
        self.buffer = self.buffer + create_function_definition(node)
        self.buffer = self.buffer + "\n\n"
        #print(create_function_definition(node))

def create_func_defs(filename):
    ast = parse_file(filename, use_cpp=True)

    v = FuncDeclVisitor()
    v.visit(ast)

    return v.buffer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a .c stub file from a header file.")
    parser.add_argument("infiles", metavar="file.h", nargs="+", help="Input header file")
    args = parser.parse_args()

    for infile in args.infiles:
    	output_buffer = ""
    	outfilename = os.path.basename(infile).split(".")[0] + ".c"
    	with open(outfilename, 'w') as outfile:
            outfile.write("// Automatically generated from: " + infile + "\n\n")
            outfile.write('#include "' + infile + '"\n\n')
            outfile.write(create_func_defs(infile))
