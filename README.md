neologos



  ┌┐┌┌─┐┌─┐┬  ┌─┐┌─┐┌─┐┌─┐
  
  │││├┤ │ ││  │ ││ ┬│ │└─┐
  
  ┘└┘└─┘└─┘┴─┘└─┘└─┘└─┘└─┘

Neologos: a python package to apply OT rules to input words. Package also has functionality to read csv dataframes if words, translations, etc and to transcribe them (although for some languages this is a beast in and of itself so I may remove this for languages that donʼt have easy 1-to-1 ipa to orthography correspondents).

Hereʼs an example of the input, from which a script randomly draws an affix and a root word that will work with it, and organizes them in the correct order. Then the package can be called to analyze this new word.

And here is a result of a script that does this four times and analyzes the new words to count the violations of constraints I have specified:
 
If these violate any constraints, they need other possible candidates to compete with, so thatʼs the next step. I have some reading to do to determine a reasonable minimum number of candidates to go through these constraints and still determine a winner while using a reasonable amount of computational power. Below is the guts of the vowel_harmony function which when called will default to matching all three parameters unless otherwise specified. Its input is a string of IPA objects and its output is simply an integer count of how many times this rule was violated by this string.

For now the order in which the script calls the packageʼs constraints is hard- coded, but it will soon take a config.txt file where the user can list constraints to be judged, as well as the location for the language data and stuff, so they will never need to actually read the python code if they donʼt want to.
