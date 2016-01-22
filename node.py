import math


class Node:
    def __init__(self, headers, sub_data, level, class_name, header, zero_data, one_data):
        """

        :param headers: set of potential attributes that was used to compute this nodes attribute
        :param sub_data: the data that was used to compute this nodes attribute
        :param level: how levels down the tree are we (the root is level 0)
        :param class_name: the name of the classification header in the dataset
        :param header: the attribute that this node is splitting the data on
        :param zero_data: the dataset where header has value 0
        :param one_data: the dataset where header has value 1
        """

        self.headers = headers
        self.sub_data = sub_data
        self.class_name = class_name
        if header != None:
            self.header = header
        else:
            self.header = self.get_header(self.sub_data, self.headers)

        self.level = level

        self.zero_data = []
        self.one_data = []
        if zero_data == None:
            for row in sub_data:
                if row[self.header] == 0:
                    self.zero_data.append(row)
                elif row[self.header] == 1:
                    self.one_data.append(row)
        else:
            self.zero_data = zero_data
            self.one_data = one_data
        self.headers.remove(self.header)
        self.left = self.compute_next(self.zero_data, self.headers[:])
        self.right = self.compute_next(self.one_data, self.headers[:])

    def __str__(self):
        final = '\n'
        for i in range(0, self.level):
            final += "| "
        final += self.header + " = 0 : "
        final += str(self.left)
        if type(self.left) is int:
            final += "\n"

        for i in range(0, self.level):
            final += "| "
        final += self.header + " = 1 : "
        final += str(self.right)
        if type(self.right) is int:
            final += "\n"

        return final

    def compute_next(self, _data, _headers):
        """

        :param _data: data set for next node
        :param _headers: potential atrributes to split on
        :return: a new node in our tree or a leaf
        """

        zero = 0
        one = 0

        for row in _data:
            if row[self.class_name] == 0:
                zero += 1
            elif row[self.class_name] == 1:
                one += 1
        if zero == 0:
            return 1
        if one == 0:
            return 0
        if not _headers:
            if zero > one:
                return 0
            else:
                return 1

        new_header = self.get_header(_data, _headers)
        zero_data = []
        one_data = []
        for row in _data:
            if row[new_header] == 0:
                zero_data.append(row)
            elif row[new_header] == 1:
                one_data.append(row)

        if self.chi_square(_data, zero_data, one_data)<6.635:
            if zero >= one:
                return 0
            else:
                return 1

        return Node(_headers[:], _data, self.level + 1, self.class_name, new_header, zero_data, one_data)

    def chi_square(self, data, zero_data, one_data):
        """

        :param data: whole data set to compute chi square test one
        :param zero_data: data set where attribute being tested equals 0
        :param one_data: data set where attribute being tested equals 1
        :return: a value of chi-squared
        """

        p = 0
        n = 0
        for row in data:
            if row[self.class_name] == 0:
                n += 1
            else:
                p += 1

        p_zero = 0
        p_one = 0
        n_zero = 0
        n_one = 0

        for row in zero_data:
            if row[self.class_name] == 0:
                n_zero += 1
            elif row[self.class_name] == 1:
                p_zero += 1

        for row in one_data:
            if row[self.class_name] == 0:
                n_one += 1
            elif row[self.class_name] == 1:
                p_one += 1

        p_hat_zero = (p/(p+n))*len(zero_data)
        n_hat_zero = (n/(p+n))*len(zero_data)
        p_hat_one = (p/(p+n))*len(one_data)
        n_hat_one = (n/(p+n))*len(one_data)

        dev_zero = (((p_zero - p_hat_zero)**2)/p_hat_zero) + (((n_zero - n_hat_zero)**2)/n_hat_zero)
        dev_one = (((p_one - p_hat_one)**2)/p_hat_one) + (((n_one - n_hat_one)**2)/n_hat_one)
        dev = dev_zero + dev_one

        return dev

    def get_header(self, _data, _headers):
        """

        :param _data: data used to find next attribute to split on
        :param _headers: all attributes available to split on
        :return: the attribute that should be split on based on the data
        """

        max_gain = 0
        max_header = ''

        for header in _headers:
            gain = self.information_gain(_data, header)
            if gain >= max_gain:
                max_gain = gain
                max_header = header
        return max_header

    def entropy(self, data):
        """

        :param data: data to calculate entropy from
        :return: entropy of data set
        """
        zero = 0
        one = 0
        for row in data:
            if row[self.class_name] == 0:
                zero += 1
            elif row[self.class_name] == 1:
                one += 1
        total = zero + one
        if zero == 0 or one == 0:
            return 0

        ent = -(one / total) * (math.log((one / total), 2)) - (zero / total) * (math.log((zero / total), 2))

        return ent

    def information_gain(self, data, header):
        """

        :param data: data set to calculate information gain from
        :param header: attribute to test the gain of
        :return: information gain of header given data set, i.e. Gain(data,header)
        """
        e = self.entropy(data)
        _zero_data = []
        _one_data = []
        s = len(data)
        s_0 = 0
        s_1 = 0

        for row in data:
            if row[header] == 0:
                _zero_data.append(row)
                s_0 += 1
            else:
                _one_data.append(row)
                s_1 += 1

        return e - (s_0 / s) * self.entropy(_zero_data) - (s_1 / s) * self.entropy(_one_data)
