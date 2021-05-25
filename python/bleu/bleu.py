from nltk.translate.bleu_score import sentence_bleu
import warnings
warnings.filterwarnings("ignore")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_with_color(color, str, end='\n'):
    print(color + str + bcolors.ENDC, end = end)

reference = [['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']]
candidates= [['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'],
             ['the', 'fast', 'brown' , 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'],
             ['the', 'quick', 'brown', 'dog', 'jumped', 'over', 'the', 'lazy', 'dog'],
             ['the','brown', 'quick' , 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'],
             ['the', 'fast', 'yellow', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'],
             ['the', 'fast', 'yellow', 'fox', 'jumped', 'over', 'the', 'lazy', 'pig'],
             ['the', 'fast', 'yellow', 'fox', 'jumped', 'over', 'the', 'busy', 'dog'],
             ['the', 'fast', 'brown' , 'fox', 'jumped', 'over', 'za' , 'lazy', 'dog'],
             ['the', 'quick','brown' , 'dog', 'jumped', 'over', 'za' , 'lazy', 'dog'],
             ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy'],
             ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the'],
             ['the', 'fast' , 'brown', 'fox', 'jumped', 'over', 'the']
            ]

print_with_color(bcolors.HEADER,"reference : ")

print(" ".join(reference[0]))
print()


for candidate in candidates:
    score = sentence_bleu(reference, candidate)

    print_with_color(bcolors.HEADER,"candidate : ")

    for i in range(len(reference[0])):

        if(i >= len(candidate)):
            print_with_color(
                bcolors.UNDERLINE+bcolors.WARNING,
                reference[0][i], end=' ')
            continue

        if(candidate[i] == reference[0][i]):

            print(candidate[i], end=' ')
        else:
            print_with_color(bcolors.FAIL,candidate[i], end=' ')

    print('\nscore:', end=' ')
    print_with_color(bcolors.OKCYAN,'{}\n'.format(round(score*100,4)))
