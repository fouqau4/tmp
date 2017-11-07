from ethereum.tools import tester as t
from ethereum.utils import privtoaddr, big_endian_to_int

c = t.Chain()
bank = c.contract( 'bank.se', language = 'serpent' )

def show_eoas_balance( key_list ) :
	print ''
	print '* show EOA\'s balance :'
	for k in key_list :
		show_balance( k )

def show_balance( key ) :
	print '\t[address] : %d' % big_endian_to_int( privtoaddr( key ) )
	print '\t[balance] : %d' % bank.balance( sender = key )


def transfer( sender, receiver, amount ) :
	print ''
	print '* transfer balance :'
	print '\t[sender] : %d' % big_endian_to_int( privtoaddr( sender ) )
	print '\t[receiver] : %d' % big_endian_to_int( privtoaddr( receiver ) )
	print '\t[amount] : %d' % amount	
	bank.transfer( amount, privtoaddr( receiver ), sender = sender )

def deposit( key, amount ) :
	print ''
	print '* deposits balance :'
	print '\t[address] : %d' % big_endian_to_int( privtoaddr( key ) )
	print '\t[amount] : %d' % amount
	bank.deposit( sender = key, value = amount )

def withdraw( key, amount ) :
	print ''
	print '* withdraw balance :'
	print '\t[address] : %d' % big_endian_to_int( privtoaddr( key ) )
	print '\t[amount] : %d' % amount
	bank.withdraw( amount, sender = key )



show_eoas_balance( [ t.k0, t.k1 ] )

deposit( t.k1, 10000 )
transfer( t.k1, t.k0, 500 )
withdraw( t.k1, 600 )

show_eoas_balance( [ t.k0, t.k1 ] )
