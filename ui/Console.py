
import Anvil.core
import BCconverter
import Forge

class Console():
	def __init__( self, parent, ui ):

		# defind layouts
		layout_main = Anvil.core.Layout( parent=parent )

		#define actions
		write = Forge.core.Process.partial( BCconverter.core.Actions.Write, ui )

		# defind buttons
		button_write = Anvil.core.Button( name='Write', cmd=write, w=120, h=35 )

		# defind layouts content
		layout_main.add( button_write )
