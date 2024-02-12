def functionMaster():
    print("This function was added in the master branch.")

def functionDev():
    print("This function was added in the dev branch.")


def functionTest():
    print("This function was added in the test branch.")

if _name_ == '_main_':
    functionMaster()
    functionTest()
    functionDev()
