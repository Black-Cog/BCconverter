
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
		button_write = Anvil.core.Button( name='GO !', cmd=write, w=120, h=25 )

		# defind dropmenu 
		presets = [
					{0:"Images sequence to video"},
					{1:"Video to images sequence"},
				  ]

		self.dropmenu_encode = Anvil.core.Dropmenu(items=presets, w=180, h=25, x=0, y=0 )
		
		# defind text
		text_menuEncode = Anvil.core.Text( text='Choose the operation you want to perform :', w=220 )
		
		# defind layouts content
		layout_main.add( [text_menuEncode, self.dropmenu_encode, button_write] )
