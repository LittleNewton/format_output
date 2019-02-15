2019-02-14，晚上

我跟小老弟讨论起他的初中一年级数学期末考试试卷，有一道题目就是预测如图output.png中，序列的第45行第8列的数据数值。

这个问题很简单，是一个等差数列问题，用平方关系也可以解出来，但是小老弟想把它列出来。我认为，这种应试题目肯定有规律。

不过小老弟坚持列举，而且很不耐烦。我就写了这个简单的代码，列举一下。代码的使用方法如下，如果你在教育孩子的过程中遇到这个问题，可以用这个代码演示一下手工列举是多么困难的一件事。

``` Bash
newton@newton-pc-4 ~/Desktop/打印
$ python3 format_output.py 
小老弟你想输出多少行呢？12
1 	2 	5 	10 	17 	26 	37 	50 	65 	82 	101 	122 	



4 	3 	6 	11 	18 	27 	38 	51 	66 	83 	102 	123 	



9 	8 	7 	12 	19 	28 	39 	52 	67 	84 	103 	124 	



16 	15 	14 	13 	20 	29 	40 	53 	68 	85 	104 	125 	



25 	24 	23 	22 	21 	30 	41 	54 	69 	86 	105 	126 	



36 	35 	34 	33 	32 	31 	42 	55 	70 	87 	106 	127 	



49 	48 	47 	46 	45 	44 	43 	56 	71 	88 	107 	128 	



64 	63 	62 	61 	60 	59 	58 	57 	72 	89 	108 	129 	



81 	80 	79 	78 	77 	76 	75 	74 	73 	90 	109 	130 	



100 	99 	98 	97 	96 	95 	94 	93 	92 	91 	110 	131 	



121 	120 	119 	118 	117 	116 	115 	114 	113 	112 	111 	132 	



144 	143 	142 	141 	140 	139 	138 	137 	136 	135 	134 	133 	
```
