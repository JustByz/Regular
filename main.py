import csv
import re


phone_number_pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
phone_sub = r"+7(\2)-\3-\4-\5 \6\7"



def name_info(contact_list):

    temp = list()
    for i in contact_list:
        name = ' '.join(i[:3]).split(' ')
        #  получили список ФИО
        name_info = [name[0], name[1], name[2], i[3], i[4]]
        #  составили ФИО раздельно по полям и прочую информацию о человеке
        pnone_number = [re.sub(phone_number_pattern, phone_sub, i[5]), i[6]]
        #  составили номер телефона в установленной форме + добавочный
        result = name_info + pnone_number
        temp.append(result)
    return delete_repeat(temp)


def delete_repeat(contacts):
    
    repeat_for_remove = []
    for i in range(len(contacts)-1):
        for j in range(i+1, len(contacts)):
            if contacts[i][:2] == contacts[j][:2]:
                contacts[j][2] = contacts[i][2] or contacts[j][2]
                contacts[j][3] = contacts[i][3] or contacts[j][3]
                contacts[j][4] = contacts[i][4] or contacts[j][4]
                contacts[j][5] = contacts[i][5] or contacts[j][5]
                contacts[j][6] = contacts[i][6] or contacts[j][6]

                repeat_for_remove.append(contacts[i])
    for i in repeat_for_remove:
        contacts.remove(i)
    return (contacts)



with open("files/phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contact_list = list(rows)



with open("files/phonebook_out.csv", "w", newline='', encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(name_info(contact_list))