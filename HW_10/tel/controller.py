import view as v
import modul_import as mi
import modul_export as me
import modul_export_json as mej
import modul_search as ms

def button_click():
    choice = v.hello()
    phones = []
    if choice == "1":
        choice_1 = v.str_or_line()
        if choice_1 == "1":
            phones = mi.get_number()
        elif choice_1 == "2":
            phones = mi.get_number_line()
        else:
            print("Error!")
        me.write_in_txt(phones)
        me.write_in_csv(phones)
        mej.convert_to_json(phones)
    elif choice == "2":
        me.print_from_txt()
    elif choice == "3":
        choice_3 = v.search_for()
        find_value = str(v.search_in())
        if choice_3 == "1":
            ms.search_for(find_value, "family")
        elif choice_3 == "2":
            ms.search_for(find_value, "name")
        elif choice_3 == "3":
            ms.search_for(find_value, "phone")
        else:
            print("Error!")
    else:
        print("Error!")