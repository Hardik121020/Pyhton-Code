class store:
    _item_count = 0
    
    @classmethod
    def addItem(self,count):
        self._item_count = self._item_count + count
    @classmethod
    def issueItem(self,count):
        self._item_count = self._item_count - count
    @classmethod
    def getItemCount(self):
        return self._item_count
counter1 = store()
counter2 = store()

counter1.addItem(10)
counter2.issueItem(4)

print(store().getItemCount())
