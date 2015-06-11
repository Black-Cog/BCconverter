
import Anvil.core
import BCconverter

class Console():
	def __init__( self, parent ):

		# defind layouts
		layout_main = Anvil.core.Layout( parent=parent )

		# defind buttons
		button_write = Anvil.core.Button( name='Write', cmd=BCconverter.core.Actions.Write, w=120, h=35 )

		# defind layouts content
		layout_main.add( button_write )
