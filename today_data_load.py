import json

sa_block = ['深a', '创业板', '沪a', '科创版']
for d_i in range(4):
    with open('today_data' + str(d_i) + '.json', 'r') as read_file:
        temp = json.load(read_file)
        with open('今日' + sa_block[d_i] + '.csv', 'w', encoding="utf8") as f:
            f.write(
                '股票代码,名称,板块,时间,今收,跌涨幅,跌涨额,成交量,成交额,振幅,最高,最低,今开,换手率,行业板块,地区板块,市盈率,市净率\n')
            for i in range(len(temp)):
                f.write(temp[i][0] + ',' + temp[i][1]+',' + sa_block[d_i])
                for j in range(len(temp[i][2])):
                    f.write(',' + str(temp[i][2][j]))
                f.write('\n')
    print('ok')
