def create_record(name, telephone, address):
    '''Create Record'''
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record
user1 = create_record('Vasya', '+7909999', 'russiya')
user2 = create_record('Olejean', '+79637690939', 'chelkovo')
print(user1,'\n', user2)
