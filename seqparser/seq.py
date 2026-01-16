# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """

    ### Although the function is called transcribe, this is not biology right?
    ### So I am literally just replacing T to U?

    for bp in seq:
        if bp not in TRANSCRIPTION_MAPPING:
            raise ValueError("Invalid base pair in input.")

    SeqMod = seq.replace("T", "U")
    
    if reverse == False:
        return SeqMod
    elif reverse == True: 
        return SeqMod[::-1]

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    reverseTranscript = ""

    for bp in seq:
        if bp not in TRANSCRIPTION_MAPPING:
            raise ValueError("Invalid base pair in input.")
        else: 
            reverseTranscript += TRANSCRIPTION_MAPPING.get(bp, bp)
            return reverseTranscript[::-1]
        
    # Hey this is my comment
    # Again!
