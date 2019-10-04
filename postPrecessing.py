"""
运行程序后处理内容，用于最后一次作业中的检查输出文件内容。
"""
import os

def verify_file(std:str,output:str)->str:
    """
    将标准答案输出和程序输出做比较。返回检查结果。字符串。
    """
    text = f"<br>------------输出文件检查{output}--------------<br>"
    fpstd = open(std,'r')
    try:
        fpoutput = open(output,'r')
    except:
        text+=f"<br>cannot open file {output}<br>"
        return text
    # 依次比较所有数据是否相等
    stdData = list(map(int,fpstd.read().split()))
    try:
        outputData = list(map(int,fpoutput.read().split()))
    except ValueError:
        text+=("<br>文件转换失败，内容如下<br>")
        fpoutput.seek(0)
        text+=(fpoutput.read())
        text+=("<br>使用系统diff命令比较<br>")
        out = os.popen(f'diff "{std}" "{output}"')
        text += "<br>"+out.read().replace('\n','<br>')+'<br>'
        return text
    if stdData==outputData:
        text+=("<br>文件数据完全相同<br>")
    else:
        text+=("<br>文件数据不同，内容如下<br>")
        fpoutput.seek(0)
        text+=(fpoutput.read().replace('\n','<br>'))
        text+=("使用系统diff命令比较")
        out = os.popen(f'diff "{std}" "{output}"')
        text += "<br>" + out.read().replace('\n','<br>') + '<br>'
    fpstd.close()
    fpoutput.close()
    return text
