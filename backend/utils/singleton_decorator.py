def singleton(cls_):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls_ not in instances:
            instances[cls_] = cls_(*args, **kwargs)
        return instances[cls_]

    return get_instance