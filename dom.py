from xml.dom import minidom


def pars_and_fetch(input_string, keyword):
    print("======================================")
    # print(input_string)
    doc = minidom.parseString(input_string)
    name = doc.getElementsByTagName("input")
    ret = ""
    for element in name:
        if element.hasAttribute('id') \
                and element.getAttribute('id') == keyword:
            ret = element.getAttribute('value')
    return ret

