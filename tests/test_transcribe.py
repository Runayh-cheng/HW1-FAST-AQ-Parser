# write tests for transcribe functions
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    assert transcribe("ATCGT", False) == "AUCGU"
    assert transcribe("ATCGT", True) == "UGCUA"
   
    with pytest.raises(ValueError) as info:
        transcribe("ABCDE")
    assert info.type is ValueError
    



def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert transcribe("ATCGT") == "ACGAU"

    with pytest.raises(ValueError) as info:
        transcribe("ABCDE")
    assert info.type is ValueError

    