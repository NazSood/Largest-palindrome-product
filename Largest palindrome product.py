    
greatestPalin = 0


for i in range (899, 1000):
  for l in range(899, 1000):
    result = l * i
    HTHdigit= int(result / 100000)
    TTHdigit= int(result / 10000) - ((HTHdigit * 10))
    THdigit = int(result / 1000)  - ((HTHdigit * 100) + (TTHdigit * 10))
    HUdigit = int(result / 100)   - ((HTHdigit * 1000) + (TTHdigit * 100) + (THdigit * 10))
    TNdigit = int(result / 10)    - ((HTHdigit * 10000) + (TTHdigit * 1000) + (THdigit * 100) + (HUdigit * 10)) 
    ONdigit = int(result)         - ((HTHdigit * 100000) + (TTHdigit * 10000) + (THdigit * 1000) + (HUdigit * 100) + (TNdigit * 10))


    result_palin = (ONdigit * 100000) + (TNdigit * 10000) + (HUdigit * 1000) + (THdigit * 100) + (TTHdigit * 10) + HTHdigit

    if(result == result_palin):
      if(result_palin > greatestPalin):
        greatestPalin = result_palin
        print("Greatest: {:d}" .format(greatestPalin))
        print("NUmber1: {:d} & NUmber2: {:d}" .format(i, l))
      #print("palindrome: " ,result)
     
    


