immutable_var=tuple_=5,6,7,8, True,"apple"
print(immutable_var)
print("\n'tuple' object does not support item assignment")
print("\nОперация сложения")
tuple_=(5,6,7,8,True,"apple")+(9,10,False,"peach")
print(tuple_)
print('Умножение'.upper())
tuple_=(5,6,7,8,True,'apple')*4
print(tuple_)
mutable_list=["cards",'money','two pistols', 2000]
mutable_list.append ('Holliwood, USA')
print(mutable_list)
mutable_list.remove("money")
print(mutable_list)
mutable_list[0]='bowling'
print(mutable_list)
print('cards'in mutable_list)
print('cards'not in mutable_list)
print(mutable_list[::2])
print (mutable_list[::-1])