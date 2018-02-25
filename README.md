# Apriori-Algorithm
> Frequent Itemset Generation and Association Rule Mining


## Includes:
* `Apriori Algorithm`: To find frequent-itemsets from a set of transactions.
* `Rule generation`: Generation of 'interesting' rules from the frequent itemset.
* `Hashing`: Itemsets are hashed to get their support count in almost constant time.

## Requirements:

Only `python3` is required to run this algorithm. No need to install anything else.

`python3` is installed in most Linux distributions, by default.

## Mining the Rules:

First make the Apriori file executable and then simply run it as:
```
$ chmod +x ./Apriori
$ ./Apriori
```
##### This will make a directory: `results` at your current path and store the results in the in a file.

`Name of file`: It will be the values of support and confidence for which Apriori Algorithm is run.

## Paremeters:
`Support`: Defaults value of support is 0.02

`Confidence`: Default value of confidence is 0.45

`Input Transaction file`: Currently set as [groceries.csv](http://www.sci.csueastbay.edu/~esuess/classes/Statistics_6620/Presentations/ml13/groceries.csv).

>All the parameters can be changed from within the code.

## Output:
>In a file `s=0.001 c=0.95`

```
Frequnet Itemsets:
1-itemsets:
['liquor'] | support: 109
['dessert'] | support: 365
['sliced cheese'] | support: 241
['bottled water'] | support: 1087
['oil'] | support: 276
['yogurt'] | support: 1372
....
Count: 88

2-itemsets:
['whole milk', 'citrus fruit'] | support: 300
['other vegetables', 'margarine'] | support: 194
['whipped/sour cream', 'citrus fruit'] | support: 107
['whole milk', 'cream cheese'] | support: 162
['rolls/buns', 'citrus fruit'] | support: 165
['soda', 'citrus fruit'] | support: 126
...
Count: 213

...
Total number of frequent itemset(s): 333


Rules:
['citrus fruit', 'root vegetables'](174) -> ['other vegetables'](1903) | confidence:
0.5862068965517241
['root vegetables', 'tropical fruit'](207) -> ['other vegetables'](1903) | confidence:
0.5845410628019324
['curd', 'yogurt'](170) -> ['whole milk'](2513) | confidence: 0.5823529411764706
['other vegetables', 'butter'](197) -> ['whole milk'](2513) | confidence:
0.5736040609137056
['root vegetables', 'tropical fruit'](207) -> ['whole milk'](2513) | confidence:
0.5700483091787439
....
Total number of rules: 14


```
<b> Format of Rules:

`[LHS] (item set (count))` -> `[RHS] (item set (count))` | `confidence: confidence value`</b>