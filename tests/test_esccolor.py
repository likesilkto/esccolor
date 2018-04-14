#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from esccolor.esccolor import esccolor
from esccolor.esccolor import black, red, green, yellow, blue, magenta, cyan, white

from esccolor.esccolor import colorcode, attributecode


class test_esccolor( unittest.TestCase ):
###################################################################
	@classmethod
	def setUpClass(cls): # it is called before test starting
		pass

	@classmethod
	def tearDownClass(cls): # it is called before test ending
		pass

	@classmethod
	def setUp(self): # it is called before each test
		pass

	@classmethod
	def tearDown(self): # it is called after each test
		pass
                
###################################################################
	def test_id(self):
		
		self.assertEqual(colorcode['red'], 1)
		self.assertEqual(colorcode['cyan'], 6)
		
		self.assertEqual(attributecode['low'], 2)
		self.assertEqual(attributecode['reverse'], 7)

	def test_esccolor(self):
		text = esccolor( 'Red' ) ('__test__')
		print( text )
		self.assertEqual( text, '\033[31m__test__\033[0m' )


		text = esccolor( 'Magenta', 'CYAN' ) ('__test__')
		print( text )
		self.assertEqual( text, '\033[35;46m__test__\033[0m' )


		text = esccolor( 'Yellow', 'Blue','blink' ) ('__test__')
		print( text )
		self.assertEqual( text, '\033[33;44;5m__test__\033[0m' )

	def test_color(self):
		text = black('str')
		self.assertEqual( text, '\033[30mstr\033[0m' )

		text = red('str')
		self.assertEqual( text, '\033[31mstr\033[0m' )

		text = green('str')
		self.assertEqual( text, '\033[32mstr\033[0m' )

		text = yellow('str')
		self.assertEqual( text, '\033[33mstr\033[0m' )

		text = blue('str')
		self.assertEqual( text, '\033[34mstr\033[0m' )

		text = magenta('str')
		self.assertEqual( text, '\033[35mstr\033[0m' )

		text = cyan('str')
		self.assertEqual( text, '\033[36mstr\033[0m' )

		text = white('str')
		self.assertEqual( text, '\033[37mstr\033[0m' )

###################################################################
	def suite():
		suite = unittest.TestSuite()
		suite.addTests(unittest.makeSuite(test_esccolor))
		return suite
  
if( __name__ == '__main__' ):
	unittest.main()
