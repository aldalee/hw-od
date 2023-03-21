def find_longest_password(passwords):
    # 将密码本中的密码存储到set中，便于查找
    password_set = set(passwords)
    result = ""
    for password in passwords:
        # 对于每个密码，从它的末尾开始依次去掉一位，判断新密码是否在密码本中存在
        for i in range(len(password) - 1, -1, -1):
            new_password = password[:i] + password[i + 1:]
            if new_password in password_set:
                # 如果新密码在密码本中存在，则将当前密码与之前的结果比较
                if len(password) > len(result) or (len(password) == len(result) and password > result):
                    result = password
                break
    return result


def main():
    passwords = input().split()
    print(find_longest_password(passwords))


if __name__ == '__main__':
    main()
