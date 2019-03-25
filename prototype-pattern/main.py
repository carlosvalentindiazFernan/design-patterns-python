from share_cache import ShareCache


def main():

    """
    Value 1 => get Circle
    Value 2 => get Rectangle

    """

    ShareCache.inizialize()
    print(ShareCache.getClone("1"))

if __name__ == "__main__":
    main()