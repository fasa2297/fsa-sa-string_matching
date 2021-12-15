from typing import Container
from dictionary_S import kamus, kamus_txt
from datetime import datetime

def search(kalimat, kamus_txt):
    M = len(kalimat)
    N = len(kamus_txt)
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
        # For current index i, check
        # for pattern match */
        while(j < M):
            if (kamus_txt[i + j] != kalimat[j]):
                break
            j += 1
        if (j == M):
            print("Pattern found at index ", i)

def autoCorrect(kata):
  suggestion = {} # {0: {wrongChars: 3, inputKata: } (wrong chars)}
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

print(' BRUTE FORCE :) \n')
kalimat = input('cek kata/kalimat: ')
start_time = datetime.now()

search(kalimat, kamus_txt)
end_time = datetime.now()
print('Duration Bruteforce: {}'.format(end_time - start_time),'\n')

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
# Driver Code
#if __name__ == '__main__':
#    pat = input('Masukan kata: ')
#    search(pat, txt)