import logging

def readFileLine(filepath):
    with open(filepath,'r') as f:
        for line in f.readlines():
            line = line.strip()
            wrds = line.split()
            wrdsLen = len(wrds)
            if 1<wrdsLen<=2:
                wrds.append('')
            elif wrdsLen > 2:
                wrds = line.split(" ", 2)
            else:
                logging.error('The new value is not appropriate')
            yield wrds


def processFile():
    filePath = 'C:\\Users\\Janki\\Desktop\\CS-555-Agile\\Project\\Janki_Patel_Project01.ged'
    actual_tag = {'DIV': '1', 'DATE': '2', 'HEAD': '0', 'TRLR': '0', 'NOTE': '0', 'NAME': '1', 'SEX': '1',
                  'MARR': '1', 'HUSB': '1', 'WIFE': '1', 'CHIL': '1', 'BIRT': '1', 'DEAT': '1', 'FAMC': '1',
                  'FAMS': '1'}
    s_actual_tag = {'FAM': '0', 'INDI': '0'}

    for level, tag, argument in readFileLine(filePath):
        print("-->", level, tag, argument)
        output = list()
        actual_tag_level = False
        s_tags = False
        if argument not in ['INDI', 'FAM']:
            for current_tag, current_level in actual_tag.items():
                if level == current_level and tag == current_tag:
                    actual_tag_level = True
                    break


        else:
            s_tags = True
            for current_tag, current_level in s_actual_tag.items():
                if level == current_level and argument == current_tag:
                    actual_tag_level = True
                    break

        if (actual_tag_level and s_tags) or (actual_tag_level and not s_tags) or (not actual_tag_level and s_tags):
            output.append(level)
            elem = argument if (actual_tag_level and s_tags) or (not actual_tag_level and s_tags) else tag
            output.append(elem)

            elem = "Y" if (actual_tag_level and s_tags) or (actual_tag_level and not s_tags) else 'N'
            output.append(elem)

            elem = argument if actual_tag_level and not s_tags else tag
            output.append(elem)

        else:
            output= [level + " " + tag,'N',argument]
        output = "|".join(output)
        print("<-- {0}".format(output))


processFile()