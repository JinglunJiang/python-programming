class ESArray(list):
    def join(self, s):
        """
        The method that joins the itme in the object with a given delimeter
        Input: the object and the delimiter
        Output: A string joins the items in the list with the provided delimeter
        """
        if len(self) == 0:
            return ""
        result = ""
        for item in self[:-1]:
            # the delimiter added after each item except for the last one
            result += str(item) + s
        result += str(self[-1])
        return result

    def every(self, func):
        """
        A method if every item inside the object is returning true for the given function
        Input: the function and the object itself
        Output: boolean represent if every item is returning true by the given function
        """
        return all(func(item) for item in self)

    def for_each(self, func):
        for item in self:
            func(item)

    def flatten(self):
        """
        Method to extract all items in the list
        Input: the object itself
        Output: A list with all the items
        """
        result = []
        for item in self:
            if type(item) == list:
                # recursively call the flatten method after casting
                result.extend(ESArray(item).flatten())
            else:
                result.append(item)
        return result
