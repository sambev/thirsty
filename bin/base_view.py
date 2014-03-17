from flask.views import MethodView

class NameAPI(MethodView):

    def get(self, name_id):
        if name_id is None:
            # return a list of names
            pass
        else:
            # expose a single name
            pass

    def post(self):
        # create a new name
        pass

    def delete(self, name_id):
        # delete a single name
        pass

    def put(self, name_id):
        # update a single name
        pass