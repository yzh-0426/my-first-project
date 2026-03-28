# 姓名：叶祉航
# Python程序设计
# Teamwork1: DNA分析

#这个程序读取DNA测序器的输出并计算统计数据，比如GC的含量。
#从如下命令行运行：python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# sys模块支持读取文件、命令行参数等。
import sys


###########################################################################
### 将核苷酸读入一个名为seq的变量中
###

# 需要指定文件名
if len(sys.argv) < 2:
    print( "运行此程序时，必须提供一个文件名作为参数。")
    sys.exit(2)
# 在命令行上指定的文件名，作为字符串。
filename = sys.argv[1]
# 可以从中读取数据的文件对象。
inputfile = open(filename)

# 输入文件中迄今为止已读取的所有核苷酸。
seq = ""
# 当前行号（=到目前为止读取的行数）。
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # 如果我们在2，6，10行
    if linenum % 4 == 2:
        # 从行尾删除换行符
        line = line.rstrip()
        seq = seq + line


###########################################################################
### 计算统计
###

# 迄今为止发现的总核苷酸。
total_count = 0
# G和C核苷酸的数量。
gc_count = 0
#AT
at_count = 0
a_count = 0       
t_count = 0       #
g_count = 0      
c_count = 0

# 对于字符串中的每个碱基（bp），
for bp in seq:
    # 增加我们看到的碱基总数
    total_count = total_count + 1

    # 接下来，如果bp是G或C，
    if bp == 'C' or bp == 'G':
        # 增加bp的计数
        gc_count = gc_count + 1
    if bp == 'A' or bp == 'T':
        at_count = at_count + 1    
    if bp == 'A':
        a_count = a_count + 1    
    if bp == 'T':
        t_count = t_count + 1    
    if bp == 'G':
        g_count = g_count + 1    
    if bp == 'C':
        c_count = c_count + 1    

# 用GC碱基总计数gc_count 除以总计数total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count


sum_count = a_count + t_count + g_count + c_count  # 有效碱基总和
seq_length = len(seq)                             # 序列字符串总长度

    # 计算GC含量、AT含量（使用有效碱基计数作为分母）
gc_content = (g_count + c_count) / sum_count if sum_count != 0 else 0
at_content = (a_count + t_count) / sum_count if sum_count != 0 else 0

#rate 计算
at_sum = a_count + t_count  # A+T 总数
gc_sum = g_count + c_count  # G+C 总数
# 防止除数为0（避免程序报错），计算AT/GC比率
at_gc_ratio = at_sum / gc_sum if gc_sum != 0 else 0

#8
gc_percent = gc_content * 100  # 转换为百分比
if gc_percent > 60:
    gc_class = "high (高GC含量)"
elif gc_percent < 40:
    gc_class = "low (低GC含量)"
else:
    gc_class = "medium (中等GC含量)"


    # 打印文件分析结果
print("="*50)
print(f"文件：{filename}")
print(f"A count: {a_count}")
print(f"T count: {t_count}")
print(f"G count: {g_count}")
print(f"C count: {c_count}")
print(f"Sum count (A+T+G+C): {sum_count}")
print(f"Total count (循环计数): {total_count}")
print(f"Seq length (len(seq)): {seq_length}")
print(f"GC 含量: {gc_content:.4f}")
print(f"AT 含量: {at_content:.4f}")
print("="*50 + "\n")
print(f"AT/GC 比率: {at_gc_ratio:.4f}")
print(f"GC含量分类: {gc_class}")



