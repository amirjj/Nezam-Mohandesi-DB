from parser_config import output_path
from bs4 import BeautifulSoup
import io


def test():
    all_data = list()
    with open("./out_page1.html", 'rb') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        rows = soup.find('table', id='GridView1').find_all('tr')
        print(len(rows))
        header = rows[0]
        data = rows[1:-2]
        for row in data:
            # print(dir(row))
            row_data = row.findAll('td')
            row_number = row_data[0].text.strip()
            fname = row_data[1].text.strip()
            lname = row_data[2].text.strip()
            email = row_data[3].text.strip()
            mobile = row_data[4].text.strip()
            occupation = row_data[6].text.strip()
            tmp_dict = {
                'fname': fname,
                'lname': lname,
                'email': email,
                'mobile': mobile,
                'occupation': occupation
            }
            all_data.append(tmp_dict.copy())
            tmp_dict.clear()

    return all_data


def dump_to_csv(all_data):
    # print(all_data)
    with io.open('output.csv', 'w', encoding='utf-8-sig') as f:
        f.write('Name, Last Name, Mobile, Email, Occupation \n')
        for row in all_data:
            s = u','.join([row['fname'], row['lname'], row['mobile'], row['email'], row['occupation']]) + u'\n'
            f.write(s)


def crawl():
    all_data = list()
    for file in output_path.glob('*.html'):
        print(file)
        with open(file, 'rb') as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            rows = soup.find('table', id='GridView1').find_all('tr')
            # print(len(rows))
            header = rows[0]
            data = rows[1:-2]
            for row in data:
                # print(dir(row))
                row_data = row.findAll('td')
                row_number = row_data[0].text.strip()
                fname = row_data[1].text.strip()
                lname = row_data[2].text.strip()
                email = row_data[3].text.strip()
                mobile = row_data[4].text.strip()
                occupation = row_data[6].text.strip()
                tmp_dict = {
                    'fname': fname,
                    'lname': lname,
                    'email': email,
                    'mobile': mobile,
                    'occupation': occupation
                }
                all_data.append(tmp_dict.copy())
                tmp_dict.clear()
    return all_data


if __name__ == "__main__":
    # all_data = test()
    all_data = crawl()
    dump_to_csv(all_data)

