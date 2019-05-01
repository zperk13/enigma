import random
from string import ascii_letters, ascii_lowercase

rotors = ['dmtwsilruyqnkfejcazbpgxohv', 'hqzgpjtmoblncifdyawveusrkx', 'uqntlszfmrehdpxkibvygjcwoa',
          'jgdqoxuscamifrvtpnewkblzyh', 'ntzpsfbokmwrcjdivlaeyuxhgq', 'jviubhtcdyakeqzposgxnrmwfl',
          'qyhognecvpuztfdjaxwmkisrbl', 'qwertzuioasdfghjkpyxcvbnml', 'pezuohxscvfmtbglrinqjwaydk',
          'zouesydkfwpciqxhmvblgnjrat', 'ehrvxgaobqusimzflynwktpdjc', 'imetcgfraysqbzxwlhkdvupojn',
          'ekmflgdqvzntowyhxuspaibrcj', 'ajdksiruxblhwtmcqgznpyfvoe', 'bdfhjlcprtxvznyeiwgakmusqo',
          'esovpzjayquirhxlnftgkdcmwb', 'vzbrgityupsdnhlxawmjqofeck', 'jpgvoumfyqbenhzrdkasxlictw',
          'nzjhgrcxmyswboufaivlpekqdt', 'fkqhtlxocbjspdzramewniuygv', 'leyjvcnixwpbqmdrtakzgfuhos',
          'fsokanuerhmbtiycwlqpzxvgjd', 'ejmzalyxvbwfcrquontspikhgd', 'yruhqsldpxngokmiebfzcwvjat',
          'fvpjiaoyedrzxwgctkuqsbnmhl', 'enkqauywjicopblmdxzvfthrgs', 'rdobjntkvehmlfcwzaxgyipsuq']


def format_string(string):
    string = string.lower()
    result = ''
    for character in string:
        if character in ascii_letters:
            result += character
    return result


def swap_letters(string, swap_code):
    def error_checking():
        if not isinstance(swap_code, str):
            raise TypeError('swap_code must be a string')
        if not isinstance(string, str):
            raise TypeError('string must be a string')
        if len(swap_code) != 20:
            raise ValueError('swap_code must have 20 letters')
        for character in swap_code:
            if character not in ascii_lowercase:
                raise ValueError('swap_code must be comprised of only lowercase letters')
        check_for_duplicates = []
        for letter in swap_code:
            if letter in check_for_duplicates:
                raise ValueError('swap code cannot have duplicates')
            check_for_duplicates.append(letter)

    error_checking()
    string = format_string(string)

    # swap code is a string with an 20 letters. letter 0 and 1 are swapped, 2 and 3 are swapped and so on
    def is_even(integer):
        if integer % 2 == 0:
            return True
        else:
            return False

    result = ''
    for letter in string:
        if letter in swap_code:
            index = swap_code.index(letter)
            if is_even(index):
                result += swap_code[index + 1]
            else:
                result += swap_code[index - 1]
        else:
            result += letter
    return result


def rotate_rotor(rotor_string, amount):
    return rotor_string[amount:] + rotor_string[:amount]


def rotor_swap(string, rotor_string, rotor_pos):
    def check_for_errors(rotor_string):
        if not isinstance(rotor_string, str):
            raise TypeError('rotor_string must be a string')
        rotor_string = rotor_string.lower()
        if len(rotor_string) != 26:
            raise ValueError('rotor_string must be 26 letters long')
        check_for_duplicates = []
        for letter in rotor_string:
            if letter not in ascii_lowercase:
                raise ValueError('All characters in the strings in rotor_list must be lowercase letters')
            if letter in check_for_duplicates:
                raise ValueError('Letters can not appear multiple times in each of the strings in rotor_list')
            check_for_duplicates.append(letter)

    check_for_errors(rotor_string)
    string = format_string(string)
    result = ''
    for letter in string:
        result += rotor_string[ascii_lowercase.index(letter)]
    return result


