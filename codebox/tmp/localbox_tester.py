from codebox.tmp.localbox import LocalBox

if __name__ == '__main__':
    cbox=LocalBox()
    status=cbox.start()
    print(f"status={status}")

    ouput=cbox.run("print('hello world')")
    print(f"ouput={ouput}")

    after_install=cbox.install("pip install jupyter_client")
    print(f"after_install={after_install}")

    final=cbox.stop()
    print(f"final={final}")
