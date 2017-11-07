from ethereum.tools import tester as t
c = t.Chain()
filename = 'checksender.se'
check = c.contract(filename,language='serpent')

print check.tx_origin()
print check.tx_gasprice()
print check.msg_gas()
print check.msg_sender()
print check.msg_value()
print check.self()
print check.self_balance()
print check.block_coinbase()
print check.block_timestamp()
print check.block_prevhash()
print check.block_difficulty()
print check.block_number()
print check.block_gaslimit()
