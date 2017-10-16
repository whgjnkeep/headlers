import json
import re

with open("E:\dataunit\idea.question.v1_question.json",'r',encoding='utf-8') as f:
    lines = f.readlines()
    marriage_case = 0  # 婚姻
    labor_case = 0  # 劳动
    land_case = 0  # 土地
    traffic_case = 0  # 交通
    wage_case = 0  # 工资
    child_case = 0  # 孩子
    house_case = 0  # 房屋
    criminal_case = 0  # 刑事
    work_injury_case = 0  # 工伤
    contract_case = 0  # 合同
    consumption_case = 0  # 消费
    operating_case = 0  # 经营
    inherit_case = 0  # 继承
    guaranteed_case = 0  # 取保
    personal_debt_case = 0  # 个人债务
    family_disputes_case = 0  # 家庭纠纷
    other = 0
    for line in lines:
        data = json.loads(line)
        if re.search('婚', data['questionClassPath'][4]):
            marriage_case += 1
        elif re.search('劳', data['questionClassPath'][4]):
            labor_case += 1
        elif re.search('地', data['questionClassPath'][4]):
            land_case += 1
        elif re.search('交通', data['questionClassPath'][4]):
            traffic_case += 1
        elif re.search('工资', data['questionClassPath'][4]):
            wage_case += 1
        elif re.search('子女', data['questionClassPath'][4]):
            child_case += 1
        elif re.search('房', data['questionClassPath'][4]):
            house_case += 1
        elif re.search('刑事', data['questionClassPath'][4]):
            criminal_case += 1
        elif re.search('工伤', data['questionClassPath'][4]):
            print('questionTitle: ', data['questionTitle'])
            print('questionContent: ', data['questionContent'])
            for key in data['answer']:
                print('answer: ', key['answerContent'])
            print()
            work_injury_case += 1
        elif re.search('合同', data['questionClassPath'][4]):
            contract_case += 1
        elif re.search('消费', data['questionClassPath'][4]):
            consumption_case += 1
        elif re.search('经营', data['questionClassPath'][4]):
            operating_case += 1
        elif re.search('继承', data['questionClassPath'][4]):
            inherit_case += 1
        elif re.search('取保', data['questionClassPath'][4]):
            guaranteed_case += 1
        elif re.search('个人债务', data['questionClassPath'][4]):
            personal_debt_case += 1
        elif re.search('家庭纠纷', data['questionClassPath'][4]):
            family_disputes_case += 1
        else:
            other += 1

    print('婚姻QA对的数目是：\t', marriage_case,'\t',"占比:\t", str(marriage_case/807900))
    print('劳  QA对的数目是：\t', labor_case,'\t',"占比:\t", str(labor_case/807900))
    print('地  QA对的数目是：\t', land_case,'\t',"占比:\t", str(land_case/807900))
    print('交通QA对的数目是：\t', traffic_case,'\t',"占比:\t", str(traffic_case/807900))
    print('工资QA对的数目是：\t', wage_case,'\t',"占比:\t", str(wage_case/807900))
    print('子女QA对的数目是：\t', child_case,'\t',"占比:\t", str(child_case/807900))
    print('房  QA对的数目是：\t', house_case,'\t',"占比:\t", str(house_case/807900))
    print('工伤QA对的数目是：\t', work_injury_case,'\t',"占比:\t", str(work_injury_case/807900))
    print('合同QA对的数目是：\t', contract_case,'\t', "占比:\t",  str(contract_case / 807900))
    print('消费QA对的数目是：\t', consumption_case,'\t', "占比:\t",  str(consumption_case / 807900))
    print('经营QA对的数目是：\t', operating_case,'\t', "占比:\t", str(operating_case / 807900))
    print('继承QA对的数目是：\t', inherit_case,'\t', "占比:\t", str(inherit_case / 807900))
    print('取保QA对的数目是：\t', guaranteed_case,'\t', "占比:\t", str(guaranteed_case / 807900))
    print('个人债务QA对的数目是：\t', personal_debt_case,'\t', "占比:\t", str(personal_debt_case / 807900))
    print('家庭纠纷QA对的数目是：\t', family_disputes_case,'\t', "占比:\t", str(family_disputes_case / 807900))
    print('其他QA对的数目是：\t', other,'\t',"占比:\t",str(other/807900))




        # if re.search("劳", data['questionClassPath'][4]):
        #     marriage_case += 1
        #     print('questionTitle: ', data['questionTitle'])
        #     print('questionContent: ', data['questionContent'])
        #     for key in data['answer']:
        #         print('answer: ', key['answerContent'])
        #     print()
        # else:
        #     pass


