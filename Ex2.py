class py_class:
    def subset_(self, set_):
        return self.subset_recursive([], sorted(set_))

    def subset_recursive(self, current, set_):
        if set_:
            return (self.subset_recursive(current, set_[1:]) +
                    self.subset_recursive(current + [set_[0]], set_[1:])
                    )
        return [current]


for i in py_class.__dict__:
    print(i)
