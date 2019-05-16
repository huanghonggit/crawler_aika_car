import time
import requests
from lxml import etree
import csvWriter

base_url = "http://newcar.xcar.com.cn/{id}/config.htm"
id_list = ['56','232','152','60','174','536','2516','2390','167','3089','141','2380','3603','3333','4162','3791','561','2515','3670','2522','1550','3404','1217','3240','3445','3409','2448','3162','2834','3596','3142','3216','3914','176','1314','2997','1491','2988','2901','3722','3703','1946','172','3470','3571','1222','2426','4135','3592','3174','1367','283','1932','1578']
tm = str(int(time.time()))
dumper = csvWriter.CSVDumper('output_' + tm + '.csv')
for id in id_list:
    url = base_url.format(id=id)
    res = requests.get(url).text
    # print(res)

    html = etree.HTML(res)
    carname_dict = {}
    carname_list = html.xpath("//tr[@id='base_title']/td")
    for i in carname_list:
        if i.xpath("./@ci"):
            carname_dict[i.xpath("./@ci")[0]] = i.xpath("./a/text()")[0] if i.xpath("./a/text()") else ""
        else:
            carname_dict["0"] = "carname"
    print(carname_dict)
    # base_1_dict = {}
    table_base_1 = html.xpath("//table[@id='base_1']/tr")
    big_list = []
    for line in table_base_1:
        base_1_dict = {}
        for i in line.xpath("./td"):
            if i.xpath("./@ci"):
                base_1_dict[i.xpath("./@ci")[0]] = ''.join(i.xpath(".//text()")).strip()
            else:
                base_1_dict["0"] = ''.join(i.xpath(".//text()")).strip()
        big_list.append(base_1_dict)
    dumper.process_item(carname_dict)
    for i in big_list:
        dumper.process_item(i)

    table_base_2 = html.xpath("//table[@id='base_2']/tr")
    big_list_2 = []
    for line in table_base_2:
        base_2_dict = {}
        for i in line.xpath("./td"):
            if i.xpath("./@ci"):
                base_2_dict[i.xpath("./@ci")[0]] = ''.join(i.xpath(".//text()")).strip()
            else:
                base_2_dict["0"] = ''.join(i.xpath(".//text()")).strip()
        big_list_2.append(base_2_dict)
    for i in big_list_2:
        dumper.process_item(i)

    table_base_3 = html.xpath("//table[@id='base_3']/tr")
    big_list_3 = []
    for line in table_base_3:
        base_3_dict = {}
        for i in line.xpath("./td"):
            if i.xpath("./@ci"):
                base_3_dict[i.xpath("./@ci")[0]] = ''.join(i.xpath(".//text()")).strip()
            else:
                base_3_dict["0"] = ''.join(i.xpath(".//text()")).strip()
        big_list_3.append(base_3_dict)
    for i in big_list_3:
        dumper.process_item(i)

    table_base_4 = html.xpath("//table[@id='base_4']/tr")
    big_list_4 = []
    for line in table_base_4:
        base_4_dict = {}
        for i in line.xpath("./td"):
            if i.xpath("./@ci"):
                base_4_dict[i.xpath("./@ci")[0]] = ''.join(i.xpath(".//text()")).strip()
            else:
                base_4_dict["0"] = ''.join(i.xpath(".//text()")).strip()
        big_list_4.append(base_4_dict)
    for i in big_list_4:
        dumper.process_item(i)

    table_base_5 = html.xpath("//table[@id='base_5']/tr")
    big_list_5 = []
    for line in table_base_5:
        base_5_dict = {}
        for i in line.xpath("./td"):
            if i.xpath("./@ci"):
                base_5_dict[i.xpath("./@ci")[0]] = ''.join(i.xpath(".//text()")).strip()
            else:
                base_5_dict["0"] = ''.join(i.xpath(".//text()")).strip()
        big_list_5.append(base_5_dict)
    for i in big_list_5:
        dumper.process_item(i)
    dumper.process_item({" ":" "})