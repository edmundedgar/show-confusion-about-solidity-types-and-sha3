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




mynum = 123

code3 = open('hash_checker_int256.sol').read()
c3 = tester.state().abi_contract(code3, language='solidity')

print "This would be more useful if I could pass in an int, but that gives me a different hash"

c3.check_hash(
    mynum,
    sha3_256(hex(mynum)).hexdigest().decode('hex')
)




code2 = open('hash_checker_bytes32.sol').read()
c2 = tester.state().abi_contract(code2, language='solidity')

print "Likewise with bytes"

c2.check_hash(
    mystring,
    sha3_256(mystring).hexdigest().decode('hex')
)



