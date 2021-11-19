import pandas as pd
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
df = pd.read_csv(url, sep='	')

print('#1')
print('Количество наблюдений: ' + str(df['order_id'].count()) + '\n')
print('#2')
print(df.columns + '\n')
msfr = df.groupby('item_name').sum()['quantity']
print('#3')
print('Cамая частая позиция в заказе: ' + str(msfr.idxmax()) + '\n')

print('#4')
hists = plt.figure()
hs1 = hists.add_subplot(121)

msfr.plot.bar()

print('#5')
print(df['item_price'].dtype)

df['item_price'] = df['item_price'].apply(lambda x: pd.to_numeric(x[1:]))
print(df['item_price'].dtype)
print('\n')

print('#6')
hs2 = hists.add_subplot(122)

df.groupby('item_name').sum()['item_price'].plot.bar()

orders = df.groupby('order_id').sum()['item_price']
print('#7')
print('Средняя сумма заказа: ' + str(orders.mean()))
print(str(orders.sum()/orders.count()) + '\n')


print('#8')
unique = df[['order_id', 'item_name']]
unique = unique.groupby('order_id')['item_name'].nunique()
unique = unique.describe()
print(unique.drop(['25%', '75%']))
print('\n')

print('#9')
steaks = df.loc[df['item_name'].str.contains(r'Steak')]
print(steaks.groupby('item_name').sum()['quantity'])
print('\n')


roast = steaks['choice_description'].str.split(pat='(', expand=True)[1]
roast = roast.str.split(pat=')', expand=True)[0]
steaks['roast'] = roast
print(steaks.groupby('roast').sum()['quantity'])

print('#10')
df['price_in_rubles'] = df['item_price'] * 72.56
print(df['price_in_rubles'])
print('\n')


print('#11')
not_steaks = df.loc[~df['item_name'].str.contains(r'Steak')]
group1 = steaks.groupby('roast').sum()['quantity']
group2 = not_steaks.groupby('item_name').sum()['quantity']
fin_group = pd.concat([group1, group2])
print(fin_group)
print('\n')

print('#12')
df['price_per_item'] = df['item_price'] / df['quantity']
unique_items = df[['item_name', 'price_per_item']]
unique_items = unique_items.drop_duplicates(subset=['item_name'])
print(unique_items)
print('\n')



plt.show()