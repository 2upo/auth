class CustomBaseModel():

    _excluded_fields = []

    def to_dict(self):
        res = {k:v for k, v in self.__dict__.items() if k not in self._excluded_fields}
        res.pop("_sa_instance_state")
        return res
