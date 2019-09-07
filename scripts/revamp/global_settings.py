#!/usr/bin/env python3.7
# coding: utf-8
# dependences: none

#===================================================================================#
#=====================================SETTINGS======================================#
#===================================================================================#

words_to_create = 10			# any integer
stress_feet = 'l'				# 'l' or 'r' or 'm' if foot_max == 3
build_feet = 'r'				# 'l' or 'r'
main_stressed_foot = 'l'		# 'l' or 'r' or int <= min_len/foot_max -1
syllabic_consonant_freq = 0.0	# float 0.0 - 1.0
complex_onsets_freq = 0.0		# float 0.0 - 1.0
complex_nucleus_freq = 0.0		# float 0.0 - 1.0
coda_frequency = 0.0			# float 0.0 - 1.0
geminate_freq = 0.0				# float 0.0 - 1.0
min_len = 2						# any integer <= max_len
max_len = 2						# any integer >= min_len
foot_max = 2					# any integer (ideally 2 or 3)

file_name = 'inventory_4th.csv'
ipa_file_name = 'ipa.csv'

onsets = ["pʰ","kʰ","p","m","t","n","r","s","l","c","k","j","ç","ʀ","p̪"]
codas = ["p","m","t","n","r","s","l","c","k","j","ɱ","ɳ","ŋ","ç","ʀ"]
nuclear_vowels = ["aː","iː","uː","i","a","u","ɛː"]
syllabic_consonants = ["m̩","n̩","l̩","ɱ̍","ɳ̩","ŋ̍"]

sample_string = "◌̥◌̊◌̤◌̪◌͆◌̬◌̰◌̺◌ʰ◌̼◌̻◌̹◌͗◌˒◌ʷ◌̃◌̜◌͑◌˓◌ʲ◌ⁿ◌̟◌˖◌ˠ◌ˡ◌̠◌˗◌ˤ◌̚◌̈◌̴◌ᵊ◌̽◌̝◌˔◌ᶿ◌̩◌̍◌̞◌˕◌ˣ◌̯◌̑◌̘◌ʼ◌˞◌̙◌͡◌◌͜◌n͡mŋ͡mt͡pd͡bk͡pɡ͡bq͡ʡɧɥ̊ɥʍwɫj̃w̃h̃ˈˌːˑ◌̆|‖.‿◌̋◌́◌̄◌̀◌̏ꜜ◌ꜛ◌◌̌◌̂◌᷄◌᷅◌᷇◌᷆◌᷈◌᷉↗︎↘︎[]//()⸨⸩{}˥˦˧˨˩˩˥˥˩˧˥˩˧˥˧˧˩˧˦˨˧˨˦iyɨʉɯuɪʏʊeøɘɵɤoe̞ø̞əo̞ɛœɜɞʌɔæɐaɶäɑɒpʼtʼʈʼcʼkʼqʼʡʼt̪θʼtsʼt̠ʃʼʈʂʼkxʼqχʼɸʼfʼθʼsʼʃʼʂʼɕʼxʼχʼtɬʼcʎ̝̊ʼkʟ̝̊ʼɬʼʘǀǃǂʘ̬ǀ̬ǃ̬ǂ̬ʘ̃ǀ̃ǃ̃ǂ̃ǁǁ̬ɓɗᶑʄɠʛɓ̥ɗ̥ᶑ̊ʄ̊ɠ̊ʛ̥m̥mɱn̼n̥nɳ̊ɳɲ̊ɲŋ̊ŋɴpbp̪b̪t̼d̼tdʈɖcɟkɡqɢʡʔtsdzt̠ʃd̠ʒʈʂɖʐtɕdʑpɸbβp̪fb̪vt̪θd̪ðtɹ̝̊dɹ̝t̠ɹ̠̊˔d̠ɹ̠˔cçɟʝkxɡɣqχʡʢʔhszʃʒʂʐɕʑɸβfvθ̼ð̼θðθ̠ð̠ɹ̠̊˔ɹ̠˔ɻ˔çʝxɣχʁħʕhɦʋ̥ʋɹ̥ɹɻ̊ɻj̊jɰ̊ɰʔ̞ⱱ̟ⱱɾ̼ɾ̥ɾɽ̊ɽɢ̆ʡ̆ʙ̥ʙr̥rɽ̊r̥ɽrʀ̥ʀʜʢtɬdɮʈɭ̊˔cʎ̝̊kʟ̝̊ɡʟ̝ɬɮɭ̊˔ɭ˔ʎ̝̊ʎ̝ʟ̝̊ʟ̝lɭ̊ɭʎ̥ʎʟ̥ʟʟ̠ɺɭ̆ʎ̆ʟ̆"

fix_randomization = True		# boolean (set to True to set seed)
seed_variable = 2				# any integer, even if fix_randomization is False

#===================================================================================#
#=====================================CHANGES=======================================#
#===================================================================================#

# insert, change, delete
# insertions.initial(word,'n')

