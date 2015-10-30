contract HashChecker {

    event LogI(int256);
    event LogA(address);
    event LogB(bytes32);
    event LogS(string);

    function HashChecker() {
    }

    function check_hash(string mystring, bytes32 expected_result_hash) {

        bytes32 result_hash = sha3(mystring);
        LogB(result_hash);
        LogB(expected_result_hash);

    }

}
