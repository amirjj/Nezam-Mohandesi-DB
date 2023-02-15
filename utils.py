"""General utilities to be used by program

"""

def logit(msg, **data):
    """ arg: page_number, exception, msg
    
    log he current progress of the programm and the message
    """
    pass
    
def json_to_tuple_conv(json_par):
    """return a tuple
    converted from a json
    """
    tuple_par = ()
    for el in json_par:
        tuple_par = tuple_par + ((el, json_par[el]),)
    
    return tuple_par
    
def make_formfields_config(form_fields, page_number, viewstat, eventvalidation):
    """ create formfileds tuple configuration for request
    
    based on current progress of program
    """
    form_fields['__EVENTARGUMENT'] = r'Page$%s'%str(page_number)
    if page_number is None:
        form_fields['__EVENTARGUMENT'] = r''
        form_fields['__EVENTTARGET'] = r''
    
    form_fields['__VIEWSTATE'] = viewstat
    form_fields['__EVENTVALIDATION'] = eventvalidation
    
    form_fields_tup = json_to_tuple_conv(form_fields)
    
    return form_fields_tup
    