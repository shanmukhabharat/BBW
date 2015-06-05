#!/usr/bin/env python

def print_uvs( xys ):
    xys = [ map( float, xy ) for xy in xys ]
    from numpy import array
    xys = array( xys )
    xys0 = xys - xys.min(axis=0)
    xys0.min(0)
    xys0/=xys0.max(0)
    xys0.max(0)
    
    for x, y in xys0:
        print 'vt', x, y
    print

def main():
    import sys
    
    first_face = True
    
    vlines = []
    for line in open( sys.argv[1] ):
        sline = line.strip().split()
        will_print = True
        
        if len( sline ) == 0:
            pass
        elif sline[0] == 'v':
            vlines.append( sline[1:3] )
        
        elif sline[0] == 'f':
            if first_face:
                print_uvs( vlines )
                first_face = False
            
            print 'f %s/%s %s/%s %s/%s' % ( sline[1], sline[1], sline[2], sline[2], sline[3], sline[3] )
            will_print = False
        
        if will_print:
            print line.strip()

if __name__ == '__main__': main()
