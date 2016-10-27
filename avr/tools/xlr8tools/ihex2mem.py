#!/usr/bin/env python
#
# Intel Hex to Verilog Memory format converter
#
# Copyright (c) 2004 Guy Hutchison (ghutchis@opencores.org)
#  Modified (c) 2016 Matt Weber (matt@aloriumtech.com) to write out to
#                        wider memories
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

class mem_image:
    def __init__ (self):
        self.min = 100000
        self.max = -1
        self.map = {}
        self.bcount = 0

    def load_ihex (self, infile):
        ifh = open (infile, 'r')
    
        line = ifh.readline()
        while (line != ''):
            if (line[0] == ':'):
                rlen = int(line[1:3], 16)
                addr = int(line[3:7], 16)
                rtyp = int(line[7:9], 16)
                ptr = 9
                for i in range (0, rlen):
                    laddr = addr + i
                    val = int(line[9+i*2:9+i*2+2], 16)
                    self.map[laddr] = val
                    self.bcount += 1
                    if (laddr > self.max): self.max = laddr
                    if (laddr < self.min): self.min = laddr
    
            line = ifh.readline()
            
        ifh.close()

    def save_vmem (self, outfile, start=-1, stop=-1, width=1):
        if (start == -1): start = self.min
        if (stop == -1): stop = self.max

        ofh = open (outfile, 'w')
        for addr in range(start, stop+1, width):
            if self.map.has_key (addr):
                wordaddr = addr/width
                ofh.write ("@%04x " % wordaddr)
                for byte in range(width):
                    # output bytes in reverse order
                    addro = addr + (width-byte-1)
                    # or in normal order
                    #addro = addr + byte
                    if self.map.has_key (addro):
                        ofh.write ("%02x" % self.map[addro])
                    else:
                        ofh.write ("00")
                ofh.write ("\n")
        ofh.close()

def ihex2mem (infile, outfile, width=1):
    ifh = open (infile, 'r')
    ofh = open (outfile, 'w')

    bcount = 0
    line = ifh.readline()
    while (line != ''):
        if (line[0] == ':'):
            rlen = int(line[1:3], 16)
            addr = int(line[3:7], 16)
            rtyp = int(line[7:9], 16)
            ptr = 9
            assert rlen%width == 0, "hex line not a multiple of desired output width"
            cwidth = 2*width #characters to create the output width, 2 chars per byte
            for i in range (0, rlen/width):
                val = int(line[9+i*cwidth:9+(i+1)*cwidth], 16)
                ofh.write ('@{addr:0{cwidth}X} {val:0{cwidth}X}\n'.format(addr=addr,val=val,cwidth=cwidth))
                #ofh.write ("@%02x %02x\n" % (addr+i, val))
                bcount += width

        line = ifh.readline()
        
    ifh.close()
    ofh.close()

    return bcount

def cmdline ():
    import sys
    
    infile = sys.argv[1]
    outfile = sys.argv[2]
    if (len(sys.argv) == 4):
        width = int(sys.argv[3])
    else:
        width = 1

    #bc = ihex2mem (infile, outfile)
    conv = mem_image()
    conv.load_ihex(infile)
    conv.save_vmem(outfile,width=width)
    print "Converted %d bytes from %s to %s" % (conv.bcount, infile, outfile)
    
if __name__ == '__main__':
    cmdline()
