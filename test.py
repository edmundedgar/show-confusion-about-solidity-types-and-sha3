from ethereum import tester
from sha3 import sha3_256

code1 = open('hash_checker_string.sol').read()
c1 = tester.state().abi_contract(code1, language='solidity')

print "Passing a string produces the sha3 I expect but I'm left with a string"

mystring = "foo"

c1.check_hash(
    "foo",
    sha3_256(mystring).hexdigest().decode('hex')
)

# Produces:
# {'': 'A\xb1\xa0d\x97R\xaf\x1b(\xb3\xdc)\xa1Un\xeex\x1eJL:\x1f\x7fS\xf9\x0f\xa84\xde\t\x8cM', '_event_type': 'LogB'}
# {'': 'A\xb1\xa0d\x97R\xaf\x1b(\xb3\xdc)\xa1Un\xeex\x1eJL:\x1f\x7fS\xf9\x0f\xa84\xde\t\x8cM', '_event_type': 'LogB'}



mynum = 123

code3 = open('hash_checker_int256.sol').read()
c3 = tester.state().abi_contract(code3, language='solidity')

print "This would be more useful if I could pass in an int, but that gives me a different hash"

c3.check_hash(
    mynum,
    sha3_256(hex(mynum)).hexdigest().decode('hex')
)

# Produces:
# {'': 'Ui\x04G\x19\xa1\xec;\x04\xd0\xaf\xa9\xe7\xa51\x0c|\x04s3\x1d\x13\xdc\x9f\xaf\xe1C\xb2\xc4\xe8\x14\x8a', '_event_type': 'LogB'}
# {'': '8\x84\x8a\xa0\xa2\xda\xd9\x8b|\x8c\xe9FE\x9e4&\x19>q\xeeC\x9c{\x0c\xeb-\xfba\\\xf4\x1d\xf9', '_event_type': 'LogB'}



code2 = open('hash_checker_bytes32.sol').read()
c2 = tester.state().abi_contract(code2, language='solidity')

print "Likewise with bytes"

c2.check_hash(
    mystring,
    sha3_256(mystring).hexdigest().decode('hex')
)

# Produces:
# {'': '\xca\x91\xe6I\x7f\xf2\xef\xafO\xfe\x80\xfa\xb4v\xcb|S\x99Y\xee5y\xed\x98~t\x85Xe\x9b\x97T', '_event_type': 'LogB'}
# {'': 'A\xb1\xa0d\x97R\xaf\x1b(\xb3\xdc)\xa1Un\xeex\x1eJL:\x1f\x7fS\xf9\x0f\xa84\xde\t\x8cM', '_event_type': 'LogB'}




