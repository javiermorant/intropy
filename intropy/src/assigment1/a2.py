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