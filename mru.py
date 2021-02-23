import winreg

def get_run_mru():    
    regKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU')
    # recent = winreg.QueryValueEx(regKey,'MRUList')[0]
    # recent_list = []
    # for subkey in recent:
    #     recent_list.append(winreg.QueryValueEx(regKey,subkey)[0])
    # return recent_list
    
    list_of_lists = []    
    try:
        recent = winreg.QueryValueEx(regKey,'MRUList')[0]
        print(f"recent is {recent}")
        recent_list = []
        if type(recent) != int: 
            print("recent valid \n")
            for i, subkey in enumerate(recent):
                print(f"i is {i} subkey is {subkey} \n")
                recent_list.append(winreg.QueryValueEx(regKey,subkey)[0])
            list_of_lists.append(recent_list)
        else: return list_of_lists
        # return recent_list
    # except FileNotFoundError: 
    #     print(f"FileNotFoundError error with subkey: {subkey} ")
    #     subkey = subkey + recent[i + 1]
    #     print(f"new subkey: {subkey}")
    #     recent_list.append(winreg.QueryValueEx(regKey,subkey)[0])
    except WindowsError: 
        print(f"windows error with subkey: {subkey} ")
        
        while i < 8: 
            # print(f"windows error with subkey: {subkey} ")
            # subkey += recent[i + 1]
            try: 
                print(f"new subkey: {subkey} and i is {i}")
                print(f"recent_list is {recent_list}")
                recent_list.append(winreg.QueryValueEx(regKey,subkey)[0])
                break
            except: 
                if i < 10:  
                    i += 1
                    try: subkey += recent[i]
                    except IndexError: return list_of_lists
                else: return list_of_lists
        return recent_list
                
            

def Create_SubKey(): 
    regKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU')
    state = winreg.CreateKeyEx(regKey, "Yuval Subkey")
    print(f"state is {state}\n")

def Key_Info(): 
    regKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU')
    return winreg.QueryInfoKey(regKey)
    
def Enum_Key_Value(index): 
    regKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU')
    return winreg.EnumValue(regKey, index)

def Create_Value_InKey():
    regKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU', access=winreg.KEY_ALL_ACCESS)    
    ### creating the value
    # winreg.SetValue(regKey, None, winreg.REG_SZ, "Yuval\\1")
    VAL_NAME = "z"
    winreg.SetValueEx(regKey, VAL_NAME, 0, winreg.REG_SZ, "Yuval\\1")

    ### adding the value to the mru list
    mru_val = winreg.QueryValueEx(regKey,'MRUList')[0]
    winreg.SetValueEx(regKey, "MRUList", 0, winreg.REG_SZ, mru_val + VAL_NAME)

def main():
    l = get_run_mru()
    print(f"\nl is: {l}\n")
    Create_SubKey()
    Create_Value_InKey()
    info = Key_Info()
    print(f"info is: {info}\n")

    for value in range(info[1]):
        try:  
            print(Enum_Key_Value(value))
        except OSError:
            print("got an os error") 
            break


if __name__ == "__main__":
    main()



    # def delete_sub_key(key0, current_key, arch_key=0):

    #     open_key = winreg.OpenKey(key0, current_key, 0, winreg.KEY_ALL_ACCESS | arch_key)
    #     info_key = winreg.QueryInfoKey(open_key)
    #     for x in range(0, info_key[0]):
    #         # NOTE:: This code is to delete the key and all sub_keys.
    #         # If you just want to walk through them, then
    #         # you should pass x to EnumKey. sub_key = winreg.EnumKey(open_key, x)
    #         # Deleting the sub_key will change the sub_key count used by EnumKey.
    #         # We must always pass 0 to EnumKey so we
    #         # always get back the new first sub_key.
    #         sub_key = winreg.EnumKey(open_key, 0)
    #         try:
    #             winreg.DeleteKey(open_key, sub_key)
    #             print("Removed %s\\%s " % (current_key, sub_key))
    #         except OSError:
    #             delete_sub_key(key0, "\\".join([current_key,sub_key]), arch_key)
    #             # No extra delete here since each call
    #             # to delete_sub_key will try to delete itself when its empty.

    #     winreg.DeleteKey(open_key, "")
    #     open_key.Close()
    #     print("Removed %s" % current_key)
    #     return


    # # Allows to specify if operating in redirected 32 bit mode or 64 bit, set arch_keys to 0 to disable
    # arch_keys = [winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY]

    # # Base key
    # root = winreg.HKEY_LOCAL_MACHINE

    # # List of keys to delete
    # keys = ['SOFTWARE\MyInstalledApp', 'SOFTWARE\SomeKey\SomeOtherKey']

    # for key in keys:
    #     for arch_key in arch_keys:
    #         try:
    #             delete_sub_key(root, key, arch_key)
    #         except OSError as e:
    #             print(e)