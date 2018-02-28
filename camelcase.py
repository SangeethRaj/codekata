def CamelCase(string_ip):
    import re
    return ''.join(x.capitalize() or '_' for x in string_ip.split('_'))
print(CamelCase('new_york _is _a _beautiful _city.'))
