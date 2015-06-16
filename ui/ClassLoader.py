
import Anvil.core
import BCconverter.core
import BCconverter.ui
import Forge.core.System

class ClassLoader():

	def __init__(self):

		# set env
		currentPath = Forge.core.System.getPath( __file__ )
		Forge.core.System.setEnv( currentPath )

		self.ui()

	def app( self ):
		return self.window

	def ui( self ):

		__size = [ 800, 500 ]

		# defind class
		Abox = Anvil.core.Box

		# window init
		self.window = Anvil.core.Window( title='BCconverter', iconPath='../core/icon/BCconverter.png', size=__size, menuBar=False )
		layout_main = Anvil.core.Layout( parent=self.window )

		# boxs init
		box_input  = Abox( name='Input', w=__size[0]/2-20, h=__size[1]/3-10 )
		box_output = Abox( name='Output',  w=__size[0]/2-20, h=__size[1]/3-10 )
		box_console = Abox( name='Console',  w=__size[0]-20, h=__size[1]/3-10 )

		# setup content
		self.input  = BCconverter.ui.Input( parent=box_input )
		self.output = BCconverter.ui.Output( parent=box_output )
		self.console = BCconverter.ui.Console( parent=box_console, ui=self )

		# define layouts content
		layout_main.add( [box_input, box_output] )
		layout_main.add( box_console )

		self.window.show()
