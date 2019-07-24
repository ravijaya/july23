author = 'jaya'


def power(x, n):
    return x ** n


def get_user_list(data_file, target_file):
    """function definition"""

    list_of_users = []

    with open(data_file) as fp:
        for line in fp:
            login = line.split(':')[0]
            list_of_users.append(login)

    line_no = 1

    with open(target_file, 'w') as fw:  # open the target file for writing
        for user in sorted(list_of_users):
            content = '{:>6}  {}'.format(line_no, user)
            print(content)
            fw.write(content + "\n")  # writes into the files
            line_no += 1
