from typing import Container
from dictionary_S import kamus, kamus_txt
from datetime import datetime
 
NO_OF_CHARS = 256
 
def badCharHeuristic(string, size):
    badChar = [-1]*NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i;
    return badChar
 
def search(kamus_txt, kalimat):
    m = len(kalimat)
    n = len(kamus_txt)
    badChar = badCharHeuristic(kalimat, m)
    s = 0
    while(s <= n-m):
        j = m-1
        while j>=0 and kalimat[j] == kamus_txt[s+j]:
            j -= 1
        if j<0:
            print("Pattern occur at shift = {}".format(s))
            s += (m-badChar[ord(kamus_txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(kamus_txt[s+j])])

def autoCorrect(kata):
  suggestion = {}
  maxWrongChars = 2

  for i in range(len(kata)):
    for k in range(len(kamus)):
      if k in suggestion or i == 0:
        if i < len(kamus[k]):
          if kamus[k][i] == kata[i]:
            if k not in suggestion:
              suggestion[k] = {'wrongChars': 0, 'inputKata': kata}
            if i == len(kamus[k]) - 1 and len(kata) <= len(kamus[k]):
              suggestion.pop(k)
          else:
            if k in suggestion:
              suggestion[k]['wrongChars'] += 1
              if suggestion[k]['wrongChars'] > maxWrongChars:
                  suggestion.pop(k)
        else:
          if k in suggestion or i == 0:
            suggestion[k]['wrongChars'] += 1
            if suggestion[k]['wrongChars'] > maxWrongChars:
              suggestion.pop(k)

  # print(suggestion)
  for s in suggestion:
    print(suggestion[s]['inputKata'], 'mungkin =', kamus[s])

print(' BOYER MOORE :) \n')
kalimat = input('cek kata/kalimat: ')
start_time = datetime.now()

search(kamus_txt, kalimat)
end_time = datetime.now()
print('Duration BoyerMoore: {}'.format(end_time - start_time),'\n')

kalimatLower = kalimat.lower()
kalimatArray = kalimatLower.split(sep=' ')
print('Kalimat:', kalimat ,'\n')

for kata in kalimatArray:
  if kata in kamus:
    print('kata (',kata,') tersebut baku')
  else:
    print('kata (',kata,') tersebut tidak baku atau mungkin terjadi typo')

print('\nSuggestion: ')
for kata in kalimatArray:
  autoCorrect(kata)

end_time_2 = datetime.now()
print('\nDuration Total Execution: {}'.format(end_time_2 - start_time))