"""
==================================================
文件：test-small.fastq
A count: 5
T count: 2
G count: 1
C count: 2
Sum count (A+T+G+C): 10
Total count (循环计数): 10
Seq length (len(seq)): 10
GC 含量: 0.3000
AT 含量: 0.7000
==================================================

AT/GC 比率: 2.3333
GC含量分类: low (低GC含量)





==================================================                                                                      
文件：test-moderate-gc-2.fastq                                                                                          
A count: 11813                                                                                                          
T count: 12027                                                                                                          
G count: 7972                                                                                                           
C count: 7999                                                                                                           
Sum count (A+T+G+C): 39811                                                                                              
Total count (循环计数): 40000                                                                                           
Seq length (len(seq)): 40000                                                                                            
GC 含量: 0.4012                                                                                                         
AT 含量: 0.5988                                                                                                         
==================================================                                                                      
                                                                                                                        
AT/GC 比率: 1.4927                                                                                                      
GC含量分类: medium (中等GC含量)  



==================================================
文件：test-moderate-gc-1.fastq
A count: 10077
T count: 9963
G count: 9818
C count: 9983
Sum count (A+T+G+C): 39841
Total count (循环计数): 40000
Seq length (len(seq)): 40000
GC 含量: 0.4970
AT 含量: 0.5030
==================================================

AT/GC 比率: 1.0121
GC含量分类: medium (中等GC含量)




==================================================
文件：test-high-gc-2.fastq
A count: 3908
T count: 4023
G count: 15955
C count: 15955
Sum count (A+T+G+C): 39841
Total count (循环计数): 40000
Seq length (len(seq)): 40000
GC 含量: 0.8009
AT 含量: 0.1991
==================================================

AT/GC 比率: 0.2485
GC含量分类: high (高GC含量)




==================================================
文件：test-high-gc-1.fastq
A count: 7970
T count: 7894
G count: 12176
C count: 11800
Sum count (A+T+G+C): 39840
Total count (循环计数): 40000
Seq length (len(seq)): 40000
GC 含量: 0.6018
AT 含量: 0.3982
==================================================

AT/GC 比率: 0.6617
GC含量分类: high (高GC含量)



S_6
GC-content: 0.4915185185185185                                                                                          
AT-content: 0.5081111111111111                                                                                          
G count: 7304                                                                                                           
C count: 5967                                                                                                           
A count: 6867                                                                                                           
T count: 6852                                                                                                           
Sum count: 26990                                                                                                        
Total count: 27000                                                                                                      
seq length: 27000                                                                                                       
AT/GC Ratio: 1.0337578177982065                                                                                         
GC Classification: Medium GC content  





 sample_5.fastq                                                
GC-content: 0.2631578947368421                                                                                          
AT-content: 0.7236842105263158                                                                                          
G count: 11                                                                                                             
C count: 9                                                                                                              
A count: 27                                                                                                             
T count: 28                                                                                                             
Sum count: 75                                                                                                           
Total count: 76                                                                                                         
seq length: 76                                                                                                          
AT/GC Ratio: 2.75                                                                                                       
GC Classification: Low GC content  



sample_4
GC-content: 0.3478523411663431
AT-content: 0.6521429498904319
G count: 1620779
C count: 1851138
A count: 3304273
T count: 3204771
Sum count: 9980961
Total count: 9981008
seq length: 9981008
AT/GC Ratio: 1.8747694717356433
GC Classification: Low GC content


sample_3.fastq
GC-content: 0.6468641125240355
AT-content: 0.3531311560764628
G count: 3008039
C count: 3144239
A count: 1561973
T count: 1796632
Sum count: 9510883
Total count: 9510928
seq length: 9510928
AT/GC Ratio: 0.5459124246336072
GC Classification: High GC content




sample_2.fastq
GC-content: 0.45105133333333336
AT-content: 0.548112925925926
G count: 6103168
C count: 6075218
A count: 7467696
T count: 7331353
Sum count: 26977435
Total count: 27000000
seq length: 27000000
AT/GC Ratio: 1.2151896811285174
GC Classification: Medium GC content




sample_1.fastq
GC-content: 0.4302926296296296
AT-content: 0.5689938518518518
G count: 5738773
C count: 5879128
A count: 7701287
T count: 7661547
Sum count: 26980735
Total count: 27000000
seq length: 27000000
AT/GC Ratio: 1.3223416174746196
GC Classification: Medium GC content

1. 数值差异情况：
   部分fastq文件中 Sum count < Total count = seq length
2. 差异原因：
   FASTQ测序文件中存在非A/T/G/C的字符（最常见为N，代表未识别的碱基），
   这类字符会计入Total count和seq length，但不会计入Sum count，因此三者不相等。
3. 分母使用规则：
   计算GC/AT含量时，必须使用 seq length / Total count 作为分母（代表序列真实长度）；
   禁止使用Sum count，否则会导致计算结果错误，不符合生物学定义。

   

   独立在AI帮助下理解作业找出误差完成了作业
结论：直接交给AI会出现无法读取，Ai幻觉，作业前后要求不符，格式整体被改等问题，但可以用来辅助理解：作业要我做什么以及怎么打开文件。还可以帮忙注释和解决error。
另，完成时长5小时，加上代码运行时间高达7小时。（代码有一次运行一半电脑自己睡眠了，我也睡眠了，半个多小时才发现）

"""
