def color(this_color, string):
    return "\033[" + this_color + "m" + string + "\033[0m"

for i in range(30, 38):
    c = str(i)
    print('This is %s' % color(c, 'color ' + c))

    c = '1;' + str(i)
    print('This is %s' % color(c, 'color ' + c))
for i in range(256):
    c = '38;05;%d' % i
    print( color(c, 'color ' + c) )