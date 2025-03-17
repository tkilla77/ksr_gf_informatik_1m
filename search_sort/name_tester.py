from null79 import names
import string

vowels = 'aeiou'
def is_good_name(name):
    name = name.lower()
    if name[-1] != 'a':
        return False
    vowel_expected = None
    last = None
    for ch in name:
        if ch == last:
            last = None
            continue
        last = ch
        if vowel_expected is True and ch not in vowels:
            return False
        elif vowel_expected is False and ch in vowels:
            return False
        vowel_expected = not ch in vowels
    return True

print(is_good_name('Hanna'))

#print(sum(1 for n in names if is_good_name(n)))

for name in names:
    if is_good_name(name):
        print(f'good: {name}')
    else:
        print(f'bad: {name}')