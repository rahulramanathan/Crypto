from caesar_freq_analysis_functions import getChiSquareScore
message = """FTUE UE M FQEF EQZFQZOQ""".upper() #encrypted message

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = message.upper()
min_score = 0
decrypted_msg = ''
predicted_key = None
for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
   chi_square_score = getChiSquareScore(translated)
   print('Brute Forcing #%s: %s, %s' % (key, translated, chi_square_score))
   if min_score is 0 or chi_square_score < min_score:
      min_score = chi_square_score
      predicted_key = key
      decrypted_msg = translated

print('Final Result:\nKey:%s\nMessage:%s\nFitness:%s' % (predicted_key,decrypted_msg,min_score))