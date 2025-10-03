# -*- coding: utf-8 -*-
import re
FILE_PATH="stock_data.txt"
'''将数据源txt变成字典'''

def load_data():
    #字典最后放列表
    stocks=[] 
    with open(FILE_PATH,'r',encoding='utf-8')as f:
        lines=f.readlines()
        #保存表头
        header=lines[0].strip().split(',')
        #保存每行
        for line in lines:
            if not line:
                continue
            data=[x.strip() for x in line.split(',')]
            if len(data)==len(header):
                stock=dict(zip(header,data))
                stocks.append(stock)
    return stocks,header
#print stock data：
def print_stock(stocks,header):
    if not stocks:
        print("no such stock")
        return
    print('\t'.join(header))
    for s in stocks:
        print('\t'.join(s[h] for h in header))

#模糊匹配
def search_by_name(stocks,keyword):
    keyword=keyword.lower()
    return [s for s in stocks if keyword in s['股票名称'].lower()]

#条件筛选
def filter_by_condition(stocks,condition):
    m=re.match(r'(\S+)([<>])([\d.]+)',condition)
    if not m:
        print("条件格式错误，应如 当前价>50")
        return []
    col_name,op,var=m.groups()
    var=float(var)

    result=[]
    for s in stocks:
        if col_name not in s:
            print(f"{col_name} is not exit")
        try:
            v=s[col_name].replace("%",'').replace('万','').replace('亿','').replace(',','')
            v=float(v)
        except:
            continue
        if op =='>' and v>var:
            result.append(s)
        elif op=='<' and v<var:
            result.append(s)
    return result

def main():
        
    stocks, header = load_data()
    while True:
        print("\n查询方式：")
        print("1. 按名称模糊查询")
        print("2. 按条件筛选（如 当前价>50）")
        print("3. 退出")
        choice = input("请输入选项(1/2/3): ").strip()

        if choice=='1':
            keyword=input("请输入股票名称关键词: ").strip()
            res=search_by_name(stocks,keyword)
            print_stock(res,header)
        elif choice=='2':
            condition=input("请输入筛选条件: ").strip()
            res=filter_by_condition(stocks,condition)
            print_stock(res,header)
        elif choice=='3':
            print("退出程序")
            break
        else:
            print("输入错误")
if __name__=='__main__':
    main()





    









