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


def parse_str(str_lst):
    return [i.replace('  ',' ').split(' ') for i in str_lst]

def open_refer_candi(refer_file_path, candi_file_path):
    refer_file = open(refer_file_path)
    refer_lst = refer_file.read().splitlines()
    refer_lst = parse_str(refer_lst)
    # print(refer_lst)

    candi_file = open(candi_file_path)
    candi_lst = candi_file.read().splitlines()
    candi_lst = parse_str(candi_lst)

    # for i in candi_lst:
    #     print(i)

    refer_file.close()
    candi_file.close()

    return refer_lst, candi_lst
