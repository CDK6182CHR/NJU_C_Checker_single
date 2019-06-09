"""
运行程序后处理内容，用于最后一次作业中的检查输出文件内容。
"""
import os

def verify_file(std:str,output:str)->str:
    """
    将标准答案输出和程序输出做比较。返回检查结果。字符串。
    """
    text = f"------------输出文件检查{output}--------------\n"
    fpstd = open(std,'r')
    try:
        fpoutput = open(output,'r')
    except:
        text+=f"cannot open file {output}\n"
        return text
    # 依次比较所有数据是否相等
    stdData = list(map(int,fpstd.read().split()))
    try:
        outputData = list(map(int,fpoutput.read().split()))
    except ValueError:
        text+=("文件转换失败，内容如下\n")
        fpoutput.seek(0)
        text+=(fpoutput.read())
        text+=("使用系统diff命令比较\n")
        out = os.popen(f'diff "{std}" "{output}"')
        text += "\n"+out.read()+'\n'
        return text
    if stdData==outputData:
        text+=("文件数据完全相同\n")
    else:
        text+=("文件数据不同，内容如下\n")
        fpoutput.seek(0)
        text+=(fpoutput.read())
        text+=("使用系统diff命令比较")
        out = os.popen(f'diff "{std}" "{output}"')
        text += "\n" + out.read() + '\n'
    fpstd.close()
    fpoutput.close()
    return text