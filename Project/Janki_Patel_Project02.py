
import sys
def freader(p):
    ln=0
    
    for ln, li in enumerate(open(p, 'r')):
        f = li.strip().split()
        if len(f) > 1 and len(f) <= 2:
            f = li.strip().split()
            f.append("")
            
        elif len(f) >= 3:
            f = li.strip().split(" ", 2)
            
        else:
            print("The value is not approriate")
           
        yield f


def main():
    p = 'C:\\Users\\Janki\\Desktop\\CS-555-Agile\\Project\\Janki_Patel_Project01.ged'
    for level, tag, argument in freader(p):
        print("-->", level, tag, argument)
        output = list()
        actual_tag = {'DIV': '1', 'DATE': '2', 'HEAD': '0', 'TRLR': '0', 'NOTE': '0','NAME': '1', 'SEX': '1', 'MARR': '1','HUSB': '1', 'WIFE': '1', 'CHIL': '1','BIRT': '1', 'DEAT': '1', 'FAMC': '1', 'FAMS': '1'}
        s_actual_tag = { 'FAM': '0','INDI': '0'}

      


        if argument not in  ['INDI', 'FAM']:
            actual_tag_level = False
            s_tags = False
            for current_tag, current_level in actual_tag.items():
                if level == current_level and tag == current_tag:
                    actual_tag_level = True
                    break
           

        else:
            actual_tag_level = False
            s_tags = True
            for current_tag, current_level in s_actual_tag.items():
                if level == current_level and argument == current_tag:
                    actual_tag_level = True
                    break
           
           
       
        if (actual_tag_level and s_tags) or (actual_tag_level and not s_tags) or (not actual_tag_level and s_tags):
            output.append(level)
            output.append(argument) if (actual_tag_level and s_tags) or (not actual_tag_level and s_tags) else output.append(tag)
            output.append("Y") if (actual_tag_level and s_tags) or (actual_tag_level and not s_tags) else output.append("N")
            output.append(argument) if actual_tag_level and not s_tags else output.append(tag)
            output = print("<-- " + "|".join(output))
        else:
            output.append(level + " " + tag)
            output.append("N")
            output.append(argument)
            output = print("<-- " + "|".join(output))


if __name__ == '__main__':
    main()

