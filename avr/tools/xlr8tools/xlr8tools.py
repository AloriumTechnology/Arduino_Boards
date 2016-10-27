#!/usr/bin/env python
#
# Small script to copy stuff needed for running Modelsim
#   simulation on OpenXLR8 design
#
# Copyright (c) 2016 Matt Weber (matt@aloriumtech.com)
#

import ihex2mem
import os
import shutil
import argparse
import sys

def cmdline ():

    parser = argparse.ArgumentParser(description="Various helpful items for the OpenXLR8 tool flow")
    parser.add_argument("--simprep", help="Convert given program memory file from intel hex format " +\
                        "to verilog memory format. Copy that and some header files to required locations " +\
                        "for simulation. Also requires --sketchbook option.")
    parser.add_argument("--sketchbook", help="Path to Arduino sketchbook folder")
    args = parser.parse_args()

    if args.simprep:
        if (not args.sketchbook):
            print "ERROR: --simprep option also requires --sketchbook option"
            parser.print_usage()
        infile = args.simprep
        outdir = args.sketchbook
        outfile = os.path.join(outdir, 'libraries', 'XLR8Build', 'extras', 'quartus', 'simulation', 'modelsim', 'sketch.dat')

        conv = ihex2mem.mem_image()
        conv.load_ihex(infile)
        conv.save_vmem(outfile,width=4)
        print "Converted %d bytes from %s to %s" % (conv.bcount, infile, outfile)

        # TODO: Also generate and copy the assembly code listing

        # Modelsim likes to have the included header file in the same directory as the files that use it, so
        #  copy it there
        infile = os.path.join(outdir, 'libraries', 'XLR8Core', 'extras', 'rtl', 'avr_adr_pack.vh')
        outfile = os.path.join(outdir, 'libraries', 'XLR8Build', 'extras', 'rtl')
        shutil.copy2(infile,outfile)
        outfile = os.path.join(outdir, 'libraries', 'XLR8Build', 'extras', 'modelsim')
        shutil.copy2(infile,outfile)
    
if __name__ == '__main__':
    cmdline()
