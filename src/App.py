import json
from src.API_Controller import *

class Env:
    fi = open('./src/sec/env.json',) 
    data = json.load(fi)
    key = data['api_key']

#TODO
    #Add some button elements
        #Button to call api
        #Button to show response data
        #Button to download videoId 1 link -- for testing
        #Button to download all links
    #Add some text fields:
        #Query Field
        #VideoID -- for testing
        #Output folder location
    #Visual elements
        #Thumbnail image
        #
def main():
    local = Env()
    # print(local.key)
    secret = local.key
    api = API_Controller(secret)
    print('program complete!')
    #TO USE:
        # req = api.search('rick roll')
        # res = api.parse_response(req)


if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     local = Env()
#     # print(local.key)
#     secret = local.key
#     api = API_Controller(secret)
#     print('program complete!')
    #TO USE:
    # req = api.search('rick roll')
    # res = api.parse_response(req)

    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # desktop = QtWidgets.QApplication.desktop()
    # resolution = desktop.availableGeometry()
    # myapp = PyQtApp()
    # myapp.setWindowOpacity(0.95)
    # myapp.show()
    # myapp.move(resolution.center() - myapp.rect().center())
    # sys.exit(app.exec_())
# else:
#     print('else')
    # desktop = QtWidgets.QApplication.desktop()
    # resolution = desktop.availableGeometry()