from nltk.translate.bleu_score import sentence_bleu
import warnings
from util import bcolors,print_with_color, open_refer_candi
warnings.filterwarnings("ignore")


reference, candidates = open_refer_candi('refer2', 'candi2')
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
