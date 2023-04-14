def foo():
    assert False


def greeting(name: str) -> None:
    print(f"Hello {name}!")
    foo()


if __name__ == '__main__':
    greeting("Bazel")