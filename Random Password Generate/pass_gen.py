from pass_create import Password
import argparse

arg = argparse.ArgumentParser('pass_gen.py By Satya Anurag Das\n ')
arg.add_argument('-c', '--charset', required=True)
arg.add_argument('-l', '--length', default=8)
options = arg.parse_args()
# print(options.charset)
# print(options.length)

password = Password(options.charset, int(options.length))
password.set_charset()
password.gen_pass()
print('The random password is: ', password.get_pass())
