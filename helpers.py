import csv

def Detecting_change(filepath):
    output = {}

    # Read files
    try:
        with open(filepath) as file:
            reader = csv.reader(file)
            
            header_row = next(reader)
            if len(header_row) != 2 and header_row[0] != 'Date':
                return False

            tmp = next(reader)[1]
        
            for row in reader:
                if eval(tmp) == False and eval(row[1]) == True:
                    output[row[0]] = True
                tmp = row[1]

    except IOError:
        sys.exit(f"Could not read {filepath}")
        return False

    return output


def Season(filepath):
    output = {}

    # Read files
    try:
        with open(filepath) as file:
            reader = csv.reader(file)
            
            header_row = next(reader)
            if len(header_row) != 3 and header_row[0] != 'Ord_id':
                return False      

            for ord_id, date, *_ in reader:

                parser = date.split('/')

                numb = int(parser[0] + parser[1].zfill(2))

                if numb >= 319 and numb <=619:
                    tmp = 'spring'
                if numb >= 620 and numb <=921:
                    tmp = 'summer'
                if numb >= 922 and numb <=1220:
                    tmp = 'fall'
                if numb >= 1221 or numb <=318:
                    tmp = 'winter'
                output[ord_id] = tmp

    except IOError:
        sys.exit(f"Could not read {filepath}")
        return False

    return output


def Order_status(filepath):
    # Read files
    try:
        with open(filepath) as file:
            reader = csv.reader(file)

            header_row = next(reader)
            if len(header_row) != 3 and header_row[0] != 'Ord_id':
                return False

            writer_key, _, writer_value = next(reader)
            output = {writer_key: writer_value}
            overall = writer_value
            writer_value = False

            for ord_id, _, status in reader:

                if ord_id != writer_key:
                    output[writer_key] = writer_value or overall 
                    writer_key = ord_id
                    overall = writer_value
                    writer_value = False
                

                if status == 'PENDING':
                    writer_value = 'PENDING'

                if status == 'SHIPPED' :
                    overall = 'SHIPPED'

            output[writer_key] = writer_value or overall
        
    except IOError:
        sys.exit(f"Could not read {filepath}")
        return False

    return output
