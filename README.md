esccolor
====

It is a python package to colorize text for print.

## Usage

### black( **str** )
- **str** (str): string to be colored
- **output** : colored string

### red( **str** )
- **str** (str): string to be colored
- **output** : colored string

### green( **str** )
- **str** (str): string to be colored
- **output** : colored string

### yellow( **str** )
- **str** (str): string to be colored
- **output** : colored string

### blue( **str** )
- **str** (str): string to be colored
- **output** : colored string

### magenta( **str** )
- **str** (str): string to be colored
- **output** : colored string

### cyan( **str** )
- **str** (str): string to be colored
- **output** : colored string

### white( **str** )
- **str** (str): string to be colored
- **output** : colored string

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
	from esccolor.esccolor import green

	print( esccolor('red')('aka') )
	print( esccolor('red', 'cyan')('mizu') )
	blink = escolor('white', attr='blink')
	print( blink('ten') )
	print( green('midori') )

## Install

`% pip install git+https://github.com/likesilkto/esccolor`

## Links

[likesilkto](https://github.com/likesilkto)

[ASCII Table - ANSI Escape sequences](http://ascii-table.com/ansi-escape-sequences.php)
