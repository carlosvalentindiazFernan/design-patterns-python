from db_apdater.dba_factory import DBAFactory



def main():
    factory = DBAFactory()
    factory.connection('mongo')


if __name__ == '__main__':
    main()