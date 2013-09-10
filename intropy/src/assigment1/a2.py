import unittest

class TestA1(unittest.TestCase):
    def test_seconds_difference(self):
        self.assertEqual(get_length('ATCGAT'), 6)
        self.assertEqual(get_length('ATCG'), 4)
        self.assertEqual(get_length(''), 0)
        self.assertEqual(is_longer('ATCG', 'AT'),True)
        self.assertEqual(is_longer('ATCG', 'ATCGGA'),False)
        self.assertEqual(count_nucleotides('ATCGGC', 'G'),2)
        self.assertEqual(count_nucleotides('ATCTA', 'G'),0)
        self.assertEqual(count_nucleotides('ATCTA', ''),0)
        self.assertEqual(count_nucleotides('', 'G'),0)
        self.assertEqual(contains_sequence('ATCGGC', 'GG'),True)
        self.assertEqual(contains_sequence('ATCGGC', 'GT'),False)
        self.assertEqual(contains_sequence('', 'GT'),False)
        #self.assertEqual(contains_sequence('ATCGGC', ''),False)
        self.assertEqual(is_valid_nucleotid('A'),True)
        self.assertEqual(is_valid_nucleotid('C'),True)
        self.assertEqual(is_valid_nucleotid('T'),True)
        self.assertEqual(is_valid_nucleotid('G'),True)
        self.assertEqual(is_valid_nucleotid('a'),False)
        self.assertEqual(is_valid_nucleotid('c'),False)
        self.assertEqual(is_valid_nucleotid('t'),False)
        self.assertEqual(is_valid_nucleotid('g'),False)
        self.assertEqual(is_valid_nucleotid('k'),False)
        self.assertEqual(is_valid_nucleotid('AG'),False)
        
        self.assertEqual(is_valid_sequence('AGT'),True)
        self.assertEqual(is_valid_sequence('atcg'),False)
        self.assertEqual(is_valid_sequence('xyz'),False)
        self.assertEqual(is_valid_sequence('XYZ'),False)
        
        self.assertEqual(insert_sequence('ATCGGC','CGG',0),'CGGATCGGC')
        self.assertEqual(insert_sequence('ATCGGC','CGG',1),'ACGGTCGGC')
        self.assertEqual(insert_sequence('ATCGGC','CGG',5),'ATCGGCGGC')
        self.assertEqual(insert_sequence('ATCGGC','CGG',6),'ATCGGCCGG')
        self.assertEqual(insert_sequence('CCGG','AT',2),'CCATGG')
        
        self.assertEqual(get_complement('A'),'T')
        self.assertEqual(get_complement('T'),'A')
        self.assertEqual(get_complement('C'),'G')
        self.assertEqual(get_complement('G'),'C')
        
        self.assertEqual(get_complementary_sequence('GTCCCAATAA'),'CAGGGTTATT')
        self.assertEqual(get_complementary_sequence('GATACCA'),'CTATGGT')
        self.assertEqual(get_complementary_sequence('AT'),'TA')

      
if __name__ == '__main__':
    unittest.main()
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1)>get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    accumulator=0;
    for current in dna :
        if current==nucleotide:
            accumulator=accumulator+1
    return accumulator

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1
def is_valid_nucleotid(nucleotid):
    """(str) -> bool
    
    >>> is_valid_nucleotid('A')
    True
    >>> is_valid_nucleotid('C')
    True
    >>> is_valid_nucleotid('T')
    True
    >>> is_valid_nucleotid('G')
    True
    >>> is_valid_nucleotid('a')
    False
     >>> is_valid_nucleotid('c')
    False
     >>> is_valid_nucleotid('t')
    False
     >>> is_valid_nucleotid('g')
    False
     >>> is_valid_nucleotid('k')
    False
     >>> is_valid_nucleotid('AC')
    False
    
    The parameter is a potential nucleotid. 
    Return True if and only if the nucleotid is valid (that is, it is no other than 'A', 'T', 'C' and 'G').
    """
    return len(nucleotid)==1 and nucleotid in 'ACTG' 
def is_valid_sequence(dna):
    """(str) -> bool
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('atcg')
    False
     >>> is_valid_sequence('atcg')
    False
     >>> is_valid_sequence('xyz')
    False
     >>> is_valid_sequence('XYZ')
    False
    
    The parameter is a potential DNA sequence. 
    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G').
    """
    for nucleotid in dna:
        if not is_valid_nucleotid(nucleotid):
            return False
    return True;

def insert_sequence(dna1, dna2, index):
    """(str, str, int) -> str
     
     >>> insert_sequence('ATCGGC','CGG',0)
    'CGGATCGGC'   
    >>> insert_sequence('ATCGGC','CGG',1)
    'ACGGTCGGC'
    >>> insert_sequence('ATCGGC','CGG',5)
    'ATCGGCGGC'
    >>> insert_sequence('ATCGGC','CGG',5)
    'ATCGGCCGG'
    
    The first two parameters are DNA sequences and the third parameter is an index. 
    Return the DNA sequence obtained by inserting the second DNA sequence into 
    the first DNA sequence at the given index.
    Precondition: You can assume that the index is valid.
    """
    return dna1[:index]+dna2+dna1[index:]

def get_complement(nucleotid):
    """(str) -> str
    
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    
       The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the nucleotide's complement.
    """
    if nucleotid=='A' :
        return 'T'
    elif nucleotid=='T' :
        return 'A'
    elif nucleotid=='C' :
        return 'G'
    elif nucleotid=='G' :
        return 'C'
    
def get_complementary_sequence(dna):
    """(str) -> str
    
    >>>get_complementary_sequence('GTCCCAATAA')
    'CAGGGTTATT'
    >>>get_complementary_sequence('GATACCA')
    'CTATGGT'
    >>>get_complementary_sequence('AT')
    'TA'
    
    The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence.
    """
    complementary=''
    for nucleotid in dna:
        complementary=complementary+get_complement(nucleotid)
    return complementary
    