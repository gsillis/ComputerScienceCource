from find_vowel import find_vowel

def test_find_vowel_when_called_passing_a_vowel_should_return_true ():
    sut = find_vowel("a")
    assert sut == True

def test_find_vowel_when_called_passing_a_consonant_should_return_false ():
    sut = find_vowel("b")
    assert sut == False

def test_find_vowel_when_called_passing_a_uppercased_letter_should_return_expect_result ():
    sut = find_vowel("B")
    assert sut == False