def decode_rotor_swap(string, rotor_string):
    def check_for_errors(rotor_string):
        if not isinstance(rotor_string, str):
            raise TypeError('rotor_string must be a string')
        rotor_string = rotor_string.lower()
        if len(rotor_string) != 26:
            raise ValueError('rotor_string must be 26 letters long')
        check_for_duplicates = []
        for letter in rotor_string:
            if letter not in ascii_lowercase:
                raise ValueError('All characters in the strings in rotor_list must be lowercase letters')
            if letter in check_for_duplicates:
                raise ValueError('Letters can not appear multiple times in each of the strings in rotor_list')
            check_for_duplicates.append(letter)

    check_for_errors(rotor_string)
    string = format_string(string)
    result = ''
    for letter in string:
        result += ascii_lowercase[rotor_string.index(letter)]
    return result


def tri_rotor(string, rotor1, rotor2, rotor3, rotor1pos, rotor2pos, rotor3pos):
    rotor1 = rotate_rotor(rotor1, rotor1pos)
    rotor2 = rotate_rotor(rotor2, rotor2pos)
    rotor3 = rotate_rotor(rotor3, rotor3pos)
    string = format_string(string)
    count = 0
    result = ''
    for letter in string:
        result += decode_rotor_swap(decode_rotor_swap(
            decode_rotor_swap(decode_rotor_swap(decode_rotor_swap(decode_rotor_swap(letter, rotor1), rotor2), rotor3),
                              rotor3), rotor2), rotor1)
        rotor1 = rotate_rotor(rotor1, 1)
        if count % 26 == 0:
            rotor2 = rotate_rotor(rotor2, 1)
        if count % (26 * 26) == 0:
            rotor3 = rotate_rotor(rotor3, 1)
    return result


def decode_tri_rotor(string, rotor1, rotor2, rotor3, rotor1pos, rotor2pos, rotor3pos):
    rotor1 = rotate_rotor(rotor1, rotor1pos)
    rotor2 = rotate_rotor(rotor2, rotor2pos)
    rotor3 = rotate_rotor(rotor3, rotor3pos)
    string = format_string(string)
    count = 0
    result = ''
    for letter in string:
        result += rotor_swap(rotor_swap(
            rotor_swap(rotor_swap(rotor_swap(rotor_swap(letter, rotor1, 1), rotor2, 1), rotor3, 1), rotor3, 1), rotor2,
            1), rotor1, 1)
        rotor1 = rotate_rotor(rotor1, 1)
        if count % 26 == 0:
            rotor2 = rotate_rotor(rotor2, 1)
        if count % (26 * 26) == 0:
            rotor3 = rotate_rotor(rotor3, 1)
    return result


# Code is the 20 letters for plug board (swap_letters) then the 2 digit representation of the index of the each of the 3 rotor codes
def encode_enigma(string, code):
    string = swap_letters(string, code[:20])
    rotor1 = int(code[20:22])
    rotor2 = int(code[22:24])
    rotor3 = int(code[24:26])
    rotor1pos = int(code[26:28])
    rotor2pos = int(code[28:30])
    rotor3pos = int(code[30:32])
    string = tri_rotor(string, rotors[rotor1], rotors[rotor2], rotors[rotor3], rotor1pos, rotor2pos, rotor3pos)
    return string


def decode_enigma(string, code):
    rotor1 = int(code[20:22])
    rotor2 = int(code[22:24])
    rotor3 = int(code[24:26])
    rotor1pos = int(code[26:28])
    rotor2pos = int(code[28:30])
    rotor3pos = int(code[30:32])
    string = decode_tri_rotor(string, rotors[rotor1], rotors[rotor2], rotors[rotor3], rotor1pos, rotor2pos, rotor3pos)
    string = swap_letters(string, code[:20])
    return string


def generate_random_code():
    def generate_swap_code():
        result = ''
        letters = [letter for letter in ascii_lowercase]
        for _ in range(20):
            choice = random.choice(letters)
            result += choice
            letters.remove(choice)
        return result

    def generate_random_indexes():
        result = ''
        indexes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                   '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
        for _ in range(3):
            choice = random.choice(indexes)
            result += choice
            indexes.remove(choice)
        return result

    def generate_random_positions():
        result = ''
        for _ in range(3):
            number = str(random.randint(0, 25))
            if len(number) == 1:
                number = '0' + number
            result += number
        return result

    return generate_swap_code() + generate_random_indexes() + generate_random_positions()
