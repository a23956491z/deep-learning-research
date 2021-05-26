from util import bcolors,print_with_color, open_refer_candi
import math

# s = ['a','b','c','d','f']
def n_gram(seq, n):
    return [ seq[i:i+n] for i in range(0, len(seq)-n+1)]

reference, candidates = open_refer_candi('refer2', 'candi2')
# print(n_gram(candidates[0] ,3))

def bleu(refer, candi, n_grams=4):

    n_grams = min(len(candi), n_grams)
    scores = 0
    for i in range(1, n_grams+1):

        refer_gram_n = n_gram(refer ,i)
        candi_gram_n = n_gram(candi ,i)

        counter = 0
        for i in candi_gram_n:
            if i in refer_gram_n:
                counter+=1

        n_gram_percision = (counter/ len(candi_gram_n))
        if(n_gram_percision == 0):
            return 0
        scores += math.log(n_gram_percision)

    scores /= n_grams
    brevity_penalty = math.exp(1-(len(refer)/ len(candi)))
    bleu_score = math.exp(scores)*brevity_penalty

    return bleu_score

# print(bleu(reference[0], candidates[1]))

print_with_color(bcolors.WARNING, " ".join(reference[0]))
print()

for candidate in candidates:
    score = bleu(reference[0], candidate)

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
