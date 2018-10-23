class Report(object):
    """docstring for Report."""
    def __init__(self, election_id,callback_function):
        self.election_id = election_id
        self.callback_function = callback_function
        self.result = dict()

    def addResult(self,res):
        test_id = res[0].id
        parent_id = int(test_id[0])
        child_dict = self.result.get(parent_id,dict())
        child_dict[test_id]=res
        self.result[parent_id]=child_dict
        self.callback_function(res)

    def getResult(self):
        return self.result

    def getStat(self,id):
        res_arr = self.result.get(int(id)).values()
        correct_test = len(list(filter(lambda x: x[1],res_arr)))
        return str(correct_test)+"/"+str(len(res_arr))
