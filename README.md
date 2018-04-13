esccolor
====

It is a python package to colorize text for print.

## Usage

### esccolor( **fg**, **bg**=None, **attr**=None)
- **fg** (str): text color
- **bg** (str): background color
- **attr** (str): text attribution
- **output** : function to decorate string

#### valid text for color
- Black
- Red
- Green
- Yellow
- Blue
- Magenta
- Cyan
- White

#### valid text for text attribution
- bold
- low
- underline
- blink
- reverse
- invisible

## Sample
    from esccolor.esccolor import esccolor
	print( esccolor('red')('aka') )
	print( esccolor('red', 'cyan')('mizu') )
	blink = escolor('white', attr='blink')
	print( blink('ten') )

## Install

`% pip install git+https://github.com/likesilkto`

## Links

[likesilkto](https://github.com/likesilkto)

[ASCII Table - ANSI Escape sequences](http://ascii-table.com/ansi-escape-sequences.php)
