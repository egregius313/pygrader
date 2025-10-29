from .pycanvasgrader import main

RUN_WITH_TESTS = False
ONLY_RUN_TESTS = False

if __name__ == "__main__":
    if RUN_WITH_TESTS or ONLY_RUN_TESTS:
        import py

        py.test.cmdline.main()
    if not ONLY_RUN_TESTS:
        main()
