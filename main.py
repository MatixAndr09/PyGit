
def main():
    import components.init as init
    init.init()


    import components.CHANGE_LOGGER as cl
    import components.GIT_CLIENT as gc
    import components.UI as ui

    ui.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit(1)