import sys

def file_reader(path:str):
    try:
        file_open = open(path, 'r')
        with file_open:
                for record_num, record in enumerate(file_open):
                    column: list = record.strip().split()
                    if len(column) >= 3:
                        column = record.strip().split(" ", 2)
                    elif len(column) < 1:
                        raise ValueError
                    else:
                        column = record.strip().split()
                        column.append("")
                    yield column
    except ValueError:
        print(" Columns are not present")

def main():
    path = 'C:\\Users\\Janki\\Desktop\\CS-555-Agile\\Project\\Janki_Patel_Project01.ged'
    for level, tag, argument in file_reader(path):
        print("-->", level, tag, argument)
        outcome = list()
        valid_tags: dict = {'NAME': '1', 'SEX': '1', 'MARR': '1',
                      'BIRT': '1', 'DEAT': '1', 'FAMC': '1', 'FAMS': '1',
                      'HUSB': '1', 'WIFE': '1', 'CHIL': '1',
                      'DIV': '1', 'DATE': '2', 'HEAD': '0', 'TRLR': '0', 'NOTE': '0'}
        special_valid_tags: dict = {'INDI': '0', 'FAM': '0'}

        valid_tag_level: bool = True
        if argument in ['INDI', 'FAM']:
            special_tags = False
            for current_tag, current_level in special_valid_tags.items():
                if level == current_level and argument == current_tag:
                    valid_tag_level = False
                    break
        else:
            special_tags: bool = True
            for current_tag, current_level in valid_tags.items():
                if level == current_level and tag == current_tag:
                    valid_tag_level = False
                    break

        if (not valid_tag_level and not special_tags) or (valid_tag_level and not special_tags) or (valid_tag_level and special_tags):
            outcome.append(level)
            outcome.append(argument) if (not valid_tag_level and not special_tags) or (valid_tag_level and not special_tags) else outcome.append(tag)
            outcome.append(
                "N") if (valid_tag_level and not special_tags) or (valid_tag_level and special_tags) else outcome.append("Y")
            outcome.append(tag) if (not valid_tag_level and not special_tags) or (valid_tag_level and not special_tags) else outcome.append(argument)
        else:
            outcome.append(level+" "+tag)
            #outcome.append(tag)
            outcome.append("Y")
            outcome.append(argument)
            #if valid_tag_level and special_tags:
                
        print("<-- "+"|".join(outcome))


if __name__ == "__main__":
    main()