import mend_tab as mb







def search(types_,value_,returntype_=1):
    if types_ == "id":
        if returntype_ == 1:
            return mb.get_use_id(value_)
        else:
            return mb.get_use_id(value_)["name"],mb.get_use_id(value_)["atom_mas"],mb.get_use_id(value_)["id"]
    elif types_ == "name":
        if returntype_ == 1:
            return mb.get_use_name(value_)
        else:
            return mb.get_use_name(value_)["name"],mb.get_use_id(value_)["atom_mas"],mb.get_use_id(value_)["id"]