                              ,,                                      
                            `7MM                                      
                              MM                                      
`7MMpMMMb.  .gP"Ya   ,pW"Wq.  MM  ,pW"Wq.   .P"Ybmmm ,pW"Wq.  ,pP"Ybd 
  MM    MM ,M'   Yb 6W'   `Wb MM 6W'   `Wb :MI  I8  6W'   `Wb 8I   `" 
  MM    MM 8M"""""" 8M     M8 MM 8M     M8  WmmmP"  8M     M8 `YMMMa. 
  MM    MM YM.    , YA.   ,A9 MM YA.   ,A9 8M       YA.   ,A9 L.   I8 
.JMML  JMML.`Mbmmd'  `Ybmd9'.JMML.`Ybmd9'   YMMMMMb  `Ybmd9'  M9mmmP' 
                                           6'     dP                  
                                           Ybmmmd'     

neologos: a python package create and evolve words for a new or existing conlang. 



Based off an early project:

Package has functionality to read .csv dataframes of words, translations, etc and to transcribe them (although for some languages this is a beast in and of itself so I may remove this for languages that donʼt have easy 1-to-1 ipa to orthography correspondents).

Hereʼs an example of the input, from which a script randomly draws an affix and a root word that will work with it, and organizes them in the correct order. Then the package can be called to analyze this new word.

And here is a result of a script that does this four times and analyzes the new words to count the violations of constraints I have specified:
 
If these violate any constraints, they need other possible candidates to compete with, so thatʼs the next step. I have some reading to do to determine a reasonable minimum number of candidates to go through these constraints and still determine a winner while using a reasonable amount of computational power. Below is the guts of the vowel_harmony function which when called will default to matching all three parameters unless otherwise specified. Its input is a string of IPA objects and its output is simply an integer count of how many times this rule was violated by this string.

For now the order in which the script calls the packageʼs constraints is hard-coded, but it will soon take a config.txt file where the user can list constraints to be judged, as well as the location for the language data.
