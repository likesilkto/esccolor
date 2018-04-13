#!/usr/bin/env python
# -*- coding: utf-8 -*-

colorcode = {\
'black':   0, \
'red':     1, \
'green':   2, \
'yellow':  3, \
'blue':    4, \
'magenta': 5, \
'cyan':    6, \
'white':   7, \
}

attributecode = {\
'bold':      1, \
'low':       2, \
'underline': 4, \
'blink':     5, \
'reverse':   7, \
'invisible': 8,\
}

def esccolor( fg, bg=None, attr=None ):
	pre ='\033[3{}'.format( colorcode[ fg.lower() ] )
	
	if( bg is not None ):
		pre += ';4{}'.format( colorcode[ bg.lower() ] )
	
	if( attr is not None ):
		pre += ';{}'.format( attributecode[ attr.lower() ] )
	
	pre += 'm'
	end = '\033[0m'
	def text( str ):
		return pre + str + end

	return text
