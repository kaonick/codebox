import jupyter_client


def tmp_01():
    kernel_manager, kernel_client = jupyter_client.manager.start_new_kernel(kernel_name='python3')
    kernel_client.execute("print('hello world')")
    msg=kernel_client.get_shell_msg()

    print(f"msg={msg}")

def tmp_02():
    from jupyter_client import KernelManager
    km = KernelManager()
    km.start_kernel()
    kc = km.client()
    # now execute something in the client
    kc.execute("2+2")
    while True:
        try:
            kc_msg = kc.get_iopub_msg(timeout=1)
            if 'content' in kc_msg and 'data' in kc_msg['content']:
                print('the kernel produced data {}'.format(kc_msg['content']['data']))
                break
        except:
            print('timeout kc.get_iopub_msg')
            pass
# https://blog.csdn.net/cccssss333/article/details/115199697
def tmp_03():
    import io
    from IPython import get_ipython

    # from nbformat import current
    from nbformat import read
    with io.open("my_example.ipynb") as f:
        nb=read(f,as_version=4)
        # nb = current.read(f, 'json')

    ip = get_ipython()
    # for cell in nb.worksheets[0].cells:
    for cell in nb.cells:
        if cell.cell_type != 'code':
            continue
        else:
        # if cell.prompt_number == 4186:

            ip.run_cell(cell.input)

def tmp_04():
    import jupyter_client

    cf = jupyter_client.find_connection_file('26052')
    km = jupyter_client.BlockingKernelClient(connection_file=cf)
    km.load_connection_file()
    # km.start_channels()

    def run_cell(km, code):
        # now we can run code.  This is done on the shell channel
        # shell = km.shell_channel

        print("running:")
        print(code)


        msg_id =km.execute('a=5')

        while True:
            try:
                kc_msg = km.get_iopub_msg(timeout=1)
                if 'content' in kc_msg and 'data' in kc_msg['content']:
                    print('the kernel produced data {}'.format(kc_msg['content']['data']))
                    break
            except:
                print('timeout kc.get_iopub_msg')
                break
                # passe


        # reply = km.get_iopub_msg()
        # # reply = km.get_msg()
        #
        # status = reply['content']['status']
        # if status == 'ok':
        #     print('succeeded!')
        #
        # elif status == 'error':
        #     print('failed!')
        #     for line in reply['content']['traceback']:
        #         print(line)


    run_cell(km, 'a=5')
    run_cell(km, 'b=0')
    run_cell(km, 'c=a/b')

if __name__ == '__main__':
    # tmp_01()
    # tmp_02()
    # tmp_03()
    tmp_04()