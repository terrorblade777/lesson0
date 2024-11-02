immutable_var=1, 2, 3, 4, 'h', 'e', 'l', 'p'
print(immutable_var)
immutable_var['h']='p'
# Не получается, так как это не список, а лишь ссылка на него.





mutable_list=['kunjut',3,5,'oreh']
print(mutable_list)
print(mutable_list[0])
mutable_list.append('nuts')
print(mutable_list)
mutable_list.remove (3)
print(mutable_list)
print ('arahis' in mutable_list)