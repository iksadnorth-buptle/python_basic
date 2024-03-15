# Section10

# 예제 1
name = ['Kim','Lee','Park',]

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as e:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')


# 예제 2
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')

# 예제 3
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')
finally:
    print('finally ok!')

# 예제 4
try:
    print('Try')
finally:
    print('finally ok!')

# 예제 5
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as e:
    print('Not found it! - ValueError Error!')
except IndexError as e:
    print('Not found it! - IndexError Error!')
except Exception as e:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')


# 예제 6
try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise IndexError
except ValueError as e:
    print('Not found it! - ValueError Error!')
except IndexError as e:
    print('Not found it! - IndexError Error!')
except Exception as e:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')


