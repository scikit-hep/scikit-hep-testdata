import os


__all__ = ["data_path"]


__top_directory__ = os.path.realpath(os.path.dirname(__file__))


def data_path(filename, raise_missing=False):
    path = os.path.join(__top_directory__, filename)
    if not os.path.isfile(path) and raise_missing:
        raise RuntimeError("%s cannot be found" % filename)
    return path


if __name__ == "__main__":
    print("BEK __top_directory__", __top_directory__)
    print("BEK", data_path("hello.root"))
    print("BEK", data_path("hello.root", raise_missing=True))
