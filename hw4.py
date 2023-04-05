def rep_char(c, n):
    print(c * n)

def draw_line_string(name, msg1, msg2):
    first = len(msg1) + len(name)
    num = first if first > len(msg2) else len(msg2)
    rep_char('-', num + 4)
    print(f' {msg1} {name},')
    print(f' {msg2}')
    rep_char('-', num + 4)

name = input('Input his/her name: ')
msg1 = 'Hello'
msg2 = 'Welcome to Seoul,'
draw_line_string(name, msg1, msg2)
