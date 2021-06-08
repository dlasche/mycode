#!/usr/bin/env python3

switch = {"hostname": 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

##display parts
print(switch['hostname'])
print(switch['ip'])

## request a fake key
## print(switch['lynx'])

#use get method

print('First test - .get()')
print(switch.get('lynx'))

print('second test - .get()')
print(switch.get('lynx', 'THEY KEY IS IN ANOTHER CASTLE!'))

print('third test - .get()')
print(switch.get('version'))

print('sixth test - ADD a new value')
switch['adminlogin'] = 'karl08'
print(switch.keys())
print(switch.values())


print('Eigth test - ADD a new value')
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())


